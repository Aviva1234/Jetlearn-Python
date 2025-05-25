landmarks = {
    "Statue of Liberty": "New York",
    "Taj Mahal": "India",
    "Great Wall of China": "China",
    "Leaning Tower of Pisa": "?",
    "Colosseum": "Rome",
}
landmarks["Leaning Tower of Pisa"] = "Pisa, Italy"
landmarks["Eiffel Tower"] = "France"
print(landmarks)
del(landmarks["Colosseum"])
print(landmarks.keys())
print(landmarks.values())
print(landmarks["Statue of Liberty"])
if "Taj Mahal" in landmarks:
    print(True)
if "Colosseum" in landmarks:
    print(True)
else:
    print(False)
for key in landmarks:
    print(key,landmarks[key])