import os


import base64
testArguments = 100

X = [[12, 7],
     [4, 5],
     [3, 8]]

result = [[0, 0, 0],

          [0, 0, 0]]

# iterate through rows
for i in range(len(X)):
    # iterate through columns
    for j in range(len(X[0])):

        result[j][i] = X[i][j]

def pay_status(result):
    '''根据接口返回code状态，给用户提示对应的结果'''
    if result.get("code") == 0:
        return "支付成功"
    elif result.get("code") == 30000:
        return "支付失败: %s" % result.get("msg")
    elif result.get("code") == 30001:
        return "支付失败: %s" % result.get("msg")
    elif result.get("code") == 30002:
        return "支付失败: %s" % result.get("msg")
    elif result.get("code") == 201102:
        return "支付失败: %s" % result.get("msg")
    else:
        return "支付失败: 系统异常，未知错误"

for r in result:
    print(r)

def test_main():
    testURL = "https://www.baidu.com"
    # res = requests.get(testURL)
    print("test main function")
    string = "x"



    return base64.b64encode(string.encode("utf-8"))


def main():

    print("hello world")


if __name__ == "__main__":
    main()
