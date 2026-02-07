products = ['heels', 'shirts', 'handbags', 'laptop', 'facewash']
search = input("Enter the item:")

if search in products:
    print(f'{search} is found!\nGo and shop now!!!')
else:
    print(f"{search} not found!\nLook for other things")
