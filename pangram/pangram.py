def is_pangram(sentence):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    ma = {}
    for item in alphabet:
        ma[item]=0

    sentence = str.lower(sentence)

    for item in sentence:
        if ma.__contains__(item):
            ma[item] = ma[item]+1

    isPangram = True

    for item in ma.keys():
        if ma[item] == 0:
            isPangram=False
            break

    return isPangram
#if __name__ == "__main__":
#    is_pangram("babi")


