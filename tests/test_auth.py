from application.models import Entry
import datetime as datetime
import pytest
from flask import json

# Validation Test

# Test Sign Up API

@pytest.mark.xfail(reason="Already exist")
@pytest.mark.parametrize("logInInfo", [
  ["email","username2","password", 0],
  ["sohhongyu@gmail.com","Hong Yu","123", 0],
  ["test@gmail.com", "test", "123", 0],
  ["sohhongyu@gmail.com", "987", "128", 0],
]
)
# Validation Test
@pytest.mark.xfail(reason="Not Valid Username or Password")
@pytest.mark.parametrize("logInInfo", [
  ["sohhongyu@gmail.com","123", 0],
  ["sohhongyu123@gmail.com", "123", 1],
  ["sohhongyu@gmail.com","123123", 1],
  ["devops@gmail.com", "123", 1]
]
)
def test_signUpAPI(client, logInInfo, capsys):
    with capsys.disabled():
        # prepare the data into a dictionary
        logInData = {
            "email": logInInfo[0],
            "password": logInInfo[1]
        }
    response = client.post('/api/login',
                           data=json.dumps(logInData),
                           content_type="application/json",)
    # check the outcome of the action
    assert response.status_code == 200
    assert response.headers["Content-Type"] == "application/json"
    response_body = json.loads(response.get_data(as_text=True))
    assert not response_body["isLogin"] == logInInfo[2]
