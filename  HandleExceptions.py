#Create a script called HandleExceptions.py. In the script, create a section of code that requests sales numbers from a user. The user should be able to enter as many sales values as they choose to. All sales values should always be entered as float values. Each value entered should be added to a list of sales values.
value_of_sales = []

#In this section we will mainly focus on the input
while True:
    try:
        value = float(input("Insert your value of sale (or q to quit): "))

#in this section we mainly focus to give the value_of_sales a value because for the moment its empty.
        value_of_sales.append(value)
    except ValueError:
        #The value error will lead to a error message for the user that the input is invalid
        print("invalid input.please try again")
    except KeyboardInterrupt:
        print("exfilling program")
        break
    except:
        #other issues related to the code will deliver the following statement
        print("an error has occurred, simply try again")

    #Here we calculate the value of sales to the input inserted above
    total = 0
    try:
        #Get the value of sales to the inserted number above
        number_of_sales = int(input("enter the number of value related to sales to add to total: "))

        #Here will the number be added to total
        for i in range(number_of_sales):
            total += value_of_sales[i]
    except ValueError:
        #Handle the exception if the user make a mistake
        print("invalid input please try again")
    except IndexError:
        #Handle the exception if the user enters a number greater than the length of the list
        print("invalid input. the value of sales only contains " + str(len(value_of_sales)) + "values.")
    except:
        #handle other errors
        print("an error has occurred.please try again")
    
    #print the value of sales
    print("total sales " + str(value))

