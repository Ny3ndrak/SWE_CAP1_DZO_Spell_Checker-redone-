
This project aims to clean and spell-check a given dictionary text file. It includes scripts to convert `.docx` files to `.txt` format, remove unwanted noise, and check the spellings.

## Features

- **Convert `.docx` to `.txt`**: Using the `python-docx` library, i converted dictionary document to a text file.
- **Clean Text**: Removed unwanted characters, numbers, and extra whitespace from text files.
- **Spell Checker**: Extract words and identify potential misspellings by comparing two text files.

# 1. Read the input file #
# Step 1: Import the requests Library
First, ensure you’ve imported the requests library, which is essential for making HTTP requests.
    import requests

# Step 2: Define the URL
Specify the URL from which you want to download the file.
    url = 'https://csf101-server-cap1.onrender.com/get/input/352'

# Step 3: Make the HTTP GET Request
Use the requests.get() method to make a GET request to the specified URL. This method returns a response object that contains the server's response to the request.
    txt_file = requests.get(url)

# Step 4: Open the Output File
Open a new file (or overwrite an existing one) in binary write mode ('wb'). This is where the content from the URL will be saved.
    with open('352.txt', 'wb') as file:

# Step 5: Write the Content to the File
Write the content of the response object to the file using the write method.
    data = file.write(txt_file.content)

# Step 6: Confirm the Download
Print a message to confirm that the file has been successfully downloaded.
    print('Downloaded 352.txt')


# 2. clean the dictionary #
# Step 1: Define the Function
* Function Definition: The function is defined to accept two parameters: input_file (the file to read from) and output_file (the file to write to).

* Initialize List: cleaned_words is an empty list that will store the cleaned words.

# Step 2: Open the Input File             
* Open File: with open(input_file, 'r', encoding='utf-8') as file: opens the file in read mode with UTF-8 encoding.
* Iterate Lines: for line in file: iterates through each line in the file.
* Split Line: words = line.split() splits the line into individual words.
* Check Words: if words: checks if the line has any words.
* Extract First Word: dzongkha_word = words[0] takes the first word from the line.
* Append to List: cleaned_words.append(dzongkha_word) adds the extracted word to the cleaned_words list.

# Step 3: Open the Output File
* Open File: with open(output_file, 'w', encoding="utf-8") as file: opens the file in write mode with UTF-8 encoding.
* Write Words: for words in cleaned_words: iterates through the cleaned words list.
* Write to File: file.write(words + "\n") writes each word to the output file, followed by a newline.
* Print Confirmation: print(f"cleaned words saved to {output_file}") prints a message indicating that the cleaned words have been saved to the output file.

# Step 4: Define File Paths
You specify the input and output file names.
input_file = "dzo.txt"
output_file = "clean.txt"
Input File: input_file is set to "dzo.txt".
Output File: output_file is set to "clean.txt".

# Step 5: Call the Function
Finally, you call the clean_text function with the specified file names.
clean_text(input_file, output_file)
Function Call: clean_text(input_file, output_file) executes the function, passing the input and output file names as arguments.

# 3. Spell checker #
# Step 1: Define the parse_words Function

* Function Declaration: def parse_words(file_path):
This function takes a file path as an input and returns a dictionary of words with their positions.

* Initialize Dictionary: words_dict = {}
An empty dictionary to store words and their positions.

* Open File: with open(file_path, "r", encoding="utf-8") as file:
Opens the specified file in read mode with UTF-8 encoding.

* Read Lines: for line_num, line in enumerate(file, start=1):
Reads the file line by line, keeping track of the line number starting from 1.

* Split Words: words = line.split('་')
Splits each line into words using the specified delimiter (་).

* Enumerate Words: for pos, word in enumerate(words, start=1):
Iterates over each word and keeps track of its position within the line starting from 1.

* Clean Word: word = word.strip().lower()
Strips whitespace from the word and converts it to lowercase.

* Check Word: if word:
Checks if the word is not an empty string after cleaning.

* Store Word: if word not in words_dict: words_dict[word] = []
If the word is not already in the dictionary, add it with an empty list.

* Append Position: words_dict[word].append((line_num, pos))
Append the line number and position of the word to the list in the dictionary.

* Return Dictionary: return words_dict
Returns the dictionary containing words and their positions.

# Step 2: Define the spell_checker Function
* Function Declaration: def spell_checker(text_path, 
dictionary_path):
 This function takes two file paths (text and dictionary) as inputs and returns a dictionary of incorrect words.

* Parse Text Words: text_words = parse_words(text_path)
 Calls the parse_words function on the text file to get a dictionary of words and their positions.

* Parse Dictionary Words: dict_words = parse_words(dictionary_path)
Calls the parse_words function on the dictionary file to get a dictionary of words and their positions.

* Initialize Dictionary: incorrect = {}
An empty dictionary to store incorrect words and their positions.

* Find Incorrect Words: for word in text_words: if word not in dict_words: incorrect[word] = text_words[word]
Iterates over words in the text file. If a word is not found in the dictionary, it adds the word to the incorrect dictionary with its positions.

* Return Incorrect Words: return incorrect
Returns the dictionary containing incorrect words and their positions.

# Step 3: Main Execution
* Define File Paths: text_path = "352.txt" and dictionary_path = "cleaneddict.txt"
Specifies the paths to the text and dictionary files.

* Call Spell Checker: incorrect_words = spell_checker(text_path, dictionary_path)
 Calls the spell_checker function with the specified file paths to get the incorrect words.

* Print Header: print('Incorrect Words:')
Prints the header for the output.

* Print Incorrect Words: for word, positions in incorrect_words.items():
Iterates over the incorrect words and their positions.

* Print Details: for line, pos in positions: print(f"line: {line}, position: {pos}, word: {word} is incorrect")
For each position of the incorrect word, prints the line number, position, and the word.