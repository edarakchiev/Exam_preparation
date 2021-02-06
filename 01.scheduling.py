from collections import deque


jobs = deque([int(num) for num in input().split(", ")])
index = int(input())
my_job = jobs[index]
cycles = 0
#
# for i in range(index+1):
#     if jobs[i] <= my_job:
#         cycles += jobs.popleft()

for _ in range(len(jobs)):
    current_job = jobs.popleft()
    if current_job <= my_job:
        cycles += current_job


print(cycles)
