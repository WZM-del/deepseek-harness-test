import random

# 随机生成 1-100 的数字
target = random.randint(1, 100)

print("猜数字游戏开始！我想了一个 1-100 之间的数字。")

guesses = 0

while True:
    try:
        guess = int(input("请输入你的猜测："))
    except ValueError:
        print("请输入一个有效的整数！")
        continue

    guesses += 1

    if guess < target:
        print("小了")
    elif guess > target:
        print("大了")
    else:
        print(f"恭喜你猜对了！数字是 {target}，你一共猜了 {guesses} 次。")
        break
