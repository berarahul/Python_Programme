def sort_words_alphabetically(sentence):
    words = sentence.split()
    sorted_words = sorted(words, key=lambda x: x.lower())
    return ' '.join(sorted_words)

def main():
    try:
        sentence = input("Enter a sentence: ")
        sorted_sentence = sort_words_alphabetically(sentence)
        print("Sorted sentence:")
        print(sorted_sentence)
    except Exception as e:
        print(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    main()
