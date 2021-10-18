from flask import Flask

def create_app(test_config=None):
    # create and configure the app
  app = Flask(__name__)
    
  from . import Customer_Details
  app.register_blueprint(Customer_Details.bp)
   

  return app
    
    
def create_app():
    app = app.teardown_appcontext(close_db)
    app = app.cli.add_command(init_db_command)   

    from . import db
    db.init_app(app)

    return app