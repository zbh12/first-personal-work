import jieba

txt = open('comment.txt','r', encoding = 'utf-8').read()
txt = jieba.lcut(txt)
counts = {}

for word in txt:
    if len(word) == 1:
        continue
    else:
        counts[word] = counts.get(word, 0) + 1

li = list(counts.items())
li.sort(key=lambda x:x[1], reverse=True)

with open('词频.txt','a',encoding='utf-8') as file:
    for i in range(1,21):
        key,value = li[i]
        print('{:<3}{:<6}{:>5}'.format(i,key,value))
        file.write(key+'\n')