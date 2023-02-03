import random
#la computadora elegira aleatoriamente

options = ('piedra', 'papel', 'tijera')

computer_wins = 0
user_wins = 0

rounds = 1

while True:

  print('*' * 10)
  print('ROUND', rounds)
  print('*' * 10)

  print('el contador del pc va en ', computer_wins)
  print('el contador del user va en ', user_wins)
  
  user = input('piedra, papel o tijera: ')
  user_option = user.lower()

  #contador de rounds
  rounds += 1
  
  #si user options no esta dentro de las opciones preestablecidas
  if not user_option in options:
    print('esa opcion no es valida')
    continue
  
  #seleccionar aleatoriamente basado en una tupla
  computer_option = random.choice(options)
  
  print('User option => ', user_option)
  print('Computer option => ', computer_option)
  
  if user_option == computer_option:
    print('empate!')
    
  
  elif user_option == 'piedra':
    if computer_option == 'tijera':
      print('piedra le gana a tijera')
      print('user gano')
      user_wins += 1
    else:
      print('papel gana a piedra')
      print('computadora gano!')
      computer_wins += 1
      
  elif user_option == 'papel':
    if computer_option == 'piedra':
      print('papel gana a piedra')
      print('Usuario gano')
      user_wins += 1
    else:
      print('tijera ganan a papel')
      print('computador gano')
      computer_wins += 1
      
  elif user_option == 'tijera':
    if computer_option == 'papel':
      print('tijera gana a papel!!!')
      print('usuario gano!')
      user_wins += 1
    else:
      print('piedra gana a tijera ')
      print('computador gano!')
      computer_wins += 1

  if computer_wins == 2:
    print('se rompe el ciclo gana pc!!!!!!!!')
    break
  
  if user_wins == 2:
    print("se rompe el ciclo gana user !!!!!!!!!!!!")
    break

  
  
      
