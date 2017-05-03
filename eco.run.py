"""
Axis and Allies Economy
-Pierce de Jong
-this program keeps track of the bank and income of each nation
-It also allows the player to buy units on each nations turn and keeps track of the purchase
"""

import pygame
import time
import pickle

from pygame.locals import *


#Open a new file or override and continue a game
newGame = str(input("\nWould you like to start a (n)ew game or (c)ontinue an old one: "))
if newGame == "n":
    gameVersion = str(input("Enter a save slot to override: "))
    readFile = open("newGamePG.txt", "r")
if newGame == "c":
    gameVersion = str(input("Enter save slot to open: "))
    readFile = open("continueGamePG_"+gameVersion+".txt", "r")

pygame.init()

#This is the music for when one side has the victory objectives
nazi = pygame.mixer.Sound("nazi.wav")
ussr = pygame.mixer.Sound("ussr.wav")
japan = pygame.mixer.Sound("japan.wav")
britain = pygame.mixer.Sound("britain.wav")
italy = pygame.mixer.Sound("italy.wav")
america = pygame.mixer.Sound("america.wav")
victory_song = [nazi,ussr,japan,america,britain,italy]
#pygame.mixer.music.load("")
#pygame.mixer.music.play(-1) #repeats forever
#pygame.mixier.music.stop()

display_width = int(pygame.display.Info().current_w)
display_height = int((pygame.display.Info().current_h*0.9))
red = (255,0,0)
orange = (255,128,0)
yellow = (255,255,0)
green = (0,255,0)
blue = (0,0,255)
purple = (127,0,255)
pink = (255,0,127)
grey = (128,128,128)
black = (10,10,10)
white = (255,255,255)
brown = (139,69,19)
beige = (253,213,183)

light_red = (255,102,102)
light_orange = (255,178,102)
light_yellow = (255,255,102)
light_green = (102,255,102)
light_blue = (102,102,255)
light_purple = (178,102,255)
light_pink = (255,102,178)
light_grey = (192,198,198)
light_black = (90,90,90)
light_brown = (205,133,63)
light_beige = (255,235,205)


dark_red = (153,0,0)
dark_blue = (0,0,153)
dark_grey = (64,64,64)
light_cyan = (155,205,205)
darkish_grey = (100,100,100)

CHANGE_INCOME_COLOR = grey #Color for button to change the bank and income buttons
button_color_1 = yellow #Color 1 for Unit Buy
button_color_2 = black #Color 2 for Unit buy
capitol_count_color = white #Color of the text on the Capitol buttons
button_text_color = red #Color for reset buy and next turn
button_income_font_color = black #Color for bank,income and capitol color text
BACKGROUND_COLOR = dark_grey #Background Color
SELECT = light_cyan #Color for when a mouse hovers over a button

axis_color = red #Color for AXIS Capitols and Victory
allies_color = blue #Color for ALLIES Capitols and Victory

NATION_COLOR = [black,brown,orange,green,purple,beige,pink,darkish_grey,blue] #List of Colors for Nations text at the top of the screen
NATION_COLOR_NATION = [white,brown,orange,green,purple,beige,pink,grey,blue] #Colors for the bank and income
NATION_LIGHT_COLOR = [light_black,light_brown,light_orange,light_green,light_purple,light_beige,light_pink,light_grey,light_blue] #Other colors for bank and income

gameDisplay = pygame.display.set_mode((display_width,display_height))
gameDisplay.fill(BACKGROUND_COLOR)
pygame.display.set_caption("Triple Dank | Save: " + gameVersion)
pygame.display.update()
clock = pygame.time.Clock()

Y_MOVEMENT = display_height/22 #Sets the distance betrween each

BUTTON_SIZE = Y_MOVEMENT
FONT_SIZE = int(Y_MOVEMENT*1.25)
BUTTON_FONT_SIZE = int(FONT_SIZE*.75)

