
def compute_average(numbers):
  if not numbers:
    return 0
  else:
    total = sum(numbers)
    average = total / len(numbers)
    return average
my_list = [1, 2, 3, 4, 5]
result = compute_average(my_list)
print(result)  # Output: 3.0

empty_list = []
result = compute_average(empty_list)
print(result)  # Output: 0


