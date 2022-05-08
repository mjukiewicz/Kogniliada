import pygame
from os import system

def draw_text(text_display, xval, yval):
    text = font.render(text_display, True, yellow, black)
    textRect = text.get_rect()
    textRect.midleft = (xval, yval)
    display_surface.blit(text, textRect)

def check_if_correct_char(team):
    while True:
        if team.isdigit():
            if team in ['1','2']:
                team = int(team)
                break
        team = input("Niepoprawna wartość ")
    return team

def check_if_correct_val(user_answer):
    while True:
        if user_answer.isdigit():
            if n_answers >= int(user_answer) >= 0:
                user_answer = int(user_answer)
                break
        else:
            user_answer = input("Niepoprawna wartość ")
    return user_answer

def select_display():
    try: val = int(input("Na którym ekranie ma zostać wyświetlona kogniliada? "))
    except ValueError: return 1
    else: return val

dataset = [["wzokowa", '60', "korowa", '25', "słuchowa", '15'],
["kanapka", '60', "pizza", '30', "zapiekanka", '5', "kebs", '5'],
["pralka", '50', "lodówka", '25', "zmywarka", '20', "kuchenka", '4', "mikrofalówka", '1']]

answers = [[0 for j in range(len(i)) if j%2] for i in dataset]

pygame.init()
black = (0, 0, 0)
yellow = (255, 255, 0)
display_surface = pygame.display.set_mode((0, 0), pygame.FULLSCREEN, display=select_display())
X, Y = pygame.display.get_surface().get_size()
pygame.display.set_caption('Kogniliada')
font = pygame.font.Font('freesansbold.ttf', 80)
question = 0
n_points = [0, 0]
mistake = 0
team = 0
start = True
next = False
points = 0

while True:
    system('cls')
    n_answers = int(len(dataset[question]) / 2)
    display_surface.fill(black)
    y_val = 50

    for i in range(6-n_answers):
        y_val += 90
        draw_text(" ", 120, y_val)

    for i in range(0, 2*n_answers, 2):
        y_val += 90
        if answers[question][int(i / 2)] == 1:
            draw_text(str(int(i/2)+1)+". "+dataset[question][i], 200, y_val)
            draw_text(dataset[question][i+1], X-200, y_val)
        elif answers[question][int(i / 2)] == 0:
            draw_text("."*60, 200, y_val)
            draw_text(str(0), X-200, y_val)
        if not start and not next:
            print(str(int(i / 2)+1)+". "+dataset[question][i])

    draw_text(str(n_points[0]), 50, Y-100)
    draw_text(str(n_points[1]), X-200, Y-100)
    draw_text(str(points), X / 2, 100)

    if team==1:
        if mistake >= 1: draw_text("X", 100, Y / 5)
        if mistake >= 2: draw_text("X", 100, 2 * Y / 5)
        if mistake == 3: draw_text("X", 100, 3 * Y / 5)

    elif team==2:
        if mistake >= 1: draw_text("X", X-100, Y / 5)
        if mistake >= 2: draw_text("X", X-100, 2 * Y / 5)
        if mistake == 3: draw_text("X", X-100, 3 * Y / 5)

    pygame.display.update()
    for event in pygame.event.get(): pass

    if next:
        team = input("Która grupa odpowiada? 1 lub 2 ")
        team = check_if_correct_char(team)
        next = False

    elif mistake == 3:
        user_answer = input("Jaką odpowiedź podali przeciwnicy? ")
        user_answer = check_if_correct_val(user_answer)
        if user_answer > 0 and answers[question][user_answer - 1] == 0:
            team = abs(3 - team)
            points += int(dataset[question][(user_answer - 1) * 2 + 1])
            answers[question][user_answer - 1] = 1
        mistake = 0
        next = True

    elif sum(answers[question]) == n_answers and not start or next:
        next = False
        n_points[team-1] += points
        points = 0
        input("Czy mogę wyswietlić następne pytanie?")
        question += 1
        mistake = 0
        next = True

    elif not start:
        user_answer = input("0. niepoprawna odpowiedź\nJaką podano odpowiedź ")
        user_answer = check_if_correct_val(user_answer)
        if user_answer > 0 and answers[question][user_answer - 1] == 0:
            points +=int(dataset[question][(user_answer - 1) * 2 + 1])
            answers[question][user_answer - 1] = 1
        elif user_answer == 0:
            mistake += 1

    elif start:
        team = input("Która grupa odpowiada? 1 lub 2 ")
        team = check_if_correct_char(team)
        start = False

    if question == 3: break
