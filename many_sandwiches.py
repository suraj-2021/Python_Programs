#Python function that accepts a list of sandwich items and prints a summary of the sandwich being ordered

def sandwich_order(*items):
    print("You have ordered a sandwich with the following items:")
    for item in items:
        print(f"- {item}")
    print("Enjoy your sandwich!\n")

sandwich_order('turkey', 'lettuce', 'tomato', 'mayonnaise')
sandwich_order('peanut butter', 'jelly')
sandwich_order('ham', 'cheese', 'mustard', 'lettuce', 'tomato')
