from flask import Flask, render_template, request
import json
import subprocess

app = Flask(__name__, template_folder='templates')

@app.route('/')
def function():
    return render_template('password_form.html')

@app.route('/submit', methods=['POST'])
def submit():
    # Get form data
    data = {
        "username": request.form['username'],
        "servername": request.form['servername'],
        "password": request.form['password'],
        "incident": request.form['incident']
    }

    # Save data to a JSON file
    with open('config.json', 'w') as json_file:
        json.dump(data, json_file)

    # Execute another Python script
    subprocess.run(['python', 'password_reset_mail.py'])

    return "Form submitted successfully! Data saved and script executed."

if __name__ == '__main__':
    app.run(debug=True, port=5000)