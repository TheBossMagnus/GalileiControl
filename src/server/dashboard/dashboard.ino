//const int ledPins[3][3] = {
//    {3, 4, 5}, // LED  0
//    {6, 7, 8}, // LED  1
//    {9, 10, 11} // LED  2
//};

const int ledPins[2][3] = {
    {3, 5, 6}, // LED 0
    {9, 10, 11} // LED 1
};

void setup() {
    Serial.begin(9600); // Inizializza la comunicazione seriale
    for(int i=0; i<3; i++){
        for(int j=0; j<3; j++){
            pinMode(ledPins[i][j], OUTPUT); // Imposta i pin dei LED YMC come output
        }
    }
}
void rgbLedDisplay(int ledPinR, int ledPinG, int ledPinB, int red, int green, int blue) {
// Set three ledPin to output the PWM duty cycle
analogWrite(ledPinR, constrain(red, 0, 255));
analogWrite(ledPinG, constrain(green, 0, 255));
analogWrite(ledPinB, constrain(blue, 0, 255));
}

void loop() {
    if(Serial.available()>0){ // Controlla se sono disponibili dati nella seriale
        String input = Serial.readStringUntil('\n'); // Legge la stringa fino al carattere di nuova riga
        input.trim(); // Rimuove spazi bianchi iniziali o finali se presenti
        
        // Estrae i valori dalla stringa ricevuta e li converte ad int (es: "1.200.200.200" -> LED 1, Y 200, M 200, C 200)
        int indiceLed = input.substring(0, 1).toInt(); // Identifica quale LED controllare
        int r = input.substring(2, 5).toInt(); // Estrae il valore C
        int g = input.substring(6, 9).toInt(); // Estrae il valore M
        int b = input.substring(10, 13).toInt(); // Estrae il valore Y
      
        Serial.print(r);
        Serial.print(g);
        Serial.print(b);
        
        
        // Controlla se l'indice del LED è valido (0, 1 o 2) e imposta il colore corretto al LED stesso
        if(indiceLed>=0 && indiceLed<3){
            rgbLedDisplay(ledPins[indiceLed][0], ledPins[indiceLed][1], ledPins[indiceLed][2], r, g, b); // Imposta il valore del rosso
 
        }
    }
}
