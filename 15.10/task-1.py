import os

def longest_words(file):
    path = os.getcwd()
    path += file
    print(path)
    with open(file, "r", encoding="utf-8") as f:
        text = f.read()

    words = text.split()

    max_len = max(len(word) for word in words)

    longest = [word for word in words if len(word) == max_len]

    if len(longest) == 1:
        return longest[0]
    else:
        return longest

result = longest_words('article.txt')
print(result)