def text_objects(text,font,color):
    text_surface = font.render(text,True,color)
    return text_surface, text_surface.get_rect()

def message_display_center(text,x,y,color,size):
    font = pygame.font.Font(None, size)
    TextSurf, TextRect= text_objects(text, font, color)
    TextRect.center = (x,y)
    gameDisplay.blit(TextSurf, TextRect)
    pygame.display.update()
    return TextRect

def message_display_right(text,x,y,color,size):
    font = pygame.font.SysFont(None, size)
    TextSurfValue = text_objects(text, font, color)
    TextSurf = TextSurfValue[0]
    TextRect= (x,y)
    gameDisplay.blit(TextSurf, TextRect)
    pygame.display.update()
    return TextRect, TextSurfValue[1]

#Function to display Nations name, and original bank and income
#Returns the x placment of all nations to be re drawn
def nation_bank_first_run(text,y,color,size,bank,income,nation,count): #Draws Nations and their bank values to screen
    x = 10
    new_x_values=[]
    while nation < count:
        display_text = text[nation]+str(bank[nation])+"|"+str(income[nation])
        value = message_display_right(display_text,x,y/2,color[nation],size)
        new_x_values.append(x)
        x = x + value[1][2]+20
        nation = nation + 1
    pygame.display.update()
    return new_x_values

#Function to display Nations NAME, NEW BANK AND INCOME
def nation_bank(text,x,y,color,size,bank,income,nation,count,): #Draws Nations and their bank values to screen

    if nation == NATION_TOTAL-1: #For out of bounds
        gameDisplay.fill(BACKGROUND_COLOR, rect = [x[nation]-x[0],y/2,display_width-x[nation],size])
    else:
        gameDisplay.fill(BACKGROUND_COLOR, rect = [x[nation]-x[0],y/2,x[nation+1]-x[nation],size])
    while nation < count:
        display_text = text[nation]+str(bank[nation])+"|"+str(income[nation])
        value = message_display_right(display_text,x[nation]-x[0],y/2,color[nation],size)
        nation = nation + 1
    pygame.display.update()

#Function to end one nations turn and go to the next and check if there is a winner
#Adds the income to the bank and keeps track of Turn number
def button_next_turn(text,x,y,a,b,color,new_color,text_color,font_size,bank,income,nation,axis_v,allies_v,vic,vic_income,turn):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    click_yes = 0
    if x+a > mouse[0] > x and y+b > mouse[1] > y:
        pygame.draw.rect(gameDisplay, new_color,(x,y,a,b))
        if click[0] == 1: #If button is pressed
            bank = bank + income
            print("N_Bank:   " + str(bank))
            print("N_Income: " + str(income))
            print(text)
            print("")
            nation = nation + 1
            if nation == NATION_TOTAL: #When reaces last nation goes back to orginol
                turn = turn + 1
                print("Axis Victory Cities:   " +str(vic))
                print("Allies Victory Cities: " + str(CAPITOL_TOTAL - vic))
                nation = 0
                vic_income_max = max(vic_income)
                vic_income_max_index = vic_income.index(vic_income_max)
                pygame.mixer.stop()
                if vic >= axis_v: #If Axis have enough victory cities after last nation has played for round, plays music of nation with largest income
                    print("\nAXIS WIN")
                    message_display_center("AXIS WIN",display_width/3*2,display_height/2,axis_color,int(FONT_SIZE*3))
                    nation = NATION_TOTAL-1
                    if vic_income_max_index == 0:
                        pygame.mixer.Sound.play(victory_song[0])
                    elif vic_income_max_index == 2:
                        pygame.mixer.Sound.play(victory_song[2])
                    elif vic_income_max_index == 6:
                        pygame.mixer.Sound.play(victory_song[5])
                if vic <= allies_v: #If Allies have enough victory cities after last nation has played for round, plays music of nation with largest income
                    print("\nALLIES WIN")
                    message_display_center("ALLIES WIN",display_width/3*2,display_height/2,allies_color,int(FONT_SIZE*3))
                    nation = NATION_TOTAL-1
                    if vic_income_max_index == 1:
                        pygame.mixer.Sound.play(victory_song[1])
                    elif vic_income_max_index == 3:
                        pygame.mixer.Sound.play(victory_song[3])
                    elif vic_income_max_index == 5:
                        pygame.mixer.Sound.play(victory_song[4])

            click_yes = 1
            pygame.time.wait(50)
    else:
        pygame.draw.rect(gameDisplay, color,(x,y,a,b))

    message_display_center(text,int(x+a/2),int(y+b/2),text_color,font_size)
    pygame.display.update()
    return bank, nation, click_yes, turn

