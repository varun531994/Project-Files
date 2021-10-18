from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for,current_app
)

bp = Blueprint('register', __name__)
@bp.route('/register', methods=('GET', 'POST'))
def register():
    cursor = current_app.db.connection.cursor()
    
    if request.method == 'POST':
        First_Name = request.form['First_Name']
        Last_Name = request.form['Last_Name']
        Address = request.form['Address']
        error = None

        if not First_Name:
            error = 'First Name is required.'
        if not Last_Name:
            error = 'Last Name is required.'
        if not Address:
            error = 'Address is required.'    
       

        if not error:
           cursor.execute("INSERT INTO student (first_name,last_name,address) VALUES('{0}','{1}','{2}')".format(First_Name,Last_Name,Address))
           
            cursor.execute("SHOW*FROM student")
           
        current_app.db.connection.commit()


    return render_template('register.html')
    
    
    
  
#@bp.route('/login', methods=('GET', 'POST'))
#def login():
 #   if request.method == 'POST':
  #      username = request.form['username']
   #     password = request.form['password']

    #return render_template('login.html')