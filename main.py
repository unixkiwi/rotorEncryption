import json
import argparse
import os

ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def verifyChar(value):
    if len(value) != 1 or value not in ALPHABET:
        raise argparse.ArgumentTypeError(f"'{value}' is not a valid char of the alphabet.")
    return value

def verifyPath(value: str):
    if not os.path.isfile(value):
        raise argparse.ArgumentTypeError(f"'{value}' is not a valid file.")
    return value

def loadFile(path):
    result = {}

    with open(path, 'r') as f:
        fileData = json.load(f)

    for i, j in fileData['keyDict'].items():
        result[int(i)] = j

    return result

parser = argparse.ArgumentParser(description="Decrypt and encrypt messages using a key character and a rotor.")

parser.add_argument(
    "-v", "--verbose",
    action="store_true",
    help = "Show verbose outputs. Show Logs"
)

parser.add_argument(
    "-f", "--config_file",
    type = verifyPath,
    help = "Take input file",
    required=False
)

parser.add_argument(
    "-b", "--brute_force",
    action = "store_true",
    help = "Bruteforce every key",
    required=False
)

parser.add_argument(
    "-l", "--verbose_brute_force",
    action = "store_true",
    help = "Log every bruteforce",
    required=False
)

parser.add_argument(
    "-e", "--expected_word",
    type = str,
    help = "The word expected when bruteforce",
    required=False
)

parser.add_argument(
    "-c", "--char",
    type = verifyChar,
    help = "Encrypt char",
    required=True
)

parser.add_argument(
    "-m", "--msg",
    type = str,
    help = "Message",
    required=True
)

# parse
args = parser.parse_args()

# Log stuff
LOG = False

if args.verbose:
    LOG = True

# Char stuff
KEY = args.char

# message stuff
message = args.msg

# encryptionDict
encryptDict = {
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

if args.config_file:
    encryptDict = loadFile(args.config_file)


def log(msg: str):
    if LOG:
        print(msg)

def rotorEncryption(text: str, key: str, encryptDict):
    result: str = ""

    text = text.upper()

    keyPos = ALPHABET.index(key)

    log(f"[LOG] Begin encryption. KeyPos: {keyPos}")

    for letterIt in range(len(text)):
        letter = text[letterIt]

        log(f"\n[LOG] Letter: {letter}")

        encryptCharPos = encryptDict.get((ALPHABET.index(letter) - letterIt - keyPos) % 26)

        log(f"[LOG] encryptCharPos dict: {encryptCharPos} rawPos: {(ALPHABET.index(letter) - letterIt - keyPos) % 26} raw: {ALPHABET.index(letter)} index: {ALPHABET.index(letter)}")

        encryptCharPos += letterIt

        log(f"[LOG] encryptCharPos plusLetterIt: {encryptCharPos}")

        encryptCharPos += keyPos

        log(f"[LOG] encryptCharPos plusKey: {encryptCharPos} with modulo: {encryptCharPos % 26}")

        encryptChar = ALPHABET[encryptCharPos % 26]

        result += encryptChar

        log(f"[LOG] final: it: {letterIt} Char: {letter} encrypt: {encryptChar}")

    log(f"[LOG] Finished encrypting. Final word: {result}")
    return result

if args.brute_force:
    if not args.expected_word: raise argparse.ArgumentTypeError(f"Expected an expected_word with -e '' ")

    for ch in ALPHABET:
        if args.verbose_brute_force:
            print(f"Char: {ch} Word: {rotorEncryption(message, ch, encryptDict)}")

        if args.expected_word.upper() == rotorEncryption(message, ch, encryptDict):
            print(f"\nChar: {ch} Word: {rotorEncryption(message, ch, encryptDict)}\n")
            break
else:
    print(rotorEncryption(message, KEY, encryptDict))
