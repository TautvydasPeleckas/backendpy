from flask import Flask, request
from flask_cors import CORS

import os
app = Flask(__name__)
CORS(app)

@app.route('/defuse')
def checkCode(code=None):
	args = request.args
	code = args.get('code')
	answers = os.getenv('answercodes')
	result = os.getenv('answerresult')
	print(code)
	print('-')
	print(answers)
	if code == answers:
		return result
	else:
		return 'TRY AGAIN...'
