# Import Flask
import flask
from yandex_translate import YandexTranslate
import json


# Create the application
app = flask.Flask(__name__)

@app.route('/')
def page():
	translate = YandexTranslate(readKey())
	translation = translate.translate('dog', 'en-fr')
	return flask.render_template('language.html', word=translation['text'][0].upper())

def readKey():
	f = open("secrets.txt", "r")
	contents = f.read()
	return contents.strip()

if __name__ == '__main__':
	app.run(debug=True)