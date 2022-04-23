something = input('write something with cucumber: ')
if 'cucumber' in something:
    something.index('cucumber')
    print(something[something.index('cucumber'):])
elif 'Cucumber' in something:
    something.index('Cucumber')
    print(something[something.index('Cucumber'):])
else:
    print('agh, no \'cucumber\' here, please try again')
