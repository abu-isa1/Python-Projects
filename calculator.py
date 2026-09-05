while True:
    first_no= input ("Enter first number: ")
    if first_no.lower()=="quit":
        break
    first= float(first_no)


    while True:
        operator=input ("Enter operator: ")
        if operator.lower()=="quit":
             break
        second_no= input("Enter second number: ")
        if second_no.lower()=="quit":
             break
        second=float(second_no)

        if operator =="+":
            res=first+second
        elif operator =="-":
            res=first-second
        elif operator =="/":
            res=first/second
        elif operator =="//":
            res=first//second
        elif operator =="%":
            res=first%second
        elif operator =="*":
            res=first*second   
        else:
            print("Invalid Input")
            break  

        print(res)

        choise= input (f"continue with {res} ? (y/n)")
        first=res
        if choise== "y":
            continue
        else:
            break



