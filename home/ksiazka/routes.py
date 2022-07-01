from flask import render_template, request, redirect, url_for, make_response
from ksiazka import app ,db
from ksiazka.forms import WydzialForm, ReferatForm, UrzednikForm, KordynatorForm
from ksiazka.model import Wydzial, Referat, Urzednik



@app.route('/kordynator',methods=['GET','POST'])
def kordynator():
    tytul = 'Kordynator Dzielnicowy'
    form = KordynatorForm(request.form)
    return render_template('spis.html', form=form, tytul=tytul)


@app.route('/spis',methods=['GET','POST'])
def spis():
    tytul = 'Zapisz wydział'
    form = WydzialForm(request.form)
    if request.method == 'POST' and form.validate():
        wydzialk = request.form['wydzial_krotko']
        wydzialp = request.form['wydzial_pelny']
        kolej = request.form['wydzial_kolej']
        wydziall = Wydzial.query.filter_by(wydzial_krotko=wydzialk).first()
        if wydziall is None:
            wydziaa = Wydzial(wydzial_krotko=wydzialk, wydzial_pelny=wydzialp, wydzial_kolej=kolej)
            db.session.add(wydziaa)
            db.session.commit()
            return 'Dodano'
        return f'Wydział już jest o takiej nazwie: { wydziall.wydzial_krotko }'
    else:
        return render_template('spis.html', form=form, tytul=tytul)

@app.route('/referat',methods=['GET','POST'])
def referat():
    tytul = 'Zapisz referat'
    form = ReferatForm(request.form)
    form.wydzial_id.choices = [(r.id,r.wydzial_pelny) for r in Wydzial.query.order_by(Wydzial.wydzial_kolej).all() ]
    if request.method == 'POST' and form.validate():
        referatk = request.form['referat_krotko']
        referatp = request.form['referat_pelny']
        referatkol = request.form['referat_kolej']
        wydzial_id = request.form['wydzial_id']
        referatt = Referat.query.filter_by(referat_krotko=referatk).first()
        if referatt is None:
            referaa = Referat(wydzial_id=wydzial_id, referat_krotko=referatk, referat_pelny=referatp, referat_kolej=referatkol)
            db.session.add(referaa)
            db.session.commit()
            return 'Dodano'
        return f'Referat już jest o takiej nazwie: { referatt.referat_krotko }'
    else:
        return render_template('spis.html', form=form, tytul=tytul)

@app.route('/user', methods=['GET', 'POST'])
def user():
    tytul = 'Zapisz urzędnika'
    form = UrzednikForm()
    form.referat_id.choices = [(r.id, r.referat_pelny) for r in Referat.query.order_by(Referat.referat_kolej).all() ]
    form.wydzial_id.choices = [(r.id,r.wydzial_pelny) for r in Wydzial.query.order_by(Wydzial.wydzial_kolej).all() ]
    if form.validate_on_submit():
        imie = request.form['imie']
        nazwisko = request.form['nazwisko']
        user_kolej =request.form['user_kolej']
        pokoj = request.form['pokoj']
        tel_wew = request.form['tel_wew']
        telefon = request.form['telefon']
        fax = request.form['fax']
        stanowisko = request.form['stanowisko']
        opis = request.form['opis']
        wydzial_id = request.form['wydzial_id']
        referat_id = request.form['referat_id']
        userr = Urzednik(imie=imie, nazwisko=nazwisko, user_kolej=user_kolej, pokoj=pokoj, tel_wew=tel_wew, telefon=telefon,
                   fax=fax, stanowisko=stanowisko, opis=opis, wydzial_id=wydzial_id, referat_id=referat_id )
        db.session.add(userr)
        db.session.commit()
        return 'Dodano'
    else:
        return render_template('spis.html', form=form, tytul=tytul)

@app.route('/delete/<string:delete>/<int:id>')
def delete(delete, id ):
    if delete == "referat":
        referat_to_delete = Referat.query.get_or_404(id)
        try:
            db.session.delete(referat_to_delete)
            db.session.commit()
            return redirect('/wydzial')
        except:
            return "wystąpił bład przy usuwaniu"
    elif delete == "wydzial":
        wydzial_to_delete = Wydzial.query.get_or_404(id)
        try:
            db.session.delete(wydzial_to_delete)
            db.session.commit()
            return redirect('/wydzial')
        except:
            return "wystąpił bład przy usuwaniu"
    elif delete == "urzednik":
        urzednik_to_delete = Urzednik.query.get_or_404(id)
        try:
            db.session.delete(urzednik_to_delete)
            db.session.commit()
            return redirect('/wydzial')
        except:
            return "wystąpił bład przy usuwaniu"
    return 'Coś poszło nie tak'
