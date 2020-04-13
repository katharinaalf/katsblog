from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def hello():
    all_posts = {'post_title':'First Post', 'post_title': 'Blog 2: Why you should read this'}
    return render_template('home.html', all_posts=all_posts)

@app.route('/aboutthis')   
def about():
    return render_template('about.html')

if __name__ == '__main__':
    app.run(debug=True)

