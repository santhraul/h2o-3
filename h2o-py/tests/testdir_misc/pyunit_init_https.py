#!/usr/bin/env python
# -*- encoding: utf-8 -*-
import sys
sys.path.insert(1,"../../")
import h2o
from tests import pyunit_utils
from h2o.exceptions import H2OConnectionError

def test_https_startup():
    try:
        h2o.init(ip = "127.0.0.1", port="12345", https=True)  # Port 12345 is used, as 54321 is expected to be occupied
        assert False, "Expected to fail starting local H2O server with https=true"
    except H2OConnectionError as err:
        print(err)  # HTTPS is not allowed during localhost startup
        assert "Unable to start local server with https enabled. Consider disabling https." == str(err)

if __name__ == "__main__":
    pyunit_utils.standalone_test(test_https_startup)
else:
    test_https_startup()
