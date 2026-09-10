

correct_id = "admin"
correct_pw = "1234"

count = 0

while count < 3:
    user_id = input("ID를 입력하세요: ")
    user_pw = input("PASSWORD를 입력하세요: ")

    if user_id == correct_id and user_pw == correct_pw:
        print("로그인 되었습니다.")
        print("===== 메뉴 =====")
        print("1. ")
        print("2. ")
        print("3. ")
        break

    else:
        count = count + 1
        print("ID 또는 PASSWORD가 일치하지 않습니다.")

        if count == 3:
            print("3회 실패하여 프로그램을 종료합니다.")

def login():

    correct_id = "admin"
    correct_pw = "1234"

    count = 0

    while count < 3:

        user_id = input("ID를 입력하세요: ")
        user_pw = input("PASSWORD를 입력하세요: ")

        if user_id == correct_id and user_pw == correct_pw:
            print("로그인 되었습니다.")
            return True

        else:
            count = count + 1
            print("ID 또는 PASSWORD가 일치하지 않습니다.")

    print("3회 실패하여 프로그램을 종료합니다.")
    return False  