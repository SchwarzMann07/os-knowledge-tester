print("Welcome to the OS Knowledge tester")
print("OS stands for Operating System")
print()

counter = 0
score = 0
total_num_of_qn = 3


counter +=1
tracker = 0

while tracker !=1:
  
  print("Q"+str(counter)+") "+ "What OS do most people have on their computers?")
  print("   a) Linux")
  print("   b) macOS")
  print("   c) Windows")
  print("   d) DeXOS")
  answer = input("Your answer: ")
  answer = answer.lower()
  if answer == "a":
    output = "Wrong. Try again"
    score -=1
  elif answer == "b":
    output = "Wrong. Try again"
    score -=1
  elif answer == "c":
    output = "Yes, that's right!"
    tracker =1
    score +=1
  elif answer == "d":
    output = "Wrong. Try again"
    score -=1
  else:
    output = "Please choose a, b, c or d only."
  
  print()
  print(output)
  print()
  print("Your current score: " + str(round((score/total_num_of_qn*100),1)) + "%"  )
  print()
  print()
  


counter +=1
tracker = 0

while tracker !=1:
  
  print("Q"+str(counter)+") "+ "Which OS is found everywhere?")
  print("   a) Linux")
  print("   b) macOS")
  print("   c) Windows")
  print("   d) DeXOS")
  answer = input("Your answer: ")
  answer = answer.lower()
  if answer == "a":
    output = "Yes, that's right!"
    tracker =1
    score +=1
  elif answer == "b":
    output = "Wrong. Try again"
    score -=1
  elif answer == "c":
    output = "Wrong. Try again"
    score -=1
    
  elif answer == "d":
    output = "Wrong. Try again"
    score -=1
  else:
    output = "Please choose a, b, c or d only."

  print()
  print(output)
  print()
  print("Your current score: " + str(round((score/total_num_of_qn*100),1)) + "%"  )
  print()
  print()
  
  

counter +=1
tracker = 0

while tracker !=1:
  
  print("Q"+str(counter)+") "+ "Which is the least used OS from the following?")
  print("   a) Linux")
  print("   b) macOS")
  print("   c) Windows")
  print("   d) DeXOS")
  answer = input("Your answer: ")
  answer = answer.lower()
  if answer == "a":
    output = "Wrong. Try again"
    score -=1
  elif answer == "b":
    output = "Wrong. Try again"
    score -=1
  elif answer == "c":
    output = "Wrong. Try again"
    score -=1
    
  elif answer == "d":
    output = "Yes, that's right!"
    tracker =1
    score +=1
  else:
    output = "Please choose a, b, c or d only."

  

  print()
  print(output.lower())
  print()
  print("Your current score: " + str(round((score/total_num_of_qn*100),1)) + "%"  )
  print()
  print()
  
print("End of quiz, hope you learnt something and had fun!")
  
