def my_func():
    user_input = input("Do you already have mortgage? (YES or NO)")
    if(user_input == "yes"):
        print("Sorry you can't take another mortgage at the moment")
    elif(user_input == "no"):
        property_value = float(input("What is the value of the property?"))
        user_salaray = float(input("What is your annual salary?"))
        if(user_salaray >= property_value * 20 / 100):
            upfront_cost = float(input("How much do you intend to give upfront?"))
            if(upfront_cost >= property_value * 10 / 100):
                monthly_spend = float(input("How much do you spend per month?"))
                if(monthly_spend <= user_salaray * 25 / 100):
                    print("You are eligible to take a mortgage!!")
                else:
                    print("Unfortunately you don't meet the minimum requirments.")
            else:
                print("Sorry, you don't meet the minimum requirments")
        else:
            print("Sorry, you don't meet the minimum requirments")
    else:
        print("Something went wrong, please try again.")



my_func()