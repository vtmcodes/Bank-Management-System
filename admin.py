from beatm import load_data, save_data

bank_data = load_data()

if bank_data is None:
    exit()

accounts = bank_data["accounts"]
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
            oneauthchoice = input().strip()

            if oneauthchoice == "0":
                loop_state = 1
                continue


            elif not oneauthchoice:
                print()
                print("Please enter a account number. ")
                loop_state = 1.1
                continue

            elif not oneauthchoice.isdigit():
                print()
                print("Dont use letters, accounts only have numbers. ")
                loop_state = 1.1
                continue

            elif oneauthchoice not in accounts:
                print("Account doesnt exist! Try again. ")
                loop_state = 1.1
                continue

            else:
                loop_state = 1.11
                while loop_state == 1.11:
                    print()
                    print("Enter the sum of money to add to user account. ")
                    print()
                    add_account_sum = input().strip()
                    if not add_account_sum:
                        print()
                        print("Please enter a sum. ")
                        loop_state = 1.11
                        continue
                    elif not add_account_sum.isdigit():
                        print()
                        print("Dont use letters. ")
                        loop_state = 1.11
                        continue
                    else:
                        sumval = int(add_account_sum)
                        if sumval <= 0:
                            print()
                            print("Invalid sum to add to account. Try again. ")
                            loop_state = 1.11
                            continue
                        else:
                            accounts[oneauthchoice]["Balance"] += sumval
                            bank_data["accounts"] = accounts
                            save_data(bank_data)
                            print()
                            print(f"Successfully added {add_account_sum} to account number {oneauthchoice}. ")
                            print(f"New account balance is {accounts[oneauthchoice]['Balance']}. ")
                            loop_state = 1
                            continue

    elif auth_choice == "2": # UNBLOCK ACCOUNT
        loop_state = 2.1
        while loop_state == 2.1:
            print()
            print("Enter user account. ")
            print("Or enter 0 to exit. ")
            oneauthchoice2 = input().strip()

            if oneauthchoice2 == "0":
                loop_state = 1
                continue

            elif not oneauthchoice2:
                print()
                print("Enter a account to unblock. ")

            elif not oneauthchoice2.isdigit():
                print()
                print("Dont use letters. ")
                loop_state = 2.1
                continue

            elif oneauthchoice2 not in blocked_accounts:
                print()
                print("Account isnt blocked. Try agan. ")
                loop_state = 2.1
                continue
            
            else:
                print()
                blocked_accounts.remove(oneauthchoice2)
                save_data(bank_data)
                print(f"Successfully unblocked account number {oneauthchoice2}.")
                loop_state = 1
                continue

    elif auth_choice == "3": # CREATE ACCOUNT
        loop_state = 3.1
        while loop_state == 3.1:
            print()
            print("Enter user account number. ")
            print("Or enter 0 to exit. ")
            new_user_account = input()
            if new_user_account == "0":
                loop_state = 1
                continue

            elif not new_user_account:
                print()
                print("Please enter a account. ")
                loop_state = 3.1
                continue

            elif not new_user_account.isdigit():
                print()
                print("Only use numbers for account creation. ")
                loop_state = 3.1
                continue

            elif new_user_account in accounts:
                print()
                print("Account number already exists. Try again. ")
                loop_state = 3.1
                continue

            elif len(new_user_account) < 4:
                print()
                print("Enter a valid account number greater than 1000. ")
                loop_state = 3.1
                continue

            else:
                loop_state = 3.2
                while loop_state == 3.2:
                    print()
                    print("Enter pin for this user. ")
                    nuapin = input().strip()
                    if not nuapin:
                        print()
                        print("Please input a pin. ")
                        loop_state = 3.2
                        continue
                    elif not nuapin.isdigit():
                        print()
                        print("Number should be only numbers, not letters. Try again. ")
                        loop_state = 3.2
                        continue
                    elif len(nuapin) != 4:
                        print()
                        print("Pin should only be of 4 digits. ")
                        loop_state = 3.2
                        continue

                    else:
                        print("Enter it again. They must match. ")
                        nuapin2 = input()
        
                        if nuapin == nuapin2:
                            loop_state = 3.21
                            while loop_state == 3.21:
                                print()
                                print("Enter user's full name. ")
                                new_user_name = input()
                                if not new_user_name:
                                    print()
                                    print("You didnt enter the name. ")
                                    loop_state = 3.21
                                    continue
                                elif not all(char.isalpha() or char.isspace() for char in new_user_name):
                                    print()
                                    print("Name cant have numbers or special symbols. ")
                                    loop_state = 3.21
                                    continue
                                else:
                                    loop_state = 3.3
                                    while loop_state == 3.3:
                                        print()
                                        print("Enter user phone number. ")
                                        new_user_number = input()
                                        if not new_user_number:
                                            print()
                                            print("You didnt enter the number. ")
                                            loop_state = 3.3
                                            continue
                                        elif not all(char.isdigit() for char in new_user_number):
                                            print()
                                            print("Phone numbers cant have anything except numbers. ")
                                            loop_state = 3.3
                                            continue
                                        elif len(new_user_number) != 10:
                                            print()
                                            print("A phone number must contain 10 digits. ")
                                            loop_state = 3.3
                                            continue
                                        else:
                                            loop_state = 3.4
                                            while loop_state == 3.4:
                                                print()
                                                print("Enter user address. ")
                                                new_user_address = input().strip()
                                                if not new_user_address:
                                                    print()
                                                    print("You didnt enter the address. ")
                                                    loop_state = 3.4
                                                    continue
                                                else:
                                                    loop_state = 3.5
                                                    while loop_state == 3.5:
                                                        print()
                                                        print("Enter user email. ")
                                                        new_user_email = input().strip()
                                                        if not new_user_email:
                                                            print()
                                                            print("You didnt enter the email. ")
                                                            loop_state = 3.5
                                                            continue
                                                        else:
                                                            loop_state = 3.6
                                                            while loop_state == 3.6:
                                                                print()
                                                                print("Enter user date of birth. ")
                                                                new_user_dob = input().strip()
                                                                if not new_user_dob:
                                                                    print()
                                                                    print("You didnt enter the date of birth. ")
                                                                    loop_state = 3.6
                                                                    continue
                                                                else:
                                                                    loop_state = 3.7
                                                                    while loop_state == 3.7:
                                                                        print()
                                                                        print("Enter user citizenship number. ")
                                                                        new_user_cn = input().strip()
                                                                        if not new_user_cn:
                                                                            print()
                                                                            print("You didnt enter the citizenship number. ")
                                                                            loop_state = 3.7
                                                                            continue
                                                                        elif not all(char.isdigit() for char in new_user_cn):
                                                                            print()
                                                                            print("Citizenship number can only contain numbers. ")
                                                                        else:
                                                                            accounts[new_user_account] = {}
                                                                            accounts[new_user_account]["Name"] = new_user_name
                                                                            accounts[new_user_account]["Contact"] = new_user_number
                                                                            accounts[new_user_account]["Balance"] = 0
                                                                            accounts[new_user_account]["Pin"] = nuapin2
                                                                            accounts[new_user_account]["Address"] = new_user_address
                                                                            accounts[new_user_account]["DOB"] = new_user_dob
                                                                            accounts[new_user_account]["Citizenship number"] = new_user_cn
                                                                            accounts[new_user_account]["Email"] = new_user_email
                                                                            bank_data["accounts"] = accounts
                                                                            save_data(bank_data)
                                                                            print()
                                                                            print("Successfully created a new account. ")
                                                                            print("DETAILS: ")
                                                                            print(f"Name: {new_user_name}")
                                                                            print(f"Contact: {new_user_number}") 
                                                                            print(f"Balance: 0")
                                                                            print(f"Pin: {nuapin2}")
                                                                            print(f"Address: {new_user_address}")
                                                                            print(f"DOB: {new_user_dob}")
                                                                            print(f"Citizenship number: {new_user_cn}")
                                                                            print(f"E-mail: {new_user_email}")
                                                                            loop_state = 1
                                                                            continue
                        else:
                            print()
                            print("Try again. They dont match. ")
                            loop_state = 3.2
                            continue

    elif auth_choice == "4": # CHANGE PIN
        loop_state = 4.1
        while loop_state == 4.1:
            print()
            print("Enter the account to change the password of. ")
            print("Or enter 0 to exit. ")
            changepassacc = input().strip()
            if changepassacc == "0":
                loop_state = 1
                continue
            elif not changepassacc:
                print()
                print("Please enter a account. ")
                loop_state = 4.1
                continue
            elif not all(char.isdigit() for char in changepassacc):
                print()
                print("Account can only contain numbers. ")
                loop_state = 4.1
                continue
            elif changepassacc not in accounts:
                print()
                print("Account does not exist. Try again. ")
                loop_state = 4.1
                continue

            else: 
                loop_state = 4.2
                while loop_state == 4.2:
                    print()
                    print("Enter new pin for user. ")
                    print("Or: ")
                    print("Enter 1 to choose another action. ")
                    print("Enter 2 to choose another account. ")
                    newpin_choice = input()
                    try:
                        newpinuser = int(newpin_choice)
                    except ValueError:
                        print()
                        print("Pin cant contain letters. Try again. ")
                        loop_state = 4.2
                        continue
                    if not newpin_choice:
                        print()
                        print("Please enter a choice. ")
                        loop_state = 4.2
                        continue
                    if not all(char.isdigit() for char in newpin_choice):
                        print()
                        print("You can only input numbers. ")
                        loop_state = 4.2
                        continue
                    elif newpin_choice == "1":
                        loop_state = 1
                        continue
                    elif newpin_choice == "2":
                        loop_state = 4.1
                        continue
                    if newpinuser < 1000 or newpinuser > 9999:
                        print()
                        print("Invalid pin. Pin must be of 4 digits. ")
                        loop_state = 4.2
                        continue
                    else: 
                        print("Enter it again. They must match. ")
                        newpinuser2 = int(input())
                        if newpinuser == newpinuser2:
                            print()
                            accounts[changepassacc]["Pin"] = str(newpinuser2)
                            bank_data["accounts"] = accounts
                            save_data(bank_data)
                            print(f"Successfully changed user pin to {newpinuser2}. ")
                            loop_state = 1
                            continue
                        elif newpinuser != newpinuser2:
                            print()
                            print("They dont match. Try again. ")
                            loop_state = 4.2
                            continue

    elif auth_choice == "5": # BLOCK USER ACCOUNT
        loop_state = 5.1
        while loop_state == 5.1:
            print()
            print("Enter user account needed to block. ")
            print("Or enter 0 to exit. ")
            need_block_acc = input().strip()
            if need_block_acc == "0":
                loop_state = 1
                continue
            elif not need_block_acc:
                print()
                print("Please enter a account number. ")
                loop_state = 5.1
                continue
            elif need_block_acc in blocked_accounts:
                print()
                print("Account is already blocked. ")
                loop_state = 5.1
                continue
            elif need_block_acc not in accounts:
                print()
                print("Account does not exist. ")
                loop_state = 5.1
                continue
            else:
                loop_state = 5.2
                while loop_state == 5.2:
                    print()
                    print(f"Is {need_block_acc} the correct accout needed to block? ")
                    print("Enter 1 for yes ")
                    print("Enter 2 for no ")
                    block_account_verfication = input()
                    if block_account_verfication == "1":
                        blocked_accounts.append(need_block_acc)
                        bank_data["blocked_accounts"] = blocked_accounts
                        save_data(bank_data)
                        print(f"Successfully blocked {need_block_acc}")
                        loop_state = 1
                        continue
                    elif block_account_verfication == "2":
                        print()
                        print("Restarting program... ")
                        loop_state = 5.1
                        continue
                    else:
                        print()
                        print("Invalid choice. Restarting... ")
                        loop_state = 5.2
                        continue

    elif auth_choice == "6": # DELETE USER ACCOUNT
        loop_state = 6.1
        while loop_state == 6.1:
            print()
            print("You are trying to perform a very risky task. Proceed? ")
            print("Enter 1 if yes ")
            print("Enter 2 if no ")
            del_acc_choice = input()
            if not del_acc_choice:
                print()
                print("Please enter a choice. ")
                loop_state = 6.1
                continue
            elif del_acc_choice == "1":
                loop_state = 6.2
                while loop_state == 6.2:
                    print()
                    print("Enter user account do start account deletion process. ")
                    del_acc_user = input().strip()
                    if not del_acc_user:
                        print()
                        print("Please enter a valid choice. ")
                        loop_state = 6.2
                        continue
                    elif not all(char.isdigit() for char in del_acc_user):
                        print()
                        print("Choice must contain only numbers. ")
                    elif del_acc_user in accounts:
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
                                del accounts[del_acc_user]
                                bank_data["accounts"] = accounts
                                save_data(bank_data)
                                print(f"Successfully deleted account number {del_acc_user}")
                                loop_state = 1
                                continue
                            elif del_acc_verification == "2":
                                print()
                                print("Redirecting... ")
                                loop_state = 6.2
                                continue
                            else:
                                print()
                                print("Invalid choice. Try again.")
                                loop_state = 6.3
                                continue
                    else:
                        print("Account doesnt exist. Try again. ")
                        loop_state = 6.2
                        continue

            elif del_acc_choice == "2":
                print()
                print("Restarting program... ")
                loop_state = 1
                continue
            else:
                print()
                print("Invalid choice. Choose again. ")
                loop_state = 6.1
                continue

    else:
        print("Please input a valid choice to take action. ")
        continue