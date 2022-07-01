
from flask import Flask, render_template, request
from flask_mail import Mail, Message
from forms import EmailForm, ExcelForm
from flask_bootstrap import Bootstrap
import openpyxl as xl



app = Flask(__name__)
bootstrap = Bootstrap(app)

app.config['SECRET_KEY'] = 'the random string'
app.config['MAIL_SERVER']='wp.pl'
app.config['MAIL_USERNAME'] = 'test'
app.config['MAIL_PASSWORD'] = 'test'
app.config['MAIL_USE_TLS'] = True
mail = Mail(app)

@app.route("/email", methods=['GET', 'POST'])
def mailaa():
    form = EmailForm()
    tytul_w= 'Wysyłanie maili'
    if request.method == "POST":
        email=request.form["email"]
        tytul=request.form["tytul"]
        message=request.form["message"]
        msg = Message(tytul,sender='pgrabowski@wp.pl', recipients=[email] )
        msg.body= message
        mail.send(msg)


        return "Mail zostal wysałny do " + email + " o tytule " + tytul
    else:
        return render_template('email.html', form = form, tytul_w=tytul_w)

@app.route("/excel", methods=['GET', 'POST'])
def excell():
    
    form = ExcelForm()
    form1= EmailForm()
    tytul_w= 'Umieść plik'
    if request.method == "POST":
        if 'submit' in request.form:
            dane =[]
            plik = request.files["file_upload"]
            wb = xl.load_workbook(plik)
            Arkusz = wb['Arkusz1']
        
            for col in Arkusz.iter_rows(min_row=2, max_row=100, min_col=1, max_col=4,values_only=True):
                if col[0] is not None and type(col[0])==int:
                        dane.append(col)
                   

        return render_template("data.html", dane=dane, form=form1)

    else:
        return render_template("email.html", form=form, tytul_w=tytul_w)

@app.route("/wyslij/<int:id>", methods=['GET', 'POST'])
def wyslij(id):
    
    if request.method == "POST":
            email_w = request.form.get('email')
            temat_w = request.form.get('tytul')
            tresc_w = request.form.get('message')
            try:

                        msg = Message(temat_w,sender='grabul3@wp.pl', recipients=[email_w] )
                        msg.body= tresc_w

                        return 'wysłałem ' 
                
            except:

                        return 'Nie mogłem wysłać: ' + email_w +' '+ temat_w + ' '+ tresc_w
                
    return 'Coś poszło nie tak '

@app.route("/wszystko", methods=['GET', 'POST'])
def wszystko():
    if request.method == "POST" and request.form['wszystko']:
            id_w = request.form.getlist('id')
            email_w = request.form.getlist('email_addr')
            temat_w = request.form.getlist('temat_w')
            tresc_w = request.form.getlist('tresc_w')
            for id_c, email, temat, tresc in zip(id_w, email_w, temat_w, tresc_w):

                try:

                        msg = Message(temat,sender='grabul3@wp.pl', recipients=[email] )
                        msg.body= tresc

                        pass
                
                except:

                        return 'Nie mogłem wysłać: ' + email +' '+ temat + ' '+ tresc
                
            
            return "Wysłano widomości "
    return 'Coś poszło nie tak'







if __name__ == '__main__':
    app.run(debug = True)