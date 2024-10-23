#identify the array  as name_and_age
name_and_age = {}
#ask user to input the name and age
while True:
    while True:
        try:
            name = input("Please enter your name: ")
            age = int(input("Please enter your age: "))
#input will be stored in array           
            name_and_age = {
                "name" : name,
                "age" : age
            }

            print(name_and_age)
        except:
            print("ENGKKKK!!")
    #if age <= than 116(the age of the oldest person alive as of now)
        #if age > 116 then print "are you sure that is your true age? yes or no"    
    #if the user input a letter in age
        #print("Please input a valid number")
    #if name has numbers
        #print "Name must not contain numbers"
#if no error, ask if user want to continue: yes\no
    #if yes, ask again for input
    #if no, print the name and age of the oldest person the user has input

