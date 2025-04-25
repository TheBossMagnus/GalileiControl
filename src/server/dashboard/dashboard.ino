// Sketch Arduino per controllare più LED RGB tramite comunicazione seriale
// Formato per input seriale: "X.RRR.GGG.BBB" dove X è l'indice del LED (0-1), RRR, GGG, BBB sono valori RGB (000-255)

const int pinLed[2][3] = {
    {3, 5, 6},  // LED 0: pin R,G,B
    {9, 10, 11} // LED 1: pin R,G,B
};

void setup()
{
    Serial.begin(9600); // Inizializza comunicazione seriale

    // Imposta tutti i pin LED come OUTPUT
    for (int i = 0; i < 2; i++)
    { // Corretto: ciclo su 2 LED, non 3
        for (int j = 0; j < 3; j++)
        {
            pinMode(pinLed[i][j], OUTPUT);
        }
    }

    // Conferma che il dispositivo è pronto
    Serial.println("Controller LED RGB Pronto");
}

void mostraLedRgb(int pinLedR, int pinLedG, int pinLedB, int rosso, int verde, int blu)
{
    // Imposta tre pinLed per generare il ciclo di lavoro PWM
    analogWrite(pinLedR, constrain(rosso, 0, 255));
    analogWrite(pinLedG, constrain(verde, 0, 255));
    analogWrite(pinLedB, constrain(blu, 0, 255));
}

void loop()
{
    if (Serial.available() > 0)
    {                                                // Verifica se i dati sono disponibili
        String input = Serial.readStringUntil('\n'); // Legge la stringa fino a nuova riga
        input.trim();                                // Rimuove spazi bianchi

        // Verifica se l'input ha il formato corretto e la lunghezza
        if (input.length() >= 13)
        {
            // Estrae valori dalla stringa ricevuta (es. "1.200.200.200" -> LED 1, R 200, G 200, B 200)
            int indiceLed = input.substring(0, 1).toInt(); // Indice LED
            int r = input.substring(2, 5).toInt();         // Valore rosso
            int g = input.substring(6, 9).toInt();         // Valore verde
            int b = input.substring(10, 13).toInt();       // Valore blu

            // Output di debug su seriale
            Serial.print("LED: ");
            Serial.print(indiceLed);
            Serial.print(" | RGB: ");
            Serial.print(r);
            Serial.print(", ");
            Serial.print(g);
            Serial.print(", ");
            Serial.println(b);

            // Imposta colore LED se l'indice è valido (0 o 1)
            if (indiceLed >= 0 && indiceLed < 2)
            { // Corretto: verifica per < 2, non < 3
                mostraLedRgb(pinLed[indiceLed][0], pinLed[indiceLed][1], pinLed[indiceLed][2], r, g, b);
                Serial.println("Colore LED impostato con successo");
            }
            else
            {
                Serial.println("Errore: Indice LED non valido (deve essere 0 o 1)");
            }
        }
        else
        {
            Serial.println("Errore: Formato input non valido. Usa 'X.RRR.GGG.BBB'");
        }
    }
}
