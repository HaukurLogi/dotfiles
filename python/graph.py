import ast
from math import sin, log
import matplotlib.pyplot as plt
from tkinter import *

def main():
    window = Tk()

    window.geometry("800x200") # Declare the dementions of the Tkinter window
    window.resizable(False, False) # Is it resizable
    window.configure(bg="#222222") # Window Background color
    window.title("""Equation""") # Window title

    equationproblem_with_x = StringVar() # Define the equation/problem_with_x variable


    equation_problem_input_box = Entry(window, # The input box where you put your equation
                width=30, # The width of the element
                bg="#222222", # Background color
                fg="#EDEDED", # Foreground color
                highlightbackground="#000000", # Border color
                highlightthickness=3, # Border thickness
                font=("Times New Roman", 36), # Font ("Style", Size)
                textvariable=equationproblem_with_x) # Declare what variable turns into the users
    show_graph_button = Button(window, # Show graph button
                width=12,
                height=1,
                text="Show Graph",
                font=("Times New Roman", 15),
                bg="#910000",
                fg="#111111",
                border=False,
                activebackground="#750000", # Color of button when pressed
                command=lambda: showGraph(equationproblem_with_x.get())) # The function that runs when button is pressed.
    equation_text_label = Label(window,
                width=5,
                height=1,
                bg="#222222",
                fg="#EDEDED",
                font=("Times New Roman", 36),
                text="ƒ(x) = ")

    # The later the attribute the later it renders. Texts render last!
    equation_problem_input_box.place(relx=0.55, rely=0.5, anchor=CENTER)
    show_graph_button.place(relx=0.55, rely=0.75, anchor=CENTER)
    equation_text_label.place(relx=0.125, rely=0.5, anchor=CENTER)

    def showGraph(problem):
        graph_x = [] # X values
        graph_y = [] # Y values

        for i in range(1, 100+1):
            problem_with_x = problem.replace("x", str(i))
    
            graph_x.append(i) # Append X values
            graph_y.append(eval(problem_with_x)) # Append Y values 
            
        plt.plot(graph_x, graph_y) # Plot the points
        plt.show() # Show the graph

    window.mainloop() # Make window for the foreseeable future
if __name__ == "__main__":
    main()