

def sum_three(a, b, c):
    return a + b + c


def is_prime(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        if result > 1:
            if all((result % i != 0) for i in range(2, int(result ** 0.5) + 1)):
                return "Простое"
            else:
                return "Составное"

    return wrapper


@is_prime
def sum_three(a, b, c):
    result = a + b + c
    print(result)
    return result


res = sum_three(2, 3, 6)
print(res)
