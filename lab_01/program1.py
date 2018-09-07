# Warmup-1
def sleep_in(weekday, vacation):
    return (not weekday or vacation)

def monkey_trouble(a_smile, b_smile):
    return(a_smile == b_smile)

def sum_trouble(a, b):
    if a == b:
        return (a + b) * 2
    return a + b

def diff21(n):
    if n > 21:
        return 2 * abs(21 - n)
    return abs(21 - n)

def parrot_trouble(talking, hour):
    return (talking and (hour < 7 or hour > 20))

def makes10(a, b):
    return (a == 10 or b == 10 or a + b == 10)

def near_hundred(n):
    return (abs(100 - n) <= 10 or abs(200 - n) <= 10)

def pos_neg(a, b, negative):
    if negative:
        return (a < 0 and b < 0)
    return ((a < 0 and b > 0) or (a > 0 and b < 0))

def not_string(str):
  if len(str) >= 3 and str[:3] == "not":
    return str
  return "not " + str

def missing_char(str, n):
    first = str[:n]
    back = str[n + 1:]
    return first + back

def front_back(str):
    if len(str) <= 1:
      return str
    mid = str[1:-1]
    return str[-1] + mid + str[0]

def front3(str):
    return str[:3] * 3

# Warmup-2
def string_times(str, n):
    return str * n

def front_times(str, n):
    return str[:3] * n

def string_bits(str):
    return str[::2]

def string_splosion(str):
    res = ''
    for i in range(len(str) + 1):
        res = res + str[:i]
    return res

def last2(str):
  if len(str) <= 2:
    return 0
  
  search = str[-2:]
  count = 0
  
  for i in range(len(str) - 2):
    substring = str[i:i + 2]
    if substring == search:
      count = count + 1
  
  return count

def array_count9(nums):
    count = 0
    for i in nums:
        if i == 9:
            count += 1
    return count

def array_front9(nums):
    for i in nums[:4]:
        if i == 9:
            return True
    return False

def array123(nums):
    for i in range(len(nums)):
        if nums[i:i + 3] == [1, 2, 3]:
            return True
    return False

def string_match(a, b):
  count = 0
  for i in range(len(a) - 1):
    if a[i: i + 2] == b[i: i + 2]:
      count += 1
  return count

# String-1

def hello_name(name):
    return 'Hello ' + name + '!'

def make_abba(a, b):
  return a + b + b + a

def make_tags(tag, word):
    return '<' + tag + '>' + word + '</' + tag + '>'

def make_out_word(out, word):
  mid = len(out) // 2
  first_part = out[:mid]
  last_part = out[mid:]
  return first_part + word + last_part

def extra_end(str):
    return str[-2:] * 3

def first_two(str):
    return str[:2]

def first_half(str):
    half = len(str) // 2
    return str[:half]

def without_end(str):
    return str[1:-1]

def combo_string(a, b):
    s = a
    l = b
    placeholder = ''
    if len(l) < len(s):
        placeholder = l
        l = s
        s = placeholder
    return s + l + s

def non_start(a, b):
    return a[1:] + b[1:]

def left2(str):
  return str[2:] + str[:2]


# String-2
def double_char(str):
  result = ''
  for s in str:
    result = result + s + s
  return result

# Logic-1
def love6(a, b):
    """
    Given two int values, a and b, return True if either one is 6.
    Or if their sum or difference is 6."""
    return (a == 6 or b == 6 or abs(a - b) == 6 or a + b == 6)


# List-1

def first_last6(nums):
  return (nums[0] == 6 or nums[-1] == 6)

def same_first_last(nums):
  if len(nums) < 1:
    return False
  return nums[0] == nums[-1]

def make_pi():
    return [3,1,4]

def common_end(a, b):
    return (a[0] == b[0] or a[-1] == b[-1])

def sum3(nums):
    return sum(nums)

def rotate_left3(nums):
    return nums[1:] + nums[:1]

def reverse3(nums):
    return nums[::-1]

# List-2
def count_evens(nums):
    count = 0
    for n in nums:
        if n % 2 == 0:
            count += 1
    return count


def big_diff(nums):
    minimum = nums[0]
    maximum = nums[0]
    for i in nums:
        minimum = min(minimum, i)
        maximum = max(maximum, i)
    return maximum - minimum

def centered_average(nums):
    nums.sort()
    middle = nums[1:-1]
    return sum(middle) // len(middle)

    


    
