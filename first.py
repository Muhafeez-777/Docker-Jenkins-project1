from flask import Flask

app = Flask(__name__)

@app.route('/info')
def lw():
	return 'I am Abdul Muhafeez'

app.run(host='0.0.0.0')