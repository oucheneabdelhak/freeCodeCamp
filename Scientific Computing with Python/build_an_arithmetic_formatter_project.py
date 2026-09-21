def arithmetic_arranger(problems, show_answers=False):
    if len(problems) > 5:
        return 'Error: Too many problems.'
    
    for problem in problems:
        if ('*' in problem or '/' in problem) or (not ('-' in problem) and not ('+' in problem)):
            return "Error: Operator must be '+' or '-'."
    operators = []
    operands = []
    max_operands_len = []
    for problem in problems:
        if '+' in problem:
            operators.append('+')
            operands.append([p.strip() for p in problem.split('+')])
        else:
            operators.append('-')
            operands.append([p.strip() for p in problem.split('-')])
        if not (operands[-1][0].isdigit() and operands[-1][1].isdigit()):
            return "Error: Numbers must only contain digits."
        max_operands_len.append(max(len(operands[-1][0]),len(operands[-1][1]))) 
        if max_operands_len[-1] > 4:
            return "Error: Numbers cannot be more than four digits."

    line1 = '' 
    line2 = ''
    line3 = '' 
    line4 = ''
    for i in range(len(problems)):
        #Line 1
        empty_space_l1 = [' ' for j in range(max_operands_len[i]-len(operands[i][0]) + 2)]
        if line1 == '':
            line1 += ''.join(empty_space_l1) + operands[i][0]
        else:
            line1 += '    ' + ''.join(empty_space_l1) + operands[i][0]

        #Line 2
        empty_space_l2 = [' ' for j in range(max_operands_len[i]-len(operands[i][1]) + 1)]
        if line2 == '':
            line2 += operators[i] + ''.join(empty_space_l2) + operands[i][1]
        else:
            line2 += '    ' + operators[i] + ''.join(empty_space_l2) + operands[i][1]

        #Line 3
        if line3 == '':
            line3 += ''.join(['-' for j in range(max_operands_len[i]+2)])
        else:
            line3 += '    ' + ''.join(['-' for j in range(max_operands_len[i]+2)])

        #Line 4   
        if show_answers:
            if operators[i] == '+':
                result = int(operands[i][0]) + int(operands[i][1])
            else:
                result = int(operands[i][0]) - int(operands[i][1])
            empty_space_l4 = [' ' for j in range(max_operands_len[i]-len(str(result)) + 2)]

            if line4 == '':
                line4 += ''.join(empty_space_l4) + str(result)
            else:
                line4 += '    ' + ''.join(empty_space_l4) + str(result)
    output = [line1,line2,line3]  
    if show_answers:
        output.append(line4)
     
    return '\n'.join(output)

print(f'\n{arithmetic_arranger(["44 + 815", "909 - 2", "45 + 43", "123 + 49", "888 + 40", "653 + 87"],True)}')
