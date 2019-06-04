def isPrime(num):
    if num > 1:
      for i in range(2,num/2):
        if (num % i) == 0:
           return str(num) + "isNotPrime"
      else:
           return str(num) + "isPrime"
    else:
        return str(num) + "isNotPrime"

print(isPrime(16))
