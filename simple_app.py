from flask import Flask
from flask import render_template_string

app = Flask(__name__)

@app.route('/')
def hello_world():
    headline_value = "Graduate Fellowship"
    htmlpage = """
    <html>
    <h1>
    Know My {{headline}}!
    </h1>
    </html>
    """

    render_page = render_template_string(htmlpage,headline= headline_value)

#   return htmlPage.format(expertise_list_ul=expertise_list)

    return render_page




if __name__ == '__main__':
    app.run(debug=True)

