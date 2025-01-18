# for username and password
import turtle

# # Set up the screen
# screen = turtle.Screen()
# screen.title("Text Input Example")
# screen.bgcolor("cyan")

# # Create a turtle to draw the text and handle input
# drawer = turtle.Turtle()
# drawer.hideturtle()
# drawer.penup()
# drawer.speed(0)

# # Initialize input fields
# username = ""
# password = ""
# input_mode = None

# # Function to draw text
# def draw_text(x, y, text, align="center", font_size=14):
#     drawer.goto(x, y)
#     drawer.write(text, align=align, font=("Arial", font_size, "normal"))

# # Function to handle text input
# def keypress_handler(char):
#     global username, password
#     if input_mode == "username":
#         if char == "BackSpace":
#             username = username[:-1]  # Remove the last character
#         else:
#             username += char
#     elif input_mode == "password":
#         if char == "BackSpace":
#             password = password[:-1]
#         else:
#             password += char
#     draw_interface()

# def start_username_input():
#     global input_mode
#     input_mode = "username"

# def start_password_input():
#     global input_mode
#     input_mode = "password"

# def end_input():
#     global input_mode
#     input_mode = None
#     print("goes to database",username)
#     print("goes to database",password)
#     drawer.clear()

# # Bind the keyboard events
# def bind_keys():
#     for char in "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789~!@#$%^&*()_":
#         screen.onkeypress(lambda ch=char: keypress_handler(ch), char)
#     screen.onkeypress(lambda: keypress_handler("BackSpace"), "BackSpace")
#     screen.onkeypress(end_input, "Return")  # Press 'Enter' to submit


# # Draw the initial interface
# def draw_interface():
#     drawer.clear()
#     draw_text(0, 50, username)
#     draw_text(0, 0, '*' * len(password))  # Mask the password

# # Set up initial keyboard bindings
# screen.listen()
# screen.onkey(start_username_input, "Up")  # Press 'Up' to start username input
# screen.onkey(start_password_input, "Down")  # Press 'Down' to start password input
# bind_keys()

# # Main loop
# turtle.mainloop()


# for the question and options
import turtle
screen = turtle.Screen()
screen.title("Login")
# Set up the screen
def login():
    screen = turtle.Screen()
    screen.title("Login")
    # This flag will control the loop
    loop_running = True

    # Define the function that breaks the loop
    def stop_loop():
        global loop_running
        loop_running = False

    # Listen for the Enter key (keycode 'Return' in turtle)
    screen.listen()
    screen.onkey(stop_loop, "Return")

    while loop_running:
        # Get question
        question = turtle.textinput("entry", "Enter question")

        # If the user cancels the input box or presses Enter without typing, stop the loop
        if question is None or question == "":
            stop_loop()
            break
        
        # Get options
        option1 = turtle.textinput("entry", "Enter option1:")
        option2 = turtle.textinput("entry", "Enter option2:")
        option3 = turtle.textinput("entry", "Enter option3:")

        # If any option is None or empty (i.e., user cancels or presses Enter), stop the loop
        if option1 is None or option1 == "" or option2 is None or option2 == "" or option3 is None or option3 == "":
            stop_loop()
            break

        # Print question and options
        print("Question:", question)
        print("option1:", option1)
        print("option2:", option2)
        print("option3:", option3)

# i= 0
# for i in range(2):
#     # Get question
#     question = turtle.textinput("entry", "Enter question")
#     # Get options
#     option1 = turtle.textinput("entry", "Enter option1:")
#     option2 = turtle.textinput("entry", "Enter option2:")
#     option3 = turtle.textinput("entry", "Enter option3:")

#     # Print username and password (for demonstration purposes, avoid printing passwords in real applications)
#     print("Question:", question)
#     print("option1:", option1)
#     print("option2:", option2)
#     print("option3:", option3)
#     i = i+1
# Close the turtle graphics window
turtle.done()