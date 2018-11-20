from flask import Flask, render_template, request
import csv
import tablib

app = Flask(__name__)

dataset = tablib.Dataset()
fp_data = open("students.csv", "r")
dataset.csv = fp_data.read()

#students will fill this form
@app.route('/')
def student():
     return render_template('form.html')


@app.route('/form', methods=['POST', 'GET'])
def result():
    if request.method == 'POST':

        result = dict(request.form)
        fp = open("students.csv", "a")

        for key, value in result.items():
            print (type(value))
            fp.write(value+",")
            #print(value)
    
    fp.write("\n")
    fp.close()

    return render_template("thanks.html")


#view all the student data
@app.route('/all_students')
def all_data():
    return dataset.html 
    #return render_template("results.html")


if __name__ == "__main__":
    app.run(debug='true')
