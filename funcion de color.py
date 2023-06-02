from termcolor import colored
def printSort(lista, a,b):
    for i in lista:
        if(i==a):
            print(colored(i,"green"),end=",")
        elif( i== b):
            print(colored(i,"red"), end=",")
        else:
            print(i, end=",")
    print("\n")