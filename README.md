# Rotor Encryption
So, this is a project based on a task I saw. The goal was it to decrypt a given text with an Enima like machine, it has just one rotor. You also get a char which is the key for how much the rotor is rotated at the beginning.

## How it works
### Encryption
So you basically have a rotor/circle with all characters of the alphabet around the circle. A line goes from every character to another character. 
If you now want to encrypt a character you go to the character and follow the line to the end. The character at the end of the line is now the encrypted character.
But this isn't it for every character you rotate the rotor one character to the right. The same goes for the key you initially turn to rotor to the key character.
