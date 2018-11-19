from flask import Flask, render_template

app = Flask(__name__)

@app.route('/init')
def homepage():
        user = 'Harald'
        title = 'Home'
        return render_template('init.html', user=user, title=title)

app.run()