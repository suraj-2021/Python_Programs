# Mad Libs Generator in Python

# create a list of words
words = []

# get words from user
words.append(input("Enter an adjective: "))
words.append(input("Enter a noun: "))
words.append(input("Enter an adjective: "))
words.append(input("Enter a noun: "))

# create story template
story = "Once upon a time, there was a {0} {1} who lived in a {2} {3}."

# display completed story
print(story.format(words[0], words[1], words[2], words[3]))
