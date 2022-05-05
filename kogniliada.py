import pygame

def draw_text(text_display, xval, yval):
    text = font.render(text_display, True, black, white)
    textRect = text.get_rect()
    textRect.midleft = (xval, yval)
    display_surface.blit(text, textRect)

dataset = [["wzokowa", '60', "korowa", '25', "słuchowa", '15'],
["kanapka", '60', "pizza", '30', "zapiekanka", '5', "kebs", '5'],
["pralka", '50', "lodówka", '25', "zmywarka", '20', "kuchenka", '5']]

answers = [[0 for j in range(len(i)) if j%2] for i in dataset]

pygame.init()
white = (255, 255, 255)
black = (0, 0, 0)
X = 600
Y = 600
display_surface = pygame.display.set_mode((X, Y))
pygame.display.set_caption('Kogniliada')
font = pygame.font.Font('freesansbold.ttf', 32)
question = 0
n_points = [0,0]
mistake = 0
team = 0
start=True

while True:
    n_answers = int(len(dataset[question])/2)
    display_surface.fill(white)
    y_val = 50

    for i in range(6-n_answers):
        y_val +=40
        draw_text(" ", 120, y_val)

    for i in range(0, 2*n_answers, 2):
        y_val += 40
        if answers[question][int(i/2)]==1:
            draw_text(str(int(i/2)+1)+". "+dataset[question][i], 100, y_val)
            draw_text(dataset[question][i+1], X-150, y_val)
        elif answers[question][int(i/2)]==0:
            draw_text("."*20, 100, y_val)
            draw_text(str(0), X-150, y_val)
        print(str(int(i/2)+1)+". "+dataset[question][i])

    draw_text(str(n_points[0]), 100, Y-100)
    draw_text(str(n_points[1]), X-150, Y-100)

    if team==1:
        if mistake >= 1: draw_text("X", 50, Y/5)
        if mistake >= 2: draw_text("X", 50, 2*Y/5)
        if mistake == 3: draw_text("X", 50, 3*Y/5)

    elif team==2:
        if mistake >= 1: draw_text("X", X-50, Y/5)
        if mistake >= 2: draw_text("X", X-50, 2*Y/5)
        if mistake == 3: draw_text("X", X-50, 3*Y/5)

    pygame.display.update()
    for event in pygame.event.get(): pass

    if sum(answers[question])==n_answers and not start or mistake==3:
        input("Czy mogę wyswietlić następne pytanie?")
        team=int(input("Która grupa odpowiada? 1 lub 2 "))
        question +=1
        mistake = 0
    elif not start:
        user_answer = int(input("0. niepoprawna odpowiedź\nJaką podano odpowiedź "))
        if user_answer>0:
            n_points[team-1]+=int(dataset[question][(user_answer-1)*2+1])
            answers[question][user_answer-1]=1
        elif user_answer==0:
            mistake+=1
        print(answers)
    elif start:
        team=int(input("Która grupa odpowiada? 1 lub 2 "))
        start=False

    if question==3:
        break
