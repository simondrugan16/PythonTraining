dictionary_of = {
    "one": "aaa",
    "two": "bbb",
    "three": "ccc"
}

print(dictionary_of)
print(dictionary_of["one"])
#print(dictionary_of["not_a_key"])

dictionary_of["four"] = "ddd"

print(dictionary_of)

dictionary_of["one"] = "AAAA"

print(dictionary_of)

for thing in dictionary_of:
    print(thing)
    print(dictionary_of[thing])

dictionary_of = {}

print(dictionary_of)
