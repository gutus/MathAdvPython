# MySum Function For Sigma i=0-20 Sigma n**2 + 1

def mySum2(num):
    running_sum = 0
    for i in range(num+1):
        running_sum += i**2 + 1

    return running_sum


mySum2(20)
