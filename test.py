class Solution:
    def reverse(self, x: int) -> int:
        s=''
        while x>0:
            n=x
            if n<0:
                s+='-'
            n%=10
            s+=str(n)
            x//=10
        return s
    
p=Solution()
print(p.reverse(x=-123))

        
--------------------------------------

def factorial(): 
  n=int(input('Санды енгіз : ')) 
  k=n 
  x=1 
  while n>0: 
    x*=n 
    n-=1 
  print(f'{k} санының факториялы : {x}') 
  Ans = [] 
  d = 2 
  while d <= x: 
      if x % d == 0: 
        Ans.append(d) 
        x //= d 
      else: 
          d += 1 
  q=1 
  my_dict={} 
  for item in range(1000): 
    if item in Ans: 
      my_dict[item]=Ans.count(item) 
      q*=(item**(Ans.count(item)-1))*(item-1) 
  print("Жәй сандарға жіктелген : ", Ans) 
  print("Дәрежесі бойынша жіктелген : ", my_dict) 
  print("Эйлер функциясының мәні : ", q) 
def san(): 
  x=int(input('Санды енгіз : ')) 
  Ans = [] 
  d = 2 
  while d <= x: 
      if x % d == 0: 
        Ans.append(d) 
        x //= d 
      else: 
          d += 1 
  q=1 
  my_dict={} 
  for item in range(1000): 
    if item in Ans: 
      my_dict[item]=Ans.count(item) 
      q*=(item**(Ans.count(item)-1))*(item-1) 
  print("Жәй сандарға жіктелген : ", Ans) 
  print("Дәрежесі бойынша жіктелген: ", my_dict) 
  print("Эйлер функциясының мәні : ", q) 
def tanda(): 
  while True: 
    print("Эйлер функциясын табу".center(20,'-')) 
    st=input("Санның өзін табу үшін '1'-ді бас, факториалы бойынша табу үшін '2'-ні бас: ") 
    if st=='1': 
      san() 
      break 
    elif st=='2': 
      factorial() 
      break 
    else: 
      print('Қайта енгіз') 
tanda()
