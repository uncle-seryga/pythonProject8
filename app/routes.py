import flask

from app import app
import database


@app.route('/')
@app.route('/index')
def index():
    pattern = open("app/templates/product_cart.html", 'r').read()
    main = open('app/templates/index.html', 'r').read()
    print(main)
    all_data = database.get_all_from_base()
    htmlcode = ""
    for x in all_data:
        htmlcode += pattern % (x[1], x[2], x[4])
    text = main % (htmlcode,)
    open('app/static/index.html', 'w').write(text)
    return flask.render_template("index.html", dataset=htmlcode)
