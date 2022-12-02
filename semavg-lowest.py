def semavg(mp, mp2, aim):
  exam = 0
  semeavg = (3*(mp + mp2) + exam)/7
  while semeavg <= aim and exam <= 100:
    semeavg = (3*(mp + mp2) + exam)/7
    exam += 1
  return exam

def desire(mp, mp2, exam):
  return (3*(mp + mp2) + exam)/7

def main():
  end = ''
  choice = ''
  while True:
    while True:
      choice = input('lowest or semavg: ')
      if choice.lower() == 'lowest':
        break
      if choice.lower() == 'semavg':
        break
      else:
        print('\nPlease input valid choice (lowest/semavg)\n')
  
    if choice.lower() == 'lowest':
      mp = int(input('\nInput your 1st MP avg: '))
      mp2 = int(input('Input your 2nd MP avg: '))
      aim = int(input('Your desired grade: '))
      req = semavg(mp, mp2, aim)
      if req > 100:
        print('\nYou\'re doomed')
      else: 
        print('\nMinimum exam score to get', aim, 'is', round(req))
      
    if choice.lower() == 'semavg':
      mp = int(input('\nInput your 1st MP avg: '))
      mp2 = int(input('Input your 2nd MP avg: '))
      exam = int(input('Your exam grade: '))
      desireg = desire(mp, mp2, exam)
      print('\nYour semester average is', round(desireg))
      
    while True:
      end = input('\nWould you like to calculate again? y/n: ')
      if end.lower() == 'y':
        break
      if end.lower() == 'n':
        break
    if end == 'y':
      print()
      continue
    if end == 'n':
      break
  
if __name__ == '__main__':
  main()
