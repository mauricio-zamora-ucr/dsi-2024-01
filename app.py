from flask import Flask, request, redirect, render_template
app = Flask(__name__)


@app.route('/parqueo', methods=['GET', 'POST'])
def generar_parqueo():
    if request.method == 'POST':
        numero_filas = int(request.form['filas'])
        numero_columnas = int(request.form['columnas'])
        datos=[]
        for fila in range(1,numero_filas+1):
            columnas = []
            for columna in range(1, numero_columnas+1):
                columnas.append('F{:4d} C{:4d}'.format(fila, columna))

            datos.append(columnas)

        return render_template('parqueo.html',datos=datos)

    return render_template('parqueo.html')

@app.route('/calculadora', methods=['GET', 'POST'])
def calcular():
    x1 = float(request.form.get('valor1',0))
    x2 = float(request.form.get('valor2',0))
    y = float(request.form.get('resultado',0))

    if request.method == 'POST':
        y = x1 + x2

    return render_template('calculadora.html', valor1=x1, valor2=x2, resultado=y, nombre='Mauricio')

@app.route('/', methods=['GET'])
def main():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)