grades = []
scores = [95, 67, 83, 38, 59]
for i in scores:
    if i >= 80:
        grades.append("A")
    elif i >= 60 and i <=79:
        grades.append("B")
    elif i >= 40 and i <= 59:
        grades.append("C")
    else:
        grades.append("D")
print(grades)