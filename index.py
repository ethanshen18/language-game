import json
import flask
import random
import requests
from yandex_translate import YandexTranslate

app = flask.Flask(__name__)

@app.route('/')
@app.route('/<lang>')
def page(lang = 'Chinese'):
	if lang == 'Chinese': code = 'en-zh'
	elif lang == 'French': code = 'en-fr'
	elif lang == 'German': code = 'en-de'
	elif lang == 'Italian': code = 'en-it'
	elif lang == 'Japanese': code = 'en-ja'
	elif lang == 'Korean': code = 'en-ko'
	else: 
		lang = 'Chinese'
		code = 'en-zh'

	global language
	language = lang

	file = open('words.txt', 'r')
	words = file.readlines()
	file.close()

	global key
	key = words[random.randint(0, len(words))]
	op1 = words[random.randint(0, len(words))]
	op2 = words[random.randint(0, len(words))]
	op3 = words[random.randint(0, len(words))]
	op4 = words[random.randint(0, len(words))]
	op5 = words[random.randint(0, len(words))]

	global correct 
	correct = random.randint(1, 5)
	if correct == 1: op1 = key
	if correct == 2: op2 = key
	if correct == 3: op3 = key
	if correct == 4: op4 = key
	if correct == 5: op5 = key

	global translation
	translation = YandexTranslate(readKey()).translate(key, code)['text'][0]

	return flask.render_template('layout.html', word = translation, language = language, op1 = op1, op2 = op2, op3 = op3, op4 = op4, op5 = op5)

@app.route("/option1/", methods=['POST'])
def option1(): return showResult(1)

@app.route("/option2/", methods=['POST'])
def option2(): return showResult(2)

@app.route("/option3/", methods=['POST'])
def option3(): return showResult(3)

@app.route("/option4/", methods=['POST'])
def option4(): return showResult(4)

@app.route("/option5/", methods=['POST'])
def option5(): return showResult(5)

@app.route("/next/", methods=['POST'])
def next(): return page(language);

def showResult(ans):
	if correct == ans: return flask.render_template('layout.html', word = 'CORRECT', language = language, answer = key, original = translation);
	return flask.render_template('layout.html', word = 'WRONG', language = language, answer = key, original = translation);

def readKey():
	file = open('key.txt', 'r')
	contents = file.read()
	file.close()
	return contents.strip()

if __name__ == '__main__':
	app.run(debug=True)