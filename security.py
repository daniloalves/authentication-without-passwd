from commons import log
import connexion
from connexion.exceptions import OAuthProblem
import hashlib

USER_DB = {
    'user1': {
        # Passwd: 'usu1'
        'passwd': 'ea7b4ed10dd6fb56b506428183714aa40948a6d78048068657ff56c41c06bd50',
        'uid': 0
    }
}
TOKEN_DB = {} # Token to user1: 3691fc223cbc6e0a9721a0b03bd408058197ef2eb5a9d51d0b0addd9ce7cd84b

def basic_auth(username):
    log(f"Token to user: {username}")
    user_sha = USER_DB.get(username, None)
    return_token = 123
    string_token = f"{return_token}:{user_sha}"
    byte_hash = hashlib.sha256(string_token.encode()).hexdigest()
    TOKEN_DB[username] = byte_hash
    return return_token

def apikey_auth(credentials, required_scopes):
    def invalied_token(username="undefined"):
        msg = f"Invalid token User: {username}"
        log(msg,'critical')
        raise OAuthProblem('Invalid token')
    if ':' not in credentials:
        invalied_token()
    username = credentials.split(':')[0]
    token = credentials.split(':')[1]
    validate = TOKEN_DB.get(username, None)
    
    if not validate or validate != token:
        invalied_token(username)
    log(f"User Logged: {username}")
    return USER_DB.get(username)
    