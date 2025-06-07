import pandas as pd                                                                                                                                 # Importa la libreria pandas per la manipolazione e l'analisi dei dati.
import numpy as np                                                                                                                                  # Importa la libreria numpy per operazioni numeriche, anche se qui non è usata direttamente.
import matplotlib.pyplot as plt                                                                                                                     # Importa pyplot da matplotlib per creare visualizzazioni e grafici.
import seaborn as sns                                                                                                                               # Importa la libreria seaborn per creare grafici statistici più accattivanti.


def load_and_preprocess_data(filepath: str) -> pd.DataFrame:                                                                                        # Definisce una funzione per caricare e preprocessare i dati da un file CSV.
    """
    Carica i dati, converte le date con fusi orari misti in UTC,
    imposta l'indice e calcola le feature.
    """
    df = pd.read_csv(filepath)                                                                                                                      # Legge i dati dal file CSV specificato in un DataFrame pandas.

    # Aggiungiamo utc=True per gestire i fusi orari misti.
    # Questo converte tutte le date allo standard UTC, creando un indice coerente.
    df['Date'] = pd.to_datetime(df['Date'], errors='coerce', utc=True)                                                                              # Converte la colonna 'Date' in oggetti datetime, unificando i fusi orari in UTC.

    df.dropna(subset=['Date'], inplace=True)                                                                                                        # Rimuove le righe con date non valide (NaT) per garantire la coerenza dei dati.
    df.set_index('Date', inplace=True)                                                                                                              # Imposta la colonna 'Date' come indice del DataFrame per facilitare le analisi temporali.
    df.sort_index(inplace=True)                                                                                                                     # Ordina il DataFrame in base all'indice temporale, essenziale per calcoli sequenziali.

    df['daily_return'] = df['Close'].pct_change()                                                                                                   # Calcola il rendimento percentuale giornaliero basato sulla variazione del prezzo di chiusura.

    # Ora df.index è un DatetimeIndex in UTC e avrà gli attributi corretti.
    df['Year'] = df.index.year                                                                                                                      # Estrae l'anno dall'indice datetime per future aggregazioni e analisi.
    df['Month'] = df.index.month                                                                                                                    # Estrae il mese dall'indice datetime per raggruppamenti mensili.
    df['Weekday'] = df.index.day_name()                                                                                                             # Estrae il nome del giorno della settimana dall'indice per analisi specifiche.

    df.dropna(subset=['daily_return'], inplace=True)                                                                                                # Rimuove la prima riga che ha un rendimento NaN (non calcolabile).
    return df                                                                                                                                       # Restituisce il DataFrame preprocessato, arricchito e pronto per l'analisi.


def get_period_return(series: pd.Series, period: str) -> pd.Series:                                                                                 # Definisce una funzione per calcolare il rendimento su un dato periodo.
    """
    Calcola il rendimento periodico (mensile o annuale) aggregato.
    """
    return series.resample(period).apply(lambda x: (x[-1] / x[0]) - 1) * 100                                                                        # Raggruppa la serie per periodo (es. 'M' o 'Y') e calcola il rendimento totale.

def analyze_weekday_performance(daily_returns: pd.Series) -> pd.DataFrame:                                                                          # Definisce una funzione per analizzare la performance media per giorno della settimana.
    """
    Analizza il rendimento medio per giorno della settimana.
    """
    weekday_returns = daily_returns.groupby(daily_returns.index.day_name()).mean()                                                                  # Raggruppa i rendimenti giornalieri per giorno della settimana e ne calcola la media.
    days_order = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']                                                     # Definisce l'ordine corretto dei giorni per una visualizzazione logica.
    return weekday_returns.reindex(days_order).dropna() * 100                                                                                       # Riordina i risultati secondo 'days_order', rimuove i giorni non lavorativi e converte in %.

