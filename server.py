from flask import Flask, render_template, request, redirect, session
from encuesta import Form
from flask import flash
app = Flask(__name__)

app.secret_key = 'hola'



@app.route('/')
def inicio():
    return render_template('index.html')

@app.route('/process', methods=['POST'])
def send_form():
    data = {
        'first_name' : request.form['first_name'],
        'location' : request.form['location'],
        'fav_language' : request.form['fav_language'],
        'comentario' : request.form['comentario']
    }
    if not Form.validate_form(request.form):
        # redirigir a la ruta donde se renderiza el formulario de burger
        return redirect('/')

    print(data)

    Form.save(data)

    flash('Su encuesta ha entrado correctamente')

    return redirect('/result')

@app.route('/result')
def result():
    all_forms = Form.get_all()
    return render_template('result.html', all_forms = all_forms)

if __name__=="__main__":
    app.run(debug=True)
