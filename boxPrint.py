def boxPrint(string):
    words=string.split()
    highest_length=0
    for word in words:
        word_length=0
        for letter in word:
            word_length+=1
        if word_length>highest_length:
            highest_length=word_length
    
    top_box=[]
    for i in range(2+highest_length):
        top_box.append('*')
    top_string="".join(top_box)
    
    print(top_string)
    for word in words:
        spaces=highest_length
        space_string=[]
        
        for letter in word:
            spaces-=1
        for i in range(spaces):
            space_string.append(' ')
        space_string1= "".join(space_string)
        print('*' + word + space_string1 + '*')
    print(top_string)
boxPrint(input('string here '))


