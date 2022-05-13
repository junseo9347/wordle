import random as r
def Convert(string):
    list1= []
    list1[:0]=string
    return list1
word_list=[]
src=open("word_list.txt")
for word in src:
    word_list.append(word[:5])
#answer_word=Convert(r.choice(word_list))
answer_word = "steep"
print(answer_word)
y_corr =[]
g_corr=[]

i=1
while i<6:
    skip=False
    input_word=input("Input a 5 character word: ")
    if input_word not in word_list:
        print("This word does not exist.")
        continue
    for i in range(len(y_corr)):
        if y_corr[i] not in input_word:
            print("The word you inputed does not meet the requirements")
            skip = True
    if (skip):
        continue
    for i in range(len(g_corr)):
        if answer_word[g_corr[i]] != input_word[g_corr[i]]:
            print(answer_word[g_corr[i]], input_word[g_corr[i]])
            print("The word you inputed does not meet the requirements eeee")
            skip=True
    if skip==True:
        continue
    input_word=Convert(input_word)
    for i in range(len(input_word)):
        input_char = input_word[i]
        answer_char=answer_word[i]
        if input_char in answer_word:
            if input_char == answer_char:
                if i not in g_corr:
                    g_corr.append(i)
                continue
            else:
                if input_word[i] not in y_corr:
                    y_corr.append(input_word[i])
    if len(g_corr)==len(answer_word):
        print("Congrats")
        break
    print(g_corr,y_corr,answer_word)





