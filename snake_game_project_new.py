import random
import time
import turtle 
import winsound
import sqlite3

# Initial game settings
delay = 0.1
score = 0
highest_score = 0

s = turtle.Screen()      # 768 and 648 px isthe actual resolution of screen, user panel screen  
s1 = turtle.Screen()
# Snake bodies
bodies = []
# Set up the screen
s.title("Brainy snake Game")

# turtle for text written
my_turtle1 = turtle.Turtle()
game_ov = turtle.Turtle()

# List of colors to cycle through
colors = ["#FF3333", "#009999", "lightcoral", 'blue','yellow', 'black', 'white',  '#4C9900', "#66FFB2"]
colors1 = ["#006633","#000066", "#606060" ]
colors2 = ["#990000", "#660066", "#FF8000"]
current_color_index = 0

# list of themes to cycle through
theme = ['snakeproject.gif', 'snakeproject1.png', 'snakeproject2.png', 'snakeproject3.png', 'snakeproject4.png']
theme_index = 0 

#list of sounds 
sound = ['garden.wav', 'sea.wav', 'space.wav', 'candle.wav', 'ghost.wav']
sound_index = -1

def button_click(x, y, button_x, button_y, button_width, button_height, action):
    if button_x < x < button_x + button_width and button_y > y > button_y - button_height:
        action()
def on_screen_click_1(x, y):
    button_click(x, y, -150, 160, 100, 50, admin_section)
    button_click(x, y, 50, 160, 100, 50, user_section)

def on_screen_click_2(a, b):
    button_click(a, b, -150, 160, 100, 50,a_login )
    button_click(a, b, 50, 160, 100, 50, a_register)

def on_screen_click_3(a, b):
    button_click(a, b, -150, 160, 100, 50,u_login )
    button_click(a, b, 50, 160, 100, 50, u_register)

def on_screen_click_4(a,b):
    button_click(a, b, -150, -260, 100, 50,play_game_page )
    button_click(a, b, 50, -260, 100, 50, main_loop)

def draw_button():
    game_ov.penup()
    game_ov.hideturtle()
    game_ov.goto(-150,-275)
    game_ov.pendown()
    game_ov.color("white") 
    game_ov.write("Play again", font =("Courier", 16, "bold"))
    game_ov.penup() 
    game_ov.goto(50,-275) 
    game_ov.pendown()
    game_ov.write("Main menu", font =("Courier", 16, "bold"))

def help_page():
    s.bgpic("helpplay.png")
    s.onkey(home_page, "BackSpace")
# home page
def home_page():
    my_turtle1.hideturtle()
    s.bgpic("Homepage.png")
    s.listen()
    s.onkey(help_page, "i")

