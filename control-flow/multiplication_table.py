number = int(input('Enter a number to see its multiplication table:'))

for i in range(10):
  result = (i + 1) * number
  print(f'{number} * {i + 1} = {result}')