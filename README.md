##Ident Call

Library to be added to other projects for a quick auth, without requiring pypi'ing rax specific libraries but does **require requests**

##To Use:
```
from ident import IdentCall
foo = IdentCall()
foo.set_auth(username='<USER>', apikey='<APIKEY>')
token = foo.get_api_token()
#do stuff with it
```

##Unit Testing
Added unit testing. Can be run from the main directory with:
```
python -m unittest -s ./ discover -v
```
**or**
```
python -m tests.identTest --verbose
```
###Unit Testing test file
Creds must be included in the tests/testcreds.json file. The tests/testcreds.json.sample can be copied and correct values placed

##TODO
* Validate token every 13 minutes
* Pretty much serves its purpose..
* Whatever else seems handy
