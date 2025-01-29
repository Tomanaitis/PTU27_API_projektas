from models import db, Automobilis
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///automobiliai.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)
with app.app_context():
    db.create_all()


@app.route("/")
def home():
    search_text = request.args.get("searchlaukelis")
    if search_text:
        filtred_rows = Automobilis.query.filter(Automobilis.gamintojas.ilike(f"{search_text}%"))
        return render_template("index.html", automobiliai=filtred_rows)
    else:
        all_auto = Automobilis.query.all()
        return render_template("index.html", automobiliai=all_auto)


@app.route("/automobilis/<int:row_id>")
def one_car(row_id):
    auto = Automobilis.query.get(row_id)
    if auto:
        return render_template("one_car.html", automobilis=auto)
    else:
        return f"Automobilis su id {row_id} neegzistuoja"


@app.route("/automobilis/redaguoti/<int:row_id>", methods=["get", "post"])
def update_car(row_id):
    auto = Automobilis.query.get(row_id)
    if not auto:
        return f"Automobilis su id {row_id} neegzistuoja"

    if request.method == "GET":
        return render_template("update_car_form.html", automobilis=auto)

    elif request.method == "POST":
        gamintojas = request.form.get("gamintojaslaukelis")
        modelis = request.form.get("modelislaukelis")
        spalva = request.form.get("spalvalaukelis")
        price = float(request.form.get("kainalaukelis"))
        auto.gamintojas = gamintojas
        auto.modelis = modelis
        auto.spalva = spalva
        auto.kaina = price
        db.session.commit()
        return redirect(url_for("home"))


@app.route("/automobilis/trynimas/<int:row_id>", methods=["POST"])
def delete_car(row_id):
    auto = Automobilis.query.get(row_id)
    if not auto:
        return f"Automobilis su id {row_id} neegzistuoja"
    else:
        db.session.delete(auto)
        db.session.commit()
    return redirect(url_for("home"))


@app.route("/automobilis/naujas", methods=["GET", "POST"])
def create_car():
    if request.method == "GET":
        return render_template("create_car_form.html")
    if request.method == "POST":
        name = request.form.get("gamintojaslaukelis")
        model = request.form.get("modelislaukelis")
        color = request.form.get("spalvalaukelis")
        price = float(request.form.get("kainalaukelis"))
        if name and price:
            new_car = Automobilis(gamintojas=name, modelis=model, spalva=color, kaina=price)
            db.session.add(new_car)
            db.session.commit()
        return redirect(url_for('home'))


if __name__ == "__main__":
    app.run(port=5001, debug=True)
