from flask import jsonify, request
from setup import db
from setup.api import bp
from setup.api.auth import verify_password, token_auth

@bp.route('/tokens', methods=['POST'])
def get_token():
    username = request.json.get("username", None)
    password = request.json.get("password", None)
    user = verify_password(username, password)
    token = user.get_token()
    db.session.commit()
    return jsonify({'token': token})

@bp.route('/tokens', methods=['DELETE'])
@token_auth.login_required
def revoke_token():
    token_auth.current_user().revoke_token()
    db.session.commit()
    return '', 204