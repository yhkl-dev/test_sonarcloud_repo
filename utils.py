import base64
def test_case():
    print("hello world")
    print("sss")

def encrypt_string_base64(string):
    return base64.b64encode(string.encode("utf-8"))