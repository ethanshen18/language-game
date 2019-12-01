# Import Flask
import json
import flask
import random
from yandex_translate import YandexTranslate

# Create the application
app = flask.Flask(__name__)

@app.route('/')
def page():
	lang = 'en-zh'

	file = open('ENwords.txt', 'r')
	words = file.readlines()
	file.close()

	rand = random.randint(0, len(words))

	key = words[rand]
	op1 = words[rand]
	op2 = words[rand]
	op3 = words[rand]
	op4 = words[rand]
	op5 = words[rand]
	translate = YandexTranslate(readKey())
	translation = translate.translate(key, lang)
	return flask.render_template('index.html', word = translation['text'][0], 
		op1 = op1, op2 = op2, op3 = op3, op4 = op4, op5 = op5)

def readKey():
	f = open("secrets.txt", "r")
	contents = f.read()
	return contents.strip()

if __name__ == '__main__':
	app.run(debug=True)