#Count Vowels in String

def count_vowels(s):
    vowels = 'aeiou'
    return {v: s.lower().count(v) for v in vowels}

print(count_vowels("Hello World"))
