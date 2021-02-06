from collections import deque

customers = deque([int(n) for n in input().split(", ")])
taxis = ([int(n) for n in input().split(", ")])

time = 0

while customers:
    current_customer = customers[0]
    if taxis:
        current_taxi = taxis[-1]
    else:
        break
    if current_taxi >= current_customer:
        time += customers.popleft()
    taxis.pop()


if customers:
    print(f"Not all customers were driven to their destinations")
    print(f"Customers left: {', '.join([str(el) for el in customers])}")
else:
    print(f"All customers were driven to their destinations")
    print(f"Total time: {time} minutes")