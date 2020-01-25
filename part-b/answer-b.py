from propositional_logic import *

A = BoolVar('A')
B = BoolVar('B')
C = BoolVar('C')

# write code using A, B, and C, along with 
# the classes from propositional_logic.py
# and the .format() method to output the
# following expression:

# (((A => B) & (B => C)) => (A => C))
f1 = Implies(A,B)
f2 = Implies(B,C)
righteqn = Implies(A,C)

lefteqn = And(f1,f2)
eqn = Implies(lefteqn, righteqn)
print(eqn.format())
