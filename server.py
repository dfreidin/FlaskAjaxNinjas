from flask import Flask, render_template, request, jsonify
app = Flask(__name__)
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 60
@app.route("/")
def index():
    return render_template("index.html")
@app.route("/color", methods=["GET"])
def colors():
    print request
    c = request.args["color"]
    if c == "red":
        name = "Raphael"
        file = "raphael.jpg"
    elif c == "blue":
        name = "Leonardo"
        file = "leonardo.jpg"
    elif c == "orange":
        name = "Michelangelo"
        file = "michelangelo.jpg"
    elif c == "purple":
        name = "Donatello"
        file = "donatello.jpg"
    else:
        name = "an invalid color"
        file = "notapril.jpg"
    return jsonify(name=name, file=file)
app.run(debug=True)