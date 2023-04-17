from flask import Flask, request
import os
app = Flask(__name__)

@app.route('/defuse/<code>')
def checkCode(code=None):
	answers = os.getenv('answercodes')
	result = os.getenv('answerresult')
	if code in answers:
		return result
	else:
		return 'incorrect'
