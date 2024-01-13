try:
    raise ValueError("A custom error occurred.")
except ValueError as e:
    print(e)
