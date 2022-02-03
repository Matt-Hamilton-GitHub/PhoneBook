import pickle
file = open('phonebook.in', 'rb')

info = pickle.load(file)

booly = True
while booly == True:
    print('Enter')
    print('1) look up an email address')
    print('2) add a new name and email address')
    print('3) change an email address')
    print('4) delete a name and email address')
    choice = int(input('5) save address book and exit:'))
    
    if choice == 1:
        name = str(input('Enter name:'))
        if name in info:
            print(info[name])
        else:
            print('Sorry, no contact exists under that name.')
    elif choice == 2 :
        name1 = str(input('Name:'))
        email = str(input('Enter email address:'))
        info[name1] = email
    
    elif choice == 3 :
        name2 = str(input('Name:'))
        newEmail = str(input('Enter new email address:'))
        info[name2] = newEmail
        
    elif choice == 4 :
        name3 = str(input('Name:'))
        del info[name3]
        
    elif choice == 5 :
        
        newFile = open('phonebook.out', 'wb')
        inAlpha = sorted(info.items())
        Adic = {}
        for x in inAlpha:
            Adic[x[0]] = x[1]
        pickle.dump(Adic,newFile)
        booly = False
        newFile.close()
        
file.close()
