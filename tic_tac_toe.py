import time


def initialize_board():
   board=["-", "-", "-",
          "-", "-", "-",
          "-", "-", "-",]
   return board

def display_board(board):
   space=[0,1,3,4,6,7]
   new_line=[2,5,8]
   for i in range(len(board)):
      print(board[i],end="")
      if( i in space):
         print("|",end="")
      else:
         print()


def check_win(board,pos):
   win=[{0,1,2},{3,4,5},{6,7,8},
        {0,3,6},{1,4,7},{2,5,8},
        {0,4,8},{2,4,6}]
   for i in win:
      if(pos==i):
         return 1
   return 0


def start_game():
   p1=input("Player 1 enter your  name ")
   print(p1,"enter your symool ",end="")
   s1=input()
   print("Player 2 enter your  name ",end="")
   p2=input()
   if(p1==p2):
      p2=input("Player 2 choose a different name please ")
   print(p2,"enter your symool ",end="")
   s2=input()
   if(s1==s2):
      print(p2,"choose a  different symool ",end="")
      s2=input()


   flag=0
   pos=[]
   po1=set()
   po2=set()
   c=0
   board=initialize_board()
   display_board(board)
   print("Following are the position numbers remember ")
   print("1 | 2 | 3\n4 | 5 | 6\n7 | 8 | 9")
   while(flag!=1):
      print(p1,"choose a position ",end="")
      po=int(input())
      if(po in pos):
         po=int(input("You can't choose already filled position, choose again "))
      po1.add(po-1)
      board[po-1]=s1
      c=check_win(board,po1)
      if(c==1):
         print("Hurray!",p1,"you won\n")
         for j in range(5):
            print("! ! ! H U R R A Y ! ! !")
            time.sleep(1)
            print("  "*(j+1),end="")
         flag=1
         continue
      pos.append(po)
      if(len(pos)==9):
         print("! ! ! T I E ! ! !")
         flag=1
         continue
      display_board(board)

      
      print(p2,"choose a position ",end="")
      po=int(input())
      if(po in pos):
         po=int(input("You can't choose already filled position, choose again "))
      po2.add(po-1)
      board[po-1]=s2
      c=check_win(board,po2)
      if(c==1):
         print("Hurray!",p2,"you won\n")
         for j in range(5):
            print("! ! ! H U R R A Y ! ! !")
            time.sleep(1)
            print("  "*(j+1),end="")
         flag=1
         continue      
      pos.append(po)
      if(len(pos)==9):
         
         print("! ! ! T I E ! ! !")
         flag=1
         continue
      display_board(board)


   ip=input("Do you wants to play Yes/No ")
   if(ip=="Yes" or ip=="yes"):
      start_game()


start_game()
