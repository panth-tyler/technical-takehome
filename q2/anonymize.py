import re

def anonymize_names_parta(text: str):
    """
    Anonymizes names in the given text by replacing them with "ANON". Assume names are capitalized, and no other words are.

    Args:
        text (str): The input text containing names.
 
    Returns:
        str: The text with names anonymized.

    Examples:
    
    >>> anonymize_names_parta("Alice and Bob are talking to Charlie.")
    'ANON and ANON are talking to ANON.'

    >>> anonymize_names_parta("Alice, Bob, and Charlie went to the park.")
    'ANON, ANON, and ANON went to the park.'

    >>> anonymize_names_parta("Dr. Alice visited Prof. Bob at the university.")
    'ANON ANON visited ANON ANON at the university.'

    """

    # replace all capitalized words with "ANON"
    anonymized_text = re.sub(r"\b[A-Z][a-zA-Z]*\.(?=\s)|\b[A-Z][a-zA-Z]*\b", "ANON", text)
    return anonymized_text
 
def anonymize_names_partb(text: str):
    """
    Anonymizes names in the given text by replacing them with "ANON". Names can take any shape or form. The provided text is processed against dictionaries of cities, names and titles. City name are also replaced if prepended with a preposition that is found in the preposition dictionary.
  
    Args:
        text (str): The input text containing names.
 
    Returns:
        str: The text with names anonymized.

    Examples:
    
    >>> anonymize_names_partb("alice and bob are discussing with Charlie about visiting Los Angeles.")
    'ANON and ANON are discussing with ANON about visiting ANON.'

    >>> anonymize_names_partb("Alice and Bob are thinking about a trip to Vancouver.")
    'ANON and ANON are thinking about a trip to ANON.'

    >>> anonymize_names_partb("The rev. Charlie and Dr. Eve are preparing for a move to Montreal.")
    'The ANON ANON and ANON ANON are preparing for a move to ANON.'

    """

    city_dictionary = ["los angeles", "madrid", "new york city", "paris", "prague", "rome", "san francisco", "sydney", "vienna"]
    name_dictionary = {"alice", "bob", "charlie", "dave", "eve"}
    preposition_dictionary = {"from", "in", "to"}
    title_dictionary = {"dr", "prof", "rev"}

    replaced_text = text

    # dicitonary replacements
    for city in city_dictionary:
        replaced_text = re.sub(r"\b" + city + r"\b", "ANON", replaced_text, flags=re.IGNORECASE)
    for name in name_dictionary:
        replaced_text = re.sub(r"\b" + name + r"\b", "ANON", replaced_text, flags=re.IGNORECASE)
    for title in title_dictionary:
        replaced_text = re.sub(r"\b(" + title + r")\.", "ANON", replaced_text, flags=re.IGNORECASE)

    # split the text into words
    words = replaced_text.split()
    anonymized_words = []
    
    # iterate through the words and check for prepositions
    for i, word in enumerate(words):
        if word[0].isupper() and i > 0 and words[i - 1].lower() in preposition_dictionary:
            if word[-1] == "." and i == len(words) - 1:
                anonymized_words.append("ANON.")
            else:
                anonymized_words.append("ANON")
        else:    
            anonymized_words.append(word)
    
    # join anonymized words back into a text string
    result_text = " ".join(anonymized_words)

    return result_text
    
if __name__ == '__main__':
    import doctest
    doctest.testmod()

    parta_test_strings = [
        "Alice and Bob are talking to Charlie.",
        "Alice, Bob, and Charlie went to the park.",
        "Dr. Alice visited Prof. Bob at the university."
    ]
    print("Part A")
    for input_text in parta_test_strings:
         print(f"{input_text} -> {anonymize_names_parta(input_text)}")

    print()

    partb_test_strings = [
        "Alice and Bob are talking to Charlie about going to New York City.",
        "alice and bob are discussing with Charlie about visiting Los Angeles.",
        "Bob and Eve are planning a trip to paris next summer.",
        "Charlie and Alice met with Dave in San Francisco last week.",
        "eve and Charlie were excited about the event in Chicago.",
        "Charlie and Bob are thinking of moving to Tokyo soon.",
        "Alice and Dave went to see a show in London.",
        "Alice and Bob had dinner with Eve in Madrid.",
        "bob and Eve are going to Sydney for a conference.",
        "Charlie and Alice took a vacation in Rome.",
        "Charlie and Dave are considering a job offer in Berlin.",
        "eve and Charlie are visiting their friend in Amsterdam.",
        "Charlie and Bob are attending a wedding in Bangkok.",
        "Alice and Dave spent their holidays in Barcelona.",
        "Bob and Eve are looking for apartments in Vienna.",
        "Charlie and Dave are organizing an event in Prague.",
        "alice and Charlie are exploring opportunities in Dubai.",
        "Bob and Charlie are discussing their plans in Dublin.",
        "Alice and Dr. Bob are thinking about a trip to Vancouver.",
        "Charlie and Eve are preparing for a move to Montreal."
    ]
    print("Part B")
    for input_text in partb_test_strings:
        print(f"{input_text} -> {anonymize_names_partb(input_text)}")