

def anagrams(word, words):
    return [w for w in words if sorted(w) == sorted(word)]

test = anagrams('abba', ['aabb', 'abcd', 'bbaa', 'dada'])

print(test)
