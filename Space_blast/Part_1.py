import turtle
import os
import math
import random
import winsound




#set up the screen

wn=turtle.Screen()
wn.bgcolor('black')
wn.title('Space Invaders')
wn.bgpic()
wn.tracer(0)

#Draw Border
border_pen=turtle.Turtle()
border_pen.speed(0)#speed of drawing 0 as fast
border_pen.color('white')
border_pen.penup()
border_pen.setposition(-300,-300)#by default the pen will be at the center
border_pen.pendown()
border_pen.pensize(3)


for side in range(4):
    border_pen.fd(600)
    border_pen.lt(90)
border_pen.hideturtle()

#set the score 0

score=0

#draw the score on screen
score_pen=turtle.Turtle()
score_pen.speed(0)
score_pen.color('white')
score_pen.penup()
score_pen.setposition(-290,300)
scorestring='Score: %s' %score
score_pen.write(scorestring,False,align='Left',font=('Arial',14,'normal'))
score_pen.hideturtle()


#create the player turtle
player=turtle.Turtle()
player.color('blue')
player.shape('triangle')
player.penup()
player.speed(0) #this is a method
player.setposition(0,-250)
player.setheading(90)

player.speed=15 #this is a variable



#choose the number of enemies

number_of_enemies=20

enemies=[]

for i in range(number_of_enemies):
    enemies.append(turtle.Turtle())


enemy_start_x=-200
enemy_start_y=250
enemy_number=0

#create the enemy
for enemy in enemies:
    
    enemy.color('red')
    enemy.shape('circle')
    enemy.penup()
    enemy.speed(0)
    x=enemy_start_x+(50*enemy_number)
    y=enemy_start_y
    enemy.setposition(x,y)
    enemy_number+=1
    #update the enemy bnumber
    enemy_number+=1
    if enemy_number==10:

        enemy_start_y-=50
        enemy_number=0

    enemyspeed=0.2


#creat teh players bullet
bullet=turtle.Turtle()
bullet.color('yellow')
bullet.shape('triangle')
bullet.penup()
bullet.speed(0)
bullet.setheading(90)
bullet.shapesize(0.5,0.5) #bullet doesnt want to have the same size of player
bullet.hideturtle()#when the game start the bullet need to be hidden


bulletspeed=5

#define bullet state
#ready-to fire
#fire-bullet is firing

bulletstate='ready'
     

def move_left(): #the player need to move left, that is by decreasing the speed by 15
   player.speed=-1
   



def move_right():
   player.speed=1 
   

def move_player():
    x=player.xcor()#when the game start players position is 0
    x+=player.speed
    if x<-280:
        x=-280
    if x>+280:
        x=280 
    player.setx(x)


def fire_bullet():
    #declare bulletstat as a global it it needs changed
    global bulletstate
    if bulletstate=='ready':
        winsound.PlaySound('C:/Users/subin/Desktop/laser.wav',winsound.SND_ASYNC)
        bulletstate ='fire'  #this if is to decrease the speed of bullet
        x=player.xcor()
        y=player.ycor()+10
        bullet.setposition(x,y)
        bullet.showturtle() 

def isCollison(t1,t2):
    distance=math.sqrt(math.pow(t1.xcor()-t2.xcor(),2)+math.pow(t1.ycor()-t2.ycor(),2))   
    
    if distance<15:
        
        return True

#create keyboard bindings
turtle.listen()
turtle.onkey(move_left,'Left')#when the left key is pushed call fn move leftturtle.onkey(move_right,'Right')
turtle.onkey(move_right,'Right')
turtle.onkey(fire_bullet,'space')

while True:
    wn.update()

    move_player()

    for enemy in enemies:

        #move the enemy
        x=enemy.xcor()
        x+=enemyspeed # when we start the game enemy speed is 2
        enemy.setx(x)



      #once the enemy reaches the left then the enemy has to reverse
        if enemy.xcor()>280: #initial speed of the enemy is 2 which becom -2 once it hit right boundary
           #move all enemies down
            for e in enemies:
                y=e.ycor()
                y-=40
                e.sety(y)
            #change the direction of enemy
            enemyspeed*=-1
        if enemy.xcor()<-280: #initial speed of the enemy is -2 which becom 2 once it hit right boundary
            #move all enemies down
            for e in enemies:
                y=e.ycor()
                y-=40
                e.sety(y)
            #change the direction of enemy
            enemyspeed*=-1
            #check the collsion
        if isCollison(bullet,enemy):
            #reset the bullet
            winsound.PlaySound('C:/Users/subin/Desktop/explosion.wav',winsound.SND_ASYNC)
            bullet.hideturtle()
            bulletstate='ready'
            bullet.setposition(0,-400)
            enemy.setposition(0,10000)
            #reset the enemy



            #update the score
            score+=10
            scorestring='Score: %s' %score
            score_pen.clear()
            score_pen.write(scorestring,False,align='Left',font=('Arial',14,'normal'))
        if isCollison(player,enemy):
            player.hideturtle()
            enemy.hideturtle()
            break
    #move the bullet
    if bulletstate=='fire':
        y=bullet.ycor()
        y+=bulletspeed
        bullet.sety(y)
      
    #check to see if the bullet has gone to the top
    if bullet.ycor()>275:
        bullet.hideturtle()
        bulletstate='ready'

    
        
 





