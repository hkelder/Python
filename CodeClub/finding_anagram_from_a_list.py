from collections import Counter


def identify_ninja(ninja_name, all_villagers):
    anagrams = []
    counter_name = Counter(ninja_name)
    for original_name in all_villagers:
        if Counter(original_name) == counter_name:
            anagrams.append(original_name)
    return anagrams


print(identify_ninja('irneh', ['henri', 'enrih', 'taavi']))