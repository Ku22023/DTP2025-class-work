codes = ["level", "power", "deed", "fight", "meme", "run"]
for i in codes:
    if i[::-1] != i:
        codes.remove(i)
print(codes)