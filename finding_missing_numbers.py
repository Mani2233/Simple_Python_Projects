empty_list = []
for i in range(5):
    numbers = int(input("Enter a value: "))
    empty_list.append(numbers)
new_list = sorted(empty_list)

print(f"Given list is {new_list}")


def find_missing_numbers(start, end, values):
    missing_numbers = []
    for num in range(start, end + 1):
        if num not in values:
            missing_numbers.append(num)
    return missing_numbers


print(f"The missing numbers between {new_list} are:\n\n", find_missing_numbers(new_list[0], new_list[-1], new_list))
