from flask import jsonify, request
from setup import db
from setup.api import bp
from setup.api.auth import verify_password, token_auth
from setup.api.errors import error_response

@bp.route('/tokens', methods=['POST'])
def get_token():
    username = request.json.get("username", None)
    password = request.json.get("password", None)
    user = verify_password(username, password)
    if user is None:
        return error_response(401, "Incorrect username or password")
    data = user.to_dict()
    data['token'] = user.get_token()
    db.session.commit()
    return jsonify(data)

@bp.route('/tokens', methods=['DELETE'])
@token_auth.login_required
def revoke_token():
    token_auth.current_user().revoke_token()
    db.session.commit()
    return '', 204