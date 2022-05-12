import base64
from main import test_main
def test_main_func():
    string = "x"
    assert base64.b64encode(string.encode("utf-8")) == test_main()