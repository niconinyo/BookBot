def main():
    try:

        with open('books/frankenstein.txt') as f:
            file_contents = f.read()

        print(file_contents)
    except FileNotFoundError:
        print("Error: The file 'frankenstein.txt' was not found in the 'books/' directory.")

def count():
    try:
        with open('books/frankenstein.txt') as f:
            file_contents = f.read()

        words = file_contents.split()
        print(f"Number of words in 'frankenstein.txt': {len(words)}")
        return (len(words))
        
    except FileNotFoundError:
        print("Error: The file 'frankenstein.txt' was not found in the 'books/' directory.")
# main()
count()

def count_characters():
    count_dict = {}
  
    try:
       
        with open('books/frankenstein.txt') as f:
            file_contents = f.read()
            words = file_contents.lower()
            
            
        for char in words:
           
            if char in count_dict:
                count_dict[char] += 1
            else:
                count_dict[char] = 1
        return count_dict
    except FileNotFoundError:
        print("Error: The file 'franksters.txt' was not found in the 'books/' directory.")

result = count_characters()
def report(result):


    print('--- Begin report of books/frankenstein.txt ---') 
    print(f"{count()} words found in the document")
    for key, value in result.items():
        if key.isalpha():  # Ignore punctuation and special characters
            print(f"The '{key}' character was found {value} times")
    print('--- End report ---')

report(result)
# result = count_characters()
# print(f"{result} words found in the document")


