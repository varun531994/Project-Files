from flask import Flask,render_template, request
from flask_mysqldb import MySQL

def create_app(test_config=None):
    # create and configure the app
  app = Flask(__name__)
   

  app.config['MYSQL_HOST'] = 'localhost'
  app.config['MYSQL_USER'] = 'stu'
  app.config['MYSQL_PASSWORD'] = 'password'
  app.config['MYSQL_DB'] = 'student_portal'
 
  app.db = MySQL(app)   
  
  from . import register
  app.register_blueprint(register.bp)
   

  return app   
  
