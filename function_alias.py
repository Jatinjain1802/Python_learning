'''
Function Aliasing:- assising one fucntion refrene to the another varibael
name . here we are provind a new name to an exisiting function
'''
def eat(food):
    print("eating process",food)

consume=eat
digest=consume
consume("sad")
eat("happy")
digest("tryy")
