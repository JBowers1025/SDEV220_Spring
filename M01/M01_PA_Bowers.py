# Jenn Bowers
# M01_PA_Bowers.py
# Module 1 Programming Assignment
# 1/20/2025


import os
os.system("cls")


# 4.1
song = """When an eel grabs your arm,
... And it causes great harm,
... That's - a moray!"""
print(song)

words = song.split()

for i, word in enumerate(words):
    if word.startswith('m'):
        words[i] = f"{word.capitalize()}"
song2 = " ".join(words)

print(song2)


# 4.2
saying = "My kitty cat likes %s, My kitty cat likes %s, My kitty cat fell on his %s And now thinks he's a %s."

new_words = ["roast beef", "ham", "head", "clam"]


print(f"My kitty cat likes {new_words[0]}, \nMy kitty cat likes {new_words[1]}, \nMy kitty cat fell on his {new_words[2]} \nAnd now thinks he's a {new_words[3]}.")

# 4.3/4.4
salutation = "Mr."
name = "John Doe"
product = "extension cord"
verbed = "caught fire"
room = "bathroom"
animals = "cats"
amount = 5.99
percent = 70
spokesman = "Bob Speller"
job_title = "Quality Care Representative"

letter = f'Dear {salutation} {name},\n\nThank you for your letter. We are sorry that our {product} {verbed} in your {room}. Please note that it should never be used in a {room}, especially near any {animals}.\n\nSend us your receipt and {amount} for shipping and handling. We will send you another {product} that, in our tests, is {percent}% less likely to have {verbed}.\n\nThank you for your support.\n\nSincerely,\n{spokesman}\n{job_title}'

print(letter)

# 4.5
items = ["duck", "gourd", "spitz"]
contestants = ["Boaty McBoatface", "Horsey McHorseface", "Trainy McTrainface"]

for i, item in enumerate(items):
    prize_announcement = f'The winner of the "prize {(items[i])} award" goes to {(contestants[i])}!'
    print(prize_announcement)