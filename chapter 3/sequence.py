# story="once upon\n a\t time\\ "
# print(story)

letter = ''' Dear <|name|>,
you are selected!
Date: <|date|>
'''
name= input("Enter your name\n")
date= input("Enter your date\n")
letter=(letter.replace("<|name|>",name))
print(letter.replace("<|date|>",date))
