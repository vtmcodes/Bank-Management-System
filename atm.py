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
    print("Enter 0 to exit. ")
    atm_choice = input().strip().lower()

    if atm_choice == "1":
        print()
        user_input_account = input("Enter your account number: ").strip()

        if user_input_account in blocked_accounts:
            print()
            print("Account is blocked. Contact the bank authorities to unblock this account. ")
            loop_state = 1
        elif user_input_account in accounts:
            loop_state = 1.1
            while loop_state == 1.1:
                print()
                try:
                    user_input_sum = int(input("Enter the sum you want to withdraw: "))
                except ValueError:
                    print()
                    print("Invalid input, try again. ")
                    continue
                if user_input_sum <= 0:
                    print("Inavlid sum. ")
                    continue
                elif user_input_sum > accounts[user_input_account]["Balance"]:
                        print("Insufficient funds. ")
                        loop_state = 1
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
                        if user_input_pin == accounts[user_input_account]["Pin"]:
                            print()
                            print(f"Withdrawal successfull! ")                     
                            accounts[user_input_account]["Balance"] -= user_input_sum
                            bank_data["accounts"] = accounts
                            save_data(bank_data)
                            print()
                            print(f"You have {accounts[user_input_account]["Balance"]} left in your account. ")
                            pins = True
                            loop_state = 1
                            continue
                        elif user_input_pin != accounts[user_input_account]["Pin"]:
                            print()
                            print(f"Incorrect pin.")
                            pintries -= 1
                            print()
                            print(f"You have {pintries} tries left. ")
                    if pins == False and pintries == 0:
                        blocked_accounts.append(user_input_account)
                        save_data(bank_data)
                        print()
                        print("Your account has been blocked due to too many incorrect pin attempts. ")
                        continue
        else:
            print("Account doesnt exist. ")

    elif atm_choice == "0":
        print()
        print("Stopped machine. ")
        break
    
    else:
        print()
        print("Invalid choice. Redirecting... ")
        loop_state = 1
        continue