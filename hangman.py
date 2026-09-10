import random
import os


# ==========================================
# 로그인
# ==========================================

def login():
    correct_id = "admin"
    correct_pw = "1234"

    count = 0

    while count < 3:
        user_id = input("ID를 입력하세요: ")
        user_pw = input("PASSWORD를 입력하세요: ")

        if user_id == correct_id and user_pw == correct_pw:
            print("\n로그인 되었습니다.")
            return True

        count += 1
        print("ID 또는 PASSWORD가 일치하지 않습니다.")

        if count < 3:
            print(f"남은 로그인 횟수: {3 - count}")

    print("3회 실패하여 프로그램을 종료합니다.")
    return False


# ==========================================
# 닉네임 관리
# ==========================================

class NicknameManager:

    def __init__(self):
        self.names = []

    def create_nickname(self):
        while True:
            name = input("닉네임을 입력해주세요: ").strip()

            if not name:
                print("닉네임을 입력해주세요.")
                continue

            if name in self.names:
                print("중복된 닉네임입니다!")
            else:
                self.names.append(name)
                print(f"{name}님 환영합니다!")
                return name


# ==========================================
# 게임 기록 / 랭킹
# ==========================================

class History:

    def __init__(self):
        self.records = []

    def save(self, name, game, count, result):
        self.records.append({
            "name": name,
            "game": game,
            "count": count,
            "result": result
        })

    def show_ranking(self):
        if not self.records:
            print("\n아직 등록된 랭킹 기록이 없습니다.")
            return

        # 성공한 기록만 랭킹에 표시
        success_records = [
            record
            for record in self.records
            if record["result"] == "성공"
        ]

        if not success_records:
            print("\n아직 성공한 게임 기록이 없습니다.")
            return

        # 시도 횟수가 적은 순서
        ranking = sorted(
            success_records,
            key=lambda record: record["count"]
        )

        print("\n==============================")
        print("          게임 랭킹")
        print("==============================")

        for i, record in enumerate(ranking[:10], start=1):
            print(
                f"{i}위 | "
                f"{record['name']} | "
                f"{record['game']} | "
                f"{record['count']}회"
            )

        print("==============================")


# ==========================================
# 행맨 게임
# ==========================================

class Hangman:

    def __init__(self, history):
        self.history = history

        self.country = [
            "korea",
            "japan",
            "china",
            "canada",
            "mexico",
            "france",
            "italy"
        ]

    def game(self, name):

        word = random.choice(self.country)

        guessed = []
        life = 6
        count = 0

        print("\n==============================")
        print("          행맨 게임")
        print("==============================")

        print(f"단어의 길이: {len(word)}")
        print("목숨: 6")

        while life > 0:

            print()

            for letter in word:
                if letter in guessed:
                    print(letter, end=" ")
                else:
                    print("_", end=" ")

            print()

            guess = input(
                "알파벳 한 글자를 입력하세요: "
            ).lower().strip()

            # 입력 검사
            if len(guess) != 1 or not guess.isalpha():
                print("알파벳 한 글자만 입력해주세요.")
                continue

            # 이미 입력한 문자
            if guess in guessed:
                print("이미 입력한 문자입니다.")
                continue

            guessed.append(guess)
            count += 1

            if guess in word:
                print("맞혔습니다!")

            else:
                life -= 1
                print("틀렸습니다!")
                print(f"남은 목숨: {life}")

            # 정답 확인
            if all(
                letter in guessed
                for letter in word
            ):
                print("\n정답입니다!")
                print(f"정답: {word}")
                print(f"총 {count}회 시도했습니다.")

                self.history.save(
                    name,
                    "행맨",
                    count,
                    "성공"
                )

                return

        print("\n패배했습니다.")
        print(f"정답은 {word}였습니다.")

        self.history.save(
            name,
            "행맨",
            count,
            "실패"
        )


# ==========================================
# 업앤다운
# ==========================================