def find_extreme_days(daily_returns: pd.Series, n: int = 5):                                                                                        # Definisce una funzione per trovare i giorni con rendimenti estremi.
    """
    Trova i giorni con i rendimenti migliori e peggiori.
    """
    top_days = daily_returns.nlargest(n) * 100                                                                                                      # Trova i 'n' giorni con i rendimenti più alti e li converte in percentuale.
    worst_days = daily_returns.nsmallest(n) * 100                                                                                                   # Trova i 'n' giorni con i rendimenti più bassi e li converte in percentuale.
    return top_days, worst_days                                                                                                                     # Restituisce due DataFrame contenenti rispettivamente i giorni migliori e peggiori.

def plot_price_and_volume(df: pd.DataFrame, title: str):                                                                                            # Definisce una funzione per plottare l'andamento del prezzo e dei volumi.
    """
    Crea un grafico con l'andamento del prezzo di chiusura e dei volumi.
    """
    fig, axes = plt.subplots(2, 1, figsize=(14, 8), sharex=True, gridspec_kw={'height_ratios': [3, 1]})                                             # Crea una figura Matplotlib con due subplot verticali, uno più grande per il prezzo.
    fig.suptitle(f'Andamento Prezzo e Volumi - {title}', fontsize=16)                                                                               # Imposta un titolo principale per l'intera figura.

    # Grafico del prezzo
    axes[0].plot(df.index, df['Close'], label='Prezzo di Chiusura', color='navy')                                                                   # Disegna il grafico a linee del prezzo di chiusura nel primo subplot (in alto).
    axes[0].set_ylabel('Prezzo di Chiusura')                                                                                                        # Imposta l'etichetta per l'asse Y del primo subplot.
    axes[0].grid(True, linestyle='--', alpha=0.6)                                                                                                   # Aggiunge una griglia semi-trasparente per una migliore leggibilità.
    axes[0].legend()                                                                                                                                # Mostra la legenda del grafico.

    # Grafico dei volumi
    axes[1].bar(df.index, df['Volume'], label='Volume di Scambi', color='gray', alpha=0.7)                                                          # Disegna un grafico a barre per i volumi di scambio nel secondo subplot (in basso).
    axes[1].set_ylabel('Volume')                                                                                                                    # Imposta l'etichetta per l'asse Y del secondo subplot.
    axes[1].set_xlabel('Data')                                                                                                                      # Imposta l'etichetta per l'asse X, condiviso con il primo grafico.
    axes[1].grid(True, linestyle='--', alpha=0.6)                                                                                                   # Aggiunge una griglia anche al secondo grafico.
    axes[1].legend()                                                                                                                                # Mostra la legenda per il grafico dei volumi.

    plt.tight_layout(rect=[0, 0, 1, 0.96])                                                                                                          # Ottimizza la disposizione dei grafici per evitare sovrapposizioni e fare spazio al titolo.
    plt.show()                                                                                                                                      # Mostra a schermo la figura completa con entrambi i grafici.

def plot_returns_histogram(daily_returns: pd.Series, title: str, bins: int = 50):                                                                   # Definisce una funzione per visualizzare la distribuzione dei rendimenti.
    """
    Crea un istogramma della distribuzione dei rendimenti giornalieri.
    """
    plt.figure(figsize=(12, 6))                                                                                                                     # Crea una nuova figura Matplotlib con le dimensioni specificate.
    sns.histplot(daily_returns * 100, bins=bins, kde=True, color='teal')                                                                            # Usa Seaborn per disegnare un istogramma con una curva di densità (KDE).
    plt.title(f'Distribuzione dei Rendimenti Giornalieri - {title}', fontsize=16)                                                                   # Imposta il titolo del grafico.
    plt.xlabel('Rendimento Giornaliero (%)')                                                                                                        # Imposta l'etichetta per l'asse X.
    plt.ylabel('Frequenza')                                                                                                                         # Imposta l'etichetta per l'asse Y.
    plt.grid(True, linestyle='--', alpha=0.6)                                                                                                       # Aggiunge una griglia per facilitare la lettura dei valori.
    plt.show()                                                                                                                                      # Mostra il grafico a schermo.
