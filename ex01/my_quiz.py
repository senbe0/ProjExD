from random import randint, choice

Quiz = None 
QApair = {
    "サザエの旦那の名前は？": ["マスオ", "ますお"],
    "カツオの妹の名前は？": ["ワカメ", "わかめ"],
    "タラオはカツオから見てどんな関係？": ["甥", "おい", "甥っ子", "おいっこ"]
}

def shutudai():
    global Quiz
    Quiz = list(QApair)[randint(0,2)]
    print(Quiz)

# is the ans correct?
def kaitou():
    ans = input("回答を入力 > ")
    if ans in QApair[Quiz]:
        print("正解！！！")
    else:
        print("出直してこい")

if __name__ == "__main__":
    shutudai()
    kaitou()

