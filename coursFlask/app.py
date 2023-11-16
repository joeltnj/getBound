from flask import Flask, render_template, redirect, url_for

app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template("index.html")

@app.route('/user/<username>')
def show_user_profile(username):
    return render_template('page/user_profile.html', username=username)

@app.route('/redirect')
def redirect_example():
    # Redirige vers la route '/user/john'
    return redirect(url_for('show_user_profile', username='johnmoiiie'))

if __name__ == '__main__':
    app.run(debug=True)
