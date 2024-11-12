# Question 2: Anonymizing Names

This question assumes you are using Python, but you are free to use your preferred programming language.

## 2a
 
Write a Python function that accepts a string as input and replaces all occurrences of names with the string "ANON.”  In the function’s docstring, list at least three test strings and the expected output. **Assume names are capitalized words and may be separated by spaces or by punctuation. No other words are capitalized.**
 
## 2b

Suppose instead that you cannot make any assumptions about a name’s capitalization or the capitalization of other words. In other words, suppose that you need to write a Python function to anonymize an arbitrary string of text by replacing all names with the string “ANON.” Briefly describe 2-3 heuristics you might use to identify names in an arbitrary string of text. (No approach will be perfect! Simple solutions are OK.)

## Additional Notes

Part B uses predifined dictionaries to match names against and checks for capitalized words that have prepositions before them.

### Execute _anonymize_ script

```bash
python3 ./anonymize.py
```

### Execute _anonymize_ script with doctest module

```bash
python3 ./anonymize.py -v
```
