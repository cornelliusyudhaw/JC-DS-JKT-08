#Check in for class registration
def register():
    user = input('Register your username: ')
    password = input('Register your password: ')
    reg = [user, password]
    return reg

def login():
    user = input('Input your username: ')
    password = input('Input your password: ')
    log = [user, password]
    return log

def class_registration():
    class_list = {1: 'Data Science Class', 
    2: 'Web and Mobile Class', 3: 'Digital Marketing', 4: 'UI/UX Class'}

    print('''Please choose your class:\n1. Data Science Class\n2. Web and Mobile Class\n3. Digital Marketing Class\n4. UI/UX Class''')

    pilih = int(input('Choose your class: '))
    return class_list[pilih]    

def menu():
    id = {}
    #semisal kita register, isi id bisa jadi {'Cornell' : 1234}
    current_user = ''
    history ={} 
    #history ={'Cornell : ['Data Science'], 'Nel' : []}
    
    while(True):    
        if current_user == '':
            print('''Welcome to the Purwadhika Class Registration!
             Please choose your selection:\n1.Register\n2.Login\n3.Class Registration\n4.History\n5.Log Out\n6.Exit''')
        else:
            print('''\nCurrent User is {}\nWelcome to the Purwadhika Class Registration! Please choose your selection:\n1.Register\n2.Login\n3.Class Registration\n4.History\n5.Log Out\n6.Exit'''.format(current_user))        
        pilih = int(input('Choose: '))    
       
        if pilih == 1:
            reg = register()
            if reg[0] in id.keys():
                print('Username already exist')
            else:    
                id[reg[0]] = reg[1]
                #sama ajah seperti id['Cornell'] = 1234
                current_user = reg[0]
                history[current_user] = []

        elif pilih == 2:
            log = login() #[username, password]
            if current_user == log[0]:
                print('\nAlready Login')
            elif log[0] in id.keys() and log[1] == id[log[0]]:
                print('Welcome {}'.format(log[0]))
                current_user = log[0]
            else:
                print('Username or Password is wrong or username does not exist')


        elif pilih == 3:
            class_reg = class_registration()
            
            if current_user == '':
                print('Please Login First')
            elif class_reg in history[current_user]:
                print('Class already been taken')
            elif current_user in history.keys():
                history[current_user].append(class_reg)
                print('Class Successfully Registered') 

        elif pilih == 4:
            if current_user == '':
                print('Please Login First')
            elif current_user in history.keys() and len(history[current_user]) > 0:    
                if len(history[current_user]) > 1:
                    z = 'Class Taken by {} are'.format(current_user)
                    #['Data Science', 'Web Mobile'] ini isi i, [0,1] ini isi j
                    for idx, val in enumerate(history[current_user]):
                        # zip(history[current_user], range(len(history[current_user])))
                        if idx < len(history[current_user])-1:
                            z += ' {},'.format(val)
                        else:
                            z+= ' and {}'.format(val)
                    print(z)            
                elif len(history[current_user]) == 1:
                    print('Class Taken by {} is {}'.format(current_user,history[current_user][0]))

            else:
                print('No Class Registration Yet')
                
        elif pilih == 5:
            if current_user == '':
                print('Not Logged in yet')
            else:
                current_user = ''
                print('\nSuccessful Logged out')
        else:
            print('Thank You')
            break                

menu()






