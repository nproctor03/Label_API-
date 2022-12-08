from flask import Flask, jsonify, request
import label


app = Flask(__name__)



@app.route('/get_labels', methods=['POST'])
def get_labels():
    json = request.get_json()
    embedding = json['embedding']
    #print(embedding)


    status, labels = label.label_image(embedding)
    return jsonify({'msg': status, 'labels': labels})



if __name__ == "__main__":
    app.run(debug=True, port=6000)