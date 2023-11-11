print("*** Mierzenie czasu wykonania silni ***")


def calculate_factorial(number):
    function_sum = 1
    for i in range(1, number + 1):
        function_sum = function_sum * i
        # print(f"Numer iteracji to: {i}.")
        # print(f"Suma wynosi: {function_sum}.")
    return function_sum


print(calculate_factorial(10))
