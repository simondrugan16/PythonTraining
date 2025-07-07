import requests

fake_headers = {
    "X-AUTH-HEADER": "fake-test-header"
}

fake_request = {
    "id": "fake id",
    "some info": "infosss"
}

post_result = requests.post(url="http/fake-url.com", json=fake_request, headers=fake_headers)

