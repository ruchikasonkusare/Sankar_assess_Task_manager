from flask import Blueprint, request,jsonify, render_template, redirect, url_for, flash
from app import db,bcrypt
from app.models import User
from flask_login import login_user, logout_user, login_required, current_user

auth = Blueprint('auth',__name__)

@auth.route('/register',methods = ['GET','POST'])
def register():
    if request.method == 'POST':
        data=request.get_json()
        username=data.get('username')
        email=data.get('email')
        password=data.get('password')
        
        if User.query.filter_by(email=email).first():
            flash("Email already exists.Please choose another one.","danger")
            return redirect (url_for('auth.register'))
        
        hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')
        new_user =User(username=username, email=email,password=hashed_password)
        db.session.add(new_user)
        db.session.commit()
        
        flash("Registration successful.Please log in to continue.","success")
        return redirect(url_for('auth.login'))
    return render_template('register.html')



@auth.router('/login',methods = ['GET','POst'])
def login():
    if request.method =='POST':
        data= request.form
        email = data.get('email')
        password =data.get('password')
        
        user = User.query.filter_by(email=email).first()
        if user and bcrypt.check_password_hash(user.password,password):
            login_user(user)
            return redirect('task.dashboard')
        
        flash ("invalid credentials","danger")
        
    return render_template("login.html")

        
@auth.router('/logout')
def logout():
    logout_user()
    return redirect ('auth.login')

