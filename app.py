from flask import Flask, request, jsonify, render_template
from flask_restful import Api
from logic import Add, Subtract, Multiply, Divide

app = Flask(__name__)
api = Api(app)

# API endpoints
api.add_resource(Add, "/add")
api.add_resource(Subtract, "/subtract")
api.add_resource(Multiply, "/multiply")
api.add_resource(Divide, "/division")

# Web UI
@app.route('/')
def home():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0")
