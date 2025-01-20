import json

ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

KEY = 'A'

LOG = False

with open("./config.json", 'r') as f:
    fileData = json.load(f)

decryptDict = {}

for i, j in fileData['keyDict'].items():
    decryptDict[int(i)] = j

decryptDictTest = {
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

def log(msg: str):
    if LOG:
        print(msg)

def decrypt(text: str, key: str):
    result: str = ""

    text = text.upper()

    keyPos = ALPHABET.index(key)

    log(f"[LOG] Begin decrypt. KeyPos: {keyPos}")

    for letterIt in range(len(text)):
        letter = text[letterIt]

        log(f"\n[LOG] Letter: {letter}")

        decryptCharPos = decryptDict.get((ALPHABET.index(letter) - letterIt - keyPos) % 26)

        log(f"[LOG] decryptCharPos dict: {decryptCharPos} rawPos: {(ALPHABET.index(letter) + letterIt + keyPos) % 26} raw: {ALPHABET.index(letter)} index: {ALPHABET.index(letter)}")

        decryptCharPos += letterIt

        log(f"[LOG] decryptCharPos plusLetterIt: {decryptCharPos}")

        decryptCharPos += keyPos

        log(f"[LOG] decryptCharPos plusKey: {decryptCharPos} with modulo: {decryptCharPos % 26}")

        decryptChar = ALPHABET[decryptCharPos % 26]

        result += decryptChar

        log(f"[LOG] final: it: {letterIt} Char: {letter} decrypt: {decryptChar}")

    log(f"[LOG] Finished decrypting. Final word: {result}")
    return result

print("Message: " + decrypt("HALLO", "J"))