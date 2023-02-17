import statistics
nbre1 = float (input ("Entrez le premier nombre : "))
nbre2 = float (input ("Entrez le deueime nombre : "))
nbre3 = float (input ("Entrez le troisieme nombre : ") )
somme = nbre1 + nbre2 + nbre3
division = nbre1/nbre2/nbre3
soustraction = nbre1 - nbre2 - nbre3
moyenne = (nbre1 + nbre2 + nbre3)/2
ecart_type = statistics.stdev([nbre1, nbre1, nbre3])
liste = [nbre1, nbre2, nbre3]
liste.sort()
if len(liste)% 2==0:
    medianne = (liste[len(liste)//2] + liste[len(liste)//2-1])/2
else:
    medianne = liste[len(liste)//2]
print ("La somme de", nbre1, "et", nbre2, "est egale a", somme)
print ("La moyenne de", nbre1, "et", nbre2, "est egale a", moyenne)
print ("L'ecart_type de", nbre1, "et", nbre2, "est egale a", ecart_type)
print ("La medianne de", nbre1, "et", nbre2, "est egale a", medianne)
print ("La division de", nbre1, "et", nbre2, "est egale a", division)
print ("La soustraction de", nbre1, "et", nbre2, "est egale a", soustraction)

