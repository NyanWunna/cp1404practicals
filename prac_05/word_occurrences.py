user_input = input("Text: ").split()
words = {}

for i in user_input:
    if i in words:
        words[i] += 1
    else:
        words[i] = 1

max_len = max(len(x) for x in words)

for key, value in sorted(words.items()):
    print("{:{}} : {}".format(key, max_len, value))
