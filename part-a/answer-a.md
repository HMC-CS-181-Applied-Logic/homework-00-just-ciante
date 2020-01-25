## Part a

### Describe what the code in `z3-test.py` is doing in a paragraph or two.

First, we have 4 variables being declared: two booleans, a and b, and two ints, x and y. After that, we have a logical expression f being declared. Since it's wrapped in an AND, I'm assuming that the solver checks which values of a, b, x, and y can be used to keep all the expressions true. There is a way to satisfy the constraint with x=99, y=100, a=False, and b=True. Since it could be satisfied, the `f_check` is printed out, the `if` statement is entered, and the model can be printed out. 

Afterwards, another constraint y < 1 is added to the solver. The solver then checks if there are conditions in which the logical expression can be satisfied, and there aren't any. This makes sense because the expression added was y < 1, but from the already existing expression, we know x < y and x > 0. Since y < 1, there is no x value that can satisfy the expression. The f_check returns unsat and the model cannot be printed as it won't enter the `if` statement. 
