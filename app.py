from flask import Flask, render_template, request, url_for, flash, redirect
import time

app = Flask(__name__)
app.config['SECRET_KEY'] = '384af699fdc6dff9e4305beb59ca89dd670ee72f10b253c1'
message = []

@app.route('/', methods=('GET', 'POST'))
def index():
    if request.method == 'POST':
        content = request.form['content']
        if not content:
            flash('Content is required!')
        else:
            message.append(content)
            return redirect(url_for('sending'))
    return render_template('index.html')


@app.route('/received/', methods=('GET', 'POST'))
def received():
    message.clear()
    if request.method == 'POST':
        return redirect(url_for('index'))
    return render_template('received.html')


@app.route('/sending/')
def sending():
    return render_template('sending.html', message=message[0])