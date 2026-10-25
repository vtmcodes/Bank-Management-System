from beatm import load_data, save_data

bank_data = load_data()

if bank_data is None:
    exit()

accounts = bank_data["accounts"]
blocked_accounts = bank_data["blocked_accounts"]

loop_state = 1

while loop_state == 1:
    print()
    print("Do you want to continue or quit using the ATM machine? ")
    print("Enter 1 to continue. ")
    print("Enter any other number to exit. ")
    atm_choice = input().strip().lower()

    if atm_choice == "1":
        print()
        try:
            user_input_account = int(input("Enter your account number: "))
        except ValueError:
            print()
            print("Dont use letters. Try again. ")
            continue

        acc_str = str(user_input_account)

        if acc_str in blocked_accounts:
            print()
            print("Account is blocked. Contact the bank authorities to unblock this account. ")
            loop_state = 1
        elif acc_str in accounts:
            print()
            try:
                user_input_sum = int(input("Enter the sum you want to withdraw: "))
            except ValueError:
                print()
                print("Dont use letters, try again. ")
                continue
            if user_input_sum <= 0:
                print("Inavlid sum. ")
                loop_state = 1
            elif user_input_sum > accounts[acc_str]["Balance"]:
                print("Insufficient funds. ")
                loop_state = 1
            else:
                pintries = 3
                pins = False
                while pintries > 0:
                    print()
                    try:
                        user_input_pin = input("Enter your pin: ")
                    except ValueError:
                        print()
                        print("Dont use letters, try again. ")
                        continue
                    if user_input_pin == accounts[acc_str]["Pin"]:
                        print()
                        print(f"Withdrawal successfull! ")                     
                        accounts[acc_str]["Balance"] -= user_input_sum
                        bank_data["accounts"] = accounts
                        save_data(bank_data)
                        print()
                        print(f"You have {accounts[acc_str]["Balance"]} left in your account. ")
                        pins = True
                        break
                    elif user_input_pin != accounts[acc_str]["Pin"]:
                        print()
                        print(f"Incorrect pin.")
                        pintries -= 1
                        print()
                        print(f"You have {pintries} tries left. ")
                if pins == False and pintries == 0:
                    blocked_accounts.append(acc_str)
                    save_data(bank_data)
                    print()
                    print("Your account has been blocked due to too many incorrect pin attempts. ")
                    continue
        else:
            print("Account doesnt exist. ")
    
    else:
        exit