print("This program will convert ripple to USD.")

print("As of 1/23/2020 at 2:40 PM, ripple (XRP) is currently trading at $0.22 per ripple.")
rippleAmount = eval(input("Enter the ripple amount: "))

convertToDollars = rippleAmount * 0.22

print("That amount of ripple is worth ${0:.2f} USD".format(convertToDollars))