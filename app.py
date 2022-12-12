from flask import Flask, jsonify, request
import label
from flask_cors import CORS


app = Flask(__name__)
CORS(app)


@app.route('/get_labels', methods=['POST'])
def get_labels():
    json = request.get_json()
    # Need to ask if there is a better way to get this.
    embedding = json['embedding'].get('data').get('embedding')
    #embedding = embedding['data']
   # embedding = embedding['embedding']
    print(embedding)

    status, labels = label.label_image(embedding)
    return jsonify({'msg': status, 'labels': labels})


if __name__ == "__main__":
    app.run(debug=True, port=5000)
