#identify the array  as name_and_age
name_and_age = []
#ask user to input the name_and_age
#loop 1: input number
while True:
    #loop2: retry when input raised an error 
    try:
        #if name has numbers
            #print "Name must not contain numbers"
        name = input("Please enter your name: ")
        if not name.isalpha():
                print("Error: Name must not contain numbers.")
                continue
            #age should be <= than 116(the age of the oldest person alive as of now)
                #if age > 116 then print "no person alive is that old"
        while True:
            try:
                age = int(input("Please enter your age: "))
                if age > 116:
                    print("no person alive is that old")
                    continue
                break
            except:
                print("Please enter a valid number")
#input will be stored in array           
        name_and_age.append({
            "name": name, 
            "age": age
        })
                    
        print(name_and_age[-1])
            #if no error, ask if user want to continue: yes\no
        retry = input("Do you want to input another one? (yes/no): ")
        #if yes, ask again for input
        if retry == "no":
            break
    except:
        print("ENGKKKK!!")      
        
if name_and_age:
    # Find the oldest person
    oldest_person = max(name_and_age, key=lambda person: person["age"])
    print(f"The oldest person is {oldest_person["name"]} with age {oldest_person["age"]}.")
else:
    print("No data was entered.")



