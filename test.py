from flask import Flask
import json

app = Flask(__name__)
@app.route('/')

def filecheck():

def filewrite():
    # Data to be written
    dictionary = {
        "name": "sathiyajith",
        "rollno": 56,
        "cgpa": 8.6,
        "phonenumber": "9976770500"
    }

    # Serializing json
    json_object = json.dumps(dictionary, indent=4)

    # Writing to sample.json
    with open("sample.json", "w") as outfile:
        outfile.write(json_object)

        


def hello_world():
    return 'hello test'
if __name__ == '__main__':
    app.run()

