sentence = input("Enter a sentence  ").lower().strip()
#dictionary = {}
panagram = False

vowels = {"a": 0, "e": 0, "i": 0, "o": 0, "u":0}
# for letter in sentence:
#     if letter == " ":
#         continue
#     elif letter == ".":
#         continue
#     dictionary[letter] = 0
dictionary = {"a":0, "b":0, "c":0, "d":0, "e":0, "f":0, "g":0, "h":0, "i":0, "j":0, "k":0, "l":0, "m":0, "n":0, "o":0, "p":0, "q":0, "r":0, "s":0, "t":0, "u":0, "v":0, "w":0, "x":0, "y":0, "z":0}
for character in sentence:
    print(character)
    if character in dictionary:
        dictionary[character] += 1
    if character in vowels:
        vowels[character] +=1
for key in dictionary:
    if dictionary[key] >= 1:
        panagram = True
    else:
        panagram = False
if panagram == True:
    print("Is a panagram")
else:
    print("Not a panagram")
print(dictionary)
print(vowels)