# Program for the first task of BWINF 41, Round 1 - Task 1
# Your task is to find possible matches in a large text file for a given pattern

# Opening the text file containing the pattern and splitting the line into a list, seperating by spaces
with open("stoerung0.txt", "r") as example:
    pattern =example.readline().split()

# --------------------------------------------------------------
# Opening the story text file, removing special characters and converting everything to small letters
alice =open("alice", "r")

characters ="!?_-/\\.,():»«*\"§$%&{}[]^°'#+*~;Â"
wonderland ="".join(x for x in alice.read() if x not in characters)
wonderland =wonderland.lower().split()

alice.close()
# --------------------------------------------------------------

answers = []

# Going through every word in the text file, initialising temporary variables and checking if the
# word matchers with the first word of the given pattern.
for i in range(len(wonderland)):

    current =[]
    s =''

    if wonderland[i] == pattern[0]:

        # If the first word matches the program checks all the words for the lenght of the quote pattern,
        # skipping the space filler, appending fitting words to the current list and stopping the loop
        # if it recognizes that the pattern will not fit.
        for f in range(0, len(pattern)):

            if pattern[f] == "_": continue

            if wonderland[i+f] == pattern[f] or f == len(pattern): current.append(wonderland[i + f])

            else: break

        # Fill string with the fitting words to paste it in answers
        for t in range(len(pattern)):
            s +=wonderland[i+t]+" "

        # put pattern in a list leaving the space fillers
        shortlist =[item for item in pattern if item != '_']

        # If current fits the quote pattern & the lenghts are right, the possible solution
        # are added to the list of correct answers.
        if current == shortlist:
            if len(s.split()) == len(pattern):
                answers.append(s.strip())

print(answers)  # Print out all answers in a list