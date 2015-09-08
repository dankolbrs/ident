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

##TODO
* Validate token every 13 minutes
* Pretty much serves its purpose..
* Whatever else seems handy
