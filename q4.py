def main():
    """
    Reads a line of input, counts occurrences of words, and prints the count
    for the first three unique words encountered.
    """
    words = input().strip().split()  # Read input and split into words
    word_count = {}  # Dictionary to store word counts
    unique_words = []  # List to store unique words

    for word in words:
        # Add word to unique list if not already present
        if word not in unique_words:
            if len(unique_words) == 3:  # Stop if 3 unique words are found
                break
            unique_words.append(word)

        # Update word count
        word_count[word] = word_count.get(word, 0) + 1

        # Stop if the last unique word has been processed
        if len(unique_words) == 3 and word == unique_words[-1]:
            break

    # Print the count for each unique word
    for word in unique_words:
        print(f"{word} occurred {word_count[word]} times")


if __name__ == "__main__":
    main()