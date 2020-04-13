N = int(input())
S = input()

result_dic = {}

before_words = {i:0 for i in range(10)}
after_words = {i:0 for i in range(10)}
for s in S:
    after_words[int(s)] += 1

for  i, s in enumerate(S[:-1]):
    if i == 0:
        before_words[int(s)] += 1
        after_words[int(s)] -= 1
        continue
    after_words[int(s)] -= 1

    before =  [x for x, y in before_words.items() if y > 0]
    after =  [x for x, y in after_words.items() if y > 0]
    for b in before:
        for a in after:
            result_dic[str(b) + s + str(a)] = 1

    before_words[int(s)] += 1

print(len(result_dic))