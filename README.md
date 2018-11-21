# Gramener_backend
https://angel.co/gramener/jobs/451277-product-intern-python-back-end


Flask Web App:

1.Prerequisite:
Python 3.7 is used for this web app.

2.Install virtualenv for development environment:
Command to install virtualenv: pip install virtualenv.

Once installed we are now ready to install Flask in the environment: pip install Flask
In order to test Flask installation, type the following code in the editor as Hello.py

from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
   return 'Hello World’

if __name__ == '__main__':
   app.run()
   
3. Try to run it on a localhost:5000 , you will get the return value on page as 'Hello World'   

4.Debug Mode:
The Debug mode is enabled by setting the debug property of the application object to True before running or passing the debug parameter to the run() method
if __name__ == "__main__":
    app.run(debug='true')

5.HTTP Method used:POST(Used to send HTML form data to server. Data received by POST method is not cached by server.)
@app.route('/form', methods=['POST', 'GET'])
def result():
    if request.method == 'POST':

 6.import csv to store data in a csv file    
          result = dict(request.form)
        fp = open("students.csv", "a")
        
 7.form.html file is created to get the data from user :
 #student will the form here
 @app.route('/')
def student():
     return render_template('form.html')
 
 8.#view all the student data
@app.route('/all_students')
def all_data():
    return dataset.html
 
 9.import tablib to import, export, and manipulate tabular data sets.
 
 10. thanks.html will say the result on pressing the submitting button as 'Thanks for filling out the form'.

  