# actual game setup ,snake moves, eats, questions.
def play_game_page():
    global food_color, food_color1, food_color2,  main_score, a_usernameS
    score = main_score
    highest_score = 0
    delay = 0.1
    winsound.PlaySound(sound[sound_index], winsound.SND_ASYNC | winsound.SND_LOOP)
    s = turtle.Screen()
    s.clearscreen()
    s.bgpic(theme[theme_index-1])
    if a_usernameS == None:
        a_usernameS = 'admin4' # admin4 default
    cursor.execute(f"SELECT option1, option2, option3 FROM {a_usernameS}")
    result1 = cursor.fetchone()
    option1, option2, option3 = result1
    # Snake head setup
    head = turtle.Turtle()
    head.speed(0)
    head.shape("circle")
    head.color("black")
    head.fillcolor(colors[current_color_index-1])
    head.shapesize(1.5)
    head.penup()
    head.goto(0, 0)
    head.direction = "stop"

    # Snake food setup
    food = turtle.Turtle()
    food.speed(0)
    food.shape("turtle")
    food.color("red")
    food.fillcolor("red")
    food.penup()
    food.goto(0, 200)
    food.write(f"..{option1}",font=("Courier", 14, "bold"))

    food1 = turtle.Turtle()
    food1.speed(0)
    food1.shape("turtle")
    food1.color("blue")
    food1.fillcolor("blue")
    food1.penup()
    food1.goto(50, 90)
    food1.write(f"..{option2}",font=("Courier", 14, "bold"))


    food2 = turtle.Turtle()
    food2.speed(0)
    food2.shape("turtle")
    food2.color("yellow")
    food2.fillcolor("yellow")
    food2.penup()
    food2.goto(-100,-100 )
    food2.write(f"..{option3}",font=("Courier", 14, "bold"))


    # Scoreboard setup
    sb = turtle.Turtle()
    sb.color("white")
    sb.penup()
    sb.hideturtle()
    sb.goto(-250, 260)
    sb.showturtle()
    cursor.execute(f"SELECT question FROM {a_usernameS}")
    Question = cursor.fetchone()
    sb.write(f"\n    {Question} \n ",font=("Courier", 14, "bold"))
    # FUNCTION Movement of snake 
    def move():
        if head.direction == "up":
            y = head.ycor()
            head.sety(y + 20)
        if head.direction == "down":
            y = head.ycor()
            head.sety(y - 20)
        if head.direction == "left":
            x = head.xcor()
            head.setx(x - 20)
        if head.direction == "right":
            x = head.xcor()
            head.setx(x + 20)

    def go_up():
        if head.direction != "down":
            head.direction = "up"

    def go_down():
        if head.direction != "up":
            head.direction = "down"

    def go_left():
        if head.direction != "right":
            head.direction = "left"

    def go_right():
        if head.direction != "left":
            head.direction = "right"

    def go_stop():
        head.direction = "stop"

    # keyboard inputs to move the snake in required direction
    s.listen()
    s.onkey(go_up, "Up")
    s.onkey(go_down, "Down")
    s.onkey(go_left, "Left")
    s.onkey(go_right, "Right")
    s.onkey(go_stop, "space")

    # Main game loop
    while True:
        s.update()
        # Check for collision with the borders
        if head.xcor() > 340 or head.xcor() < -340 or head.ycor() > 290 or head.ycor() < -290:
            time.sleep(1)
            head.goto(0, 0)
            head.direction = "stop"
            winsound.PlaySound('gamover.wav', winsound.SND_FILENAME)

            # Hide the snake bodies
            for body in bodies:
                body.hideturtle()
            bodies.clear()

            main_score = score
            delay = 0.1

            # Update scoreboard
            user_rank(main_score)
            sb.clear()
            sb.write(f"Score: {score}\n ", align="left", font=("Courier", 14, "bold"))
            gaame_over()
            draw_button()
            s.onclick(on_screen_click_4)
            break  

        # collision with the food options(correct/incorrect)
        if head.distance(food2) < 20:
            # increase length snake
            body = turtle.Turtle()
            body.hideturtle()
            body.penup()
            body.speed(0)
            body.shape("circle")
            body.color('black')
            body.goto(300,400)
            body.fillcolor(colors[current_color_index-1])
            bodies.append(body)
            body.showturtle()
            score += 10
            delay -= 0.001
            if score > highest_score:
                highest_score = score
            # # Update scoreboard
            sb.clear()
            sb.write(f"Score: {score}  \n\n",  align="left", font=("Courier", 14, "bold"))
            if a_usernameS == None:
                a_usernameS = 'admin4'     # default admin4
            cursor.execute(f"SELECT questionid FROM {a_usernameS}")
            result = cursor.fetchall()
            number_of_row = len(result)
            random_row_id = random.randint(1, number_of_row)
            cursor.execute(f"SELECT * FROM {a_usernameS} WHERE questionid = ?", (random_row_id,))
            result1 = cursor.fetchone()
            id, Question, option1, option2, option3 = result1
            sb.write(f"""\n {Question}""", font=("Courier", 14, "bold"))
            print(id)
        
        # for general food collision
        if head.distance(food) < 20 or head.distance(food1) < 20 or head.distance(food2) < 20 :
            # Move the food to random place
            food.clear()
            x = random.randint(-240, 240)
            y = random.randint(-290, 190)
            food_color = random.choice(colors)
            food.color(food_color)
            food.fillcolor(food_color )
            food.goto(x, y)
            food.write(f"..{option1}",font=("Courier", 14, "bold"))

            # move food1 random place
            food1.clear()
            x = random.randint(-240, 240)
            y = random.randint(-290, 190)
            food_color1 = random.choice(colors1)
            food1.color(food_color1)
            food1.fillcolor(food_color1)
            food1.goto(x, y)
            food1.write(f"..{option2}", font=("Courier", 14, "bold"))
            # Move food2 random place
            food2.clear()
            x = random.randint(-240, 240)
            y = random.randint(-290, 190)
            food_color2 = random.choice(colors2)
            food2.color(food_color2)
            food2.fillcolor(food_color2)
            food2.goto(x, y)
            food2.write(f"..{option3}", font=("Courier", 14, "bold"))

        # Move the snake body
        for index in range(len(bodies) - 1, 0, -1):
            x = bodies[index - 1].xcor()
            y = bodies[index - 1].ycor()
            bodies[index].goto(x, y)

        if len(bodies) > 0:
            x = head.xcor()
            y = head.ycor()
            bodies[0].goto(x, y)

        move()

        # Check for collision with the snake body
        for body in bodies:
            if body.distance(head) < 20:
                time.sleep(1)
                head.goto(0, 0)
                head.direction = "stop"
                winsound.PlaySound('gamover.wav', winsound.SND_FILENAME)

                # Hide the snake bodies
                for body in bodies:
                    body.hideturtle()
                bodies.clear()
    
                main_score = score
                delay = 0.1
        
                # Update the scoreboard
                user_rank(main_score)
                sb.clear()
                sb.write("Score: {} ".format(score), align="left", font=("Arial", 14, "bold"))
                user_rank(main_score)
                gaame_over()
                draw_button()
                s.onclick(on_screen_click_4)
                break    
        time.sleep(delay)

