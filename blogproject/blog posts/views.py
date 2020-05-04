from flask import render_template, url_for, flash, request, redirect, Blueprint
from flask_login import current_user, login_required
from blogproject import db
from blogproject.models import BlogPost
from blogproject.blog_posts.forms import BlogPostForm

blog_posts = Blueprint('blog_posts',__name__)

# Create blog post #

@blog_posts.route('/create', methods=['GET','POST'])
@login_required
def create_post():
    form = BlogPostForm()




# View blog post #

# Update blog post #


# Delete blog post #