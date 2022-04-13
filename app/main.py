from flask import Flask, render_template, request, redirect, url_for
import block

app = Flask(__name__)

@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        sender = request.form['sender']
        amount = request.form['amount']
        recipient = request.form['recipient']

        block.write_block(name=sender, amount=amount, whom_to=recipient)
        return redirect(url_for('index'))
    return render_template('index.html')
@app.route('/checking', methods=['GET'])
def check():
    results = block.check_integrity()
    return render_template('index.html', results=results)

if __name__ == '__main__':
    app.run(debug=True)
