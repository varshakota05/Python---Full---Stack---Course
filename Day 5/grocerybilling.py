data = {
    1:{'Product' : 'Rice', 'Price' :60},
    2:{'Product' : 'Wheat Flour', 'Price' : 40},
    3:{'Product' : 'Sugar', 'Price' : 80},
    4:{'Product' : 'Milk', 'Price' : 25},
    5:{'Product' : 'Eggs', 'Price' : 70},
    6:{'Product' : 'Cooking Oil', 'Price' : 130},
    7:{'Product' : 'Tea Powder', 'Price' : 90},
    8:{'Product' : 'Salt', 'Price' : 20},
    9:{'Product' : 'Bread', 'Price' : 30},
    10:{'Product' : 'Soap', 'Price' : 25},
}

print('Index'. ljust(7), 'Product Name'.ljust(20), 'Price')
for i in data:
    print(str(i).ljust(7), data[i]['Product'].ljust(20), str(data[i]['Price']).ljust(10))
indexes = list(map(int, input("Enter the indexes:").split()))

print("Bill".center(30,'-'))
total_bill = 0
s = set()
for i in indexes:
    if i not in s:
       qty = indexes.count(i)
       cost = data[i]['Price']*qty
       print(f"{data[i]['Product']}\t{data[i]['Price']}*{qty} = {cost}")
       total_bill += cost
       s.add(i)
print(f"Your Bill: {total_bill}")
    
    
