from flask import Flask, request
import os
app = Flask(__name__)

@app.route('/defuse/<code>')
def checkCode(code):
	answers = os.getenv('answercodes')
	if code in "123":
		return 'correct code - {0} and answers - {1}'.format(code,answers)
	return 'incorrect'
