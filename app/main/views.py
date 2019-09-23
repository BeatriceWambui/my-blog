from flask import render_template,redirect,url_for
from ..requests import get_quotes
from . import main
from flask_login import login_required,current_user
from ..import db
from app.models import Post,Comments
from .form import PostForm,CommentForm

# Views
@main.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''
    quotes = get_quotes()
    print(quotes)
    # title = 'Home - this is my blog page'
    all_posts = Post.query.all()

    return render_template('index.html',quotes=quotes,all_posts=all_posts)

@main.route('/blog/new/<int:blog_id>', methods = ['GET','POST'])
@login_required
def new_blog(blog_id):
    '''
    View blog page function that returns the blog details page and its data
    '''
    return render_template(blog.html,id = blog_id)

@main.route('/posts/new',methods = ['GET', 'POSTS'])
@login_required
def new_post():
    form = PostForm()
    if form.validate_on_submit():
        user_id = current_user._get_current_object().id
        post = Post(category= form.category.data,title=form.title.data,description=form.description.data,user_id=user_id)
        post.save()
        return redirect(url_for('main.index'))
    return render_template('post.html',form=form)

@main.route('/comments/<int:post_id>',methods = ['GET','POST'])
@login_required
def comment(post_id):
    forms = CommentForm()
    comments = Comments.query.filter_by(post_id=post_id).all()
    if forms.validate_on_submit():
        post_id = post_id 
        user_id= current_user._get_current_object().id
        comment = Comments(comment=forms.comment.data,user_id=user_id,post_id=post_id)
        comment.save()
        return redirect(url_for('main.index'))
    
    return render_template('comments.html',forms= forms,comments=comments)
