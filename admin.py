from beatm import load_data, save_data

bank_data = load_data()

if bank_data is None:
    exit()

balance = bank_data["balance"]
code = bank_data["code"]
blocked_accounts = bank_data["blocked_accounts"]

while True:
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

    if auth_choice == "1":
        print()
        print("Enter the account number. ")
        oneauthchoice = input()
        acc_str = str(oneauthchoice)

        if acc_str not in balance:
            print("Account doesnt exist! Try again. ")
            continue

        else:
            print()
            print("Enter the sum of money to add to user account. ")
            print()
            add_account_sum = int(input())
            balance[acc_str] += add_account_sum
            bank_data["balance"] = balance
            save_data(bank_data)
            print()
            print(f"Successfully added {add_account_sum} to account number {acc_str}. ")
            print(f"New account balance is {balance[acc_str]}.")
            continue

    elif auth_choice == "2":
        print()
        print("Enter user account. ")
        oneauthchoice2 = input()
        acc_str2 = str(oneauthchoice2)

        if acc_str2 not in blocked_accounts:
            print()
            print("Account isnt blocked! ")
            continue

        else:
            print()
            blocked_accounts.remove(acc_str2)
            save_data(bank_data)
            print(f"Successfully unblocked account number {acc_str2}.")
            continue

    elif auth_choice == "3":
        print()
        print("Enter user account number. ")
        new_user_account = input()

        try:
            intnua = int(new_user_account)
        except ValueError:
            print("Please enter a valid number.")
            continue

        if new_user_account in balance:
            print()
            print("Account number already exists. Try again. ")
            continue
        elif intnua <= 1000:
            print()
            print("Enter a valid account number greater than 1000. ")
            continue
        else:
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
                continue
            else:
                print()
                print("Try again. They dont match. ")
                continue

    elif auth_choice == "4":
        print()
        print("Enter the account to change the password of. ")
        changepassacc = input()
        if changepassacc not in balance:
            print()
            print("Account does not exist. Try again. ")
            continue
        else: 
            print()
            print("Enter new pin for user. ")
            newpinuser = input()
            intnpu = int(newpinuser)
            if intnpu > 9999 or intnpu <= 1000:
                print()
                print("Invalid code. Code must be of 4 digits. ")
                continue
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
                    continue

    elif auth_choice == "5":
        print()
        print("Enter user account needed to block. ")
        need_block_acc = input()
        if need_block_acc in blocked_accounts:
            print()
            print("Account is already blocked. ")
            continue
        elif need_block_acc not in balance:
            print()
            print("Account does not exist. ")
            continue
        else:
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
                continue
            elif intbav == 2:
                print()
                print("Restarting program... ")
                continue
            else:
                print()
                print("Invalid choice. Try again. ")
                continue

    elif auth_choice == "6":
        print()
        print("You are trying to perform a very risky task. Proceed? ")
        print("Enter 1 if yes ")
        print("Enter 2 if no ")
        del_acc_choice = input()
        intdac = int(del_acc_choice)
        if intdac == 1:
            print()
            print("Enter user account do start account deletion process. ")
            del_acc_user = input()
            if del_acc_user in balance:
                print()
                print("Is this the correct account for deletion? ")
                print(f"Selected account: {del_acc_user}")
                print("Enter 1 if yes ")
                print("Enter 2 if no ")
                del_acc_verification = input()
                intdav = int(del_acc_verification)
                if intdav == 1:
                    print()
                    del balance[del_acc_user]
                    bank_data["balance"] = balance
                    save_data(bank_data)
                    print(f"Successfully deleted account number {del_acc_user}")
                    continue
                elif intdav == 2:
                    print()
                    print("Redirecting... ")
                    continue
                else:
                    print()
                    print("Invalid choice. Try again.")
                    continue

        elif intdac == 2:
            print()
            print("Restarting program... ")
            continue
        else:
            print()
            print("Invalid choice. Restarting... ")
            continue

    else:
        print("Please input a valid choice. ")
        continue