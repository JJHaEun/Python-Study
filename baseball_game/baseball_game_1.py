import random

numbers = list(range(1,10))
print(numbers)

three_numbers = random.sample(numbers,3)
print("맞춰야할 숫자: ", three_numbers)