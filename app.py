import os                       # Biblioteca pentru manipularea fisierelor si directoarelor
import pandas as pd             # Biblioteca pentru manipularea datelor in format tabelar (CSV, Excel etc.)
import matplotlib.pyplot as plt # Biblioteca pentru crearea si personalizarea graficelor
from flask import Flask, render_template, send_file  # Importam modulele necesare pentru aplicatia Flask
import io                       # Biblioteca pentru manipularea fluxurilor de intrare/iesire in memorie

# Cream o instanta a aplicatiei Flask, utilizata pentru definirea rutelor si functionalitatilor aplicatiei
app = Flask(__name__)

# Definim calea absoluta catre fisierul CSV
FILE_PATH = os.path.join(os.getcwd(), 'data.csv')

# Setam backend-ul matplotlib pentru a functiona fara interfata grafica (necesar in aplicatii web)
plt.switch_backend('Agg')

# Ruta principala care returneaza un template HTML
@app.route("/")
def home():
    return render_template("index.html")  # Incarca fisierul HTML `index.html` din directorul `templates`

# Ruta care genereaza graficele in functie de valoarea parametrului `plot_id`
@app.route("/plot/<int:plot_id>")
def plot(plot_id):
    plt.figure(figsize=(15, 5))  # Configuram dimensiunea graficelor

    df = pd.read_csv(FILE_PATH)  # Citim fisierul CSV si il incarcam intr-un DataFrame pandas

    # Generam graficul corespunzator pentru `plot_id`
    if plot_id == 0:
        df.plot()  # Grafic cu toate coloanele din DataFrame
        plt.title("Toate valorile")  # Titlul graficului
    elif plot_id == 1:
        df.head(6).plot(style=['b--', 'r-', 'g:', 'm'])  # Grafic cu primele 6 randuri
        plt.title("Primele 6 valori")  
    elif plot_id == 2:
        df[['Durata', 'Puls']].tail(12).plot(color=['red', 'blue'])  # Grafic cu ultimele 12 valori pentru coloanele `Durata` si `Puls`
        plt.title("Ultimele 12 valori")  

    buf = io.BytesIO()              # Cream un buffer de memorie pentru a salva imaginea graficului
    plt.savefig(buf, format="png")  # Salvam graficul in buffer in format PNG
    buf.seek(0)                     # Mutam cursorul la inceputul buffer-ului pentru a putea citi continutul
    plt.close()                     # Inchidem figura matplotlib pentru a elibera resursele

    return send_file(buf, mimetype="image/png")  # Returnam imaginea generata clientului sub forma de fisier PNG

# Pornim serverul Flask pentru a rula aplicatia
if __name__ == "__main__":
    app.run(debug=True)  # Activam modul debug pentru reimprospatare automata si afisare de erori detaliate