def user_rank(main_main_score):
    global user_position
    try:
        main_score = main_main_score
        cursor.execute(f"INSERT INTO Users (username, password, userscore) VALUES (?,?,?)", (u_username, u_entry_pin, main_score))
        conn.commit()
        cursor.execute("SELECT DISTINCT userscore FROM Users WHERE userscore IS NOT NULL ORDER BY userscore DESC")
        rows = cursor.fetchall()
        position = 1
        user_position = None
        for row in rows:
            r = row[0]
            if user_position is None and r == main_score:
                user_position = position
                break
            position += 1

    except IndexError as i:
        print('Index error', i)
    except Exception as e:
        print(e)
    except NameError as n:
        print("username not found", n)

def game_customization():
    my_turtle1.clear()
    s.bgpic("customization.png")
    s.listen()
    s.onkey(skin_options, "Left")
    s.onkey(theme_options, "Up")

# to select the skin colour of snake by pressing 'left key
def skin_options():
    global current_color_index
    snake_skin = turtle.Turtle()
    snake_skin.shape('circle')
    snake_skin.shapesize(3)
    snake_skin.color(colors[current_color_index])
    current_color_index += 1
    if current_color_index >= len(colors):
        current_color_index -= len(colors) 

def theme_options():
    global theme_index
    global sound_index
    s = turtle.Screen()
    wr = turtle.Turtle()
    wr.write("press Space key to start")
    s.bgpic(theme[theme_index])
    sound_index += 1
    theme_index += 1
    if theme_index>= len(theme):
        theme_index -= len(theme)
    if sound_index>= len(sound):
        sound_index -= len(sound)

def create_admin_specific_table(a_username):
    cursor.execute(f'''
        CREATE TABLE IF NOT EXISTS {a_username} (
            questionid INTEGER PRIMARY KEY AUTOINCREMENT,
            question TEXT,
            option1 TEXT,
            option2 TEXT,
            option3 TEXT
        );
    ''')

    conn.commit()

def admin_question_entry():
    s.clearscreen()
    s.bgpic("questionentrypage.png")
    global option2, option1, option3, Question
    while True:
        Question = turtle.textinput("Entry", "Enter Question:")
        if Question is None or Question.strip() == "":
            break
        # three options 
        option1 = turtle.textinput("Entry", "Enter option1:")
        if option1 is None or option1.strip() == "":
            break

        option2 = turtle.textinput("Entry", "Enter option2:")
        if option2 is None or option2.strip() == "":
            break

        option3 = turtle.textinput("Entry", "Enter correct option3:")
        if option3 is None or option3.strip() == "":
            break
        cursor.execute(f"INSERT INTO {a_username} (question, option1, option2, option3) VALUES (?,?,?,?)", (Question, option1, option2, option3))
        conn.commit()
    main_loop()

