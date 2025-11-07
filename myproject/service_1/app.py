from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

@app.route('/add', methods=['POST'])
def add_numbers():
    data = request.json
    num1 = data['num1']
    num2 = data['num2']
    result = num1 + num2
    return jsonify({"result": result})

@app.route('/send_to_service_2', methods=['POST'])
def send_to_service_2():
    data = request.json
    result = data['result']
    # Отправляем результат на второй сервис
    response = requests.post('http://service_2:8081/subtract', json={'num1': result, 'num2': 10})
    return jsonify(response.json())

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)
