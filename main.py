# Import Flask
import json
import flask
import random
import requests
from yandex_translate import YandexTranslate

# Create the application
app = flask.Flask(__name__)

@app.route('/')
def page():
	lang = 'en-zh'

	file = open('ENwords.txt', 'r')
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
	translation = YandexTranslate(readKey()).translate(key, lang)['text'][0]

	return flask.render_template('question.html', word = translation, op1 = op1, op2 = op2, op3 = op3, op4 = op4, op5 = op5)

@app.route("/option1/", methods=['POST'])
def option1():
	if correct == 1: return flask.render_template('result.html', word = 'CORRECT', answer = key, original = translation);
	return flask.render_template('result.html', word = 'WRONG', answer = key, original = translation);

@app.route("/option2/", methods=['POST'])
def option2():
	if correct == 2: return flask.render_template('result.html', word = 'CORRECT', answer = key, original = translation);
	return flask.render_template('result.html', word = 'WRONG', answer = key, original = translation);

@app.route("/option3/", methods=['POST'])
def option3():
	if correct == 3: return flask.render_template('result.html', word = 'CORRECT', answer = key, original = translation);
	return flask.render_template('result.html', word = 'WRONG', answer = key, original = translation);

@app.route("/option4/", methods=['POST'])
def option4():
	if correct == 4: return flask.render_template('result.html', word = 'CORRECT', answer = key, original = translation);
	return flask.render_template('result.html', word = 'WRONG', answer = key, original = translation);

@app.route("/option5/", methods=['POST'])
def option5():
	if correct == 5: return flask.render_template('result.html', word = 'CORRECT', answer = key, original = translation);
	return flask.render_template('result.html', word = 'WRONG', answer = key, original = translation);

@app.route("/next/", methods=['POST'])
def next():
	return page();

def readKey():
	file = open("secrets.txt", "r")
	contents = file.read()
	file.close()
	return contents.strip()

if __name__ == '__main__':
	app.run(debug=True)