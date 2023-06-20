# def main(s):
#     for i in set(s):
#         counter = 0
#         for x in s:
#             if i == x:
#                 counter += 1
#         print(i, counter)
#
#
# main('aawsa')


def main(s):
    sym = {}
    for i in s:
        sym[i] = sym.get(i, 0) + 1

    for i, count in sym.items():
        print(i, count)
main('kkjkjin')





