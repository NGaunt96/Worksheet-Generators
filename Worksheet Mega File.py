from Area_and_Perimeter import *
from Nice_Percentage_Increase_and_Decrease import *
from Nice_Percentage_of_an_amount import *
from Green_Nice_Percentage_Increase_and_Decrease import *
from Green_Nice_Percentage_of_an_amount import *
from Random_Percentage_Increase_and_Decrease import *
from Random_Percentage_of_an_amount import *
#from SimEquations import *
from LinearEq import *
from HCF import *
from Factorising import *
from Linear_Sequences import *
#from Add_Subtract_Decimals import *
from Prime_Factors import *
from LinearEqBrackets import *
from Factorising_Single_Bracket import *
from Expanding_Cubics import *
from SimEquations_Linear_Circle import *

funcs = {
   1: "AreaAndPerimeter",
   2: "FactorisingQuadratics",
   3: "HCF",
   4: "LinearSequences",
   5: "SolveLinearEquations",
   6: "NicePercInDe",
   7: "NicePercOfAmount",
   8: "RandPercInDe",
   9: "RandPercOfAmount",
   10: "AddSubtractDecimals",
   11: "PrimeFactors",
   12: "GreenNicePercOfAmount",
   13: "GreenNicePercInDe",
   14: "SolveLinearEquationsBrackets",
   15: "FactorisingSingleBracket",
   16: "ExpandingCubics",
   17: "SolveLinearSimultaneousLinCir"
}
for i in range(len(funcs)):
   print(str(i+1) + ":", funcs[i+1])
uIn = input("Type the number(s) of the topic(s) you want, separated by spaces: ")
worksheets = uIn.split(" ")
numQ = input("Type how many questions you want of each (just one number): ")


for i in worksheets:
   if i.isdigit() == True and int(i) in funcs:
      exec(funcs[int(i)] + "(" + numQ + ")")


