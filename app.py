from flask import Flask, render_template, request
from caesar_cipher import caesar_cipher

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    result = None
    if request.method == 'POST':
        message = request.form['message']
        shift = int(request.form['shift'])
        action = request.form['action']
        if action == '1':
            action = 'encrypt'
        elif action == '2':
            action = 'decrypt'
        else:
            return 'Invalid action. Please enter 1 for encrypt or 2 for decrypt.'
        result = caesar_cipher(message, shift, action)
    return render_template('index.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)
