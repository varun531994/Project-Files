from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)

bp = Blueprint('Customer_Details', __name__)

@bp.route('/details', methods=('GET', 'POST'))
def Customer_Details():
    if request.method == 'POST':
        username = request.form['username']
        username = request.form['username']
        error = None

        if not username:
            error = 'Username is required.'


        if not error:
           return redirect(url_for("register.login"))

    return render_template('Customer_Details.html')