#Function used to print out a button and retrun 1 if it is pressed
def button(text,x,y,a,b,color,new_color,text_color,font_size):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    click_yes = 0
    if x+a > mouse[0] > x and y+b > mouse[1] > y:
        pygame.draw.rect(gameDisplay, new_color,(x,y,a,b))
        if click[0] == 1: #left click
            click_yes = 1
        if click[2] == 1: #right click
            click_yes = 2
        pygame.time.wait(50)
    else:
        pygame.draw.rect(gameDisplay, color,(x,y,a,b))

    message_display_center(text,int(x+a/2),int(y+b/2),text_color,font_size)
    pygame.display.update()
    return click_yes

#Function to print the Stats of each unit when program starts
def unit_stat(x,y,msg,color_1,color_2,font):
    loop = 0
    value = [0,0,0,0]
    while loop < 17:
        if loop % 2 == 0: #Changes the color of the text everytime it cahnges line to make it more clear
            color = color_2
        else:
            color = color_1
        value_new = message_display_right(str(msg[loop]), x, y*(loop+2.5), color, font)
        loop = loop + 1
        if value_new[1][2] > value[2]:
            value = value_new[1]
    return value

#Function to keep track of the unit buy count when a unit is purchased
def unit_count_print(x,y,msg,color_1,color_2,font):
    gameDisplay.fill(BACKGROUND_COLOR,rect = [x,y*3.5,font/2,y*15])
    loop = 0
    while loop < 15:
        if loop % 2 == 0:
            color = color_1
        else:
            color = color_2
        value = message_display_right(str(msg[loop]), x, y*(loop+3.5), color, font)
        loop = loop + 1
    pygame.display.update()
    return value[1]

#Function to draw the buttons to buy units and remove money from the bank of nation
def buy_unit(text,x,y,a,b,color_1,color_2,new_color,text_color,font_size,count,cost,nation,bank):
    loop = 0
    while loop < 15:
        if loop % 2 == 0:
            color = color_1
        else:
            color = color_2
        value = button(text[loop],x,y*(loop+3.5),a,b,color,new_color,text_color,font_size)
        if value == 1:
            bank = bank - cost[loop]
            count[loop] = count[loop] + 1
        loop = loop + 1
    return count, bank

#Function to print out 6 buttons to change income or bank of a specific nation
def income_bank_edit(text,x,y,a,b,color_1,color_2,new_color,text_color,font_size):
    loop = 0
    value_2 = [0,0,0,0,0,0]
    while loop < 6:
        if loop % 2 == 0: #Chnage the button color between light and normal for every button
            color = color_1
        else:
            color = color_2
        value = button(text[int(loop)],x,y*(loop+3)*2,a,b,color,new_color,text_color,font_size)
        value_2[loop] = value
        loop = loop + 1
    return value_2

#function to draw bar at bottom of screen with nations turn and round number
def draw_turn_color(text,x,y,a,b,color,text_color,font_size):
    if color == (253,213,183) or color == (255,235,205):
        text_color = grey
    gameDisplay.fill(color, rect = [x,y,a,b])
    message_display_center(text,(x+a)/2,y+font_size/2,text_color,font_size)

