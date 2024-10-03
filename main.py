with open("story.txt",'r') as f:
    story=f.read()
word=''
word_list=[]
user_word_list=[]
n=len(story)
for i in range(n):
    if story[i]=='<':
        j=i+1
        while story[j]!='>':
            word+=story[j]
            j+=1
        if word in word_list:
            pass
        else:
            word_list.append(word)
            user_word=input(f"enter {word} : ")
            user_word_list.append(user_word)
        word=''
new_story=story
for i in range(len(word_list)):
    new_story=new_story.replace(f'<{word_list[i]}>',user_word_list[i])

print(new_story)
    