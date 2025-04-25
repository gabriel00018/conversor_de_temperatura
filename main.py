from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route("/conversor_temperatura", methods=["POST"])
def classificar():
        numero = int(request.form.get("numero"))
        temp_tipo = request.form.get("temp_tipo")
        Fah = (5 / 9) * (numero - 32)
        Cel = 1, 8 * numero + 32

        if temp_tipo == "C":
            Fah = (5 / 9) * (numero - 32)
            resultado = Fah
        if temp_tipo == "F":
            Cel = (5/9) * (numero - 32)
            resultado = Cel

        return render_template("index.html", resultado=resultado)

if __name__ == "__main__":
    app.run(debug=True)