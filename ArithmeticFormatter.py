def arithmetic_arranger(problems, show_answers=False):
    longestOperand = ""
    lines = ""
    firstNums = ""
    secondNums = ""
    allLines = ""
    answers = ""
    formattedProblems = ""
    if len(problems) > 5:
        return "Error: Too many problems."
    else:
        for problem in problems:
            for char in problem:
                if char == "*" or char == "/":
                    return "Error: Operator must be '+' or '-'."
                elif not (char.isdigit() or char == "+" or char == "-" or char == " "):
                    return "Error: Numbers must only contain digits."
                
            seperatedProblem = problem.split(" ")
            firstNum = seperatedProblem[0]
            operator = seperatedProblem[1]
            secondNum = seperatedProblem[2]

            longestOperand = ""
            if operator == "+":
                answer = int(firstNum) + int(secondNum)
            elif operator == "-":
                answer = int(firstNum) - int(secondNum)
            if len(firstNum) > 4 or len(secondNum) > 4:
                return "Error: Numbers cannot be more than four digits."
                    
            if int(firstNum) > int(secondNum):
                longestOperand = firstNum
            else:
                longestOperand = secondNum
            if len(longestOperand) == 1:
                lines = "---"
                firstNum = f"{firstNum:>3}"
                secondNum = f"{secondNum:>2}"
                answer = f"{answer:>3}"
            elif len(longestOperand) == 2:
                lines = "----"
                firstNum = f"{firstNum:>4}"
                secondNum = f"{secondNum:>3}"
                answer = f"{answer:>4}"
            elif len(longestOperand) == 3:
                lines = "-----"
                firstNum = f"{firstNum:>5}"
                secondNum = f"{secondNum:>4}"
                answer = f"{answer:>5}"
            elif len(longestOperand) == 4:
                lines = "------"
                firstNum = f"{firstNum:>6}"
                secondNum = f"{secondNum:>5}"
                answer = f"{answer:>6}"

            firstNums += f"{firstNum}    "
            secondNums += f"{operator}{secondNum}    "
            allLines += f"{lines}    "
            answers += f"{answer}    "
    if show_answers:
         return f"{firstNums.rstrip()}\n{secondNums.rstrip()}\n{allLines.rstrip()}\n{answers.rstrip()}"       
    else:
        return f"{firstNums.rstrip()}\n{secondNums.rstrip()}\n{allLines.rstrip()}"

print(f'\n{arithmetic_arranger([input("Enter expression with a space between each number and the operator: ")], True)}')
