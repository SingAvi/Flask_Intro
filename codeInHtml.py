from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route("/")
def hello_world():
    intern_head = "Graduate Fellowship"

    internship = ["StoreKey","Tata Steel","GigIndia","Google"]

    rendered_html =render_template("index.html",internheader = intern_head,internships = internship)


    return rendered_html



if __name__ == '__main__':
    app.run(debug=True)

