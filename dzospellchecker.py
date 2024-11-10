def parse_words(file_path):
    words_dict = {}
    with open(file_path, "r", encoding="utf-8") as file:
        line_num = 0
        for line in file:
            line_num += 1
            words = line.split('་')
            for pos, word in enumerate(words, start=1):
                word = word.strip().lower()
                if word:
                    if word not in words_dict:
                        words_dict[word] = []
                    words_dict[word].append((line_num, pos))
    return words_dict

def spell_checker(text_path, dictionary_path):
    text_words = parse_words(text_path)
    dict_words = parse_words(dictionary_path)

    incorrect = {}
    for word in text_words:
        if word not in dict_words:
            incorrect[word] = text_words[word]

    return incorrect

# File paths
text_path = "352.txt"
dictionary_path = "cleaneddict.txt"

# Identify incorrect words
incorrect_words = spell_checker(text_path, dictionary_path)

# Print results
print('Incorrect Words:')
for word, positions in incorrect_words.items():
    for line, pos in positions:
        print(f"line: {line}, position: {pos}, word: {word} is incorrect")
