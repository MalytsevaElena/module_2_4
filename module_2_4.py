numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes =[]
not_primes = []
for number in numbers:
    if number == 1:
        continue
    else:
        for i in range(2, int(number ** 0.5)+1):
            if number % i == 0:
                not_primes.append(number)
                break
        else:
            primes.append(number)
print('Primes: ', primes)
print('Not_primes: ', not_primes)
