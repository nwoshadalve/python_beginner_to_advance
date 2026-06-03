# string_utils.py

def reverse_string(text: str):
    reverse=""
    for i in range (len(text)-1, -1, -1):
        reverse += text[i]
    return reverse

def count_vowels(text: str):
    count = 0
    vowels = "aeiou"
    for char in text.lower():
        if char in vowels:
            count += 1
    return count

if __name__ == "__main__":
    text = "Hello World!!"
    print(reverse_string(text))
    print(count_vowels(text))