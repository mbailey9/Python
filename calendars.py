# -*- coding: utf-8 -*-

__version__ = 1

def gregorian(year):
    #using nested if statements
    if year  %  400  == 0:
        return True
    elif year % 100 == 0:
        return False
    elif year % 4 == 0:
        return True
    else:
        return False
    
def milankovic(year):
    #using nested if statements
    if year % 900 == 200 or year % 900 == 600:
        return True
    elif year % 100 == 0:
        return False
    elif year % 4 == 0:
        return True
    else:
        return False


def gregorian_count(year1, year2):
    m = 0
    for n in range(year1, year2):
        if n % 4 == 0 and (n % 100 != 0 or n % 400 == 0):
            #condesed gregorian_count
            m = m + 1
    return m
        
        
        


def milankovic_count(year1, year2):
    m2 = 0
    for n2 in range(year1, year2):
        if n2 %4 == 0 and (n2 %100 != 0 or n2 % 900 == 200 or n2 % 900 == 600):
            #condesed milkankoiv method
            m2 = m2 +1
    return m2

        
        


def main():
    
    pass
if __name__ == "__main__":
    #testing of all methods 
  print(gregorian(1696))
  print(gregorian(1697))
  print(gregorian(2100))
  print(gregorian(2800))  
  print(milankovic(1696))
  print(milankovic(1697))
  print(milankovic(2100))
  print(milankovic(2800))
  print(gregorian_count(1696,1697))
  print(gregorian_count(1900,1901))
  print(gregorian_count(2000,3000))
  print(gregorian_count(2000,2850))
  print(milankovic_count(1696,1697))
  print(milankovic_count(1900,1901))
  print(milankovic_count(2000,3000))
  print(milankovic_count(2000,2850))
main()    