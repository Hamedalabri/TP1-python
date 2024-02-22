from voiture import voiture


if __name__ == "__main__":
 mycar1 = voiture("BMW","M5","5","noir")
 print(f"voiture{mycar1}")
 mycar2 = voiture(None,None,None,None)
 mycar3 = voiture("honda","python",5,None)
 mycar4 = voiture(None,None,None,"noir")
 #partie 2 print(f"voiture{mycar1__couleur}")
 #print(f"voiture : {mycar1.get_marque()} \n marque de voiture 2: {mycar2.get_marque()}")

 print(mycar1)


 mycar1.ajouter_option("climatisation")
 mycar1.supprimer_option("climatisation")
 print(mycar1) 

#print(dir()) 
