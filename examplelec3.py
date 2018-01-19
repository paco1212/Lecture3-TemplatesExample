from flask import Flask, request, render_template, url_for

app = Flask(__name__)

@app.route('/oranges')
def lemons():
    title_var = "My Ice Cream Form"
    options = ["Vanilla", "Chocolate","Pistachio", "So many others!!!!"]
    return render_template('seeform.html',title=title_var, lst_stuff=options)

@app.route('/apples')
def plants():
    if request.method == "GET":
        name = request.args.get('name')
        name_len = len(name)
        flavor_options = []
        for k in request.args:
            if k != "name":
                flavor_options.append(request.args[k])
    return render_template('results.html',flavors=flavor_options, name_len=name_len, name=name)


if __name__ == "__main__":
    app.run(use_reloader=True,debug=True)
