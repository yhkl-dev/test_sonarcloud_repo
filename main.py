import os


import base64
import requests
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



for r in result:
    print(r)

def test_main():
    testURL = "https://www.baidu.com"
    res = requests.get(testURL)
    print("test main function")
    string = "x"


    
    return base64.b64encode(string.encode("utf-8"))


def main():

    print("hello world")


if __name__ == "__main__":
    main()
