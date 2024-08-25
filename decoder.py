def decode(enc, known):
    # Split the enc to convert it to list of strings
    enc_list = enc.split()
    same_length_words = []
    print(enc_list)

    # Find words with the same length as known, to find the shifted version of known if it's actually the same
    for word in enc_list:
        if len(word) == len(known):
            same_length_words.append(word)

    shift_value = 0
    is_found = False

    for word in same_length_words:
        # For each word in the list, shift each letter in that word up to 25 times
        for i in range(1, 26):  # From 1 to 25 since 0 shift means no shift
            if shift(word, i) == known:
                is_found = True
                shift_value = i
                print(f"Shift value was {shift_value} or {26 - shift_value}")
                break
        if is_found:
            break

    if is_found:
        return shift(enc, shift_value)

    return "Invalid"

def shift(word, shift_value):
    res = []
    for char in word:
        if 'a' <= char <= 'z':
            res.append(chr((ord(char) - ord('a') + shift_value) % 26 + ord('a')))
        elif 'A' <= char <= 'Z':
            res.append(chr((ord(char) - ord('A') + shift_value) % 26 + ord('A')))
        else:
            res.append(char)
    return ''.join(res)

if __name__ == "__main__":
    encrypted = "Eqfkpi vguvu ctg hwp cpf ejcnngpikpi!"
    known = "tests"
    original = decode(encrypted, known)
    print(original)
