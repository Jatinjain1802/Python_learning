'''
concatenation -> joining/adding two or more string in a single
continuous using + opreatore btw the stirng

Note: we can only concatenate string with another string only
syntx:
newstring=str1+str2+str3

String Formating it is the process of inserting variables or values in to a sting
template in a mroe readable manner without using + opreator
Advantages:-
1) No use of + operatore
2) Automaticaly type caste to string
3) expresion can be used inside the place holder
'''

country_name="Spain"
result="won"
sport="Volleyball"
opponent="Argenttina"

print(country_name+" "+result+" the "+sport+" Game "+" against "+opponent)
# tow many usage of + operatore
print("--------uncomment the code for this ----------")

player_name=input("enter the player name") # Messi
goals=int(input("enter the goals scored by the player")) #8
height=float(input("enter the player height ")) #5.6
country=eval(input("Is he form argentina"))#True

# Messi who is a True Argentinian player has scored 8 goal and height is 5.6
print(player_name+" who is a "+str(country)+" Argentinian Player has scored "+str(goals)+" and height is "+str(height))
print("-------String Formating-----------")
print(f"{player_name} who is a {country} Argentinian Player has scored {goals} and height is {height}")
name="Cheetah"
speed=78
weight=24.5
print(f"{name} weight {weight} kg and runs at {speed} mph")
print("-------Using format Method-----------")
print("{} weight {} kg and runs at {} mph".format(name,weight,speed))
