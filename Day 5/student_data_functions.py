def student_data(info):
    print(f'Name: {info[0]}')
    print(f'Course: {info[1]}')
    print(f'Gra_Year: {info[2]}')
    print('------End------')

data =[['Varsha', 'PFS', '2026'],
       ['Saaketh', 'JFS', '2025'],
       ['Dileep', 'DA', '2026'],
       ['Sirisha', 'DS', '2025'],
      ]

for i in data:
    student_data(i)
