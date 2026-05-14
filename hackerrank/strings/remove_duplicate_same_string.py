# s = "aabccddeabb"

# result = []
# i = 0

# while i < len(s):
#     if i < len(s) - 1 and s[i] == s[i + 1]:
#         result.append(s[i])
#         result.append(" ")
#         i += 2  # skip both chars
#     else:
#         result.append(s[i])
#         i += 1

# print("".join(result))
    
            
s = "apple banana hello"

for word in s.split():

    freq = {}

    for c in word:
        freq[c] = freq.get(c, 0) + 1

    max_char = max(freq, key=freq.get)

    print(word, "->", max_char)