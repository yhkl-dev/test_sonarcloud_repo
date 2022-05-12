import base64
from main import test_main,pay_status
def test_main_func():
    string = "x"
    assert base64.b64encode(string.encode("utf-8")) == test_main()

def test_pay_success():
    result = {
            "code": 0,
            "msg": "success!",
            "data": []
        }
    assert pay_status(result) == "支付成功"