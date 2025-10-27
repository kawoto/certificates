def arithmetic_arranger(problems, show_answers=False):
    if len(problems) > 5:
        return 'Error: Too many problems.'

    first_operands = []
    second_operands = []
    operators = []
    answers = []

    for problem in problems:
        problem = problem.replace(" ", "")  # Remove spaces like original
        if "*" in problem or "/" in problem:
            return "Error: Operator must be '+' or '-'."

        # Find operator
        if '+' in problem:
            operator = '+'
        elif '-' in problem:
            operator = '-'
        else:
            return 'Error: Invalid operator.'

        # Split operands
        left, right = problem.split(operator)

        # Validation
        if not left.isdigit() or not right.isdigit():
            return 'Error: Numbers must only contain digits.'

        if len(left) > 4 or len(right) > 4:
            return 'Error: Numbers cannot be more than four digits.'

        first_operands.append(left)
        second_operands.append(right)
        operators.append(operator)

        # Compute result
        result = str(int(left) + int(right)) if operator == '+' else str(int(left) - int(right))
        answers.append(result)

    # Build formatted output
    top_row = []
    bottom_row = []
    dash_row = []
    answer_row = []

    for i in range(len(problems)):
        width = max(len(first_operands[i]), len(second_operands[i])) + 2
        top_row.append(first_operands[i].rjust(width))
        bottom_row.append(operators[i] + second_operands[i].rjust(width - 1))
        dash_row.append('-' * width)
        answer_row.append(answers[i].rjust(width))

    arranged = [
        '    '.join(top_row),
        '    '.join(bottom_row),
        '    '.join(dash_row)
    ]

    if show_answers:
        arranged.append('    '.join(answer_row))

    return '\n'.join(arranged)
