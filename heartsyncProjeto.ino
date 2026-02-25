/*
 * Projeto: HeartSync - Monitoramento de ECG
 * Descrição: Leitura de sinais analógicos do sensor AD8232 e envio via Serial.
 * Desenvolvido em Grupo (UFOP - Sistemas de Informação)
 */

void setup() {
  // Inicializa a comunicação serial a 9600 bps para conversar com o Python
  Serial.begin(9600);
  
  // Pinos de detecção de leads (eletrodos) do AD8232
  pinMode(10, INPUT); // Setup para detecção de cabos desconectados (LO +)
  pinMode(11, INPUT); // Setup para detecção de cabos desconectados (LO -)
  
  // Pino A0 é usado para a entrada do sinal analógico do ECG
}

void loop() {
  // Verifica se os eletrodos estão bem conectados à pele

  if((digitalRead(10) == 1) || (digitalRead(11) == 1)){
    Serial.println('!'); // Envia '!' para o Python indicar erro de conexão
  } 
  else {
    // Lê o valor bruto do sensor (0 a 1023)
    int sensorValue = analogRead(A0);
    
    // Envia o valor para a porta Serial

    Serial.println(sensorValue);
  }
  
  // Pequeno delay de 1ms para estabilizar a leitura e não sobrecarregar o buffer
  delay(1);
}