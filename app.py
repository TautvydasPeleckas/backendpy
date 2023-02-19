from flask import Flask, request
app = Flask(__name__)

@app.route('/defuse')
def checkCode():
	code = request.args.get('code')
	if code == "123":
		return 'correct'
	return 'incorrect'
