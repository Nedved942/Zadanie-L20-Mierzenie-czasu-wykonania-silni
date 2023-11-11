from time import time
from datetime import datetime
from functools import wraps

print("*** Mierzenie czasu wykonania silni ***")


def operation_time(callback):
    @wraps(callback)
    def wrapper(number):
        # start_time = datetime.now()
        start_time = time()
        callback(number)
        # end_time = datetime.now()
        end_time = time()
        time_of_operation = end_time - start_time
        return time_of_operation
    return wrapper


@operation_time
def calculate_factorial(number):
    function_sum = 1
    for i in range(1, number + 1):
        function_sum = function_sum * i
        # print(f"Numer iteracji to: {i}.")
        # print(f"Suma wynosi: {function_sum}.")
    return function_sum


print(calculate_factorial(11000))

with open("results.txt", "w") as file_stream:
    required_factorial_values = [1, 9, 27, 88, 175, 299, 512, 1024]
    for value in required_factorial_values:
        file_stream.write(f"Czas obliczenia silni dla wartości {value} wynosi {calculate_factorial(value)}s.")
        file_stream.write("\n")



