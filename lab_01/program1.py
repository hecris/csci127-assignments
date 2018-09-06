# String-1

def hello_name(name):
    return 'Hello ' + name + '!'

print(hello_name('Chris'))

def make_abba(a, b):
  return a + b + b + a

print(make_abba('hello', 'bye'))

# String-2
def double_char(str):
  result = ''
  for s in str:
    result = result + s + s
  return result

print(double_char('hello'))

# List-1

def first_last6(nums):
  return (nums[0] == 6 or nums[-1] == 6)

print(first_last6([6, 0, 0]))
print(first_last6([2, 3, 3]))

# List-2
def count_evens(nums):
    count = 0
    for n in nums:
        if n % 2 == 0:
            count += 1
    return count

print(count_evens([2, 3, 4, 5, 6]))

    
