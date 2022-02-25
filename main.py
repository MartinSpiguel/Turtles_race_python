#Import libraries
from turtle import *
import random
import time

#Define constants
WIDTH, HEIGHT = 900, 500
COLORS = ['red', 'blue', 'orange', 'yellow', 'black', 'brown', 'green', 'pink', 'purple', 'cyan']

#Ask the user haw many turtles does he want to race and reurns that number
def get_number_of_racers():
    number_of_racers = 0
    while True:
        number_of_racers = input('How many turtles do you want to race? (2-10) ')
        if number_of_racers.isdigit():
            number_of_racers = int(number_of_racers)
        else:
            print('Input is not a number, try again!')
            continue        
        if number_of_racers >= 2 and number_of_racers <= 10:
            return number_of_racers
        else:
            print('Number not in range (2-10), try again!')

#Initialize turtle module            
def init_turtle():
    screen = Screen()
    screen.setup(WIDTH, HEIGHT)
    screen.title('Turtles race')

#Chose n random colors for the racers and return them
def choose_random_colors(number_of_racers):
    random.shuffle(COLORS)
    colors = COLORS[:number_of_racers]
    return colors

#Takes all the colors picked and create all racers, one for each color. Return a list of them as Turtle objects
def create_racers(colors):
    racers = []
    for i, color in enumerate(colors):
        racer = Turtle()
        racer.color(color)
        racer.shape('turtle')
        racer.penup()
        racer.setpos(-WIDTH//2 + WIDTH//9, HEIGHT//2 - (HEIGHT//(len(colors)+1))*(i+1))
        racer.pendown()
        racers.append(racer)
    return racers

#Draw the final line
def draw_endline():
    endline = Turtle()
    endline.color('white')
    endline.right(90)
    endline.penup()
    endline.setpos(WIDTH//2 - WIDTH//9, HEIGHT//2)
    endline.color('gray')
    endline.width(5)
    endline.pendown()
    endline.setpos(WIDTH//2 - WIDTH//9, -HEIGHT//2)

#Responsable of movement (racing) and return winner Turtle object
def race(colors):
    racers = create_racers(colors)
    draw_endline()
    while True:
        for racer in racers:
            distance = random.randrange(1,20)
            racer.forward(distance)        
            x, y = racer.pos()
            if x >= WIDTH//2 - WIDTH//9:
                return racers[racers.index(racer)]

#Takes the winner and makes a small dance
def winner_dance(winner_turtle):
    winner_turtle.penup()
    winner_turtle.setpos(WIDTH//2 - WIDTH//18, 0)
    for i in range(5):
        winner_turtle.left(360)

#Ask the user if he wants to play again
def play_again():
    while True:
        play_again = input('Do you want to play again? (Y or N): ')
        if play_again == 'Y' or play_again == 'N':
            return play_again
        else:
            print('Please select a valid option (Y or N): ')

#Define main function. Responsable of puting all together. Its is the function that we call to run the program 
def main():
    number_of_racers = get_number_of_racers()
    init_turtle()
    colors = choose_random_colors(number_of_racers)
    winner_turtle = race(colors)
    print(f'The winner is the {winner_turtle} turtle')
    time.sleep(1)
    winner_dance(winner_turtle)
    new_game = play_again()
    if new_game == 'Y':
        clearscreen()
        main()
    elif new_game == 'N':
        exit()

if __name__ == '__main__':
    main()