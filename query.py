import re
def inverse_polish(query):
    operators = ["!", "u", "n", "(", ")"]
    pattern = r'([()!un])|(\b\w+\b)'
    matches = re.findall(pattern, query)
    query = [match[0] or match[1] for match in matches]
    polish = []
    queue = []
    for i in query:
        # si es ) sacar de queue y meter en polish hasta encontrar (
        # print(f"{queue=}")
        # print(f"{polish=}")
        if i == ")":
            op = queue.pop()
            while op != "(":
                polish.append(op)
                op = queue.pop()
        # si es operador meter en queue
        elif i in operators:
            queue.append(i)
        # si es otro meter en polish
        else:
            polish.append(i)

    # append the last operand when finishing if expression not englobed by parenthesis
    if queue:
        polish.append(queue.pop())
    
    return polish