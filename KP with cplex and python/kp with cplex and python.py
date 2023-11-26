from docplex.mp.model import Model#pour les insytuctions cplex
import numpy as np
import csv

#=====================================================================

with open("Résultat.csv", "w") as f_write: # créer et ouvrir le fichier Resultat.csv
    writer = csv.writer(f_write, delimiter=";")# spécifier le délimiteur des colonnes
    writer.writerow( ["instance","objectif","temps(s)"] )#écrire les noms des colonnes dans Resultat.csv
    liste=open("all.txt", "r")# ouvrir la liste des instances
    nb_inst = liste.readline()# lire le nombre des instances à résoudre
    print("nb_inst=", int(nb_inst))#affichage du nombre des instances à résoudre pour vérification
    for j in range(int(nb_inst)): #boucle pour lire et résoudre les instances une par une
       inst = liste.readline()#lire le nom de l'instance j à résoudre
       #pour toutes les ligne dans all.txt, le nom de l'instance est sauvgardé dans la chaine inst suivit 
       #du caractère de fin de ligne \n sauf pour la dernière ligne d'ou il faut enlever ce \n
       if j < int(nb_inst): #vérifier si ce n'est pas la dernière ligne dans all.txt
           inst=inst[:-1]#prebdre toute la chaine sauf le dernier caractère (le \n)
       print('Nom instance : ', inst)
       with open(inst) as f: #ouvrir l'instance lue
           N = int(f.readline())# lire le nombre d'objet et le sauvgarder dans la bvariable N
           print("N = ", N)
           b = int(f.readline())# lire la capacité du sac et la sauvgarder dans la bvariable b
           V = {}#déclaration d'un tableau pour les volumes des objets
           P = {}#déclaration d'un tableau pour les profitss des objets
           for i in range(N):
               P[i], V[i] = [int(x) for x in next(f).split()]#remplir les tableau P et V
                                                             # La méthode split() divise une chaîne en une liste
           print('V = ', V)
           #print('P = ', P)
           print()
       
       
       
       
       
       # *********************insérer votre code ici*****************
       
       
       
       
       
       #print('optimization is done. Objectif = %.2f'objective_value) #affichage valeur de solution
       #print('temps(s) = %.3f' % time) #affichage du temps d'exécution
      
      # writer.writerow( [inst,int(objective_value),round(time,3)] )#ecrire le nom de linstance, l'objectif et le temps de résolution dans resultat.csv
       print("=========================================================")
       
    liste.close()# fermer le fichier liste des instances
#results.close()


