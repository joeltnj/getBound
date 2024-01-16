# app/routes.py
from flask import render_template, redirect, url_for, request
from flask import session,flash
from app import app, db
from flask_login import LoginManager, UserMixin, login_user, logout_user, login_required, current_user
from flask_login import LoginManager
from app.models.adherent import Adherent

login_manager = LoginManager(app)
login_manager.login_view = 'login'

@login_manager.user_loader
def load_user(user_id):
    return Adherent.query.get(int(user_id))

# route accueil 'index'
@app.route('/')
def index():
    return render_template('index.html')

# pour s'inscrire
@app.route('/sauvegarder_user', methods=['POST'])
def sauvegarder_user():
    new_username = request.form.get('username')
    new_nom=request.form.get("nom")
    new_prenom=request.form.get("prenom")
    new_email = request.form.get('email')
    new_password = request.form.get('password')
    
    adherent2 = Adherent(pseudo="jo5", mot_de_passe="2020", nom="tuzo", prenom="joel", mail="joe@gmail.com")
    with app.app_context():
        db.drop_all()
        db.create_all()
        db.session.add(adherent2)
        db.session.commit()
        
        login_user(adherent2)
        flash("je suis connecter")
    # return redirect(url_for('index'))
    return render_template('pages/seconnecter.html')

# route se connecter
@app.route('/seconnecter', methods=['POST'])
def seconnecter():
    pseudo=request.form.get('pseudo')
    password=request.form.get('password')
    user_act=Adherent.query.filter_by(pseudo=pseudo).first()

    if user_act and password==user_act.mot_de_passe:
        return render_template('pages/seconnecter.html')
    else:
        return render_template('pages/reservation.html')
        # return render_template('pages/seconnecter.html')
    # return render_template('pages/seconnecter.html')


# methode inconue
def check_password(hashed_password, user_password):
    return hashed_password == user_password


# route vers infos
@app.route('/infos/', methods=['GET'])
def infos():
    user_act=Adherent.query.get(current_user.get_id())
    return render_template('pages/infos.html', user=user_act)

# route vers pret
@app.route('/pret/', methods=['GET', 'POST'])
def pret():
    return render_template('pages/pret.html')

# route vers reservation
@app.route('/reservation/', methods=['GET', 'POST'])
def reservation():
    return render_template('pages/reservation.html')

# #  route modifier infos
# @app.route('/modifier_infos/', methods=['GET', 'POST'])
# def modifier_infos():
#     user_act=Adherent.query.get(current_user.get_id())
    
#     if request.method=="GET":
#         return render_template("pages/modifier_infos.html", user=user_act)

# route update infos
@app.route('/update_infos/', methods=['POST'])
def update_infos():
    nom = request.form['nom']
    prenom = request.form['prenom']
    email = request.form['email']
    password = request.form['password']
    user_act=Adherent.query.get(current_user.get_id())
    user_act.modifier_infos(nom=nom, prenom=prenom, mail=email, mot_de_passe=password)
    db.session.commit()
    return render_template("pages/infos.html", user=user_act)

@app.route('/modifier_infos/', methods=['GET'])
def modifier_infos():
    # nom = request.form['nom']
    # prenom = request.form['prenom']
    # email = request.form['email']
    # password = request.form['password']
    # user_act=Adherent.query.get(current_user.get_id())
    # user_act.modifier_infos(nom,prenom,email,password)
    # db.session.commit()
    return render_template("pages/modifier_infos.html")

# route deconnection
@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('index'))