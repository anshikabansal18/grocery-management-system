'''Welcome user with welcome message'''
WelcomeMessage = "Welcome to Anshika's grocery store"
lenWcMsg = len(WelcomeMessage)
print(WelcomeMessage)
print("=" * lenWcMsg)

customer = []

ans = 'y'
while ans == 'y':
    print("Kindly choose from the given options:")
    print("\t1) Enter customer details\n\t2) View details of the given customer id")
    print("\t3) Delete the record of the given customer id\n\t4) View total bill of the customer\n\t5) Exit")
    print("=========================================")
    choice = int(input("Enter the option : "))
    print("==========================================")

    if choice == 1:
        # To keep the record of the customer
        CustomerId = int(input("Please enter your customer id: "))
        CustomerType = input("Please enter if you are a regular or temporary customer: ")
        
        if CustomerType.lower() == "regular":
            print("Welcome Back again!")
        else:
            print("Happy Shopping")

        n = int(input("Enter the number of items: "))
        customer.append((CustomerId, CustomerType, n))

        for i in range(0, n):
            item = input("Item name: ")
            itemquantity = int(input("Quantity: "))
            rate = int(input("Rate: "))
            subtotal = rate * itemquantity
            print("Subtotal: ", subtotal)

            # Append item details to lists
            customer[-1] += (item, itemquantity, rate, subtotal)

    elif choice == 2:
        print("----------Searching engine(please wait....)-----------")
        ch = int(input("Enter Customer id to search: "))
        found = False

        for cust in customer:
            if cust[0] == ch:
                print("Customer id found :) following are the details")
                print(cust)
                found = True
                break

        if not found:
            print("Customer id not valid")

    elif choice == 3:
        delete = int(input("Enter the customer id to delete: "))
        found = False

        for cust in customer:
            if cust[0] == delete:
                customer.remove(cust)
                print("-----Deleting the record of customer id", delete, "---------")
                found = True
                break

        if not found:
            print("Customer id not valid")

    elif choice == 4:
        bill = int(input("Enter the customer id to view the bill: "))
        found = False

        for cust in customer:
            if cust[0] == bill:
                print("<TECH BEES GROCERY STORE>")
                print(cust)
                print("-----Bill Summary------")
                
                # Get the number of items purchased for this customer
                n = cust[2]

                for i in range(n):
                    print("Item purchased:", cust[3 + i * 4], "Quantity:", cust[4 + i * 4],
                          "Rate:", cust[5 + i * 4], "Subtotal:", cust[6 + i * 4])

                # Calculate and display the total amount
                ans = sum(cust[6 + i * 4] for i in range(n))
                print('Total amount:', ans)

                # Payment options
                modeofpayment = input("Please enter the mode of payment (card/cash): ").lower()
                if modeofpayment == "card":
                    print("Swipe your card")
                else:
                    print("Deposit cash at the front counter")

                found = True
                break

        if not found:
            print("Customer id not valid")

        # Thank you message for the customer
        print("Thank you for your purchase! Hope to see you back soon :)")

    elif choice == 5:
        print("-----Exiting------")
        ans = 'n'
    else:
        print("Wrong option")

