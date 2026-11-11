# Text Analyzer

A command-line tool written in Python. You enter a piece of text once,
then choose analyses from a menu to run on it.

## Features

- Word count
- Longest word (on a tie, the first one wins)
- Vowel count (capitals count too)
- Palindrome check (ignores capitals and spaces)
- Enter new text without restarting
- Blank text is rejected and the program asks again
- Invalid menu choices show a message and the menu again

## Requirements

- Python 3.8 or newer
- No extra packages needed

## How to run

```bash
python3 text_analyzer.py
```

## How to use

```text
MENU
1. Word count
2. Longest word
3. Vowel count
4. Palindrome check
5. Enter new text
6. Exit
```

Enter your text when asked, then pick an option. The text is kept until
you choose option 5 to replace it.

## Example

```text
Enter your text: Madam Anna saw a racecar
Choose: 1
Word count: 5
Choose: 2
Longest word: racecar
Choose: 3
Vowel count: 9
Choose: 4
No, it is not a palindrome
```

## How it works

| Function | Takes in | Gives back |
|---|---|---|
| `count_words(text)` | text | number of words |
| `count_vowels(text)` | text | number of vowels |
| `find_longest_word(text)` | text | the longest word |
| `is_palindrome(text)` | text | `True` or `False` |
| `main()` | nothing | runs the menu and prints results |

## Design decisions

- **Analysis functions return values and never print.** Only `main` talks
  to the user, so each function can be tested on its own.
- **The text lives in `main`** and is passed into each function as an
  argument, so the functions stay simple: text in, answer out.
- **`.split()` with no argument** splits on any amount of whitespace, so
  extra spaces do not give a wrong word count.
- **`>` instead of `>=`** in the longest-word check means a tie keeps the
  first word found.

## Known limitations

- Punctuation counts as part of a word, so `Hello,` is longer than `Hello`
- The palindrome check removes spaces but not punctuation, so
  `A man, a plan, a canal: Panama` returns `False`
- Only the letters a, e, i, o, u count as vowels

## Possible next steps

- Strip punctuation before analysing
- Most common word
- Sentence count
- Word frequency table
- Automated tests