from models import db, Automobilis
from flask import Flask, render_template, jsonify
from serializers import AutomobiliaiSchema

# from flask_cors import CORS

app = Flask(__name__)
# CORS(app)  # įgalina frontendą pasiekti endpointus iš kito serverio

# fizinės duomenų bazės - db, prijungimas, configas

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///automobiliai.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# paleidžiam db

db.init_app(app)
with app.app_context():
    db.create_all()


@app.route("/api/automobiliai")
def api_automobiliai():
    all_auto = Automobilis.query.all()
    auto_data = [{
        "id": auto.id,
        "name": auto.gamintojas,
        "model": auto.modelis,
        "color": auto.spalva,
        "price": auto.kaina
    } for auto in all_auto]
    return jsonify(auto_data)



if __name__ == "__main__":
    app.run()
