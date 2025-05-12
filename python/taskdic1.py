Kyle = {
    'name': 'Kyle Benjamin Uy',
    'age': '16',
}

Kyle['class'] = 'human'
Kyle['Location'] = ['Home', 'Out', 'Kitchen']
Kyle['tools'] = ['Apple', 'Banana', 'Pear']
Kyle['skills'] = ['shield bash', 'stealth', 'heal']

Kyle['skills'].append('Matthews')
print(Kyle['skills'][-2::])

for i in Kyle:
    print(f"{i}: {Kyle[i]}")

Kyle['skills'].pop()
print(Kyle['skills'])