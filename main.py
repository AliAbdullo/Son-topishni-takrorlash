import random as r
def sontop(x=10):
  taxminiyson= r.randint(1, x)
  print(f"1 dan {x} gach son o'yladim! Topa olasizmi? Taxminingiz: ")
  taxminlar=0
  while True:
    taxminlar+=1
    taxmin=int(input(f">>>"))
    if taxminiyson>taxmin:
      print (f"Bundan kattaroq")
    elif taxminiyson<taxmin:
       print (f"Bundan kichikroq")
    else:
      break
  print(f"Siz '{taxminlar}'taxmin bilan topdingiz!")    
  return taxminlar


def sontopPc(x=10):
  input(f"1 dan {x} gacha son o'ylang men topaman! OK")
  quyi = 1
  yuqori = x
  taxminlar=0

  while True:
    taxminlar+=1
    taxmin = r.randint(quyi,yuqori)
    javob=input(f"Siz  {taxmin} ni o'yladingiz! " 
                f"To'g'rimi (t), Katta bo'lsa(-), Kichik bo'lsa(+)".lower())
    if javob == '-':
      yuqori=taxmin-1
    elif javob == '+':
      quyi= taxmin+1
    else:
      break
  print(f"Men {taxminlar} ta taxmin bilan topdim!") 
  return taxminlar
    
    
def play(x=10):
 
  while True:
    userplay= sontop(x)
    pcplay= sontopPc(x)
    if userplay > pcplay:
      print("\nMen yutdim!")
    elif userplay<pcplay:
      print("\nSiz yutdingiz!")
    else:
      print('Durrang')
    savol = int(input(f"Yana o'ynaysizmi Ha(1)\Yo'q(0)"))
    if savol ==1:
      True
    else:
      break
  
  