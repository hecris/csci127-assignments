# Christopher He and Darren Zou
import random

dictionary = {
    "person":"Chris,Darren,Sally,Mike,Hercules",
    "adj":"stinky,pretty,disgusting,tasty,microscopic,boneless,hairless,massive",
    "nationality":"Chinese,Italian,Nigerian",
    "pluralnoun":"bikes,cars,tables,cats,dogs",
    "noun":"chair,oven,laptop,poop,backpack,foot,knife",
    "number":"two,three,eighty one,four hundred fifty seven",
    "shape":"squares,ovals,decagons,polyhedrons",
    "food":"pepperoni,rice,chicken,beef,broccoli,doritos"
    }

sentence = """Pizza was invented by a <adj> <nationality> chef named <person>. 
To make pizza, you need to take a lump of <noun> and make a thin, round <adj> <noun>. 
Then you cover it with <adj> sauce, <adj> cheese and fresh chopped <pluralnoun>. 
Next you have to bake it in a very hot <noun>. 
When it is done, cut it into <number> <shape>. 
Some kids like <food> pizza the best, but my favorite is the <food> pizza."""


def madlibs(sentence):
    l = sentence.split()
    res = []
    for w in l:
        if '<' in w and '>' in w:
            key = extract_key(w)
            choice = choose_and_remove_from(key, dictionary) # avoid repeats
            replaced = w.replace(key, choice).replace('<', '').replace('>', '')
            res.append(replaced)
        else:
            res.append(w)
    new_sentence = " ".join(res)
    return new_sentence

def extract_key(s):
    start = s.index('<') + 1
    end = s.index('>')
    return s[start:end]

def choose_and_remove_from(key, dictionary):
    word_bank = dictionary[key].split(',')
    choice = random.choice(word_bank)
    dictionary[key] = dictionary[key].replace("," + choice, "")
    return choice


print(madlibs(sentence))
