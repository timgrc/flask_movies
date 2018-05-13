from flask import Flask, jsonify

app = Flask(__name__)

# Config options - Make sure you created a 'config.py' file.
app.config.from_object('config')
# To get one variable, tape app.config['MY_VARIABLE']

@app.route('/')
@app.route('/index/')
def index():
  return "index"


@app.route('/recommend/<int:id_film>/')
def content(id_film):
  inputs  = {
    "_input": [
      {"id_film": id_film}
    ]
  }

  results = {
    "_results": [
      { "id": "645657", "name": "Eternal sunshine of the spotless mind" },
      { "id": "543556", "name": "500 Days of Summer" },
      { "id": "873453", "name": "Lost in Translation" }
    ]
  }
  return jsonify(inputs)
  #return jsonify(results)
