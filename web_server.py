from flask import Flask, render_template, request, redirect
import csv
app = Flask(__name__)

@app.route('/')
def my_home():
    return render_template("index.html")

@app.route('/<string:page_name>')
def html_page(page_name):
    return render_template(page_name)

@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == "POST":
        data = request.form.to_dict()
        write_to_csv(data)
        return redirect("./contacts.html")
    else:
        return "sth went wrong try again"
    
def write_to_file(data):
    with open("database.txt", mode = "a", encoding = "utf-8") as database:
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        database.write(f"\n{email}\t{subject}\t{message}")
        
def write_to_csv(data):
    with open("database.csv", mode = "a", encoding = "utf-8", newline='') as database_csv:
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        csv_writer = csv.writer(database_csv, delimiter=";", quotechar="'", quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([email,subject,message])