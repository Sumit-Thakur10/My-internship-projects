def word_counter(text):
    """
    Count the number of words in a given text.

    Args:
    - text (str): The input text.

    Returns:
    - int: The number of words in the text.
    """
    # Split the text into words
    words = text.split()
    # Count the number of words
    word_count = len(words)
    return word_count

# Get input text from the user
text = input("Enter the text: ")

# Check if the input text is empty
if not text:
    print("Error: Please enter some text.")
else:
    # Call the word_counter function and display the result
    count = word_counter(text)
    print("Number of words:", count)
    # Add a line of text
    print("Thank you for using the word counter!")



