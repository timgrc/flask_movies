from flask import Flask, render_template

app = Flask(__name__)

# Config options - Make sure you created a 'config.py' file.
app.config.from_object('config')
# To get one variable, tape app.config['MY_VARIABLE']

@app.route('/')
@app.route('/index/')
def index():
  return render_template('index.html')


@app.route('/recommend/<int:id_film>/')
def content(id_film):
  return '%s' % id_film
