from flask import Flask, render_template, request

app = Flask("Greentown")

@app.route('/')
def home():
    return render_template('accueil.html')


@app.route('/ville')
def ville():
    ville_nom = request.args.get('ville')
    ville = ' '.join(ville_nom.split('_'))
    return render_template('ville.html', ville=ville, ville_nom=ville_nom)


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000)