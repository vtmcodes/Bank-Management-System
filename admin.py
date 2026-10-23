from beatm import load_data, save_data

bank_data = load_data()

if bank_data is None:
    exit()

balance = bank_data["balance"]
code = bank_data["code"]
blocked_accounts = bank_data["blocked_accounts"]

loop_state = 1

while loop_state == 1:
    print("-----------------------")
    print("-----------------------")
    print()
    print("NEPAL RASHTRA BANK - AUTHORIZED ACCESS AND MODIFICATION ONLY")
    print()
    print("What process do you want to do?")
    print("1. Add money to user account. (Enter 1)")
    print("2. Unblock user account. (Enter 2)")
    print("3. Create a new account. (Enter 3)")
    print("4. Change user pin. (Enter 4)")
    print("5. Block user account. (Enter 5)")
    print("6. Delete user account. (Enter 6)")
    print()
    auth_choice = input()
    if auth_choice == "1": # ADD MONEY TO ACCOUNT
        loop_state = 1.1
        while loop_state == 1.1:
            print()
            print("Enter the account number. ")
            print("Or enter 0 to exit. ")
            oneauthchoice = input().strip().lower()

            if oneauthchoice not in balance and oneauthchoice != "0":
                print("Account doesnt exist! Try again. ")
                loop_state = 1.1

            elif oneauthchoice == "0":
                loop_state = 1

            else:
                print()
                print("Enter the sum of money to add to user account. ")
                print()
                add_account_sum = int(input())
                balance[oneauthchoice] += add_account_sum
                bank_data["balance"] = balance
                save_data(bank_data)
                print()
                print(f"Successfully added {add_account_sum} to account number {oneauthchoice}. ")
                print(f"New account balance is {balance[oneauthchoice]}.")
                loop_state = 1

    elif auth_choice == "2": # UNBLOCK ACCOUNT
        loop_state = 2.1
        while loop_state == 2.1:
            print()
            print("Enter user account. ")
            print("Or enter 0 to exit. ")
            oneauthchoice2 = input().strip().lower()

            if oneauthchoice2 not in blocked_accounts and oneauthchoice2 != "0":
                print()
                print("Account isnt blocked! ")
                loop_state = 2.1

            elif oneauthchoice2 == "0":
                loop_state = 1

            else:
                print()
                blocked_accounts.remove(oneauthchoice2)
                save_data(bank_data)
                print(f"Successfully unblocked account number {oneauthchoice2}.")
                loop_state = 1

    elif auth_choice == "3": # CREATE ACCOUNT
        loop_state = 3.1
        while loop_state == 3.1:
            print()
            print("Enter user account number. ")
            print("Or enter 0 to exit. ")
            try:
                new_user_account = input()
                intnua = int(new_user_account)
                if new_user_account == "0":
                    loop_state = 1

                elif new_user_account in balance:
                    print()
                    print("Account number already exists. Try again. ")
                    loop_state = 3.1

                elif intnua <= 1000:
                    print()
                    print("Enter a valid account number greater than 1000. ")
                    loop_state = 3.1

                else:
                    loop_state = 3.2
                    while loop_state == 3.2:
                        print()
                        print("Enter pin for this user. ")
                        nuapin = input()
                        print("Enter it again. They must match. ")
                        nuapin2 = input()
            
                        if nuapin == nuapin2:
                            print()
                            balance[new_user_account] = 0
                            code[new_user_account] = nuapin2
                            bank_data["balance"] = balance
                            bank_data["code"] = code
                            save_data(bank_data)
                            print(f"Successfully created account with user number {new_user_account} and pin {nuapin2}.")
                            loop_state = 1
                        else:
                            print()
                            print("Try again. They dont match. ")
                            loop_state = 3.2
            except ValueError:
                print("Dont enter letters. Try again. ")
                loop_state = 3.1


    elif auth_choice == "4": # CHANGE PIN
        loop_state = 4.1
        while loop_state == 4.1:
            print()
            print("Enter the account to change the password of. ")
            print("Or enter 0 to exit. ")
            changepassacc = input()
            if changepassacc not in balance:
                print()
                print("Account does not exist. Try again. ")
                loop_state = 4.1

            elif changepassacc == "0":
                loop_state = 1

            else: 
                loop_state = 4.2
                while loop_state == 4.2:
                    print()
                    print("Enter new pin for user. ")
                    print("Or: ")
                    print("Enter [one] to choose another action. ")
                    print("Enter [two] to choose another account. ")
                    try:
                        newpinuser = input().strip().lower()
                        intnpu = int(newpinuser)
                        if newpinuser == "one":
                            loop_state = 1
                        elif newpinuser == "two":
                            loop_state = 4.1
                        if intnpu < 1000:
                            print()
                            print("Invalid pin. Pin must be of 4 digits. ")
                            loop_state = 4.2
                        else: 
                            print("Enter it again. They must match. ")
                            newpinuser2 = input()
                            intnpu2 = int(newpinuser2)
                            if intnpu == intnpu2:
                                print()
                                code[changepassacc] = newpinuser2
                                bank_data["code"] = code
                                save_data(bank_data)
                                print(f"Successfully changed user pin to {intnpu2}. ")
                                loop_state = 1
                            elif intnpu != intnpu2:
                                print()
                                print("They dont match. Try again. ")
                                loop_state = 4.2
                    except ValueError:
                        print()
                        print("Pins cant have letters. Try again. ")
                        loop_state = 4.2

    elif auth_choice == "5": # BLOCK USER ACCOUNT
        loop_state = 5.1
        while loop_state == 5.1:
            print()
            print("Enter user account needed to block. ")
            print("Or enter 0 to exit. ")
            need_block_acc = input()
            if need_block_acc == "0":
                loop_state = 1
            elif need_block_acc in blocked_accounts:
                print()
                print("Account is already blocked. ")
                loop_state = 5.1
            elif need_block_acc not in balance:
                print()
                print("Account does not exist. ")
                loop_state = 5.1
            else:
                loop_state = 5.2
                while loop_state == 5.2:
                    print()
                    print(f"Is {need_block_acc} the correct accout needed to block? ")
                    print("Enter 1 for yes ")
                    print("Enter 2 for no ")
                    block_account_verfication = input()
                    intbav = int(block_account_verfication)
                    if intbav == 1:
                        blocked_accounts.append(need_block_acc)
                        bank_data["blocked_accounts"] = blocked_accounts
                        save_data(bank_data)
                        print(f"Successfully blocked {need_block_acc}")
                        loop_state = 1
                    elif intbav == 2:
                        print()
                        print("Restarting program... ")
                        loop_state = 5.2
                    else:
                        print()
                        print("Invalid choice. Restarting... ")
                        loop_state = 5.2

    elif auth_choice == "6": # DELETE USER ACCOUNT
        loop_state = 6.1
        while loop_state == 6.1:
            print()
            print("You are trying to perform a very risky task. Proceed? ")
            print("Enter 1 if yes ")
            print("Enter 2 if no ")
            del_acc_choice = input()
            if del_acc_choice == "1":
                loop_state = 6.2
                while loop_state == 6.2:
                    print()
                    print("Enter user account do start account deletion process. ")
                    del_acc_user = input()
                    if del_acc_user in balance:
                        loop_state = 6.3
                        while loop_state == 6.3:
                            print()
                            print("Is this the correct account for deletion? ")
                            print(f"Selected account: {del_acc_user}")
                            print("Enter 1 if yes ")
                            print("Enter 2 if no ")
                            del_acc_verification = input()
                            if del_acc_verification == "1":
                                print()
                                del balance[del_acc_user]
                                bank_data["balance"] = balance
                                save_data(bank_data)
                                print(f"Successfully deleted account number {del_acc_user}")
                                loop_state = 1
                            elif del_acc_verification == "2":
                                print()
                                print("Redirecting... ")
                                loop_state = 6.2
                            else:
                                print()
                                print("Invalid choice. Try again.")
                                loop_state = 6.3
                    else:
                        print("Account doesnt exist. Try again. ")
                        loop_state = 6.2

            elif del_acc_choice == 2:
                print()
                print("Restarting program... ")
                loop_state = 1
            else:
                print()
                print("Invalid choice. Choose again. ")
                loop_state = 6.1

    else:
        print("Please input a valid choice to take action. ")
        continue