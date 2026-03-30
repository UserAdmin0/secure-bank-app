from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def home():
    return "Welcome to Secure Bank App"

@app.route('/login', methods=['GET'])
def login():
    username = request.args.get('username')
    password = request.args.get('password')

    if username == "admin" and password == "1234":
        return "Login Successful - Balance: 10,000"
    else:
        return "Invalid Credentials"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
