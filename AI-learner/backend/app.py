from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/submit-email', methods=['POST'])
def submit_email():
    data = request.get_json()
    user_email = data.get("email", "")
    print(f"Received stored email: {user_email}")
    return jsonify({"message": f"Stored email '{user_email}' received successfully!"})

if __name__ == '__main__':
    app.run(debug=True)