# Progetto: Galilei Control

## Sommario
- [Obiettivi del Progetto](#obiettivi-del-progetto)
- [Descrizione del Progetto](#descrizione-del-progetto)
- [Ruoli e Responsabilità](#ruoli-e-responsabilità)
- [Timeline del Progetto](#timeline-del-progetto)
- [Rischi e Mitigazioni](#rischi-e-mitigazioni)
- [Risultati Attesi](#risultati-attesi)
- [Conclusioni](#conclusioni)

---

## Obiettivi del Progetto
- **Obiettivo Principale**: Un sistema IOT che permette di monitorare tramite Bluetooth lo stato dei dispositivi, raccogliendo dati utili al personale per la mautenzione e la disgnostica.
- **Obiettivi Specifici**:
  1. Sviuluppare un sistema client-server che permetta di raccogliere, inviare e salvare i dati dei dispositivi.
  2. Creare un API per l'accesso ai dati raccolti.
  3. Implementare un sistema di detezione e notifica delle anomalie nei dispositivi, intuitivo e accessibile.

## Descrizione del Progetto
Il progetto prevede un sistema per il monitoraggio di più dispositivi con Bluethooth. Vengono racccolti dati utili come, temperatura della CPU e utilizzo della RAM di un PC windows, e salvati per l’analisi. 
Vengono individuate le problematiche e notificate, per esmpio tramite un LED verde o rosso. In questo modo si ha un’indicazione immediata sullo stato del sistema.

## Ruoli e Responsabilità
| Nome                  | Responsabilità                             |
|-----------------------|--------------------------------------------|
| Andrea Parolari       | Sviluppo server, documentazione tecnica    |
| Tommaso Ingiardi      | Sviluppo Client, Presentazione             |
| Matteo Cambiè         | Sviluppo dashboard, Sviluppo Server        |
| Riccardo Donato       | Presentazione, Documentazione              |


## Timeline del Progetto
| Fase         | Data di Inizio | Data di Fine | Stato      |
|--------------|----------------|--------------|------------|
| Analisi      | 10-03          | 24-03        | Completata |
| Sviluppo     | 24-03          | 14-04        | Completata |
| Test         | 14-04          | 26-04        | Completata |
| Consegna     | 28-04          | 28-04        | Completata |

## Risorse
- **Hardware**: Rasberry Pi 4, Arduino, client windows
- **Software**: Python, Arduino sketch
- **Librerie**: `pybluez`, `flask`, `requests`, `pyserial`
- **Technologie**: Bluetooth, REST API, JSON, Socket, Arduino sketch


## Rischi e Mitigazioni
Non sono  implementate importanti misura di sicurezza in questa dimostrazione:
    - Non sono implementate misure di autenticazione per l'API
    - Non è implementata alcuna crittografia per la comunicazione Bluetooth
    - Manca la validazione dei dati in ingresso
    - Non sono presenti controlli per evitare che un utente possa inviare dati falsi
    - Non sono presenti blocchi che evitano all'utente di killare il client.py o comunque di manipolalro

Tutte queste problematiche sono superabili, richiedono però ulteriore lavoro.


## Risultati Attesi
- **Miglioramento dell'efficienza**: Riduzione dei tempi di diagnosi e manutenzione grazie al monitoraggio in tempo reale.
- **Affidabilità**: Identificazione tempestiva delle anomalie per prevenire guasti.
- **Scalabilità**: Possibilità di integrare nuovi dispositivi e funzionalità in futuro.
- **Facilità d'uso**: Interfaccia intuitiva per il personale tecnico.

## Problematcihe rimanenti
Si raccomanda di:
- Implementare un database per una gestione più efficiente dei dati.
- Aggiungere misure di sicurezza, come descirtti sopra.
- Migliorare la validazione e organizzazione dei dati.
- il server Bluetooth deve essere eseguito con i permessi di amministratore, per limitazioni di pybluez

## Conclusioni
Il progetto "Galilei Control" ha dimostrato la fattibilità di un sistema IoT per il monitoraggio e la diagnostica dei dispositivi tramite Bluetooth. Nonostante alcune limitazioni, come l'assenza di un database relazionale e la mancanza di misure di sicurezza avanzate, il sistema offre una base solida per ulteriori sviluppi. 


Ipotizziamo questi posssibili sviluppi futuri:
- Architettura con più server per una copertura più ampia
- Sistemi di allerta configurabili e intelligenti, possibile uso di intelligenza artificiale
- Sistema di visualozzazione dei dati più chiaro, con sito web o applicazione
- Ulteriori funzionalità per il client, come supporto di altri sistemi operativi o controllo remoto
