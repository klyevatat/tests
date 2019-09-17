VOWELS = "aeiouy"

import re

def translate(phrase):
    result = re.sub(f'(?<=[^{VOWELS} ])[{VOWELS}]', '', phrase)
    return re.sub(f'(?P<vowel>[{VOWELS}]){{3}}', r'\g<vowel>', result)

if __name__ == '__main__':
    print("Example:")
    print(translate("hieeelalaooo"))

    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert translate("hieeelalaooo") == "hello", "Hi!"
    assert translate("hoooowe yyyooouuu duoooiiine") == "how you doin", "Joey?"
    assert translate("aaa bo cy da eee fe") == "a b c d e f", "Alphabet"
    assert translate("sooooso aaaaaaaaa") == "sos aaa", "Mayday, mayday"
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")