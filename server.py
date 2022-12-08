from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)

app.secret_key = 'hola'



@app.route('/')
def inicio():
    return render_template('index.html')

@app.route('/process', methods=['POST'])
def send_form():
    session['name'] = request.form['name']
    session['location'] = request.form['location']
    session['fav_language'] = request.form['fav_language']
    session['comments'] = request.form['comments']
    print(session)

    return redirect('/result')

@app.route('/result')
def result():
    return render_template('result.html')

if __name__=="__main__":
    app.run(debug=True)
