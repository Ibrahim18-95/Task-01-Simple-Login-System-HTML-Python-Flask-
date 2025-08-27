from flask import Flask , redirect , request , render_template 

app = Flask(__name__)

@app.route("/")
def Login():
    return render_template("Login.html")

@app.route("/submit", methods = ["post"])
def Submit():
    Username = request.form.get("username")
    Password = request.form.get("password")
    
    if Username == "Ibrahim" and Password == "ibr123":
        return render_template("Welcome.html", name = Username)
