def coolest_word(words):
    unique_chars = []
    try:
        for word in words:
            unique_char = []
            for char in word:
                if char not in unique_char:
                    unique_char.append(char)
            unique_chars.append(''.join(unique_char))
        return words[unique_chars.index(max(unique_chars, key=len))]
    except Exception as e:
        return None
