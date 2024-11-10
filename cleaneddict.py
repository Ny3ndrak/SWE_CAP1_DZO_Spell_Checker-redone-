input_file = "dictionary.txt"
output_file = "clean.txt"
def clean_text(input_file, output_file):
    cleaned_words = []
    with open(input_file, 'r', encoding='utf-8') as file:
        for line in file:
            words = line.split()
            if words:
                dzongkha_word = words[0]
                cleaned_words.append(dzongkha_word)
    with open (output_file ,'w', encoding="utf-8") as file:
        for words in cleaned_words:
            file.write(words + "\n")
        print(f"cleaned words saved to {output_file}")
clean_text(input_file, output_file)