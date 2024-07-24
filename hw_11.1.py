'hw_11.1'
def prime_generator(end):
    def is_prime(num):
        if num <= 1:
            return False
        if num <= 3:
            return True
        if num % 2 == 0 or num % 3 == 0:
            return False
        num_init = 5
        while num_init * num_init <= num:
            if num % num_init == 0 or num % (num_init + 2) == 0:
                return False
            num_init += 6
        return True
    for num in range(2, end + 1):
        if is_prime(num):
            yield num

from inspect import isgenerator

gen = prime_generator(1)
assert isgenerator(gen) == True, 'Test0'
assert list(prime_generator(10)) == [2, 3, 5, 7], 'Test1'
assert list(prime_generator(15)) == [2, 3, 5, 7, 11, 13], 'Test2'
assert list(prime_generator(29)) == [2, 3, 5, 7, 11, 13, 17, 19, 23, 29], 'Test3'
print('Ok')