def adminselection():
    global a_usernameS, chooseadmin
    s.clearscreen()
    s.bgpic("groupselect.png") 
    chooseadmin = turtle.Turtle()
    chooseadmin.hideturtle()
    chooseadmin.penup()      
    chooseadmin.goto(-330, 260)
    chooseadmin.color('white')
    chooseadmin.write("Choose the question group :\n ", font =("Courier", 15, "bold"))
    chooseadmin.sety(chooseadmin.ycor() - 30) 
    cursor.execute("SELECT username FROM Admins ")
    adminnames = cursor.fetchall()
    for i in adminnames:
        chooseadmin.write(f"{i[0]}\n", font=("Courier", 15, "bold"))
        chooseadmin.sety(chooseadmin.ycor() - 30) 
    a_usernameS = turtle.textinput("Question group choice", "Group")
    if a_usernameS != None and (a_usernameS,) not in adminnames:
        chooseadmin1 = turtle.Turtle()
        chooseadmin1.hideturtle()
        chooseadmin1.penup()      
        chooseadmin1.goto(-150, -180)
        chooseadmin1.color("red")
        chooseadmin1.write("This admin doesnot exist.Try again", font =("Courier", 15, "bold"))
        time.sleep(3)
        adminselection()
    else:
        pass

# login and verification of user and admin
def admin_section():
    global main_e
    s.clearscreen()
    s1.bgpic("loginregister.png")
    main_e = turtle.Turtle()
    main_e.hideturtle()
    main_e.penup()      
    main_e.goto(190, 300)
    main_e.color('white')
    main_e.write("Press 'e' to goto homepage", font =("Courier", 10, "bold"))
    s1.listen()
    s1.onkey(main_loop, "e")
    s1.onclick(on_screen_click_2)
def user_section():
    main_e = turtle.Turtle()
    # s.clearscreen()
    s1.bgpic("loginregister.png")
    main_e.hideturtle()
    main_e.penup()      
    main_e.goto(190, 300)
    main_e.color('white')
    main_e.write("Press 'e' to goto homepage ", font =("Courier", 10, "bold"))
    s1.listen()
    s1.onkey(main_loop, "e")
    s1.onclick(on_screen_click_3)
def a_login():
    global a_username, a_entry_pin, table_name1
    max_attempts = 3
    attempts = 0
    while attempts < max_attempts:
        a_username = turtle.textinput("Admin  login Username", "Username")
        a_entry_pin = turtle.textinput("Admin login EntryPin", "EntryPin")
        if a_username and a_entry_pin:
            table_name1 = "Admins"
            if login(a_username, a_entry_pin, table_name1):
                create_admin_specific_table(a_username)
                admin_question_entry()
                break
            else:
                show_error_message("Invalid username or password.Please try again")
                attempts += 1
        else:
            show_error_message("Username and Entrypin cannot be empty.Please try again")
            attempts += 1       
    if attempts >= max_attempts:
        show_error_message("Login attempts exceeded!. Returning to admin section")
        admin_section()

def u_login():
    global u_username, u_entry_pin, table_name
    max_attempts = 3
    attempts = 0
    while attempts < max_attempts:  
        u_username = turtle.textinput("Player Username", "Enter Username")
        u_entry_pin = turtle.textinput("Player EntryPin", "Enter EntryPin")
        if u_username and u_entry_pin:  
            table_name = "Users"
            if login(u_username, u_entry_pin, table_name):
                adminselection() 
                chooseadmin.clear()
                game_customization()
                s.listen()
                s.onkey(play_game_page, "space")
                break
            else:
                show_error_message("Invalid username or password. Please try again.")
                attempts += 1
        else:
            show_error_message("Username and EntryPin cannot be empty. Please try again.")
            attempts += 1

    if attempts >= max_attempts:
        show_error_message("Login attempts exceeded!. Returning to user section.")
        user_section()

def a_register():
    global ar_username, ar_entry_pin, table_name1
    try:
        ar_username = turtle.textinput(" Admin Username", "Username")
        ar_entry_pin = get_four_digit_pin()
        if ar_username and ar_entry_pin:
            table_name1 = 'Admins'
            if register(ar_username, ar_entry_pin, table_name1):
                show_error_message("Username already exists. Try again!")
                a_register()
            else:
                a_login()
        else:
            admin_section()
    except Exception as E:
        print("null constraint", E)
        admin_section()
