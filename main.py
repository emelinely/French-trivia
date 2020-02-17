import random
import time

# list of questions in french and english, their possible answers, and their correct answers, all divided into categories
questions = [[["Question 1: Quelle est la traduction de \"turnip\"?", "1. navet", "2. radis", "3. tournoi", "Translation: What is the translation of turnip?", "1"], 
              ["Question 1: Quelle est la traduction de \"potato\"?", "1. pomme", "2. pomme de terre", "3. potate", "Translation: What is the translation of potato?", "2"], 
              ["Question 1: Quelle est la traduction de \"beet\"?", "1. bateau", "2. béton", "3. betterave", "Translation: What is the translation of beet?", "3"]],
             [["Question 2: Quelle est la traduction de \"bat\" (l'animal)?", "1. chauve-souris", "2. hiboux", "3. batte", "Translation: What is the translation of bat (the animal)?", "1"], 
              ["Question 2: Quelle est la traduction de \"raccoon\"?", "1. raton laveur", "2. bléreau", "3. racoune", "Translation: What is the translation of raccoon?", "1"], 
              ["Question 2: Quelle est la traduction de \"wolf\"?", "1. loup-garou", "2. grand chien", "3. loup", "Translation: What is the translation of wolf?", "3"]],
             [["Question 3: Quelle est la traduction de \"platypus\"", "1. ornythorynque", "2. platypus", "3. assiette", "Translation: What is the translation of platypus?", "1"], 
              ["Question 3: Quelle est la traduction de \"jellyfish\"", "1. poisson", "2. méduse", "3. poisson-gelée", "Translation: What is the translation of jellyfish?", "2"], 
              ["Question 3: Quelle est la traduction de \"seahorse\"", "1. hippopotame", "2. cheval de mer", "3. hippocampe", "Translation: What is the translation of seahorse?", "3"]],
             [["Question 4: Quelle est la conjugation correcte d'avoir au futur simple? (no translation will be given)", "1. j'aurai", "2. nous aurions", "3. vous ayez", "", "1"], 
              ["Question 4: Quelle est la conjugation correcte de savoir au futur simple? (no translation will be given)", "1. vous saurez", "2. tu savoiras", "3. il savait", "", "1"], 
              ["Question 4: Quelle est la conjugation correcte de faire au futur simple? (no translation will be given)", "1. nous faisions", "2. il ferait", "3. ils feront", "", "3"]],
             [["Question 5: Quelle est la conjugation correcte de être au subjonctif présent? (no translation will be given)", "1. tu serais", "2. je sois", "3. il fut", "", "2"], 
              ["Question 5: Quelle est la conjugation correcte de savoir au subjonctif présent? (no translation will be given)", "1. ils savent", "2. ils sachent", "3. tu sauras", "", "2"], 
              ["Question 5: Quelle est la conjugation correcte de aller au subjonctif présent? (no translation will be given)", "1. tu ailles", "2. vous irez", "3. il allait", "", "1"]],
             [["Question 6: Quelle est la conjugation correcte de peindre au passé simple? (no translation will be given)", "1. tu peignas", "2. nous peignons", "3. je peignis", "", "3"], 
              ["Question 6: Quelle est la conjugation correcte de vivre au passé simple? (no translation will be given)", "1. il vivait", "2. je vécus", "3. j'ai vécu", "", "2"], 
              ["Question 6: Quelle est la conjugation correcte de faire au passé simple? (no translation will be given)", "1. nous fîmes", "2. il fut", "3. je faisais", "", "1"]],
             [["Question 7: Pour offrir un cadeau à leur prof de Maths, les élèves d’une classe ont collecté soixante-quatorze € en pièces de un € et de deux €, \
soit quarante-trois pièces en tout. \nCalculer le nombre de pièces de chaque sorte. (try not to use the translation)", \
             "1. 12 de 1€, 31 de 2€", "2. 30 de 1€ et 13 de 2€", "3. 10 de 1€ et 33 de 2€", \
             "To buy a present for their math teacher, the students collected 74€ in coins of 1€ and 2€, for a total of 43 coins. \nCalculate the number of each type of coin. ", "1"]], 
             [["Question 8: Thomas a obtenu onze et seize aux deux premiers contrôles de Maths. \nQuelle note doit-il avoir au troisième contrôle pour obtenir quinze de moyenne ? \n \
(try not to use the translation)", "1. 17", "2. 18", "3. 15", "Thomas got an 11 and a 16 on the 2 first math tests. \n \
What grade must he get on the third test to have an average grade of 15.", "2"]],
             [["Question 9: Si on augmente de cinq m un côté d’un carré et si on diminue de trois m l’autre côté, on obtient un rectangle de même aire que celle du carré. \n \
Combien mesure le côté de ce carré ? (try not to use the translation)", \
              "1. 6.5 m", "2. 6 m", "3. 7.5 m", "If you increase one side of a square by 5 meters, and decrease the other by 3 meters, \n \
you get a rectangle with the same area as the square. What was the length of one of the square's sides?", "3"]], 
             [["Question 10: Le capitaine a cinquante-trois ans de moins que son bateau. \nIl y a quatre ans il avait la moitié de l'âge du bateau à l'époque. \n \
Quel est l'âge du capitaine ? (try not to use the translation)", "1. 60", "2. 49", "3. 57", \
             "The captain is 53 years younger than his boat. \nFour years ago, he was half the age of the boat at that time. \nWhat is the captain's age?", "3"]]]

# base variables
group = 0
points = 0

# function to print questions and possible answers
def question(questions, group, a):
  print(questions[group][a][0])
  print(questions[group][a][1])
  print(questions[group][a][2])
  print(questions[group][a][3])

# function to print questions in english with possible answers
def translated(questions, group, a):
  print(questions[group][a][4])
  print(questions[group][a][1])
  print(questions[group][a][2])
  print(questions[group][a][3])

# prints title and description, then waits 
print("French Quiz")
print("This is a french quiz with 10 increasingly hard questions. All the questions and answers will be in french, \n\
but a translation of the questions is available if needed. There are 3 general sections: translation, conjugation, and comprehension/ basic math. \n")
time.sleep(2)

# asks as many questions as there are, randomizing when there are multiple question options, and receives answers to check if they are correct, false, or if asking for a translation
for i in range(len(questions)):
  a = random.randint(0, len(questions[group]) - 1)
  question(questions, group, a)
  ans = input("Please enter the number of your answer (if you would like to see the question in english enter 4): ")
  if ans == questions[group][a][5]:
    print("correct \n")
    points += 1
  elif ans == "4":
    print(' ')
    translated(questions, group, a)
    ans = input("Please enter the number of your answer: ")
    if ans == questions[group][a][5]:   
      print('correct \n')
      points += 1
    else:
      print("false \n")
  else:
    print("false \n")  
  group +=1

# prints score in over ten and percentage formats
print("your score was: {}/10".format(points))
percentage = points*10
print("in percentage form that is: {}%".format(percentage))
