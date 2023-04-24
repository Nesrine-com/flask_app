from flask_app import app
from flask import render_template, request, redirect, session, flash
from flask_app.models.users_model import User
from flask_app.models.tvshows_model import Tvshow
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)

@app.route('/')
def home():
    return render_template('index.html')


#====== Register=======
@app.route('/users/create', methods=['post'])
def register():
    if User.validate(request.form):
                hashed_password = bcrypt.generate_password_hash(request.form['password'])
                user_data = {
                    **request.form,
                    'password':hashed_password
                  }
                session['user_id'] = User.create(user_data)
                return redirect('/shows')
    print("Data is not valid")
    return render_template("index.html")

#=========== login=======
@app.route('/users/login', methods=['post'])
def login():
      user_from_db=User.get_by_email({'email':request.form['email']})
      if user_from_db:
            if not bcrypt.check_password_hash(user_from_db.password, request.form['password']):
                flash("Invalid Email/Password","login")
                return redirect('/')
            else:
                  session['user_id']= user_from_db.id
                  return redirect('/shows')
      flash("invalid_password/e_mail","login")
      return redirect('/')
#=======Dashboard=========
@app.route('/shows')
def dashboard():
    if 'user_id' not in session:
          return redirect('/')
    tvshows=Tvshow.get_all()
    logged_in_user=User.get_by_id({'id':session['user_id']})
    return render_template("dashboard.html", user=logged_in_user, tvshows=tvshows)
@app.route('/logout')
def logout():
      session.clear()
      return redirect('/')