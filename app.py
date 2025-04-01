from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/crear', methods=['POST'])
def crear():
    filas = int(request.form['filas'])
    columnas = int(request.form['columnas'])
    return render_template('matrices.html', filas=filas, columnas=columnas)

@app.route('/sumar', methods=['POST'])
def sumar():
    filas = int(request.form['filas'])
    columnas = int(request.form['columnas'])
    matriz1 = []
    matriz2 = []
    for i in range(filas):
        fila1 = []
        fila2 = []
        for j in range(columnas):
            valor1 = int(request.form[f"m1_{i}_{j}"])
            valor2 = int(request.form[f"m2_{i}_{j}"])
            fila1.append(valor1)
            fila2.append(valor2)
        matriz1.append(fila1)
        matriz2.append(fila2)
    
    resultado = []
    for i in range(filas):
        fila_resultado = []
        for j in range(columnas):
            fila_resultado.append(matriz1[i][j] + matriz2[i][j])
        resultado.append(fila_resultado)
    
    return render_template('result.html', resultado=resultado)

if __name__ == '__main__':
    app.run(debug=True)
