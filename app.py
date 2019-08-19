from flask import Flask, request, render_template
from flask_restful import Resource, Api


app = Flask(__name__)
api = Api(app)

@app.route('/')
def home():
  return render_template('index.html')

class Landing(Resource):
    def home():
      return render_template('index.html')

api.add_resource(Landing, '/')

app.run(port=5000, debug=True)
