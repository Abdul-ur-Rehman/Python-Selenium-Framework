import pytest

@pytest.fixture(scope="class")
def setup():
    print("I will be executing first")
    yield
    print(" I will execute last")

@pytest.fixture()
def dataLoad():
    print("user profile data is being created")
    return ["Abdur","Rehman","testdemo@gmail.com"]


@pytest.fixture(params=[("chrome","Abdur","Rehman"), ("Firefox","Chattha"), ("IE","ABC")])
def crossBrowser(request):
    return request.param