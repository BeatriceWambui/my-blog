from flask import render_template
from ..requests import get_quotes
from . import main
from flask_login import login_required
# Views
@main.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''
    quotes = get_quotes()
    print(quotes)
    # title = 'Home - this is my blog page'


    return render_template('index.html',quotes=quotes)

@main.route('/blog/new/<int:blog_id>', methods = ['GET','POST'])
@login_required
def new_blog(blog_id):
    '''
    View blog page function that returns the blog details page and its data
    '''
    return render_template(blog.html,id = blog_id)

