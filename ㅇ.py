import random

history = []
gamers = []

        

def lotto_numbers():
    lotto = []
    while len(lotto) < 6:
        target = random.randint(1, 45)
        if target not in lotto:
            lotto.append(target)
        else:
            continue
    lotto.sort()
    print("출력", lotto)
    with open("lotto_history.txt","a", encoding="utf-8")as file:
        file.write(str(lotto))
    return lotto  


def lotto_game():
    lotto = lotto_numbers() 
    print("추첨 결과: ", end="")
    print(*lotto)

    history.append(lotto.copy())


def updown_game(name, n):
    count = 0
    while True:
        x = int(input("숫자를 입력하세요!:"))
        print(n)
        count += 1
        if n == x:
            print(f"정답입니다!총{count}회 시도하셨습니다.")
            gamers.append({"name": name, "count": count})
            break
        elif n < x:
            print("낮게 입력하세요!")
        else:
            print("높게 입력하세요")

    with open("lotto_history.txt","a", encoding="utf-8")as file:
            file.write(str(gamers))
            
def ranking_view():
    if len(history) == 0:
        print("아직 로또 추첨 기록이 없습니다.")
    else:
        print()
        print("==========================")
        print("      로또 과거 이력")
        print("==========================")
        for i in range(len(history)):
            print(i + 1, "회차 :", history[i])


    if len(gamers) == 0:
        print("아직 등록된 랭킹 기록이 없습니다.")
    else:
        gamers.sort(key=lambda player: player["count"])

    print("--- 현재 랭킹 ---")
    for player in gamers:
        print(f"이름: {player['name']} | 시도 횟수: {player['count']}회")

    with open("lotto_history.txt","a", encoding="utf-8")as file:
        file.write(str(history))
def main():
    while True:
        m = input("모드 선택:1.게임 선택 2.랭킹보기 3.종료하기:")

        if m == "1":
            game = input("어떤 게임을 선택하시겠어요? 1.로또 2.업앤다운:")

            if game == "1":
                lotto_game()

            elif game == "2":
                name = input("닉네임을 입력하세요->")
                level = input("1.상,2.중,3.하 선택하세요->")
                if level == '1' :
                    max = 500
                elif level == '2':
                    max = 250
                elif level=='3':
                    max = 50
                a = random.randint(1, max)
                updown_game(name, a)

        elif m == "2":
            ranking_view()

        elif m == "3":
            print("종료하겠습니다.")
            break
        
def save_lotto(lotto):
    line = ""

    for i in range(len(lotto)):
        line += str(lotto[i])

        if i < len(lotto) - 1:
            line += ","

    with open("lotto_history.txt", "a", encoding="utf-8") as file:
        file.write(line + "\n")        
        
def load_lotto_history():
    lotto_history = []

    try:
        with open("lotto_history.txt", "r", encoding="utf-8") as file:
            lines = file.readlines()

        for line in lines:
            data = line.strip().split(",")
            lotto = []

            for number in data:
                lotto.append(int(number))

            lotto_history.append(lotto)

    except FileNotFoundError:
        print("아직 저장된 로또 이력이 없습니다.")

    return lotto_history
main()