from flask import Flask

app = Flask(__name__)

@app.route('/')
def random_function():
    htmlPage = """
    <html>
    <h1>
    Google is my dream company
    <h1>
    {expertise_list_ul}
    </html>
    """

    expertise = ["Android","Python","UI | UX Designing"]
    expertise_list = "<ul>"
    expertise_list += "\n".join(["<li>{expert}</li>".format(expert=expert) for expert in expertise])
    expertise_list +="<ul>"
    print(expertise_list)

    return htmlPage.format(expertise_list_ul=expertise_list)


if __name__ == '__main__':
    app.run(debug=True)

