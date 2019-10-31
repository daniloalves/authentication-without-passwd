## What's up
* This model create a security authentication based deal tokens or hashs. Without send a secret key. Is a very simple model, think communication server to server.

## How To
* Get a token.
    * `curl http://localhost:5000/api/token/user1`
* Encrypt token with secret key.
* Send token encripted on header.
    * `curl -H "X-Auth: user1:$user1_token" http://localhost:5000/api/name/user1`
    
## Issues
* Create a example of client.
    * Get Hash: http://localhost:5000/api/token/user1
    * Convert pass to SHA256 (named passwd_sha).
    * Convert passwd_sha+Hash first step to SHA256.
