from flask import Flask, render_template, url_for, flash, redirect
from main import app, db, bcrypt
from main.forms import RegistrationForm, LoginForm
from main.models import User, Post
from flask_login import login_user

posts = [
    {
        'author': 'Jake Mobley',
        'title'	: 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'April 22, 2020'
    },
    {
        'author': 'Ariel Smith',
        'title'	: 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'April 23, 2020'

    }
]


@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', posts=posts)


@app.route('/about')
def about():
    return render_template('about.html', title='About')


@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username=form.username.data,
                email=form.email.data, password=hashed_password)
        db.session.add(user)
        db.session.commit()
        flash(f'Your account has been created. Welcome!', 'success')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            return redirect(url_for('home'))
        else:
            flash('Login Unsuccessful. Please check email and password.', 'danger')
    return render_template('login.html', title='Login', form=form)