# String-1

def hello_name(name):
    return 'Hello ' + name + '!'

print(hello_name('Chris'))

def make_abba(a, b):
  return a + b + b + a

print(make_abba('hello', 'bye'))

def make_out_word(out, word):
  mid = len(out) // 2
  first_part = out[:mid]
  last_part = out[mid:]
  return first_part + word + last_part

print(make_out_word('<<>>', 'chris'))

def non_start(a, b):
    """Given 2 strings, return their concatenation,
    except omit the first char of each.
    The strings will be at least length 1."""
    return a[1:] + b[1:]

print(non_start('java', 'script'))

# String-2
def double_char(str):
  result = ''
  for s in str:
    result = result + s + s
  return result

print(double_char('hello'))

# Logic-1
def love6(a, b):
    """
    Given two int values, a and b, return True if either one is 6.
    Or if their sum or difference is 6."""
    return (a == 6 or b == 6 or abs(a - b) == 6 or a + b == 6)


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

    
