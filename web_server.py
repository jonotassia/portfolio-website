from flask import Flask, render_template, request, redirect, session, flash
import csv

app = Flask(__name__)
app.secret_key = '1feawrf233rdf@#%#R@F12131dwqada'


def write_to_csv(data):
    with open('./database.csv', 'a', newline="") as database:
        name = data['name']
        email = data['email']
        subject = data['subject']
        message = data['message']

        file_writer = csv.writer(database)
        file_writer.writerow([name, email, subject, message])


@app.route(f'/')
def index():
    return render_template('index.html')


@app.route('/<string:page_name>')
def web_page(page_name):
    return render_template(page_name)


@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        try:
            # session['name'] = request.form['name']
            response = request.form.to_dict()
            write_to_csv(response)
        except:
            return 'Did not save to database'

        flash(f"Thank you, {request.form['name']}. I will be in touch shortly.")
        return redirect('./thank_you.html')

    else:
        return 'Something went wrong, try again'


# @app.route('/thank_you.html')
# def thank_you():
#     return render_template('/thank_you.html', name=session['name'])
