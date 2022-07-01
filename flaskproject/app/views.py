from app import app, db
from flask import Flask,flash, render_template, url_for, request, redirect 
from app.forms import ContactForm, Blogform
from app.model import Blog
from werkzeug.utils import secure_filename
import os





@app.route('/')
def index():
    return render_template('index.html')


@app.route('/kontakt', methods=['GET','POST'])
def kontakt():
    form = ContactForm()

    if form.validate_on_submit():
        return 'Wysłane'
    elif request.method =='GET':
        return render_template('kontakt.html', form=form)



@app.route('/addblog', methods=['GET', 'POST'])
def addblog():
    forma = Blogform()

    if request.method =='POST':
        post_title = request.form["title"]
        post_tresc = request.form["tresc"]
        image = request.files["photo"]
        if image and allowed_file(image.filename):
            filename = secure_filename(image.filename)
            new_blog = Blog(title=post_title, tresc=post_tresc, name=image.filename)
            try:
                db.session.add(new_blog)
                db.session.commit()
                image.save(os.path.join(app.config['UPLOAD_FOLDER'],filename))
                return redirect('/addblog')
            except:
                return 'Wystąpił bład'

    else:
        return render_template('addblog.html',forma = forma)


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in app.config['ALLOWED_EXTENSIONS']



@app.route("/blog", methods=['GET', 'POST'])
def blog():
    if request.method == "POST":
        tag = request.form['search']
        search = "%{}%".format(tag)
        blogs = Blog.query.filter(Blog.title.like(search)).order_by(Blog.data_created).all()
        return render_template('blog.html', blogs=blogs)
    else:
        blogs = Blog.query.order_by(Blog.data_created).all()
        return render_template('blog.html', blogs=blogs)
   
@app.route("/delete/<int:id>")
def delete(id):
    blog_to_delete = Blog.query.get_or_404(id)

    try:
        db.session.delete(blog_to_delete)
        db.session.commit()
        return redirect('/blog')
    except:
        return "Wystąpił bład przy usuwaniu"


if __name__ == "__main__":
    app.run(debug=True)

