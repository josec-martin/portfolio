from flask import Flask, render_template, request, redirect
import csv

app = Flask(__name__)

@app.route("/")
def home_page():
    return render_template("index.html")

@app.route("/<page_name>")
def render_page(page_name):
    return render_template(page_name)

def save_data(data):
    try:
        with open('database.csv', 'a', newline='') as csvfile:
            email = data["email"]
            subject = data["subject"]
            message = data["message"]
            csv_writer = csv.writer(csvfile, delimiter=',', quotechar='"',
                                    quoting=csv.QUOTE_MINIMAL)
            csv_writer.writerow([email, subject, message])
        print("One more contact!")
        return True
    except Exception as err:
        print(f"Error: {err}")
        return False


@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        try:
            data = request.form.to_dict()
            if save_data(data):
                return redirect('/thankyou.html')
        except Exception as err:
            print(f"Error: {err}")
    return redirect('/tryagain.html')
