from time import perf_counter
from functools import wraps, cache

print("*** Mierzenie czasu wykonania silni ***")


def operation_time(callback):
    @wraps(callback)
    def wrapper(number):
        start_time = perf_counter()
        callback(number)
        end_time = perf_counter()
        time_of_operation = end_time - start_time
        return time_of_operation
    return wrapper


@operation_time
def calculate_factorial(number):
    function_sum = 1
    for i in range(1, number + 1):
        function_sum *= i
        # print(f"Numer iteracji to: {i}.")
        # print(f"Suma wynosi: {function_sum}.")
    return function_sum


@cache
@operation_time
def calculate_factorial_with_cache(number):
    function_sum = 1
    for i in range(1, number + 1):
        function_sum *= i
        # print(f"Numer iteracji to: {i}.")
        # print(f"Suma wynosi: {function_sum}.")
    return function_sum


with open("results.txt", "w") as file_stream:
    required_factorial_values = [1, 9, 27, 88, 175, 299, 512, 1024]
    for value in required_factorial_values:
        file_stream.write(f"Czas obliczenia silni dla wartości {value} wynosi {calculate_factorial(value):.25f}s.")
        file_stream.write("\n")


with open("results_with_cache.txt", "w") as file_stream:
    required_factorial_values = [1, 9, 27, 88, 175, 299, 512, 1024]
    for value in required_factorial_values:
        file_stream.write(f"Czas obliczenia silni dla wartości {value} "
                          f"wynosi {calculate_factorial_with_cache(value):.25f}s.")
        file_stream.write("\n")

print("Polecenie wykonano pomyślnie.")