class UpDown:

    def __init__(self, history):
        self.history = history

    def game(self, name):

        print("\n==============================")
        print("        업앤다운 게임")
        print("==============================")

        print("난이도를 선택하세요.")
        print("1. 상 (1~500)")
        print("2. 중 (1~250)")
        print("3. 하 (1~50)")

        level = input("선택: ")

        if level == "1":
            maximum = 500

        elif level == "2":
            maximum = 250

        elif level == "3":
            maximum = 50

        else:
            print("잘못된 선택입니다.")
            return

        answer = random.randint(1, maximum)

        count = 0

        print(f"\n1부터 {maximum} 사이의 숫자입니다.")

        while True:

            try:
                number = int(
                    input("숫자를 입력하세요: ")
                )

            except ValueError:
                print("숫자만 입력해주세요.")
                continue

            if number < 1 or number > maximum:
                print(
                    f"1부터 {maximum} 사이의 숫자를 입력해주세요."
                )
                continue

            count += 1

            if number == answer:

                print(
                    f"\n정답입니다! "
                    f"총 {count}회 시도하셨습니다."
                )

                self.history.save(
                    name,
                    "업앤다운",
                    count,
                    "성공"
                )

                break

            elif number < answer:
                print("UP! 더 높게 입력하세요.")

            else:
                print("DOWN! 더 낮게 입력하세요.")


# ==========================================
# 로또
# ==========================================

class Lotto:

    def __init__(self):
        self.history = []
        self.filename = "lotto_history.txt"

        self.load_history()

    def generate_numbers(self):

        numbers = random.sample(
            range(1, 46),
            6
        )

        numbers.sort()

        return numbers

    def game(self):

        print("\n==============================")
        print("          로또 게임")
        print("==============================")

        numbers = self.generate_numbers()

        print("추첨 결과:")
        print(*numbers)

        self.history.append(numbers)

        self.save_numbers(numbers)

    def save_numbers(self, numbers):

        with open(
            self.filename,
            "a",
            encoding="utf-8"
        ) as file:

            file.write(
                ",".join(
                    map(str, numbers)
                )
                + "\n"
            )

    def load_history(self):

        if not os.path.exists(self.filename):
            return

        try:

            with open(
                self.filename,
                "r",
                encoding="utf-8"
            ) as file:

                for line in file:

                    line = line.strip()

                    if not line:
                        continue

                    numbers = [
                        int(number)
                        for number in line.split(",")
                    ]

                    if len(numbers) == 6:
                        self.history.append(numbers)

        except Exception:
            print("로또 기록을 불러오는 중 문제가 발생했습니다.")

    def show_history(self):

        print("\n==============================")
        print("       로또 과거 추첨 기록")
        print("==============================")

        if not self.history:
            print("아직 로또 추첨 기록이 없습니다.")
            return

        for i, numbers in enumerate(
            self.history,
            start=1
        ):
            print(
                f"{i}회차 : {numbers}"
            )


# ==========================================
# 통합 게임 프로그램
# ==========================================

class GameProgram:

    def __init__(self):

        self.nickname_manager = NicknameManager()

        self.history = History()

        self.hangman = Hangman(
            self.history
        )

        self.updown = UpDown(
            self.history
        )

        self.lotto = Lotto()

    def start(self):

        print("==============================")
        print("       통합 게임 프로그램")
        print("==============================")

        # 로그인
        if not login():
            return

        # 닉네임
        name = self.nickname_manager.create_nickname()

        while True:

            print("\n==============================")
            print("            메뉴")
            print("==============================")
            print("1. 행맨")
            print("2. 업앤다운")
            print("3. 로또")
            print("4. 게임 랭킹")
            print("5. 로또 기록 보기")
            print("6. 종료")
            print("==============================")

            choice = input("메뉴를 선택하세요: ")

            if choice == "1":

                self.hangman.game(name)

            elif choice == "2":

                self.updown.game(name)

            elif choice == "3":

                self.lotto.game()

            elif choice == "4":

                self.history.show_ranking()

            elif choice == "5":

                self.lotto.show_history()

            elif choice == "6":

                print("\n프로그램을 종료합니다.")
                print(f"{name}님 이용해주셔서 감사합니다.")
                break

            else:

                print("잘못된 메뉴입니다.")


# ==========================================
# 실행
# ==========================================

if __name__ == "__main__":

    program = GameProgram()

    program.start()
