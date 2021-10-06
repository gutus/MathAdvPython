# Sum Function to The Specified number


running_sum = 0
for i in range(5):
    running_sum += i
print(running_sum)


def mySum(num):
    running_sum = 0
    for i in range(1, num+1):
        running_sum += i
    print(running_sum)


mySum(10)
