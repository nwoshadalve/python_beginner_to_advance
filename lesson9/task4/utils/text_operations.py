# text_operations.py

def haveVowel(text: str):
    containsVowel = False
    vowels = "aeiou"
    for char in text:
        if char in vowels:
            containsVowel = True
            break
    return containsVowel

def getTextLength(text: str):
    return len(text)

# Test this script
if __name__ == "__main__":
    print(haveVowel("Hello"))
    print(getTextLength("Hello"))