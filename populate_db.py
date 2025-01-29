from models import Automobilis, db
from app import app

with app.app_context():
    automobiliai = [
        Automobilis(gamintojas="Toyota", modelis="Corolla", spalva="Juoda", kaina="18000"),
        Automobilis(gamintojas="Volkswagen", modelis="Golf", spalva="Balta", kaina="20000"),
        Automobilis(gamintojas="BMW", modelis="3 Series", spalva="Sidabrinė", kaina="25000"),
        Automobilis(gamintojas="Mercedes-Benz", modelis="C-Class", spalva="Pilka", kaina="27000"),
        Automobilis(gamintojas="Audi", modelis="A4", spalva="Mėlyna", kaina="26000"),
        Automobilis(gamintojas="Honda", modelis="Civic", spalva="Raudona", kaina="19000"),
        Automobilis(gamintojas="Ford", modelis="Focus", spalva="Juoda", kaina="17000"),
        Automobilis(gamintojas="Nissan", modelis="Qashqai", spalva="Pilka", kaina="23000"),
        Automobilis(gamintojas="Hyundai", modelis="Tucson", spalva="Balta", kaina="24000"),
        Automobilis(gamintojas="Kia", modelis="Sportage", spalva="Raudona", kaina="22000"),
        Automobilis(gamintojas="Peugeot", modelis="3008", spalva="Juoda", kaina="21000"),
        Automobilis(gamintojas="Renault", modelis="Megane", spalva="Sidabrinė", kaina="18000"),
        Automobilis(gamintojas="Škoda", modelis="Octavia", spalva="Pilka", kaina="20000"),
        Automobilis(gamintojas="Mazda", modelis="CX-5", spalva="Mėlyna", kaina="26000"),
        Automobilis(gamintojas="Subaru", modelis="Forester", spalva="Žalia", kaina="28000"),
        Automobilis(gamintojas="Volvo", modelis="XC60", spalva="Balta", kaina="32000"),
        Automobilis(gamintojas="Tesla", modelis="Model 3", spalva="Juoda", kaina="35000"),
        Automobilis(gamintojas="Chevrolet", modelis="Malibu", spalva="Sidabrinė", kaina="19000"),
        Automobilis(gamintojas="Dacia", modelis="Duster", spalva="Pilka", kaina="17000"),
        Automobilis(gamintojas="Jeep", modelis="Renegade", spalva="Raudona", kaina="26000"),
        Automobilis(gamintojas="Fiat", modelis="500", spalva="Balta", kaina="16000"),
        Automobilis(gamintojas="Opel", modelis="Astra", spalva="Mėlyna", kaina="19000"),
        Automobilis(gamintojas="Land Rover", modelis="Discovery", spalva="Žalia", kaina="40000"),
        Automobilis(gamintojas="Mini", modelis="Cooper", spalva="Raudona", kaina="23000"),
        Automobilis(gamintojas="Suzuki", modelis="Vitara", spalva="Pilka", kaina="21000"),
        Automobilis(gamintojas="Citroën", modelis="C5 Aircross", spalva="Sidabrinė", kaina="24000"),
        Automobilis(gamintojas="Mitsubishi", modelis="Outlander", spalva="Juoda", kaina="30000"),
        Automobilis(gamintojas="Lexus", modelis="RX", spalva="Balta", kaina="45000"),
        Automobilis(gamintojas="Infiniti", modelis="Q50", spalva="Mėlyna", kaina="35000"),
        Automobilis(gamintojas="Alfa Romeo", modelis="Giulia", spalva="Raudona", kaina="37000"),
        Automobilis(gamintojas="Jaguar", modelis="XE", spalva="Sidabrinė", kaina="45000"),
        Automobilis(gamintojas="Cadillac", modelis="XT5", spalva="Juoda", kaina="50000"),
        Automobilis(gamintojas="Chrysler", modelis="300", spalva="Pilka", kaina="34000"),
        Automobilis(gamintojas="Dodge", modelis="Charger", spalva="Mėlyna", kaina="33000"),
        Automobilis(gamintojas="GMC", modelis="Terrain", spalva="Žalia", kaina="29000"),
        Automobilis(gamintojas="Ram", modelis="1500", spalva="Juoda", kaina="42000"),
        Automobilis(gamintojas="Buick", modelis="Encore", spalva="Balta", kaina="28000"),
        Automobilis(gamintojas="Porsche", modelis="Cayenne", spalva="Raudona", kaina="60000"),
        Automobilis(gamintojas="Acura", modelis="RDX", spalva="Pilka", kaina="35000"),
        Automobilis(gamintojas="Lincoln", modelis="Nautilus", spalva="Sidabrinė", kaina="45000"),
        Automobilis(gamintojas="Genesis", modelis="GV80", spalva="Mėlyna", kaina="55000"),
        Automobilis(gamintojas="Rolls-Royce", modelis="Ghost", spalva="Balta", kaina="300000"),
        Automobilis(gamintojas="Bentley", modelis="Continental", spalva="Juoda", kaina="250000"),
        Automobilis(gamintojas="Aston Martin", modelis="DBX", spalva="Raudona", kaina="220000"),
        Automobilis(gamintojas="Ferrari", modelis="Portofino", spalva="Mėlyna", kaina="250000"),
        Automobilis(gamintojas="Lamborghini", modelis="Urus", spalva="Žalia", kaina="300000"),
        Automobilis(gamintojas="Maserati", modelis="Levante", spalva="Pilka", kaina="150000"),
        Automobilis(gamintojas="McLaren", modelis="GT", spalva="Sidabrinė", kaina="210000")

    ]

    db.session.add_all(automobiliai)
    db.session.commit()
    print("Duomenys užpildyti")
