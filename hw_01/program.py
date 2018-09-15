def capitalize(name):
    """
    input: name --> a string in the form "first last"
    output: returns a string with each of the two words capitalized
    note: this is the one we started in class
    """
    s = name.split()
    return s[0][0].upper() + s[0][1:] + ' ' + s[1][0].upper() + s[1][1:]

def init(name):
    """
    Input: name --> a string in the form "first last"
    Returns: a string in the form "F. Last" where it's a capitalized first inital 
    and capitalized last name
    """
    
    return name[0].upper() + '. ' + name.split(' ')[1][0].upper() + name.split(' ')[1][1:]
    #alternative
    #return name[0].upper() + '.' + name[name.find(' '):]

def part_pig_latin(name):
    """
    Input: A string that is a single lower case word
    Returns: that string in fake pig latin -> move the first letter of the word to the end and add "ay"
    so: "hello" --> "ellohay"
    """
    return name[1:] + name[0] + 'ay'

def make_out_word(out, word):
    mid = len(out) // 2
    first_part = out[:mid]
    last_part = out[mid:]
    return first_part + word + last_part

def make_tags(tag, word):
    return '<' + tag + '>' + word + '</' + tag + '>'


print(capitalize('christopher he'))

print(init('christopher he'))

print(part_pig_latin('hello'))

print(make_out_word('<<>>', 'Hello'))

print(make_tags('p', 'Paragraph.'))
