while(1):
    uzzbefore = input('Please enter your word: ')
    if('girl' in uzzbefore):
        print('huzz')
    else:
        found = False
        i = 0
        it = False
        while(found == False and i<len(uzzbefore)):
            if(uzzbefore[i] == 'a' or uzzbefore[i] == 'e' or uzzbefore[i] == 'i' or uzzbefore[i] == 'o' or uzzbefore[i] == 'u'):
                if(i != 0):
                    if(uzzbefore[i-1] != 'a' and uzzbefore[i-1] != 'e' and uzzbefore[i-1] != 'i' and uzzbefore[i-1] != 'o' and uzzbefore[i-1] != 'u'):
                        found = True
                        break
            i += 1
        print(uzzbefore + ' uzzified = ' + uzzbefore[0:i] + 'uzz')