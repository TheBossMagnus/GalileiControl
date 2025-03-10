const int ledPins[3][3] = {
    {2, 3, 4}, // LED RGB 0
    {5, 6, 7}, // LED RGB 1
    {8, 9, 10} // LED RGB 2
};

void setup() {
    Serial.begin(9600); // Inizializza la comunicazione seriale
    for(int i=0; i<3; i++){
        for(int j=0; j<3; j++){
            pinMode(ledPins[i][j], OUTPUT); // Imposta i pin dei LED RGB come output
        }
    }
}

void loop() {
    if(Serial.available()>0){ // Controlla se sono disponibili dati nella seriale
        String input = Serial.readStringUntil('\n'); // Legge la stringa fino al carattere di nuova riga
        input.trim(); // Rimuove spazi bianchi iniziali o finali se presenti
        
        // Estrae i valori dalla stringa ricevuta e li converte ad int (es: "1.200.200.200" -> LED 1, R 200, G 200, B 200)
        int indiceLed = input.substring(0, 1).toInt(); // Identifica quale LED controllare
        int r = input.substring(2, 5).toInt(); // Estrae il valore R
        int g = input.substring(6, 9).toInt(); // Estrae il valore G
        int b = input.substring(10, 13).toInt(); // Estrae il valore B
        
        // Controlla se l'indice del LED è valido (0, 1 o 2) e imposta il colore corretto al LED stesso
        if(indiceLed>=0 && indiceLed<3){
            analogWrite(ledPins[indiceLed][0], r); // Imposta il valore del rosso
            analogWrite(ledPins[indiceLed][1], g); // Imposta il valore del verde
            analogWrite(ledPins[indiceLed][2], b); // Imposta il valore del blu
        }
    }
}
