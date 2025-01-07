ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

KEY = 'A'

decryptDict = {
    0: 7,
    1: 2,
    2: 1,
    3: 6,
    4: 10,
    5: 8,
    6: 3,
    7: 0,
    8: 5,
    9: 11,
    10: 4,
    11: 9,
    12: 15,
    13: 20,
    14: 17,
    15: 12,
    16: 18,
    17: 14,
    18: 16,
    19: 24,
    20: 13,
    21: 25,
    22: 23,
    23: 22,
    24: 19,
    25: 21
}

def decrypt(text: str, start: str):
    result: str = ""

    text = text.upper()

    for letterIt in range(len(text)):
        letter = text[letterIt]

        result += ALPHABET[decryptDict.get(ALPHABET.index(letter))+letterIt]
        print(letterIt, ALPHABET.index(letter))

    return result

print(decrypt("HALLO", "C"))