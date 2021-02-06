from collections import deque

males = [int(num) for num in input().split() if int(num) > 0]
females = deque([int(num) for num in input().split() if int(num) > 0])
matches_count = 0

while females and males:
    current_female = females[0]
    current_male = males[-1]
    if current_male % 25 == 0:
        males.pop()
        continue
    elif current_female % 25 == 0:
        females.popleft()
        continue
    elif current_female == current_male:
        males.pop()
        females.popleft()
        matches_count += 1
    else:
        females.popleft()
        males[-1] -= 2
        if males[-1] <= 0:
            males.pop()


print(f"Matches: {matches_count}")
if males:
    print(f"Males left: {', '.join(reversed([str(num) for num in males]))}")
else:
    print("Males left: none")
if females:
    print(f"Females left: {', '.join([str(num) for num in females])}")
else:
    print("Females left: none")