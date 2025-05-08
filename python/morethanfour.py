morethan4 = []
text = "Play the Game now"
text = text.split()
for i in text:
    if len(i) >= 4:
        morethan4.append(i)
print(morethan4)