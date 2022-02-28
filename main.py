print('''
 __________________
    .-'  \ _.-''-._ /  '-.
  .-/\   .'.      .'.   /\-.
 _'/  \.'   '.  .'   './  \'_
:======:======::======:======:  
 '. '.  \     ''     /  .' .'
   '. .  \   :  :   /  . .'
     '.'  \  '  '  /  '.'
       ':  \:    :/  :'
         '. \    / .'
           '.\  /.'    miK
             '\/'
''')
print("Welcome to Diamond Quest.")
print("Your mission is to find the Diamond.") 

#https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload

#Write your code below this line 👇
step1 = input ('You\'re at a cross road. Where do you want to go? Type "left" or "right" \n').lower()
if step1 == "left":
   step2 = input ('You\'ve reached a taxi stop. What do you do? Type "walk" or "taxi" \n') .lower()
   if step2 == "walk":
     step3 = input ('You\'re next to the caves. What cave do you want to go? Type "left" or "right" or "middle" \n').lower()
     if step3 == "middle":
         print("Congratulations!. You found the diamond")
     elif step3 == "right":
       print ("You entered a cave full snakes. Game Over")
     elif step3 == "left":
       print("You entered a cave with a bear. Game Over")
   else:
    print("You lost. Game Over")
else:
  print("You got too far from the diamond. Game Over")
