# app/routes.py
from flask import render_template, redirect, url_for, request
from flask import session
from app import app, db

from app.gestionnaire import Gestionnaire

gestionnaire = Gestionnaire()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/sauvegarder_user', methods=['POST'])
def sauvegarder_user():
    new_username = request.form.get('username')
    new_email = request.form.get('email')
    new_password = request.form.get('password')

    message = gestionnaire.sauvegarder_user(new_username, new_password, new_email)
    
    # return render_template('pages/sauvegarder_user.html', message=message)
    return render_template('pages/seconnecter.html')

@app.route('/recuperer_user <int:user_id>')
def recuperer_user(user_id):
    # user_id = 6  # Remplacez par l'ID spécifique que vous recherchez
    retrieved_user = gestionnaire.get_user(user_id)

    if retrieved_user:
        return render_template('pages/recuperer_user.html', user=retrieved_user)
    else:
        message = "Aucun utilisateur trouvé."
        return render_template('pages/recuperer_user.html', message=message)
# pour un abonner
# Exemple de configuration de session dans votre route seconnecter


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

# Ajoutez une fonction pour vérifier le mot de passe (peut varier en fonction de votre implémentation de hachage)
def check_password(hashed_password, user_password):
    # À implémenter en fonction de votre méthode de hachage
    return hashed_password == user_password

@app.route('/modifier_infos/', methods=['GET', 'POST'])
def modifier_infos():
    # Assurez-vous que l'utilisateur est authentifié en vérifiant s'il existe dans la session
    if 'user_id' not in session:
        return redirect(url_for('index'))

    # Obtenez l'utilisateur à partir de la session
    user_id_session = session['user_id']
    user = gestionnaire.get_user(user_id_session)

    # Gérez le cas où l'utilisateur n'existe pas
    if user is None:
        return redirect(url_for('index'))

    if request.method == 'POST':
        nouveau_nom = request.form.get('username')
        nouveau_password = request.form.get('password')
        nouveau_email = request.form.get('email')

        message = gestionnaire.modifier_infos(user, nouveau_nom, nouveau_password, nouveau_email)

        # Utilisez user_id dans l'URL pour la redirection
        return redirect(url_for('recuperer_user', user_id=user.id, message=message))

    return render_template('pages/modifier_infos.html', user=user)
