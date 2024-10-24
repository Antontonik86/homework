def all_variants(text):
    len_text = len(text)
    for i in range(1, len_text + 1):
        for start in range(len_text - i + 1):
            yield text[start:start + i]

a = all_variants("abc")
for i in a:
    print(i)