from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Startseite mit Formular
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Daten aus dem Formular sammeln
        name = request.form['name']
        datum = request.form['datum']
        baustelle = request.form['baustelle']
        verletzter = request.form['verletzter']
        notfall_art = request.form['notfall_art']
        verletztes_koerperteil = request.form['verletztes_koerperteil']
        beschreibung = request.form['beschreibung']
        
        # Speichere die Daten (z.B. in einer Datenbank oder Datei)
        # Hier nur als Beispiel: In einer Datei speichern
        with open('notfaelle.txt', 'a') as f:
            f.write(f"{name},{datum},{baustelle},{verletzter},{notfall_art},{verletztes_koerperteil},{beschreibung}\n")
        
        return redirect(url_for('index'))
    
    return render_template('index.html')

# Seite zur Auswertung
@app.route('/auswertung')
def auswertung():
    notfaelle = []
    with open('notfaelle.txt', 'r') as f:
        for line in f:
            notfaelle.append(line.strip().split(','))
    
    return render_template('auswertung.html', notfaelle=notfaelle)

if __name__ == '__main__':
    app.run(debug=True, port=8001)
    
