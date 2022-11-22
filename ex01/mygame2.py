import random
import string

num_of_allset = 5
num_of_fail = 2

def game2():
    QLst = []
    FLst = []
    for i in range(num_of_allset):
        while True:
            item = random.choice(string.ascii_uppercase)
            if item not in QLst:
                QLst.append(item)
                break
            else:
                continue
    
    print("対象文字:")
    for item in QLst:
        print(item + "　", end="")
    print()

    for i in range(num_of_fail):
        
        index = random.randint(0, len(QLst)-1)
        FLst.append(QLst.pop(index))
        
    print("欠損文字:")
    for item in FLst:
        print(item + "　", end="")
    print()

    print("表示文字:")
    for item in QLst:
        print(item + "　", end="")
    print()
    


    



if __name__ == "__main__":
    game2()
