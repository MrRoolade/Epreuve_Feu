#~~> MrRøølåÐe <~~#
# Evaluer une expression
# Créez un programme qui reçoit une expression arithmétique dans une chaîne de caractères et en retourne le résultat après l’avoir calculé.
# Vous devez gérer les 5 opérateurs suivants : “+” pour l’addition, “-” pour la soustraction, “*” la multiplication, “/” la division et “%” le modulo.

#Algorithme Shunting-yard / Methode NPI

import sys
import re

def handle_error(user_value): 
    if not check_digit("".join(user_value[1])) :
        quit_program("veuillez ne rentrer que des chiffres et des opérateurs")
    elif not check_parentheses (re.findall(r'\d+|\+|\-|\*|\/|\(|\)', "".join(user_value[1]))):
        quit_program("problème de parenthèses") 
    elif len(user_value)!=2: 
        quit_program("veullez rentrer une expression entre guillemets svp")

def quit_program(message):
    sys.exit(message)

def list_operators():
    operators = {'+': (1, lambda x, y: x + y),
                    '-': (1, lambda x, y: x - y),
                    '*': (2, lambda x, y: x * y),
                    '/': (2, lambda x, y: x / y),
                    '%': (2, lambda x, y: x % y),
                    '(': (0,),
                    ')': (0,),
                    }
    return operators

def check_parentheses(expressions):
    open_parentheses = sum(1 for value in expressions if value =='(')
    close_parentheses = sum(1 for value in expressions if value ==')')
    return open_parentheses == close_parentheses

def check_digit(expression):
    return not bool((re.search(r'[^0-9+\-*/%() ]', expression)))

def calcul_npi(array_output, array_operator_stack, operators):
    operator = array_operator_stack.pop()
    operand_one = array_output.pop()
    operand_two = array_output.pop()
    array_output.append(operators[operator][1](operand_two, operand_one))

def run_shunting_yard(expr_value, operators):
    array_output = []
    array_operator_stack = []
    for value in expr_value :
        if value.isdigit():
            array_output.append(int(value))
        elif value == '(':
            array_operator_stack.append(value)
        elif value == ')':
            while array_operator_stack[-1] != '(':
                calcul_npi(array_output, array_operator_stack, operators)
            array_operator_stack.pop()
        elif value in operators :
            while (array_operator_stack and operators[array_operator_stack[-1]][0] >= operators[value][0]):
                calcul_npi(array_output, array_operator_stack, operators)
            array_operator_stack.append(value)

    while array_operator_stack: 
       calcul_npi(array_output, array_operator_stack, operators)

    return array_output

def main(): 
    handle_error(sys.argv)
    operators = list_operators()
    tokens = re.findall(r'\d+|\+|\-|\*|\/|\(|\)|\%', "".join(sys.argv[1]))
    result = run_shunting_yard(tokens, operators)
    final_result = result[0]
    print(final_result)

if __name__ == "__main__":
    main()