def count_words(text):
    words = text.split()
    return len(words)


def count_vowels(text):
    count = 0
    for letter in text:
        if letter.lower() in "aeiou":
            count += 1
    return count


def find_longest_word(text):
    words = text.split()
    longest = words[0]
    for word in words:
        if len(word) > len(longest):
            longest = word
    return longest


def is_palindrome(text):
    cleaned = text.lower().replace(" ", "")
    return cleaned == cleaned[::-1]


def main():
    print("=" * 23)
    print("TEXT ANALYZER")
    print("=" * 23)

    text = ""
    while text == "":
        text = input("Enter your text: ").strip()
        if text == "":
            print("Text cannot be blank")

    while True:
        print("MENU")
        print("1. Word count")
        print("2. Longest word")
        print("3. Vowel count")
        print("4. Palindrome check")
        print("5. Enter new text")
        print("6. Exit")
        choice = input("Choose: ").strip()

        if choice == "1":
            print("Word count:", count_words(text))
        elif choice == "2":
            print("Longest word:", find_longest_word(text))
        elif choice == "3":
            print("Vowel count:", count_vowels(text))
        elif choice == "4":
            if is_palindrome(text):
                print("Yes, it is a palindrome")
            else:
                print("No, it is not a palindrome")
        elif choice == "5":
            new_text = input("Enter new text: ").strip()
            if new_text == "":
                print("Text cannot be blank")
            else:
                text = new_text
        elif choice == "6":
            print("goodbye")
            break
        else:
            print("Oops: choose a number from 1 to 6")


main()