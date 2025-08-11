from flask import Flask, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # handle calculation
        return "Calculation done"
    return '''
        <form method="POST">
            <input type="text" name="number">
            <input type="submit">
        </form>
    '''

if __name__ == '__main__':
    app.run(debug=True)
