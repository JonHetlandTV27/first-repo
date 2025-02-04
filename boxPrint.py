def boxPrint(string):
    words=string.split()
    print('**********')
    for word in words:
        print('* '+ word + ' *')
    print('**********')

boxPrint(input('what string would you like to be input?'))