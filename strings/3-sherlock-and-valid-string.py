#!/bin/python3
# https://www.hackerrank.com/challenges/sherlock-and-valid-string
# 26.76/35
import math


def isValid(s):
    s = sorted(s)
    # print(s)
    maxi = -float('inf')
    mini = float('inf')
    min_occurrences = 0
    max_occurrences = 0
    set_s = set(s)
    print(set_s)
    if len(s) == len(set_s):
        return 'YES'
    for ch1 in list(set_s):
        current_count = 0
        print('ch1', ch1)
        for ch2 in s:
            if (ch1 == ch2):
                # print('ch1', ch1)
                current_count += 1
        print('current_count', current_count)
        if (current_count > maxi):
            maxi = current_count
            max_occurrences = 0

        if (current_count == maxi):
            max_occurrences += 1

        if (current_count < mini):
            mini = current_count
            min_occurrences += 0

        if (current_count == mini):
            min_occurrences += 1
            # if min_occurrences > 2:
            # return 'NO'
    print(mini)
    print(maxi)
    print('min_occurrences', min_occurrences)
    print('max_occurrences', max_occurrences)
    return 'YES' if (maxi - mini == 1 and (min_occurrences < 2 or max_occurrences < 2)) else 'NO'


if __name__ == '__main__':
    s = 'ibfdgaeadiaefgbhbdghhhbgdfgeiccbiehhfcggchgghadhdhagfbahhddgghbdehidbibaeaagaeeigffcebfbaieggabcfbiiedcabfihchdfabifahcbhagccbdfifhghcadfiadeeaheeddddiecaicbgigccageicehfdhdgafaddhffadigfhhcaedcedecafeacbdacgfgfeeibgaiffdehigebhhehiaahfidibccdcdagifgaihacihadecgifihbebffebdfbchbgigeccahgihbcbcaggebaaafgfedbfgagfediddghdgbgehhhifhgcedechahidcbchebheihaadbbbiaiccededchdagfhccfdefigfibifabeiaccghcegfbcghaefifbachebaacbhbfgfddeceababbacgffbagidebeadfihaefefegbghgddbbgddeehgfbhafbccidebgehifafgbghafacgfdccgifdcbbbidfifhdaibgigebigaedeaaiadegfefbhacgddhchgcbgcaeaieiegiffchbgbebgbehbbfcebciiagacaiechdigbgbghefcahgbhfibhedaeeiffebdiabcifgccdefabccdghehfibfiifdaicfedagahhdcbhbicdgibgcedieihcichadgchgbdcdagaihebbabhibcihicadgadfcihdheefbhffiageddhgahaidfdhhdbgciiaciegchiiebfbcbhaeagccfhbfhaddagnfieihghfbaggiffbbfbecgaiiidccdceadbbdfgigibgcgchafccdchgifdeieicbaididhfcfdedbhaadedfageigfdehgcdaecaebebebfcieaecfagfdieaefdiedbcadchabhebgehiidfcgahcdhcdhgchhiiheffiifeegcfdgbdeffhgeghdfhbfbifgidcafbfcd'
    # s = 'aaaaacccccdddddtstttt'
    result = isValid(s)
    print(result)
