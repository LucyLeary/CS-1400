def words_without_periods(sentences):
    cleaned_words = []
    for sentence in sentences:
        if sentence[-1] == ".":
            sentence = sentence[: -1]
        cleaned_words += sentence.split()  # adds words separate at their own indices, append creates a list of 3 lists
    return cleaned_words


print(words_without_periods(["my name is cat.", "I like to ski sometimes", "I go to school."]))

a_dictionary = {"first": 1, "second": 2, "third": 3}

for key, value in a_dictionary.items():
    print(1)

print(a_dictionary.items())

a_tuple = ("first", "last")
a_tuple = a_tuple[0], "middle", a_tuple[1]
print(a_tuple)
f, m, la = a_tuple
print((f, m, la)[0])

words_list = ["yello", "hi", "fine", "fine", "yello", "yello"]
count_dict = {}
for word in words_list:
    count_dict[word] = count_dict.get(word, 0) + 1
print(count_dict)
