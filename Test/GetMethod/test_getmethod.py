from email.headerregistry import ContentTypeHeader

from playwright.sync_api import sync_playwright

api_url = "https://jsonplaceholder.typicode.com/todos/1"
def test_get_method():
    with sync_playwright() as playwright:
        context = playwright.request.new_context()
        response = context.get(url= api_url)
        print(response)
        assert response.status == 200
        assert response.status_text == "OK"
        assert response.json().get("id") == 1
        assert response.json().get("title") == "delectus aut autem"
        print(response.json()["title"])













