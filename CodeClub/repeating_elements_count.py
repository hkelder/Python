def elements_count(*lists):
    dictionary = {}
    for list in lists:
        for number in list:
            if number in dictionary:
                dictionary[number] += 1
            else:
                dictionary[number] = 0
    for list in lists:
        for number in list:
            if dictionary[number] == 0:
                del dictionary[number]
    return dictionary
