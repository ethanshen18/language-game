# Import Flask
import flask
from yandex_translate import YandexTranslate
import json


# Create the application
app = flask.Flask(__name__)

@app.route('/')
def page():
	return flask.render_template('language.html')

@app.route('/game')
def gamePage():

	translate = YandexTranslate(readKey())
	translation = translate.translate('dog', 'en-fr')
	obj = json.dumps(translation)
	print(translation)
	return obj



def readKey():
	f = open("secrets.txt", "r")
	contents = f.read()
	return contents.strip()


if __name__ == '__main__':
	app.run(debug=True)