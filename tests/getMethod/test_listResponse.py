from playwright.sync_api import sync_playwright

api_url = 'https://reqres.in/api/users'
x_api_key = 'reqres-free-v1'

def test_listResponse():
    with sync_playwright() as playwright:
        context = playwright.request.new_context()
        response = context.get(url=api_url, headers={"x-api-key": x_api_key})
        print(response.json())
        res = response.json()
        #print(res["data"][0]["first_name"])
        assert res["data"][0]["first_name"] == "George"
        assert res["data"][0]["email"] == "george.bluth@reqres.in"
        assert res["data"][1]["first_name"] == "Janet"
        assert res["data"][1]["email"] == "janet.weaver@reqres.in"

