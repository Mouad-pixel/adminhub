from flask import Flask, request, jsonify
import random
import string

app = Flask(__name__)


def generate_code(length=5):
    characters = string.ascii_lowercase + string.digits
    return ''.join(random.choice(characters) for _ in range(length))


@app.route('/generate', methods=['POST'])
def generate():
    data = request.json
    difficulty = data.get('difficulty')
    code = generate_code()
    with open('codes.txt', 'a') as f:
        f.write(f'{code},{difficulty}\n')
    return jsonify({'code': code})


if __name__ == '__main__':
    app.run(debug=True)
