from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/chatbot', methods=['POST'])
def chatbot():
    message = request.json['message']
    
    # Perform machine learning operations and generate a response
    response = "Hello, I am your chatbot."
    
    return jsonify({'message': response})

if __name__ == '__main__':
    app.run(debug=True)