@app.route('/update/<string:update>/<int:id>', methods=['GET', 'POST'] )    
def update(update, id):
    if update == "wydzial":
        tytul = 'Edycja wydziału'
        abc = db.session.query(Wydzial).filter(Wydzial.id==id)
        test = abc.first()
        if test:
            form = WydzialForm(formdata=request.form, obj=test)
            if request.method == 'POST':
                test.wydzial_krotko = request.form['wydzial_krotko']
                test.wydzial_pelny = request.form['wydzial_pelny']
                test.wydzial_kolej = request.form['wydzial_kolej']
                try:
                    db.session.commit()
                    return redirect('/wydzial')
                except:
                    return "coś poszło nie tak"

            return render_template('spis.html', form=form, tytul=tytul)
        else:

            return "Niewłaściwy id {}".format(id=id)
    if update == "referat":
            tytul = 'Edycja referatu'
            abc = db.session.query(Referat).filter(Referat.id==id)
            test = abc.first()
            if test:
                form = ReferatForm(formdata=request.form, obj=test)
                form.wydzial_id.choices = [(r.id,r.wydzial_pelny) for r in Wydzial.query.order_by(Wydzial.wydzial_kolej).all() ]
                if request.method == 'POST':
                    test.wydzial_id = request.form['wydzial_id']
                    test.referat_krotko = request.form['referat_krotko']
                    test.referat_pelny = request.form['referat_pelny']
                    test.referat_kolej = request.form['referat_kolej']
                    try:
                        db.session.commit()
                        return redirect('/wydzial')
                    except:
                        return "coś poszło nie tak"

                return render_template('spis.html', form=form, tytul=tytul)
            else:

                return "Niewłaściwy id {}".format(id=id)

    if update == "urzednik":
        tytul = 'Edycja urzednika'
        abc = db.session.query(Urzednik).filter(Urzednik.id==id)
        test = abc.first()
        if test:
            form = UrzednikForm(formdata=request.form, obj=test)
            form.referat_id.choices = [(r.id, r.referat_pelny) for r in Referat.query.order_by(Referat.referat_kolej).all() ]
            form.wydzial_id.choices = [(r.id,r.wydzial_pelny) for r in Wydzial.query.order_by(Wydzial.wydzial_kolej).all() ]
            if request.method == 'POST':
                test.imie = request.form['imie']
                test.nazwisko = request.form['nazwisko']
                test.user_kolej =request.form['user_kolej']
                test.pokoj = request.form['pokoj']
                test.tel_wew = request.form['tel_wew']
                test.telefon = request.form['telefon']
                test.fax = request.form['fax']
                test.stanowisko = request.form['stanowisko']
                test.opis = request.form['opis']
                test.wydzial_id = request.form['wydzial_id']
                test.referat_id = request.form['referat_id']
                try:
                        db.session.commit()
                        return redirect('/wydzial')
                except:
                        return "coś poszło nie tak"

            return render_template('spis.html', form=form, tytul=tytul)
        else:

            return "Niewłaściwy id {}".format(id=id)

@app.route('/info/<string:wydzialk>/<int:id>')
def get_wydzial(wydzialk, id):
    if wydzialk == "wydzial":
        info = Wydzial.query.get_or_404(id)
        return f'Pelna nazwa wydziału to: {info.wydzial_pelny}' 
    if wydzialk == "referat":
        info = Referat.query.get_or_404(id)
        return f'Pelna nazwa referatu to: {info.referat_pelny}' 
    else: 
        return "niewłasciwe pole"

@app.route('/wydzial')
def wydzial():
    wydzialy = Wydzial.query.order_by(Wydzial.wydzial_kolej).all()
    referaty = Referat.query.order_by(Referat.referat_kolej).all()
    urzedniki = db.session.query( Referat.referat_pelny, Wydzial.wydzial_kolej, Wydzial.wydzial_pelny, Urzednik.id, Urzednik.fax, Urzednik.user_kolej, Urzednik.imie, Urzednik.wydzial_id, Urzednik.nazwisko, Urzednik.tel_wew, Urzednik.telefon, Urzednik.opis, Urzednik.pokoj, Urzednik.stanowisko).join(Wydzial, Wydzial.id==Urzednik.wydzial_id).join(Referat, Referat.id==Urzednik.referat_id).all()
    return render_template('wydzial.html', wydzialy=wydzialy, referaty=referaty, urzedniki=urzedniki)

@app.route('/ksiazka')
def ksiazka():
    wydzialy = Wydzial.query.order_by(Wydzial.wydzial_kolej).all()
    referaty = Referat.query.order_by(Referat.referat_kolej).all()
    urzedniki = Urzednik.query.order_by(Urzednik.user_kolej).all()
        
    
    return render_template('Ksiazka.html', wydzialy=wydzialy, referaty=referaty, urzedniki=urzedniki)
