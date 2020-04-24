from flask import Flask, render_template
app = Flask(__name__, template_folder='templates')

@app.route('/')
@app.route('/home')
def home():
    return render_template('home.hmtl')

@app.route('/about')
def about():
    return '<h1>About Page</h1>'

if __name__ == '__main__':
	app.run(debug=True)
