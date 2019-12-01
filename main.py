# Import Flask
import json
import flask
from yandex_translate import YandexTranslate

# Create the application
app = flask.Flask(__name__)

@app.route('/')
def page():
	lang = 'en-fr'
	
	key = 'dog'
	op1 = 'dog'
	op2 = 'dog'
	op3 = 'dog'
	op4 = 'dog'
	op5 = 'dog'

	translate = YandexTranslate(readKey())
	translation = translate.translate(key, lang)
	return flask.render_template('index.html', word = translation['text'][0].upper(), op1 = op1, op2 = op2, op3 = op3, op4 = op4, op5 = op5)

def readKey():
	f = open("secrets.txt", "r")
	contents = f.read()
	return contents.strip()

if __name__ == '__main__':
	app.run(debug=True)