def longest_repeated_seq(word):
    lower_word = word.lower()
    lenght = len(lower_word)
    count = 0
    for i in range(lenght):
        cur_count = 1
        for j in range(i + 1, lenght):
            if lower_word[i] != lower_word[j]:
                break
            cur_count += 1
        if cur_count > count:
            count = cur_count
    if count == 1:
        count = 0
    return count