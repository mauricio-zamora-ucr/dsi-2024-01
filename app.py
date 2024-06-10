from flask import Flask, request, redirect, render_template
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def main():
    x1 = float(request.form.get('valor1',0))
    x2 = float(request.form.get('valor2',0))
    y = float(request.form.get('resultado',0))

    if request.method == 'POST':
        y = x1 + x2

    return render_template('index.html', valor1=x1, valor2=x2, resultado=y, nombre='Mauricio')

if __name__ == '__main__':
    app.run(debug=True)