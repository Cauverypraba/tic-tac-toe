def display_board(board):
  print('---------')
  print('|'+board[7]+'|',board[8]+'|',board[9]+'|')
  print('---------')
  print('|'+board[4]+'|',board[5]+'|',board[6]+'|')
  print('---------')
  print('|'+board[1]+'|',board[2]+'|',board[3]+'|')
  print('---------')
valuesin_board=[' ']*10
##print(display_board(valuesin_board))
def player_input():
  letter=''
  while letter!='X' and letter!='O':
  #while True: 
    print('Player1,Choose a letter X or O')
    letter=input().upper()
    player1=letter
  if player1=='X':
    player2='O'
  else:
    player2='X'
  print("Player 1: ",player1)
  print("Player 2: ",player2)
##print(player_input())
def choose_position(board,letter,position):
   board[position]=letter
##print(choose_position(valuesin_board,'X',8))
##print(display_board(valuesin_board))
def check_win(board,letter):
  return((board[7]==board[8]==board[9]==letter)or
         (board[4]==board[5]==board[6]==letter)or
         (board[1]==board[2]==board[3]==letter)or
         (board[7]==board[4]==board[1]==letter)or
         (board[8]==board[5]==board[2]==letter)or
         (board[9]==board[6]==board[3]==letter)or
         (board[7]==board[5]==board[3]==letter)or
         (board[9]==board[5]==board[1]==letter))
##print(check_win(valuesin_board,'X'))
##print(display_board(valuesin_board))
import random
def choose_first():
   player=random.randint(0,1)
   if player==0:
     return 'Player 1'
   else:
     return 'Player 2'
##print(choose_first())
def check_space(board,position):
   return board[position]==' '
##print(check_space(valuesin_board,2))
#checks if board is full or not
def full_board_check(board):
     for i in range(0,10):
        if check_space(valuesin_board,i):
           return False
     return True
##print(full_board_check(valuesin_board))
def player_choice(board):
   position=0
   while position not in [1,2,3,4,5,6,7,8,9] or not check_space(board,position):
       position=int(input('Choose a position (1-9): '))
   return position
##print(player_choice(valuesin_board))
#play again or not
def replay():
  response=input('Do you want to play again? say Yes or No: ')
  return response=='Yes'
##print(replay())
print('WELCOME TO TIC TAC TOE GAME!!')
while True:
   player1_letter,player2_letter=player_input()
   turn=choose_first()
   print(turn +'will go first')
   play_game=input('Ready to play? say yes or no: ')
   if play_game=='yes':
     game_on=Ready
   else:
     game_on=Notready
   while game_on:
      if turn=='Player 1':
         print(display_board(valuesin_board))
         position=player_choice(valuesin_board)
         choose_position(valuesin_board,player1_letter,position)
         if check_win(valuesin_board,player1_letter):
            display_board(valuesin_board)
            print('Player 1 has won!!')
            game_on=False
         else:
             if full_board_check(valuesin_board):
              print(display_board(valuesin_board))
              print("TIE GAME!")
              game_on=False
             else:
              turn='Player 2'
      else:
         print(display_board(valuesin_board))
         position=player_choice(valuesin_board)
         choose_position(valuesin_board,player2_letter,position)
         if check_win(valuesin_board,player2_letter):
            print(display_board(valuesin_board))
            print('Player 2 has won!!')
            game_on=False
         else:
             if full_board_check(valuesin_board):
               print(display_board(valuesin_board))
               print("TIE GAME!")
               game_on=False
             else:
               turn='Player 1'
   if not replay():
      break
