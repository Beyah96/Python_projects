def turn_right():
    turn_left()    
    turn_left()    
    turn_left()

def move_and_turn_right_twice() :
    move()
    turn_right()
    move()
    turn_right()    
    
def move_and_turn_left() :
    move()
    turn_left()
   
def jump():
    move_and_turn_left()
    move_and_turn_right_twice()
    move_and_turn_left()
    
for i in range(1, 7) :    
    jump()

################################################################
# WARNING: Do not change this comment.
# Library Code is below.
################################################################
