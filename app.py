from flask import Flask, request
import os
app = Flask(__name__)

@app.route('/defuse/<code>')
def checkCode(code=None):
	answers = os.getenv('answercodes')
	if code in answers:
		return 'correct, MH:next'
	else:
		return 'incorrect'
