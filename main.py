with open("stoerung5.txt", "r") as example:   # Open txt file with example quote in reading mode
    pattern = example.readline().split()      # Read first line of example and split all words by spaces

alice = open("alice", "r")  # open "Alice im Wunderland" txt file

characters = "!?_-/\\.,():»«*\"§$%&{}[]^°'#+*~;Â"
wonderland = "".join(x for x in alice.read() if x not in characters)
wonderland = wonderland.lower().split()

alice.close()   # close the file with "Alice im Wunderland"

answers=[]      # initialize list for all possible quotes

for i in range(len(wonderland)):    # loop for all words in wonderland

    current=[]  # initialize list for current possible quote
    s=''        # initialize string later filled with quote

    if wonderland[i] == pattern[0]:     # if the current word matches the first word of the quote
        for f in range(0, len(pattern)):    # loop for lenght of quote

            # if current item in pattern is a spacefiller, skip to next loop
            if pattern[f] == "_":
                continue

            # if to check for equal words or just true if last word
            if wonderland[i+f] == pattern[f] or f == len(pattern):
                current.append(wonderland[i + f])   # fill current with possible words for quote

            # if words don't fit, go to next place in wonderland and clear current
            else:
                current = []
                break

        # fill s with the fitting words to paste it in answers
        for t in range(len(pattern)):
            s += wonderland[i+t]+" "

        # put pattern in a list leaving the space fillers
        shortlist = [item for item in pattern if item != '_']

        # if current fits the quote pattern & the lenghts are right
        if current == shortlist:
            if len(s.split()) == len(pattern):
                answers.append(s.strip())       # fill list answers with the right quotes

print(answers)  # print out all answers in a list
