from flask import Flask, request
import os
app = Flask(__name__)

@app.route('/defuse')
def checkCode(code=None):
	args = request.args
    	code = args.get('code')
	answers = os.getenv('answercodes')
	result = os.getenv('answerresult')
	if code == answers:
		return result
	else:
		return 'incorrect'
