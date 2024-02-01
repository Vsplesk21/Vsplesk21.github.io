from flask import Flask, render_template, request, flash

app = Flask(__name__)

@app.route("/")
@app.route("/index")
def index():
    return render_template("index.html")
@app.route("/BMW")
def BMW():
    return render_template("BMW.html")
@app.route("/Mercedes")
def Mercedes():
    return render_template("Mercedes.html")
@app.route("/Audi")
def Audi():
    return render_template("Audi.html")
@app.route("/Volkswagen")
def Volkswagen():
    return render_template("Volkswagen.html")
@app.route("/About")
def About():
    return render_template("About.html")

if __name__=="__main__":
    app.run(debug=True)