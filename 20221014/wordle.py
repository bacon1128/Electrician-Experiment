#使用者輸入（Commit）
if __name__ == "__main__":
    user_input = input("Type a word:")
    print("Your input is", user_input)

    #指定一個正確答案（Commit）(簡易)
    answer = "apple"

    #判斷使用者輸入與解答（Commit）
    for i in range(len(user_input)):
        if user_input[i] == answer[i]:
            print("A")
        elif user_input[i] in answer:
            print("B")
        else:
            print("X")