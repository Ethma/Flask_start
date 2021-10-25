from flask import Flask, jsonify, render_template, request #importer les modules nécessaires

app = Flask(__name__)            #initialiser et donner un nom à l'application ici ce sera app

@app.route('/', methods=['GET', 'POST'])                  #définir une 1ere page (ou route) par défaut avec flask
def index():
		return render_template("home.html")

@app.route('/home/<name>')              #définir une 2ème page (ou route) avec flask
def home(name):
     return '<h1>Hello {}, you are on the home page!</h1>'.format(name)

@app.route('/json')               #définir une 3ème page avec un contenu personnalisé..
def json():
    return jsonify({'key' : 'value', 'listkey' : [1,2,3]})

@app.route('/contact', methods=['GET', 'POST'])
def contact():
	if request.method == 'GET':
		return render_template('post.html')
	else:
		text = request.form['text']
		return render_template('thx.html', message=text)

@app.route('/afficher')
@app.route('/afficher/<prenom>.<nom>')
def afficher(nom=None, prenom=None):
    if nom is None or prenom is None:
        return "Entrez votre nom et votre prénom comme il le faut dans l'url"
    return "Vous vous appelez {} {} !".format(prenom, nom)
if __name__ == '__main__':
    app.run()