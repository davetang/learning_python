#!/usr/bin/env python3

import random
import signal

my_list = {
    "name" : ["Alanine", "Arginine", "Asparagine", "Aspartate", "Cysteine", "Glutamine", "Glutamate", "Glycine", "Histidine", "Isoleucine", "Leucine", "Lysine", "Methionine", "Phenylalanine", "Proline", "Serine", "Threonine", "Tryptophan", "Tyrosine", "Valine"],
    "three letter symbol" : ["Ala", "Arg", "Asn", "Asp", "Cys", "Gln", "Glu", "Gly", "His", "Ile", "Leu", "Lys", "Met", "Phe", "Pro", "Ser", "Thr", "Trp", "Tyr", "Val"],
    "one letter symbol" : ["A", "R", "N", "D", "C", "Q", "E", "G", "H", "I", "L", "K", "M", "F", "P", "S", "T", "W", "Y", "V"],
    "class" : ["Aliphatic", "Fixed cation", "Amide", "Anion", "Thiol", "Amide", "Anion", "Aliphatic", "Aromatic cation", "Aliphatic", "Aliphatic", "Cation", "Thioether", "Aromatic", "Cyclic", "Hydroxylic", "Hydroxylic", "Aromatic", "Aromatic", "Aliphatic"]
}

def print_table():
    header = list(my_list.keys())
    print("\t".join(header))
    for i in range(len(my_list[header[0]])):
        line = [my_list.get(key)[i] for key in header]
        print("\t".join(line))

def ask_question(n):
    question_type = random.choice((list(my_list)))
    for_type = random.choice((list(my_list)[:-1]))
    while question_type == for_type:
        for_type = random.choice((list(my_list)[:-1]))

    i = random.randrange(len(my_list[for_type]))
    specific_type = my_list[for_type][i]

    question = f"{n}. What is the {question_type} for {specific_type}? "
    answer = my_list[question_type][i]
    attempt = input(question).lower()

    while attempt != answer.lower():
        if attempt == "answer":
            print(answer)
        elif attempt == "hint" or attempt == "help":
            print(set(my_list[question_type]))
        elif attempt == "table":
            print_table()
        else:
            print("Wrong!")
        attempt = input(question).lower()

    print("Correct!")
    if n == 10:
        again = input("Do you want to answer another 10 questions? [Y/n] ")
        if again == "n":
            print("Bye!")
            quit()
        else:
            ask_question(1)
    n += 1
    ask_question(n)

def handler(signum, frame):
    print("\nBye!")
    quit()
                         
signal.signal(signal.SIGINT, handler)

print("Answer ten questions correctly!")
ask_question(1)
