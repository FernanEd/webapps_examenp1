from flask import Flask, render_template, redirect, request
from forms import ComisionForm
from funciones import calcularComision

app = Flask(__name__)
app.secret_key = 'PMasdASsdfL12'

@app.route('/', methods=['GET', 'POST'])
def index():
    form = ComisionForm()

    if request.method == 'POST':
      if form.validate_on_submit():
        monto = form.monto.data
        comision = calcularComision(monto)
        total = monto - comision
        return render_template('resultado.html', monto = monto, comision = comision, total=total)

    return render_template('index.html', form = form)
