import streamlit as st
import matplotlib.pyplot as plt
from collections import deque
import random
import time
import numpy as np
import serial  # Bibliotecas necessárias para comunicação serial
import serial.tools.list_ports

# Configuração da página
st.set_page_config(layout="wide", page_title="HeartSync ECG")

# --- CSS para esconder widgets de status ---
st.markdown("""<style>[data-testid="stStatusWidget"] {display: none;}</style>""", unsafe_allow_html=True)

# --- Configurações do Buffer e Variáveis Globais ---
max_pontos = 200
dados = deque([0]*max_pontos, maxlen=max_pontos)
bpm_max = 0
bpm_min = float("inf")
limiar = 800 
ultimos_batimentos = deque(maxlen=10)

# --- Lógica de Conexão Serial ---
@st.cache_resource
def conectar_arduino():
    try:
        # Tenta encontrar a porta do Arduino automaticamente ou defina manualmente (ex: 'COM3' ou '/dev/ttyUSB0')
        ports = list(serial.tools.list_ports.comports())
        for p in ports:
            if "Arduino" in p.description or "USB" in p.description:
                return serial.Serial(p.device, 9600, timeout=0.1)
    except:
        return None
    return None

ser = conectar_arduino()

# --- Interface Streamlit ---
st.markdown("<h1 style='text-align: center;'>💓 HeartSync - Monitoramento ECG</h1>", unsafe_allow_html=True)

if ser:
    st.success(f"Conectado ao Arduino na porta: {ser.port}")
else:
    st.warning("Arduino não detectado. Iniciando em Modo Simulação 🧪")

left, center, right = st.columns([1, 6, 1])
grafico_placeholder = center.empty()
bpm_placeholder = right.empty()
right.markdown("---")
max_placeholder = right.empty()
right.markdown("---")
min_placeholder = right.empty()

# --- Loop Principal ---
while True:
    valor = 0
    
    # Tenta ler do Arduino, se falhar, simula
    if ser and ser.in_waiting > 0:
        try:
            linha = ser.readline().decode('utf-8').strip()
            if linha.isdigit():
                valor = int(linha)
            elif linha == '!':
                st.error("⚠️ Eletrodos desconectados!")
                continue
        except:
            valor = random.randint(400, 600) # Fallback
    else:
        # Simulação de sinal de ECG mais realista
        valor = random.randint(0, 1023) 

    dados.append(valor)

    # Detector de batimento 
    if valor > limiar:
        tempo_atual = time.time()
        if len(ultimos_batimentos) == 0 or (tempo_atual - ultimos_batimentos[-1]) > 0.3:
            ultimos_batimentos.append(tempo_atual)
    
    # Calcula BPM
    bpm = 0
    if len(ultimos_batimentos) > 1:
        intervalos = np.diff(ultimos_batimentos)
        media_intervalo = np.mean(intervalos)
        bpm = 60 / media_intervalo

    if bpm > 0:
        bpm_max = max(bpm_max, bpm)
        bpm_min = min(bpm_min, bpm)

    # --- Renderização do Gráfico ---
    fig, ax = plt.subplots(figsize=(8, 4))
    fig.patch.set_facecolor("#0E1117")
    ax.set_facecolor("#0E1117")
    ax.plot(dados, color="#FF0000", linewidth=2) # Vermelho vibrante
    ax.set_ylim(0, 1023)
    
    # Estilização de eixos
    ax.tick_params(colors="white")
    for spine in ax.spines.values():
        spine.set_color("white")
    ax.grid(True, color="white", linestyle="--", linewidth=0.5, alpha=0.2)

    grafico_placeholder.pyplot(fig)
    plt.close(fig) 

    # --- Métricas Laterais ---
    if bpm > 0:
        status = "🟢 Normal" if 60 <= bpm <= 100 else "🔴 Alerta"
    else:
        status = "⏳ Calculando..."

    bpm_placeholder.metric(label="❤️ BPM Atual", value=f"{bpm:.1f}", delta=status)
    max_placeholder.metric(label="📈 Máximo", value=f"{bpm_max:.1f}")
    min_placeholder.metric(label="📉 Mínimo", value=f"{bpm_min:.1f if bpm_min != float('inf') else 0}")

    time.sleep(0.5)
