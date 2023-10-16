#Programme qui demande l’âge d’un enfant à l’utilisateur et il l’informe de sa catégorie 
a=int(input("Entrer l'age de l'enfant : "))
if(a>=6 and a<=7):
    print("Poussin")
elif(a>=8 and a<=9):
    print("Popille")
elif(a>=10 and a<=11):
    print("Minime")
elif(a>=12):
    print("Cadet")
else:
    print("Error")