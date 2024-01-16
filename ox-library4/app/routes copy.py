# app/routes.py
from flask import render_template, redirect, url_for, request
from flask import session
from app import app, db

# from app.gestionnaire import Gestionnaire

# gestionnaire = Gestionnaire()








@app.route('/')
def index():
    return render_template('index.html')

# pour s'inscrire
@app.route('/sauvegarder_user', methods=['POST'])
def sauvegarder_user():
    pseudo = request.form.get('pseudo')
    password = request.form.get('password')
    nom=request.form.get("nom")
    prenom=request.form.get("prenom")
    email = request.form.get('email')
    
  
    
    new_role="user"
    
    
    

    message = gestionnaire.sauvegarder_user(new_username, new_password, new_email, new_nom, new_prenom, new_role)
    user = None
    if message == 'Utilisateur sauvegardé avec succès':
        user = gestionnaire.get_user(new_username)
        session['user_id'] = user.id  #
    
    return render_template('pages/sauvegarder_user.html', message=message)
    return render_template('pages/seconnecter.html',user=user)

# ici on recure user depuis BD en usant sin "id"
@app.route('/recuperer_user <int:user_id>')
def recuperer_user(user_id):
    # user_id = 6  # ici est un prototype que je remplace par l'ID spécifique que je recherche
    retrieved_user = gestionnaire.get_user(user_id)

    if retrieved_user:
        return render_template('pages/recuperer_user.html', user=retrieved_user)
    else:
        message = "Aucun utilisateur trouvé."
        return render_template('pages/recuperer_user.html', message=message)
# pour un abonner



@app.route('/seconnecter', methods=['POST'])
def seconnecter():
    username = request.form.get('username')
    password = request.form.get('password')

    user = gestionnaire.get_user(username)

    if user and user.role == 'user' and check_password(user.password, password):
        session['user_id'] = user.id  # Stockez l'ID de l'utilisateur dans la session
        return render_template('pages/seconnecter.html',user=user) #, user=user)
    elif user and user.role == 'admin' and check_password(user.password, password):
        session['user_id'] = user.id  # Stockez l'ID de l'utilisateur dans la session
        return render_template('pages/admin.html', user=user)
    else:
        message = "Connexion échouée. Vérifiez vos informations d'identification."
        return render_template('pages/connexion_echouee.html', message=message)

#  fonction pour vérifier le mot de passe
def check_password(hashed_password, user_password):
    return hashed_password == user_password

@app.route('/modifier_infos/', methods=['GET', 'POST'])
def modifier_infos():
    # on assure que l'userr est authentifié en vérifiant s'il existe dans la session
    if 'user_id' not in session:
        return redirect(url_for('index'))

    # je get l'utilisateur àpartir de la session "il faut que je bouquine comment fonctionne les sessions"
    user_id_session = session['user_id']
    user = gestionnaire.get_user(user_id_session)

    # ici on jere le cas où user n'existe pas
    if user is None:
        return redirect(url_for('index'))

    if request.method == 'POST':
        nouveau_nom = request.form.get('username')
        nouveau_password = request.form.get('password')
        nouveau_email = request.form.get('email')

        message = gestionnaire.modifier_infos(user, nouveau_nom, nouveau_password, nouveau_email)

        # ce user_id est usee dans l'URL pour la redirection
        return redirect(url_for('recuperer_user', user_id=user.id, message=message))

    return render_template('pages/modifier_infos.html', user=user)
