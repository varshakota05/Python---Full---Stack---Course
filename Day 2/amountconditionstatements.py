amount = int(input("Enter the amount:"))

if amount > 50000:
    print("Go for Investments")
elif amount > 20000:
    print("Go for a trip")
elif amount > 10000:
    print("Go for Clubbings")
elif amount > 5000:
    print("Go for a Cafe/Res")
elif amount > 1000:
    print("Go for shopping!")
elif amount > 500:
    print("Go for a movie!")
elif amount > 100:
    print("Go for sub like Hotstar")
elif 20 < amount <99:
    print("Go for street food")
else:
    print("Better go to sleep!!!")