#Function to draw the capitols and keep track of how many each team owns
def capitol_count(x,y,a,b,axis_count,change,total,font_size):
    loop = total
    count = change
    text_color = black
    while count < loop:
        text_color = black
        if count <= axis_count:
            color = light_red
        else:
            color = light_blue

        if count == allied_victory:
            text_color = blue
        #    gameDisplay.fill(text_color, rect = [x,y-b,a,b])
        if count == axis_victory:
            text_color = red
        #    gameDisplay.fill(text_color, rect = [x,y-b,a,b])
        gameDisplay.fill(color, rect = [x,y,a,b])
        message_display_center(str(count+1),x+a/2,y+b/2,text_color,font_size)
        x = x + a
        count = count + 1


def main_loop(readFile):

    #This opens up a text document to read the saved files for either a new game or continues one
    lines = readFile.readlines()
    nat_name = lines[0].replace("[","").replace("]","").replace("'","").replace(","," ").replace("\"","")
    bank_new = lines[1].replace("[","").replace("]","").replace("'","").replace(","," ").replace("\"","")
    income_new = lines[2].replace("[","").replace("]","").replace("'","").replace(","," ").replace("\"","")
    nat_name = nat_name.split()
    NATION_NAME_1 = list(map(str,nat_name))
    global NATION_NAME
    NATION_NAME = [x + " " for x in NATION_NAME_1] #adds a space after nation names on the screen

    #Sets the dynamic variables to text document info
    bank = bank_new.split()
    bank = list(map(int,bank))
    bank_old = bank_new.split()
    bank_old = list(map(int,bank_old))
    income = income_new.split()
    income = list(map(int,income))

    readFile.close()

    global NATION_TOTAL
    global X_MOVEMENT
    global NATION_FONT_SIZE
    NATION_TOTAL = len(NATION_NAME)
    X_MOVEMENT= int(display_width/(NATION_TOTAL+1))
    NATION_MOVEMENT = int(display_width/(NATION_TOTAL+2))
    NATION_FONT_SIZE = int(X_MOVEMENT/4)

    loop = 0
    nation = 0
    count = NATION_TOTAL
    global CAPITOL_TOTAL
    CAPITOL_TOTAL = 22

    axis_capitols = int(lines[4])
    global allied_victory
    global axis_victory
    allied_victory = 5
    axis_victory = 16
    turn = int(lines[5]) #Keeps track of turn from save file
    click = 0
    first_run = True

    #This while loop adds a space to the front of each natikon until they are the smae length
