from flask import render_template, request, Blueprint, abort
from flask_login import current_user, login_required
from anc.models import Post

main = Blueprint('main', __name__)

@main.route('/')
@main.route('/home')
def home():
    page = request.args.get('page', 1, type=int)
    posts = Post.query.filter_by(featured='yes').order_by(
        Post.date_posted.desc()).paginate(page=page, per_page=20)
    return render_template('home.html', posts=posts)

@main.route('/about')
def about():
    return render_template('about.html', title='About')

@main.route('/categories')
def categories():
    page = request.args.get('page', 1, type=int)
    posts = Post.query.filter(Post.tags.contains('Career')).filter_by(featured='yes').order_by(
        Post.date_posted.desc()).paginate(page=page, per_page=20)
    return render_template('categories.html', posts=posts)

@main.route('/finance')
def finance():
    page = request.args.get('page', 1, type=int)
    posts = Post.query.filter(Post.tags.contains('Finance')).filter_by(featured='yes').order_by(
        Post.date_posted.desc()).paginate(page=page, per_page=20)
    return render_template('home.html', posts=posts)

@main.route('/education')
def education():
    page = request.args.get('page', 1, type=int)
    posts = Post.query.filter(Post.tags.contains('Education')).filter_by(featured='yes').order_by(
        Post.date_posted.desc()).paginate(page=page, per_page=20)
    return render_template('home.html', posts=posts)

@main.route('/career')
def career():
    page = request.args.get('page', 1, type=int)
    posts = Post.query.filter(Post.tags.contains('Career')).filter_by(featured='yes').order_by(
        Post.date_posted.desc()).paginate(page=page, per_page=20)
    return render_template('home.html', posts=posts)

@main.route('/lifestyle')
def lifestyle():
    page = request.args.get('page', 1, type=int)
    posts = Post.query.filter(Post.tags.contains('Lifestyle')).filter_by(featured='yes').order_by(
        Post.date_posted.desc()).paginate(page=page, per_page=20)
    return render_template('home.html', posts=posts)

@main.route('/wellness')
def wellness():
    page = request.args.get('page', 1, type=int)
    posts = Post.query.filter(Post.tags.contains('Wellness')).filter_by(featured='yes').order_by(
        Post.date_posted.desc()).paginate(page=page, per_page=20)
    return render_template('home.html', posts=posts)

@main.route('/edit')
@login_required
def edit():
    page = request.args.get('page', 1, type=int)
    posts = Post.query.filter_by(edit_queue='yes').order_by(
        Post.date_posted.desc()).paginate(page=page, per_page=20)
    if current_user.account_type == 'admin':
        return render_template('home.html', posts=posts)
    else:
        abort(403)

@main.route('/all')
@login_required
def all():
    page = request.args.get('page', 1, type=int)
    posts = Post.query.order_by(
        Post.date_posted.desc()).paginate(page=page, per_page=20)
    if current_user.account_type == 'admin':
        return render_template('home.html', posts=posts)
    else:
        abort(403)
