from beatm import load_data, save_data

bank_data = load_data()

if bank_data is None:
    exit()

balance = bank_data["balance"]
code = bank_data["code"]
blocked_accounts = bank_data["blocked_accounts"]

while True:
    print()
    atm_choice = input("Do you want to turn off the power or keep using the ATM? Type 'continue' to continue, and 'quit' to power off. ").strip().lower()

    if atm_choice == "continue":
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
            continue
        if acc_str in balance:
            print()
            try:
                user_input_sum = int(input("Enter the sum you want to withdraw: "))
            except ValueError:
                print()
                print("Dont use letters, try again. ")
                continue
            if user_input_sum <= 0:
                print("Inavlid sum. ")
                continue
            elif user_input_sum > balance[acc_str]:
                print("Insufficient funds. ")
                continue
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
                    if user_input_pin == code[acc_str]:
                        print()
                        print(f"Withdrawal successfull! ")                     
                        balance[acc_str] -= user_input_sum
                        bank_data["balance"] = balance
                        save_data(bank_data)
                        print()
                        print(f"You have {balance[acc_str]} left in your account. ")
                        pins = True
                        break
                    elif user_input_pin != code[acc_str]:
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
        break