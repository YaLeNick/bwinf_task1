with open("stoerung5.txt", "r") as example:   # Open txt file with example quote in reading mode
    pattern = example.readline().split()      # Read first line of example and split all words by spaces
print(pattern)

alice = open("alice", "r")  # Open "Alice im Wunderland" txt file

characters = "!?_-/\\.,():»«*\"§$%&{}[]^°'#+*~;Â"   # String with all the special characters supposed to be removed
wonderland = "".join(x for x in alice.read() if x not in characters)    # fill file with every character in book if they arent in the list above
wonderland = wonderland.lower().split()     # Split all words in string by spaces and store every word in list

alice.close()

answers=[]

for i in range(len(wonderland)):

    current=[]
    s=''

    if wonderland[i] == pattern[0]:
        for f in range(0, len(pattern)):
            print(pattern[f])

            if pattern[f] == "_":
                continue

            print(wonderland[i + f])
            if wonderland[i+f] == pattern[f] or f == len(pattern):
                current.append(wonderland[i + f])
                print(current)

            else:
                print("else")
                current = []
                break

        for t in range(len(pattern)):
            s += wonderland[i+t]+" "

        shortlist = [item for item in pattern if item != '_']

        if current == shortlist:
            print(s)
            if len(s.split()) == len(pattern):
                answers.append(s.strip())

print(answers)
