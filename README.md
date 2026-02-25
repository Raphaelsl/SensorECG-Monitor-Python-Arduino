
#💓 HeartSync: Monitoramento Bio-Sinal ECG
Integração IoT com Arduino e Visualização de Dados via Python (Streamlit)

Este projeto consiste em um ecossistema de monitoramento biomédico para leitura, processamento e visualização de sinais de Eletrocardiograma (ECG) em tempo real. Desenvolvido para unir a precisão da captura de hardware (Arduino) com a flexibilidade da análise de dados em alto nível (Python).

🛠️ Stack Tecnológica
Hardware: Arduino (Processamento de sinais analógicos).

Linguagem: Python 3.x.

Framework: Streamlit (Interface de usuário).

Processamento: NumPy/SciPy para tratamento do sinal.

##🌟 Diferenciais do Projeto
Análise em Tempo Real: Visualização dinâmica sem latência perceptível.

Motor de Inteligência: Classificação automática do estado cardíaco com base nos picos de R-R detectados.

Modo Híbrido: Suporte para hardware real via porta serial ou simulação matemática de ondas para fins de teste.

Métricas Avançadas: Monitoramento de BPM médio, oscilações mínimas e máximas durante a sessão.

##📸 Interface
(Mantenha as imagens que você já tem, elas dão o toque visual essencial)

<p align="center">
<img src="https://github.com/user-attachments/assets/9ad10961-47dc-4fb4-b375-19ec66022973" width="45%" />
<img src="https://github.com/user-attachments/assets/423c9748-c196-4a8f-a429-aaefab4a4114" width="45%" />
</p>

###👥 Desenvolvimento em Grupo
Este projeto foi desenvolvido de forma colaborativa como parte das atividades acadêmicas.

###🚀 Como Executar
Arduino: Carregue o arquivo .ino na sua placa.

Python:

Bash
pip install streamlit pyserial numpy.

streamlit run app.py.
