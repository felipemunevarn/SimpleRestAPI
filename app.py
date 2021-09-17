from flask import Flask, jsonify, request

from characters import characters

app = Flask(__name__)

@app.route('/ping', methods=['GET'])
def ping():
    return jsonify({"message": "Pong!"})

@app.route('/characters')
def getCharacters():
    return jsonify({"characters": characters, "message":"Character's List"})

@app.route('/characters/<string:character_name>')
def getCharacter(character_name):
    characterFound = [character for character in characters if character['name']== character_name]
    if(len(characterFound) > 0):
        return jsonify({"product": characterFound[0]})
    return jsonify({"message":"Character not found"})

@app.route('/characters', methods=['POST'])
def addCharacter():
    new_character = {
        "name": request.json['name'],
        "movie": request.json['movie'],
        "age": request.json['age']
    }
    characters.append(new_character)
    return jsonify({"characters": characters, "message":"Character added succesfully"})

@app.route('/characters/<string:character_name>', methods=['PUT'])
def editCharacter(character_name):
    characterFound = [character for character in characters if character['name']== character_name]
    if(len(characterFound) > 0):
        characterFound[0]['name'] = request.json['name']
        characterFound[0]['movie'] = request.json['movie']
        characterFound[0]['age'] = request.json['age']
        return jsonify({
            "message": "Character Updated",
            "character": characterFound[0]
        })
    return jsonify({"message":"Character not found"})

@app.route('/characters/<string:character_name>', methods=['DELETE'])
def deleteCharacter(character_name):
    characterFound = [character for character in characters if character['name']== character_name]
    if(len(characterFound) > 0):
        characters.remove(characterFound[0])
        return jsonify({
            "message": "Character Deleted",
            "characters": characters
        })
    return jsonify({"message":"Character not found"})

if __name__ == '__main__':
    app.run(debug = True, port = 4000)