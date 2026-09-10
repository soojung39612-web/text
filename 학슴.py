line = "민수,팔십오"

try:
    data = line.strip().split(",")
    name = data[0]
    score = int(data[1])

except ValueError:
    print("점수는 숫자로 입력해야 합니다.")

else:
    print(name, score)
    