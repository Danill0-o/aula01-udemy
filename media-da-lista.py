# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆
alturas = 0

for i in range(len(student_heights)):
        alturas += student_heights[i]

avg = alturas/len(student_heights)

print(round(avg))