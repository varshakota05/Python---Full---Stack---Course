data = {
    'ram' : {'status' : True, 'python' : 100, 'python' : 100, 'mysql' : 99, 'softskills' : 82},
    'rekha' : {'status' : False, 'python' : 33, 'mysql' : None, 'softskills' : 76},
    'riya' : {'status' : True, 'python' : 56, 'mysql' : 78, 'softskills' : 42},
    'sara' : {'status' : True, 'python' : 67, 'mysql' : 87, 'softskills' : 89},
    'hanu' : {'status' : False, 'python' : 45, 'mysql' : 68, 'softskills' : 72}
}

user = input("Enter the student name:").strip().lower()

if user in data:
    if data[user]['status']:
      sum = data[user]['python']+data[user]['mysql']+data[user]['softskills']
      avg = sum/3
      if avg > 80:
          print(f"Congrats {user}!!!\nYou got 'A' grade")
      elif avg > 60:
          print(f"Better luck {user}!!\nYou got 'B' grade")
      elif avg > 40:
          print(f"Need Improvementt {user}!\nYou got 'C' grade")
      else:
          print(f"{user}, failed in the exam.\nBring your parents")

    else:
        print(f"{user} didn't write any exams.")

else:
    print(f"{user} not found")
    
    


    
