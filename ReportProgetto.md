# Progetto Aziendale: **[Titolo del Progetto]**

## Sommario
- [Obiettivi del Progetto](#obiettivi-del-progetto)
- [Descrizione del Progetto](#descrizione-del-progetto)
- [Ruoli e Responsabilità](#ruoli-e-responsabilità)
- [Timeline del Progetto](#timeline-del-progetto)
- [Risorse](#risorse)
- [Rischi e Mitigazioni](#rischi-e-mitigazioni)
- [Risultati Attesi](#risultati-attesi)
- [Conclusioni](#conclusioni)

---

## Obiettivi del Progetto
- **Obiettivo Principale**: [Descrivere l'obiettivo principale del progetto]
- **Obiettivi Specifici**:
  1. [Obiettivo specifico 1]
  2. [Obiettivo specifico 2]
  3. [Obiettivo specifico 3]

Inserire anche i requisiti iniziali che sono stati posti e/o necessari per il completamento degli obbiettivi.

## Descrizione del Progetto
[Descrivere il progetto, includendo informazioni dettagliate su cosa si intende realizzare, il contesto e l'importanza per l'azienda.]

## Ruoli e Responsabilità
| Nome                  | Ruolo                     | Responsabilità                           |
|-----------------------|---------------------------|--------------------------------------------|
| [Nome del Membro 1]   | [Ruolo del Membro 1]      | [Descrizione delle responsabilità]         |
| [Nome del Membro 2]   | [Ruolo del Membro 2]      | [Descrizione delle responsabilità]         |
| [Nome del Membro 3]   | [Ruolo del Membro 3]      | [Descrizione delle responsabilità]         |

## Timeline del Progetto
| Fase                  | Data di Inizio  | Data di Fine  | Stato        |
|-----------------------|----------------|---------------|--------------|
| [Fase 1: Analisi]     | [Data]         | [Data]        | [Completata/In Corso] |
| [Fase 2: Sviluppo]    | [Data]         | [Data]        | [Completata/In Corso] |
| [Fase 3: Test]        | [Data]         | [Data]        | [Completata/In Corso] |
| [Fase 4: Consegna]    | [Data]         | [Data]        | [Completata/In Corso] |

## Risorse
- **Budget**: [Inserire il budget previsto]
- **Strumenti e Software**: [Elencare gli strumenti e software necessari]
- **Personale Coinvolto**: [Numero di persone e competenze richieste]

E/o per le presentazioni, inserire le entità coinvolte nella comunicazionie, come avviene lo scambio di informazioni.

- **Hardware**: Rasberry Pi 4, Arduino, client windows
- **Software**: Python, Arduino sketch
- **Librerie**: `pybluez`, `flask`, `requests`, `pyserial`


## Rischi e Mitigazioni
Non sono  implementate importanti misura di sicurezza in questa dimostrazione:
    - Non sono implementate misure di autenticazione per l'API
    - Non è implementata alcuna crittografia per la comunicazione Bluetooth
    - Manca la validazione dei dati in ingresso
    - Non sono presenti controlli per evitare che un utente possa inviare dati falsi
    - Non sono presenti blocchi che evitano all'utente di killare il client.py o comunque di manipolalro

Tutte queste problematiche sono superabili, richiedono però ulteriore lavoro.


## Risultati Attesi
[Descrivere i risultati attesi al termine del progetto, come metriche di successo o benefici per l'azienda.]

## Problematcihe rimanenti
- il server Bluetooth deve essere eseguito con i permessi di amministratore, per limitazioni di pybluez
- Non viene utilizzato un database vero e proprio, ma un file JSON. Le prestazioni con molti dispositivi potrebbero essere limitate. La gestione dei dati con più server è difficoltosa.


## Conclusioni
[Inserire un riepilogo finale del progetto, includendo eventuali raccomandazioni per il futuro.]
