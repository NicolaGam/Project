# House Price Prediction
Il progetto ha l'obbiettivo di creare un modello di machine learning in grado di prevedere i prezzi delle case basandoci su alcune variabili presenti nel datase. 
Verrà inoltre costruita un'interfaccia web per una più facile consultazione del utente.
Infine sviluppo una mappa interattiva dei prezzi di tutte le abitazioni presenti nel dataset.

# Modello
il modello che ho deciso di costruire è una Random Forest la quale, essendo un modello molto robusto, non richiede alcun tipo di preprocessing iniziale. 
sono stati costruiti complessivamente due modelli:

- il primo è in grado di predire il prezzo basandosi sulla posizione geografica della casa (longitudine e latitudine)

- il secondo è in grado di predire il valore della casa basandosi sulla distanza dalla stazione MRT più vicina, dal numero di mini market nei dintorni e dall'età della casa

l'utente potrà quindi scegliere quale modello utilizzare per svolgere l'operazione di previsione.

# Dataset
Le variabili presenti nel dataset elencate qui sotto sono riferite alle abitazioni di un distretto del taiwan (motivo per cui nel modello che utilizza la posizione geografica ho limitato i valori in quell'area):
- Latitudine
- Longitudine
- Età dell'abitazione
- Distanza dalla stazione MRT più vicina
- Numero di minimarket nelle vicinanze
- Prezzo per ogni unità di area

# Come eseguire il codice 
1. scaricare la cartella e visualizzarla nel explorer di VsCode
2. aprire il terminale (cntrl j) e utilizzare il comando python main.py per fittare i modelli specificati in precedenza (facendo attenzione di trovarci nella cartella scripts prima di eseguirlo)
3. visualizzare la web app eseguendo il comando streamlit run ui.py
4. selezionare la pillola relativa al modello (e quindi alle variabili) che si intende utilizzare per ottenere il valore della casa
5. inserire i dati richiesti e premere il tasto "Calcola" per visualizzare il valore dell'abitazione

# Mappa interattiva
la mappa presenta tutte le abitazioni, le abitazioni più costose verranno rappresentate in rosso e con dimensione maggiore mentre le più economiche saranno oro e più piccole.
nella dashboard troviamo due filtri con cui l'utente può interagire:
1. permette di visualizzare solo le abitazioni in un certo range di prezzo
2. permette di vedere solo le abitazioni che si trovano a una data distanza dalla stazione MRT più vicina

per consultare la mappa è sufficiente utilizzare il seguente link:
https://public.tableau.com/shared/P5Q6D7JWP?:display_count=n&:origin=viz_share_link
