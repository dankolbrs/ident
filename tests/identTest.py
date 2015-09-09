#! /usr/bin/env python

import json, unittest, sys

from lib.ident import IdentCall

JSON_DATA_LOC = './tests/testcreds.json'

class TestIdent(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        #find out if verbose passed.. hack?
        if ("-v" or "--verbose") in sys.argv:
           cls.verbose = True
        else:
            cls.verbose = False

    def setUp(self):
        creds = json.loads(open(JSON_DATA_LOC).read())
        self.with_key = IdentCall(username=creds["user_name"], apikey=creds["api_key"])
        self.with_pass = IdentCall(username=creds["user_name"], password=creds["password"])

    def test_api_token_not_null_with_key(self):
        if self.verbose:
            print "with_key token: ", str(self.with_key.get_api_token())
        self.assertIsNotNone(self.with_key.get_api_token(),"failed")

    def test_api_token_not_null_with_pass(self):
        if self.verbose:
            print "with_pass token: ", str(self.with_pass.get_api_token())
        self.assertIsNotNone(self.with_pass.get_api_token(),"failed")

    def test_tokens_equality(self):
        self.assertNotEqual(self.with_pass.get_api_token(),
                         self.with_key.get_api_token(),
                         "Tokens equal")

def main():
    unittest.main()

if __name__ == '__main__':
    main()
