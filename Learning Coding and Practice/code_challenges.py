#   Control Flow
# Large power
def large_power(base, exponent):
  if base ** exponent > 5000:
    return True
  else:
    return False
print(large_power(2, 13)) # prints True
print(large_power(2, 12)) # prints False


#   Control Flow Advanced
# Movie Review
def movie_review(rating):
  if rating <= 5:
    return "Avoid at all costs!"
  elif rating < 9:
    return "This one was fun."
  else:
    return "Outstanding!"
print(movie_review(9)) # prints "Outstanding!"
print(movie_review(4)) # prints "Avoid at all costs!"
print(movie_review(6)) # prints "This one was fun."

# Max Num
def max_num(num1, num2, num3):
  if num1 > num2 and num1 > num3:
    return num1
  elif num2 > num1 and num2 > num3:
    return num2
  elif num3 > num1 and num3 > num2:
    return num3
  else: return "It's a tie!"
print(max_num(-10, 0, 10)) # prints 10
print(max_num(-10, 5, -30)) # prints 5
print(max_num(-5, -10, -10)) # prints -5
print(max_num(2, 3, 3)) # prints "It's a tie!"


#   Lists
# Append Sum
def append_sum(my_list):
  for num in range(3):
    my_list.append(my_list[-2]+my_list[-1])
  return my_list
print(append_sum([1, 1, 2])) # prints [1, 1, 2, 3, 5, 8]

# Larger List
def larger_list(my_list1, my_list2):
  if len(my_list1) >= len(my_list2):
    return my_list1[-1]
  else:
    return my_list2[-1]
print(larger_list([4, 10, 2, 5], [-10, 2, 5, 10])) # prints 5

# More Than N
def more_than_n(my_list, item, n):
  if my_list.count(item) > n:
    return True
  else: 
    return False
print(more_than_n([2, 4, 6, 2, 3, 2, 1, 2], 2, 3)) # prints True

# Combine Sort
def combine_sort(my_list1, my_list2):
  combined_list = my_list1 + my_list2
  combined_list.sort()
  return combined_list
print(combine_sort([4, 10, 2, 5], [-10, 2, 5, 10])) # prints [-10, 2, 2, 4, 5, 5, 10, 10]


#   Loops
# Divisible By 10
def divisible_by_ten(nums):
  count = 0
  for num in nums:
    if num % 10 == 0:
      count += 1
  return count
print(divisible_by_ten([20, 25, 30, 35, 40])) # prints 3

# Greetings
def add_greetings(names):
  greetings = []
  for name in names:
    greetings.append('Hello, '+ name)
  return greetings
print(add_greetings(["Owen", "Max", "Sophie"])) # prints ['Hello, Owen', 'Hello, Max', 'Hello, Sophie']

# Delete Starting Even Numbers
def delete_starting_evens(my_list):
  while len(my_list) > 0:
    if my_list[0] % 2 == 0:
      my_list.pop(0)
    else:
      break
  return my_list
print(delete_starting_evens([4, 8, 10, 11, 12, 15])) # prints [11, 12, 15]
print(delete_starting_evens([4, 8, 10])) # prints []
# this challenge took me a little longer than the rests to solve

# Odd Indices
def odd_indices(my_list):
  new_list = []
  for i in range(len(my_list)):
    if not i % 2 == 0:
      new_list.append(my_list[i])
  return new_list
print(odd_indices([4, 3, 7, 10, 11, -2])) # prints [3, 10, -2]

# Exponents
def exponents(bases, powers):
  new_list = []
  for base in bases:
    for power in powers:
      new_list.append(base ** power)
  return new_list
print(exponents([2, 3, 4], [1, 2, 3])) # prints [2, 4, 8, 3, 9, 27, 4, 16, 64]


#   Loops Advanced
# Over 9000
def over_nine_thousand(lst):
  total = 0
  for i in lst:
    total += i
    if total > 9000: break
  return total
print(over_nine_thousand([8000, 900, 120, 5000])) # prints 9020

# Max Num
def max_num(nums):
  max = nums[0]
  for num in nums:
    if num > max: max = num
  return max
print(max_num([50, -10, 0, 75, 20])) # prints 75

# Same Values
def same_values(lst1, lst2):
  i = 0
  new_list = []
  while i < len(lst1) and i < len(lst2):
    if lst1[i] == lst2[i]:
      new_list.append(i)
    i += 1
  return new_list
print(same_values([5, 1, -10, 3, 3], [5, 10, -10, 3, 5])) # prints [0, 2, 3]


#   Functions
# Remainder
def remainder(num1, num2):
  return (2 * num1) % (num2 / 2)
print(remainder(15, 14)) # prints 2.0
print(remainder(9, 6)) # prints 0.0


#   Functions Advanced
# All Operations
def lots_of_math(a, b, c, d):
  a_plus_b = a + b
  print(a_plus_b)
  c_minus_d = c - d
  print(c_minus_d)
  first_times_second = a_plus_b * c_minus_d
  print(first_times_second)
  return first_times_second % a
print(lots_of_math(1, 2, 3, 4)) # prints 3, -1, -3, 0
print(lots_of_math(1, 1, 1, 1)) # print 2, 0, 0, 0