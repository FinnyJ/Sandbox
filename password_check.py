def main():
    password = input("What is your password: ")

    if len(password) <= 4:
        print("Your password is too short, try again")
        main()
    else:
        stars = len(password) * "*"
        print(stars)
main()