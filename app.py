from flask import Flask, redirect, render_template, request,make_response

app = Flask(__name__)

items = ["Python","Flask","MySQL","Html5","Django"]


@app.route("/index")
def index():
    user_ip_information = request.remote_addr
    response = make_response(redirect("/information"))
    response.set_cookie("user_ip_information",user_ip_information)   
    return response

@app.route("/information")
def informattion():
    user_ip = request.cookies.get("user_ip_information")
    context = {
        "user_ip": user_ip,
        "items":items
    }
    return render_template("infortmation.html",**context)



app.run(debug=True)