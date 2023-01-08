student_scores = input("Input a list of student scores ").split() #Recebe uma relação de numero sem vírgulas. Ex: 123 234 124
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])#pega cada item da lista, transforma em int e atribui à lista
print(student_scores)

#loop para pegar o maior valor da lista e imprimir
nota = 0
for i in range(len(student_scores)):
    if student_scores[i] > nota:
        nota = student_scores[i]
print("The highest score in the class is: ",nota)