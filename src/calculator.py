#!/usr/bin/python2
"""This module is part of PyCalc. It contains the class 'Calculator' which is
a template to create the calculator application.

Copyright (C) 2016  Wilmin Ceballos <source@wilmin.org>

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU Lesser General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU Lesser General Public License for more details.

You should have received a copy of the GNU Lesser General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.
"""


from __future__ import division
import Tkinter

Tk = Tkinter.Tk
Frame = Tkinter.Frame
Button = Tkinter.Button
Label = Tkinter.Label


class Calculator(Tk):
    '''This class contains all the functions and the layout for the calculator
    application.
    '''
    result = 0
    equation = ['']
    equation_string = ''

    def __init__(self, parent=None, resize_width=False, resize_height=False):
        """Initialize attributes
           Calls layout method to create the GUI layout

        Args:
            parent (Optional[object]): The first parameter. Defauts to None.
                This is a parent, such as a parent window or GUI that the
                calculator GUI is part of. This is to allow the app to be a
                sub-program in a larger application.

            resize_width (Optional[bool]): Defaults to False.
                Setting to True will allow horizontal resizing.

            resize_height (Optional[bool]): Defaults to False.
                Setting to True will allow vertical resizing.
        """
        self.parent = parent
        Tk.__init__(self, parent)
        self.resizable(resize_width, resize_height)
        self.screentext = Tkinter.StringVar()
        self.screentext.set('Let\'s get started')
        self.layout()

    def layout(self):
        '''Initializes the calculator layout
        '''
        master_grid = Frame(self) # Container of all contents
        master_grid.grid()

        display_grid = Frame(master_grid) # Container of calculator display
        display_grid.grid(row=0, column=0)

        buttons_grid = Frame(master_grid) # Container of all buttons
        buttons_grid.grid(row=1, column=0)

        numbers_grid = Frame(buttons_grid) # Container of number buttons
        numbers_grid.grid(row=0, column=0)

        operators_grid = Frame(buttons_grid) # Container of operator buttons
        operators_grid.grid(row=0, column=1)

        show_text = Label(display_grid, textvariable=self.screentext,
                          font=("Helvetica", 10),
                          anchor='se', width=20, height=2, pady=20, padx=10)
        show_text.grid()

        # numbers buttons
        button_0 = Button(numbers_grid, text='0', height=2, width=2,
                          command=lambda: self.click_math(0))

        button_1 = Button(numbers_grid, text='1', height=2, width=2,
                          command=lambda: self.click_math(1))

        button_2 = Button(numbers_grid, text='2', height=2, width=2,
                          command=lambda: self.click_math(2))

        button_3 = Button(numbers_grid, text='3', height=2, width=2,
                          command=lambda: self.click_math(3))

        button_4 = Button(numbers_grid, text='4', height=2, width=2,
                          command=lambda: self.click_math(4))

        button_5 = Button(numbers_grid, text='5', height=2, width=2,
                          command=lambda: self.click_math(5))

        button_6 = Button(numbers_grid, text='6', height=2, width=2,
                          command=lambda: self.click_math(6))

        button_7 = Button(numbers_grid, text='7', height=2, width=2,
                          command=lambda: self.click_math(7))

        button_8 = Button(numbers_grid, text='8', height=2, width=2, 
                          command=lambda: self.click_math(8))

        button_9 = Button(numbers_grid, text='9', height=2, width=2, 
                          command=lambda: self.click_math(9))

        # special buttons
        button_equals = Button(numbers_grid, text='=', height=2, width=2,
                               command=self.click_equals)
                               
        button_period = Button(numbers_grid, text='.', height=2, width=2,
                               command=self.click_period)
                               
        button_del = Button(operators_grid, text='DEL', height=1, pady=7,
                            command=self.click_delete, width=2)

        # operator buttons                    
        button_divide = Button(operators_grid, 
                               command=lambda: self.click_math('/'),
                               text='/', width=2, height=1, pady=7)

        button_multiply = Button(operators_grid, 
                                 command=lambda: self.click_math('x'),
                                 text='x', width=2, height=1, pady=7)

        button_add = Button(operators_grid,
                            command=lambda: self.click_math('+'),
                            text='+', width=2, height=1, pady=7)
                            
        button_subtract = Button(operators_grid, 
                                 command=lambda: self.click_math('-'),
                                 text='-', width=2, height=1, pady=7)

        button_0.grid(row=3, column=1)
        button_1.grid(row=2, column=0)
        button_2.grid(row=2, column=1)
        button_3.grid(row=2, column=2)
        button_4.grid(row=1, column=0)
        button_5.grid(row=1, column=1)
        button_6.grid(row=1, column=2)
        button_7.grid(row=0, column=0)
        button_8.grid(row=0, column=1)
        button_9.grid(row=0, column=2)

        button_period.grid(row=3, column=0)
        button_equals.grid(row=3, column=2)

        button_del.grid(row=0, column=0)
        button_divide.grid(row=1, column=0)
        button_multiply.grid(row=2, column=0)
        button_subtract.grid(row=3, column=0)
        button_add.grid(row=4, column=0)

    def click_delete(self):
        """What happens when the 'delete' button is clicked.
        """
        self.result = 0
        self.equation = ['']
        self.equation_string = ''
        self.screentext.set('')

    def click_math(self, val):
        """What happens when a number or a math operator is clicked.
        
        Args:
            val (str): Number or operator clicked is received as a string.
        """
        self.equation.append(str(val))
        self.equation_string = ' '.join(i for i in self.equation)
        self.screentext.set(str(self.equation_string))
        
    def click_period(self):
        """What happens when the period (.) is clicked.
        """
        pass

    def click_equals(self):
        """What happens when the equals (=) button is clicked.
        This method mathematically evaluates the string of operations entered.
        
        Raises:
            ZeroDivisionError: Cannot divide by zero.
                This error will be handled by displaying 'Infinity'.

            Error: If any other error occurs.
                'Error' will be displayed.
        """
        # Get rid of white spaces
        self.equation_string = self.equation_string.replace(' ', '')
        # Change 'x' to math operator '*'
        self.equation_string = self.equation_string.replace('x', '*')

        if not(self.equation_string == ''):
            try:
                self.result = eval(self.equation_string)
            except ZeroDivisionError:
                self.screentext.set('Infinity')
            except:
                self.screentext.set('Error')
            else:
                self.screentext.set(str(self.result))
        else:
            self.click_delete()
            self.screentext.set(str(self.result))
