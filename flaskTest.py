from flask import Flask, request, render_template
import subprocess




app = Flask(__name__)

mode = 0
breatheSetting = "red"
modeChange = False

@app.route("/", methods=['GET', 'POST'])
def status():
    global mode
    global breatheSetting
    global modeChange
    
    if request.method == 'GET':
        return str(mode)
    if request.method == 'POST':
        mode = request.form['mode']
        return str(mode)
    else:
        return "error"

@app.route("/settings", methods=['GET', 'POST'])
def settings():
    global mode
    global breatheSetting
    global modeChange
    
    if request.method == 'GET':
        return "mode: "+str(mode)+" b: "+breatheSetting+" modeChange: "+ str(modeChange)
    if request.method == 'POST':
        mode = request.form['num']
        breatheSetting = request.form['breatheSetting']
        modeChange = True
        return str(mode)
    else:
        return "error"

@app.route("/dashboard", methods=['GET', 'POST'])
def dashboard():
    global mode
    global breatheSetting
    global modeChange
    
    if request.method == 'GET':
        return render_template("dashboard.html")
    if request.method == 'POST':
        mode = request.form['mode']

        modeChange = True
        return render_template("dashboard.html")
    else:
        return "error"



if __name__ == "__main__":
    app.run(host = "0.0.0.0", port = "5000")
    
