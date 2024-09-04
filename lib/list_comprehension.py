#!/usr/bin/env python3

def return_evens(num_list):
    even_numbers = [number for number in num_list if number % 2 ==0]
    return(even_numbers)

return_evens([0, 1, 3, 5, 7, 8, 9])

def make_exclamation(sentence_list):
    exclamate = [ sentence.strip() + "!" for sentence in sentence_list]

    return(exclamate)

make_exclamation(["Hello", "I'm doing great", "Python is fun"])
