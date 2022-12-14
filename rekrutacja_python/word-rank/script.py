# coding=utf-8

# input: array with multiple strings
# expected output: rank of the 3 most often repeated words in given set of strings and number of times they occured, case insensitive

sentences = [
    'Taki mamy klimat',
    'Wszędzie dobrze ale w domu najlepiej',
    'Wyskoczył jak Filip z konopii',
    'Gdzie kucharek sześć tam nie ma co jeść',
    'Nie ma to jak w domu',
    'Konduktorze łaskawy zabierz nas do Warszawy',
    'Jeżeli nie zjesz obiadu to nie dostaniesz deseru',
    'Bez pracy nie ma kołaczy',
    'Kto sieje wiatr ten zbiera burzę',
    'Być szybkim jak wiatr',
    'Kopać pod kimś dołki',
    'Gdzie raki zimują',
    'Gdzie pieprz rośnie',
    'Swoją drogą to gdzie rośnie pieprz?',
    'Mam nadzieję, że poradzisz sobie z tym zadaniem bez problemu',
    'Nie powinno sprawić żadnego problemu, bo Google jest dozwolony',
]

# Example result:
# 1. "mam" - 12
# 2. "tak" - 5
# 3. "z" - 2


# Good luck! You can write all the code in this file.

def rateWords(stringSet):
    wordRank = {}
    for string in stringSet:
        for word in string.split():
            lowWord = word.lower()
            if lowWord in wordRank.keys():
                wordRank[lowWord] += 1
            else:
                wordRank[lowWord] = 1

    sortedWords = sorted(wordRank.items(), key=lambda item: item[1], reverse=True)

    for i in range(1, 4):
        print(f"{i}. \"{sortedWords[i - 1][0]}\" - {sortedWords[i - 1][1]}")


rateWords(sentences)