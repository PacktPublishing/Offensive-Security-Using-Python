from flask import Flask, request, jsonify

app = Flask(__name__)
users = {
'123': {'username': 'alice', 'email':'alice@example.com'},
'124': {'username': 'bob', 'email':'bob@example.com'}
}

@app.route('/user', methods=['GET'])
def get_user():
    user_id = request.args.get('id')
    user_data = users.get(user_id)
    return jsonify(user_data)
    
if __name__ == '__main__':
    app.run(debug=True)