from flask_app import app
from flask import render_template,redirect,request,session
from flask_app.models.email import Email

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/add_email', methods = ['POST'])
def add_email():
    if not Email.validate_email(request.form):
        return redirect('/')
    data = {
        "email" : request.form['email']
    }
    session['email'] = request.form['email']
    Email.add(data)
    return redirect('/success')

@app.route('/success')
def success():
    return render_template('success.html', emails = Email.get_all())