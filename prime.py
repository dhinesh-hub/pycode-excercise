def prime(num):
    for i in range(2,num):
        if num%i == 0:
            return "not prime"
            break
    return "prime"

print prime(7)

