'''''
import another_module
print(another_module.a_var)
from turtle import Turtle,Screen

mike = Turtle()
mike.shape("turtle")
mike.color("green")
for i in range(4):
    mike.forward(100)
    mike.left(90)
    
myscr= Screen().exitonclick()
'''''
from prettytable import PrettyTable
table= PrettyTable()
table.add_column("POKEMON NAME",["PIKACHU","CHARMADER","SQUIRTLE"])
table.add_column("Type",["ELECTRIC","FIRE","WATER"])
table.align = "l"
print(table)
