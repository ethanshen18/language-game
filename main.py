# Import Flask
import flask

# Create the application
app = flask.Flask(__name__)

@app.route('/')
def page():
	return flask.render_template('language.html')


if __name__ == '__main__':
    app.run(debug=True)