# four digit entrypin verification function 
def get_four_digit_pin():
            while True:
                entry_pin = turtle.textinput("EntryPin", "Entrypin")
                if entry_pin and entry_pin.isdigit() and len(entry_pin) == 4:
                    return entry_pin
                else:
                    pass
def u_register():
    global ur_username, ur_entry_pin, table_name, u_username, u_entry_pin
    try:
        ur_username = turtle.textinput(" Player Username", "Username")
        ur_entry_pin = get_four_digit_pin()
        if ur_username and ur_entry_pin:
            table_name = "Users"
            if register(ur_username, ur_entry_pin, table_name):
                show_error_message("Username already exists. Try again!")
                u_register()
            else:
                adminselection()
                chooseadmin.clear()
                game_customization()
                s.listen()
                s.onkey(play_game_page, "space")  
        else:
            user_section()              
    except Exception as E:
        print("null constraint", E)
        user_section()
    u_username = ur_username
    u_entry_pin = ur_entry_pin

def login(off_username, off_password, table_name):
    cursor.execute(f"SELECT * FROM {table_name} WHERE username = ? AND password = ?", (off_username, off_password))
    result = cursor.fetchone()
    conn.commit()
    if result:
        dbwrite2 = turtle.Turtle()
        dbwrite2.hideturtle()
        dbwrite2.penup()
        dbwrite2.goto(-330, 250)
        dbwrite2.color('yellow')
        dbwrite2.write(f"Welcome {off_username}! You have successfully logged in.", font=("Courier", 15, "bold"))
        time.sleep(1)
        dbwrite2.clear()
        return True
    else:
        return False
    
def register(off_username, off_password, table_name):
    #checking if username alreadys exists??
    cursor.execute(f"SELECT username FROM {table_name} WHERE username = ?", (off_username,))
    result = cursor.fetchone()
    conn.commit()
    if result:
        return True 
    else: # store values to db
        cursor.execute(f"INSERT INTO {table_name} (username, password) VALUES (?, ?)", (off_username, off_password))
        conn.commit()
        return False
    
def show_error_message(message):
    errormessage = turtle.Turtle()
    errormessage.hideturtle()
    errormessage.penup()
    errormessage.goto(-300, -150)
    errormessage.color("red")
    errormessage.write(message, font=("Courier", 14, "bold"))
    time.sleep(1)
    errormessage.clear()

def gaame_over():
    global high_score, dbwrite4
    s.clearscreen()
    s.bgpic("gameover.png") 
    dbwrite4 = turtle.Turtle()
    dbwrite4.hideturtle() 
    dbwrite4.penup()      
    dbwrite4.goto(-330, 260)
    dbwrite4.color('white')
    dbwrite4.write(f"Game Score:{main_score} ",font=("Courier", 15, "bold") )
    cursor.execute("""
        SELECT MAX(userscore) AS highest_score
        FROM Users
        WHERE username = ? AND password = ?;
        """, (u_username, u_entry_pin))
    
    high_score_row = cursor.fetchone()
    high_score = high_score_row[0]
    if high_score is not None:
        if main_score >= high_score:
            high_score = main_score
    else:
        high_score = main_score
    dbwrite4.goto(-330, 200)
    dbwrite4.write(f"High Score: {high_score}",font=("Courier", 15, "bold"))
    dbwrite4.goto(-330, 140)
    dbwrite4.write(f'Rank in leaderboard: {user_position}' ,font=("Courier", 15, "bold"))
    time.sleep(10)
    dbwrite4.clear()

# database section ~~~
conn = sqlite3.connect('snakegamedatabase.db')
cursor = conn.cursor()
cursor.execute('''
    CREATE TABLE IF NOT EXISTS Users (
        userid INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT NOT NULL,
        password TEXT NOT NULL,
        userscore INTEGER
    );
''')
cursor.execute('''
    CREATE TABLE IF NOT EXISTS Admins (
        adminid INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT NOT NULL,
        password TEXT NOT NULL
    );
''')
conn.commit() 

def main_loop(): 
    global main_score
    main_score = 0
    game_ov.hideturtle()
    game_ov.clear()
    home_page()          
    s.listen()
    s.onclick(on_screen_click_1)
main_loop()
s.mainloop() # similar to wn.done() , it retains the screen for keyboard an mouse clicks


