from flask import Flask, redirect, request, render_template, url_for

app = Flask(__name__)

@app.route("/")
def Login():
    return render_template("Login.html")

@app.route("/submit", methods=["POST"])
def Submit():
    Username = request.form.get("username")
    Password = request.form.get("password")
    
    if Username == "admin" and Password == "12345":
        return render_template("Welcome.html", name=Username)
    else:
        return render_template("Login.html", error="Invalid username or password")

@app.route("/logout")
def logout():
    return redirect(url_for("login"))

if __name__ == "__main__":
    app.run(debug=True)
