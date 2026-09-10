

# 닉네임 저장
class Nickname_save:

    def __init__(self):
        self.names = []

    def nickname(self):
        while True:
            name = input("닉네임을 입력해주세요: ")
            print()
            if name in self.names:
                print("중복된 닉네임입니다!")
                print()
            else:
                self.names.append(name)
                return name


class History:

    def __init__(self):
        self.history = {}
        self.leaderboard = []

# 히스토리 저장
    def save_history(self, name, try_count, life):

        if life > 0:
            self.history[name] = try_count

            if len(self.leaderboard) == 0:
                self.leaderboard.append(name)

            else:
                for i in range(len(self.leaderboard)):

                    if try_count < self.history[self.leaderboard[i]]:
                        self.leaderboard.insert(i, name)
                        return

                    elif i == len(self.leaderboard) - 1:
                        self.leaderboard.append(name)
                        return

    # 2. 기록 보기
    def find_leaderboard(self):

        rank = int(input("몇 순위까지 보시겠습니까?: "))
        print()

        if len(self.leaderboard) == 0:
            print("조회할 랭킹이 없습니다!")
            return
        elif rank > len(self.leaderboard):
            rank = len(self.leaderboard)

        for i in range(0, rank):
            print(f"{i+1}위: {self.leaderboard[i]} {self.history[self.leaderboard[i]]}회")

        print()
        return

