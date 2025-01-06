def check_limit(problems):
    # this function is check the limit is less then 5. if yes the return true
    if len(problems) < 6:
        return True
    else:
        return False

# <---------------------------------------->

def check_operator(operator):
    if operator in ['+','-']:
        return True
    else:
        return False

# <---------------------------------------->

def check_operand(digit1, digit2):
    if digit1.isdigit() and digit2.isdigit():
        return True
    else:
        return False

# <---------------------------------------->

def number_length(digit1, digit2):
    if len(digit1) < 5 and len(digit2) < 5:
        return True
    else:
        return False

# <---------------------------------------->

def sum_digits(digit1, digit2):
    return (int(digit1) + int(digit2))

# <---------------------------------------->

def subtract_digits(digit1, digit2):
    return  (int(digit1) - int(digit2))

# <---------------------------------------->


def final_result(operator, digit1, digit2):
    if operator == '+':
        result = sum_digits(digit1, digit2)
        return result
    else:
        result = subtract_digits(digit1, digit2)
        return result


def arithmetic_arranger(problems, display_answer = False):

    first_row = []
    second_row = []
    dashes = []
    answer = []

    # print(problems)
    if check_limit(problems):
        for problem in problems:
            part = problem.split()
            digit1, operator, digit2 = part

            if check_operator(operator):

                if check_operand(digit1, digit2):

                    if number_length(digit1, digit2):
                        width = max(len(digit1), len(digit2)) + 2

                        first_row.append(digit1.rjust(width))
                        second_row.append(operator + " " + digit2.rjust(width - 2))
                        dashes.append("-" * width)
                        answer.append(str(final_result(operator, digit1, digit2)).rjust(width))

                       

                    else:
                        return 'Error: Numbers cannot be more than four digits.'       # end number length function
                   
                else:
                    return 'Error: Numbers must only contain digits.'       # end check operand function

            else:
                return "Error: Operator must be '+' or '-'."      # end check operator function
    else:
        return 'Error: Too many problems.'       # end main function 
    arranged_problems = (

        "    ".join(first_row) + "\n" +
        "    ".join(second_row) + "\n" +
        "    ".join(dashes)
        )

    if display_answer:
        arranged_problems += "\n" + "    ".join(answer)
        
    return arranged_problems
# <---------------------------------------->

result = arithmetic_arranger(["380 + 2", "123 + 49"])
print(result)