with open("stoerung0.txt", "r") as example:   # Open txt file with example quote in reading mode
    pattern = example.readline().split()      # Read first line of example and split all words by spaces


alice = open("alice", "r")  # Open "Alice im Wunderland" txt file

characters = "!?_-/\\.,():»«*\"§$%&{}[]^°'#+*~;Â"   # String with all the special characters supposed to be removed
wonderland = "".join(x for x in alice.read() if x not in characters)    # fill file with every character in book if they arent in the list above
wonderland = wonderland.split()     # Split all words in string by spaces and store every word in list

alice.close()

