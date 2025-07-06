from flask import Flask

app = Flask(__name__)

def lw():
    return 'Hello from me!'
@app.route('/info')
def mom():
	return lw

app.run(host='0.0.0.0',port=5000)
