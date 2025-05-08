James = {
    'name': 'James Matthew Banham',
    'age': '16',
}

James['class'] = 'human'
James['tools'] = ['Apple', 'Banana', 'Pear']
James['skills'] = ['shield bash', 'stealth', 'heal']

James['skills'].append('Matthews')
print(James['skills'])

for i in James:
    print(f"{i}: {James[i]}")

James['skills'].pop
print(James['skills'])