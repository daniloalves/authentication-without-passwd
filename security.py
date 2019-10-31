from commons import log
import connexion
from connexion.exceptions import OAuthProblem

USER_DB = {
    'user1': 'ea7b4ed10dd6fb56b506428183714aa40948a6d78048068657ff56c41c06bd50'
    # Passwd: 'usu1'
}
TOKEN_DB = {}

def basic_auth(username):
    log(f"Token to user: {username}")
    return '123'

def apikey_auth(token, required_scopes):
    validate = ''
    