#    longest_name = len(max(NATION_NAME, key = len))
#    while loop < NATION_TOTAL:
#        while len(NATION_NAME[loop]) < longest_name:
#            NATION_NAME[loop] = " " + NATION_NAME[loop]
#        print(NATION_NAME[loop])
#        loop = loop + 1
    loop = 0

    #Displays Originol Nations properites from file before anychanges can be made
    nation_x_values = nation_bank_first_run(NATION_NAME,Y_MOVEMENT,NATION_COLOR,NATION_FONT_SIZE,bank,income,nation,count) #

    unit_name = ["","infantry","artillery","mobile infantry","tank","anti-tank","anti-aircarft","fighter","tactical bomber","bomber","submarine","destroyer","transport","cruiser","aircraft-carrier","battleship",""]
    unit_attack = ["A",1,2,1,3,2,0,3,3,4,2,2,0,3,0,4,"A"]
    unit_defense = ["D",2,2,2,3,3,1,4,3,1,1,2,0,3,2,4,"D"]
    unit_movement = ["M",1,1,2,2,1,1,4,5,6,2,2,2,2,2,2,"M"]
    unit_count = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    unit_cost = [3,4,4,6,6,5,10,11,12,8,8,8,12,16,20]
    unit_cost_string = ["3","4","4","6","6","5","10","11","12","8","8","8","12","16","20"]
    income_nation = 0
    unit_cost_string_2 = ["C","3","4","4","6","6","5","10","11","12","8","8","8","12","16","20","C"]
    income_edit = [1,5,10,-1,-5,-10]
    income_edit_string = ["1","5","10","-1","-5","-10"]


    #Displays the Stats of each unit
    stat_x = BUTTON_SIZE*2
    stat_x_count_unit = BUTTON_SIZE*2
    stat = unit_count_print(stat_x_count_unit,Y_MOVEMENT,unit_count,button_color_1,button_color_2,FONT_SIZE)

    stat_x = stat_x + stat[2] + 20
    stat = unit_stat(stat_x,Y_MOVEMENT,unit_name,button_color_1,button_color_2,FONT_SIZE)
    stat_x = stat_x + stat[2]+ 20
    stat = unit_stat(stat_x,Y_MOVEMENT,unit_attack,button_color_1,button_color_2,FONT_SIZE)
    stat_x = stat_x + stat[2]+ 20
    stat = unit_stat(stat_x,Y_MOVEMENT,unit_defense,button_color_1,button_color_2,FONT_SIZE)
    stat_x = stat_x + stat[2]+ 20
    stat = unit_stat(stat_x,Y_MOVEMENT,unit_movement,button_color_1,button_color_2,FONT_SIZE)
    stat_x = stat_x + stat[2]+ 20
    unit_stat(stat_x,Y_MOVEMENT,unit_cost_string_2,button_color_1,button_color_2,FONT_SIZE)

    #Displays text above change income and bank buttons
    message_display_right("Bank",display_width-BUTTON_SIZE*5,Y_MOVEMENT*5,button_text_color,int(BUTTON_FONT_SIZE))
    message_display_right("Income", display_width-BUTTON_FONT_SIZE*2-20,Y_MOVEMENT*5, button_text_color,int(BUTTON_FONT_SIZE))

    #Displays the capitols and who owns them
    capitol_count(display_width-CAPITOL_TOTAL*BUTTON_SIZE,display_height-Y_MOVEMENT*3,BUTTON_SIZE,BUTTON_SIZE,axis_capitols,0,CAPITOL_TOTAL,BUTTON_FONT_SIZE)


    nation = int(lines[3])
    draw_turn_color(NATION_NAME[nation]+"| "+str(turn),X_MOVEMENT*1.5,display_height-Y_MOVEMENT*2,display_width-X_MOVEMENT*3,Y_MOVEMENT*2,NATION_COLOR[nation],white,int(FONT_SIZE*1.5))

    print("Nation:   " + str(nation) + " | " + str(NATION_NAME[nation]))
    print("Bank:     " + str(bank[nation]))
    print("Income:   " + str(income[nation]))

    yes = False
    while not yes:

        #Closeing the program loop and saves info to a text document
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                openFile = open("continueGamePG_"+gameVersion+".txt","w")
                openFile.write(str(NATION_NAME))
                openFile.write("\n")
                openFile.write(str(bank))
                openFile.write("\n")
                openFile.write(str(income))
                openFile.write("\n")
                openFile.write(str(nation))
                openFile.write("\n")
                openFile.write(str(axis_capitols))
                openFile.write("\n")
                openFile.write(str(turn))
                openFile.close
                yes = True

        unit_buy = buy_unit(unit_cost_string,5,Y_MOVEMENT,BUTTON_SIZE,BUTTON_SIZE,button_color_1,button_color_2,SELECT,button_text_color,BUTTON_FONT_SIZE,list(unit_count),unit_cost,nation,bank[nation])
        if unit_buy[0] != unit_count: #Updates unit count when button is presed
            unit_count = list(unit_buy[0])
            bank[nation] = unit_buy[1]
            unit_count_print(stat_x_count_unit,Y_MOVEMENT,unit_count,button_color_1,button_color_2,FONT_SIZE)
            nation_bank(NATION_NAME,nation_x_values,Y_MOVEMENT,NATION_COLOR,NATION_FONT_SIZE,bank,income,nation,nation+1)

        reset_unit_count = button("Reset Buy",0,display_height-Y_MOVEMENT*2,X_MOVEMENT*1.5,Y_MOVEMENT*2,red,SELECT,black,FONT_SIZE)
        if reset_unit_count == 1: #Reset the unit_count and bank for nation
            unit_count = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
            unit_count_print(stat_x_count_unit,Y_MOVEMENT,unit_count,button_color_1,button_color_2,FONT_SIZE)
            nation_bank(NATION_NAME,nation_x_values,Y_MOVEMENT,NATION_COLOR,NATION_FONT_SIZE,bank,income,nation,nation+1)
            bank = list(bank_old)

        axis_change_button = button("+",display_width- CAPITOL_TOTAL*BUTTON_SIZE/2,display_height-Y_MOVEMENT*4,BUTTON_SIZE,BUTTON_SIZE,axis_color,SELECT,button_income_font_color,BUTTON_FONT_SIZE*2)
        if axis_change_button == 1:
            axis_capitols = axis_capitols + 1
            if axis_capitols == axis_victory:
                print(axis_capitols)
                gameDisplay.fill(red, rect = [display_width-CAPITOL_TOTAL*BUTTON_SIZE+axis_capitols*BUTTON_SIZE,display_height-Y_MOVEMENT*3,BUTTON_SIZE,BUTTON_SIZE])
                message_display_center(str(axis_capitols+1),display_width-CAPITOL_TOTAL*BUTTON_SIZE+axis_capitols*BUTTON_SIZE+BUTTON_SIZE/2,display_height-Y_MOVEMENT*3+BUTTON_SIZE/2,white,BUTTON_FONT_SIZE)
            else:
                gameDisplay.fill(light_red, rect = [display_width-CAPITOL_TOTAL*BUTTON_SIZE+axis_capitols*BUTTON_SIZE,display_height-Y_MOVEMENT*3,BUTTON_SIZE,BUTTON_SIZE])
                message_display_center(str(axis_capitols+1),display_width-CAPITOL_TOTAL*BUTTON_SIZE+axis_capitols*BUTTON_SIZE+BUTTON_SIZE/2,display_height-Y_MOVEMENT*3+BUTTON_SIZE/2,black,BUTTON_FONT_SIZE)




        allies_change_button = button("-",display_width- CAPITOL_TOTAL*BUTTON_SIZE/2-BUTTON_SIZE,display_height-Y_MOVEMENT*4,BUTTON_SIZE,BUTTON_SIZE,allies_color,SELECT,button_income_font_color,BUTTON_FONT_SIZE*2)
        if allies_change_button == 1:
            if axis_capitols == allied_victory:
                gameDisplay.fill(blue, rect = [display_width-CAPITOL_TOTAL*BUTTON_SIZE+axis_capitols*BUTTON_SIZE,display_height-Y_MOVEMENT*3,BUTTON_SIZE,BUTTON_SIZE])
                message_display_center(str(axis_capitols+1),display_width-CAPITOL_TOTAL*BUTTON_SIZE+axis_capitols*BUTTON_SIZE+BUTTON_SIZE/2,display_height-Y_MOVEMENT*3+BUTTON_SIZE/2,white,BUTTON_FONT_SIZE)
            else:
                gameDisplay.fill(light_blue, rect = [display_width-CAPITOL_TOTAL*BUTTON_SIZE+axis_capitols*BUTTON_SIZE,display_height-Y_MOVEMENT*3,BUTTON_SIZE,BUTTON_SIZE])
                message_display_center(str(axis_capitols+1),display_width-CAPITOL_TOTAL*BUTTON_SIZE+axis_capitols*BUTTON_SIZE+BUTTON_SIZE/2,display_height-Y_MOVEMENT*3+BUTTON_SIZE/2,black,BUTTON_FONT_SIZE)
            axis_capitols = axis_capitols - 1

        change_bank_income_nation = button(NATION_NAME[income_nation]+str(bank[income_nation])+"|"+str(income[income_nation]),display_width-BUTTON_SIZE*5,Y_MOVEMENT*4,BUTTON_SIZE*5,BUTTON_SIZE,CHANGE_INCOME_COLOR,SELECT,NATION_COLOR[income_nation],BUTTON_FONT_SIZE)
        if change_bank_income_nation == 1: #Change Nation for income/bank buttons forward
            income_nation = income_nation + 1
            if income_nation == NATION_TOTAL:
                income_nation = 0
        if change_bank_income_nation == 2: #Change Nation for income/bank buttons backwards
            income_nation = income_nation -1
            if income_nation == -1:
                income_nation == NATION_TOTAL-1

        loop = 0
        change_income = income_bank_edit(income_edit_string,display_width-BUTTON_SIZE*2,Y_MOVEMENT,BUTTON_SIZE*2,BUTTON_SIZE*2,NATION_LIGHT_COLOR[income_nation],NATION_COLOR_NATION[income_nation],SELECT,button_income_font_color,BUTTON_FONT_SIZE)
        while loop <len(income_edit): #creates the income buttons to change each nations income manually
            if change_income[loop] == 1:
                income[income_nation] = income[income_nation] + income_edit[loop]
                nation_bank(NATION_NAME,nation_x_values,Y_MOVEMENT,NATION_COLOR,NATION_FONT_SIZE,bank,income,income_nation,income_nation+1)
            loop = loop + 1
        loop = 0

        change_bank = income_bank_edit(income_edit_string,display_width-BUTTON_SIZE*5,Y_MOVEMENT,BUTTON_SIZE*2,BUTTON_SIZE*2,NATION_COLOR_NATION[income_nation],NATION_LIGHT_COLOR[income_nation],SELECT,button_income_font_color,BUTTON_FONT_SIZE)
        while loop <len(income_edit): #creates the bank buttons to change each banks manually. eg for bombing.
            if change_bank[loop] == 1:
                bank[income_nation] = bank[income_nation] + income_edit[loop]
                nation_bank(NATION_NAME,nation_x_values,Y_MOVEMENT,NATION_COLOR,NATION_FONT_SIZE,bank,income,income_nation,income_nation+1)
            loop = loop + 1
        loop = 0

        next_button = button_next_turn("End Turn",display_width-X_MOVEMENT*1.5,display_height-Y_MOVEMENT*2,X_MOVEMENT*1.5,Y_MOVEMENT*2,red,SELECT,black,FONT_SIZE,bank[nation],income[nation],nation,axis_victory,allied_victory,axis_capitols,income,turn)
        bank[nation] = next_button[0]
        if next_button[2] == 1: #Updates Bank of nation and reses unit_count
            nation_bank(NATION_NAME,nation_x_values,Y_MOVEMENT,NATION_COLOR,NATION_FONT_SIZE,bank,income,nation,nation+1)
            nation = next_button[1]
            print("Nation:   " + str(nation) + " | " + str(NATION_NAME[nation]))
            print("Bank:     " + str(bank[nation]))
            print("Income:   " + str(income[nation]))
            turn = next_button[3]
            bank_old = list(bank)
            unit_count = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0] #resewts unit count for new nation
            unit_count_print(stat_x_count_unit,Y_MOVEMENT,unit_count,button_color_1,button_color_2,FONT_SIZE)
            draw_turn_color(NATION_NAME[nation]+"| "+str(turn),X_MOVEMENT*1.5,display_height-Y_MOVEMENT*2,display_width-X_MOVEMENT*3,Y_MOVEMENT*2,NATION_COLOR[nation],white,int(FONT_SIZE*1.5))
        nation = next_button[1]
        pygame.display.update()
        clock.tick(4)

main_loop(readFile)

pygame.quit()
quit()
