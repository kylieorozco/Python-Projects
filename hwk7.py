'''
Name: Kylie Orozco
Purpose: Create a Halloween greeting card with a name input from user
Pre-conditions: Prompts for a name and waits for user to click the mouse
Post-conditions: Creates two pumpkins and a cat head with the user's input name, also with a prompt to close window with a click of the mouse
'''
from graphics import *
def main():
    
    win = GraphWin("Greeting", 300, 300)
    # Create a Text object
    instructions = Text(Point(win.getWidth()/2, 40), "Enter the receiver's name")
    instructions.draw(win)
    
    # Create an Entry object
    entry1 = Entry(Point(win.getWidth()/2, 275),10)
    # Draw the Entry object
    entry1.draw(win) 
    
    # Use the getMouse() method
    win.getMouse() 
    
    # Use the getText() method
    name = entry1.getText() 
    
    # Undraw input and Entry Object
    instructions.undraw()
    entry1.undraw()
    
    # Greeting with input
    greeting1 = 'Happy Halloween ' + name + '!'
    Text(Point(win.getWidth()/2, 50), greeting1).draw(win)
    
    # first pumpkin         
    circ = Circle(Point(195, 130), 30)
    circ.setFill("orange")
    circ.draw(win)  
    
    rect = Rectangle(Point(190, 90), Point(200, 100))
    rect.setFill("brown")
    rect.draw(win)
    
    # first apple
    circ = Circle(Point(155, 140), 20)
    circ.setFill("brown")
    circ.draw(win)  
    
    rect = Rectangle(Point(155, 110), Point(155, 120))
    rect.setFill("brown")
    rect.draw(win)
    
    # cat face
    circ = Circle(Point(70, 180), 35)
    circ.setFill("grey")
    circ.draw(win)     
    
    circ = Circle(Point(60, 170), 5)
    circ.setFill("green")
    circ.draw(win)  
    
    circ = Circle(Point(80, 170), 5)
    circ.setFill("green")
    circ.draw(win)  
    
    circ = Circle(Point(70, 180), 5)
    circ.setFill("pink")
    circ.draw(win)
    
    circ = Circle(Point(50, 150), 10)
    circ.setFill("grey")
    circ.draw(win) 
    
    circ = Circle(Point(90, 150), 10)
    circ.setFill("grey")
    circ.draw(win)
    
    # Closes window when user clicks mouse
    end = Text(Point(win.getWidth()/2, 250), "Click to close window")
    end.draw(win)    
    win.getMouse()
    win.close()
main()