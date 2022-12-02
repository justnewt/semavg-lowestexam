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
  choice = input('lowest or semavg: ')
  
  if choice.lower() == 'lowest':
    mp = int(input('Input your 1st MP avg: '))
    mp2 = int(input('Input your 2nd MP avg: '))
    aim = int(input('Your desired grade: '))
    req = semavg(mp, mp2, aim)
    
    if req > 100:
      print('\nYou\'re doomed')
    else: 
      print('\nMinimum exam score to get', aim, 'is', round(req))
      
  if choice.lower() == 'semavg':
    mp = int(input('Input your 1st MP avg: '))
    mp2 = int(input('Input your 2nd MP avg: '))
    exam = int(input('Your exam grade: '))
    desireg = desire(mp, mp2, exam)
    print('\nYour semester average is', round(desireg))
    
if __name__ == '__main__':
  main()
