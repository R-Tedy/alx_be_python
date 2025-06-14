pattern_size = int(input('Enter the size of the pattern:'))
count = 0

while count <= pattern_size:
  for i in range(pattern_size):
    print("*", end="") 
  print('\n')
  count += 1