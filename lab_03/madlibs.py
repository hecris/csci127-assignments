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
To make pizza, you need to take a lump of <noun> and make a thin,round <adj> <noun>. 
Then you cover it with <adj> sauce, <adj> cheese and fresh chopped <pluralnoun>. 
Next you have to bake it in a very hot <noun>. 
When it is done, cut it into <number> <shape>. 
Some kids like <food> pizza the best, but my favorite is the <food> pizza."""


def madlibs(sentence):
    sentence = take_care_of_punc(sentence, True)
    l = sentence.split()
    res = []
    for w in l:
        if '<' in w:
            to_replace = w[1:-1]
            word_bank = dictionary[to_replace].split(',')
            res.append(get_random_from_list(word_bank))
        else:
            res.append(w)
    new_sentence = take_care_of_punc(" ".join(res), False)
    return new_sentence

def take_care_of_punc(sentence, splitting):
    if splitting: # add spaces to punctuation for splitting
        sentence = sentence.replace(".", " . ")
        sentence = sentence.replace(",", " , ")
    else: # proper punctuation back in
        sentence = sentence.replace(" .", ".")
        sentence = sentence.replace(" ,", ",")
    return sentence

def get_random_from_list(l):
    rng = random.randint(0, len(l) - 1)
    return l[rng]

print(madlibs(sentence))
