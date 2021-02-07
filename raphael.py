a= 5 # c'est un integer int
b= "bonjour, raphael" # c'est string str

print("affiche moi b :"+ b) # affiche moi ma variable b(ce qu'elle contient)

#addition
c= 8
d=a+c
print(f"résultat : {d}")


def add():
    a = input("premier nombre :  ")
    b = input("second nombre :  ")
    c = int(a)+int(b)
    print(f"MAITRE VOTRE RESULTAT EST :  {c}")


#add()

def multi():
    a = input("premier nombre :  ")
    b = input("second nombre :  ")
    c = int(a)*int(b)
    print(f"MAITRE VOTRE RESULTAT EST :  {c}")

#multi()

def sous():
    a = input("premier nombre :  ")
    b = input("second nombre :  ")
    c = int(a)-int(b)
    print(f"MAITRE VOTRE RESULTAT EST :  {c}")

sous()

def autorisation():
    a=input("quel est ton age espece de .......    >")

    if int(a) >= 18:
        print("tu es majeur excuse moi pour le cloporte ")
    
    else:
        print("trop petit minus")

autorisation()
