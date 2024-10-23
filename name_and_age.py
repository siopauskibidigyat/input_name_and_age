#identify the array  as name_and_age
name_and_age = {}
#ask user to input the name_and_age
#loop 1: input number
while True:
    #loop2: retry when input raised an error 
    while True:
        try:
            #if name has numbers
                #print "Name must not contain numbers"
            name = input("Please enter your name: ")
            if not name.isalpha():
                    print("Error: Name must not contain numbers.")
                    break
                #age should be <= than 116(the age of the oldest person alive as of now)
                    #if age > 116 then print "no one is that old"
            while True:
                    age = int(input("Please enter your age: "))
                    if age > 116:
                        print("no person alive is that old")
                        continue
#input will be stored in array           
                    name_and_age = {
                        "name" : name,
                        "age" : age
                    }

                    print(name_and_age)
                    break
        except:
            print("ENGKKKK!!")      
#if no error, ask if user want to continue: yes\no
    #if yes, ask again for input
    #if no, print the name and age of the oldest person the user has input

