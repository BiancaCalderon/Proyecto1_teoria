import json

# Definir precedencias y operadores
precedence = {'*': 3, '.': 2, '|': 1}
operators = {'*', '.', '|'}
output = []
stack = []

# Clase para representar un estado en el NFA
class State:
    def __init__(self, name):
        self.name = name
        self.transitions = {}

    def add_transition(self, symbol, state):
        if symbol in self.transitions:
            self.transitions[symbol].append(state)
        else:
            self.transitions[symbol] = [state]

# Clase para representar el NFA (autómata finito no determinista)
class NFA:
    def __init__(self, start, end):
        self.start = start
        self.end = end

# Crear un nuevo estado
state_count = 0
def new_state():
    global state_count
    state = State(f'q{state_count}')
    state_count += 1
    return state

# Implementación del algoritmo de Thompson para construir el NFA a partir de una expresión postfix
def thompson_construction(postfix):
    stack = []
    states = []
    
    for token in postfix:
        if token.isalnum() or token == '_':  # Un símbolo o ε
            start = new_state()
            end = new_state()
            start.add_transition(token, end)
            states.append(start)
            states.append(end)
            stack.append(NFA(start, end))
        elif token == '*':  # Cerradura de Kleene
            nfa = stack.pop()
            start = new_state()
            end = new_state()
            start.add_transition('_', nfa.start)
            nfa.end.add_transition('_', nfa.start)
            nfa.end.add_transition('_', end)
            start.add_transition('_', end)
            states.append(start)
            states.append(end)
            stack.append(NFA(start, end))
        elif token == '.':  # Concatenación
            nfa2 = stack.pop()
            nfa1 = stack.pop()
            nfa1.end.add_transition('_', nfa2.start)
            stack.append(NFA(nfa1.start, nfa2.end))
        elif token == '|':  # Unión
            nfa2 = stack.pop()
            nfa1 = stack.pop()
            start = new_state()
            end = new_state()
            start.add_transition('_', nfa1.start)
            start.add_transition('_', nfa2.start)
            nfa1.end.add_transition('_', end)
            nfa2.end.add_transition('_', end)
            states.append(start)
            states.append(end)
            stack.append(NFA(start, end))
    
    return stack.pop(), states

# Función para agregar operadores de concatenación explícitos
def insert_concatenation_operators(regex):
    result = []
    for i in range(len(regex)):
        result.append(regex[i])
        if i + 1 < len(regex):
            if (regex[i] not in operators and regex[i] != '(' and regex[i + 1] not in operators and regex[i + 1] != ')'):
                result.append('.')
            if (regex[i] == '*' and regex[i + 1] not in operators and regex[i + 1] != ')'):
                result.append('.')
    return ''.join(result)

# Función para convertir una expresión regular a postfix (Shunting Yard)
def shunting_yard(regex):
    output.clear()
    stack.clear()
    for token in regex:
        if token not in operators and token != '(' and token != ')':
            output.append(token)
        elif token == '(':
            stack.append(token)
        elif token == ')':
            while stack and stack[-1] != '(':
                output.append(stack.pop())
            stack.pop()
        else:
            while stack and stack[-1] != '(' and precedence[token] <= precedence[stack[-1]]:
                output.append(stack.pop())
            stack.append(token)
    
    while stack:
        output.append(stack.pop())
    
    return ''.join(output)

# Función para generar la matriz de adyacencia
def generate_adjacency_matrix(states):
    state_names = [state.name for state in states]
    matrix_size = len(states)
    matrix = [['-' for _ in range(matrix_size)] for _ in range(matrix_size)]
    
    for i, state in enumerate(states):
        for symbol, transitions in state.transitions.items():
            for target in transitions:
                j = state_names.index(target.name)
                matrix[i][j] = symbol if symbol != '_' else 'ε'
    
    return matrix

# Función para imprimir la matriz de adyacencia
def print_adjacency_matrix(matrix, states):
    state_names = [state.name for state in states]
    header = '   ' + '  '.join(state_names)
    print(header)
    for i, row in enumerate(matrix):
        print(state_names[i], ' '.join(row))

# Función para guardar el resultado en un archivo JSON
def save_postfix_to_json(postfix, filename):
    data = {
        "postfix": postfix
    }
    with open(filename, 'w') as file:
        json.dump(data, file, indent=4)

# Solicitar al usuario que ingrese una expresión regular
regex = input("Ingresa una expresión regular (usa '_' para ε): ")

# Insertar operadores de concatenación explícitos
regex = insert_concatenation_operators(regex)

# Convertir la expresión regular a postfix
postfix = shunting_yard(regex)

# Mostrar el resultado
print("Postfix:", postfix)

# Guardar el resultado en un archivo JSON
save_postfix_to_json(postfix, 'postfix_output.json')
print("El resultado ha sido guardado en 'postfix_output.json'")

# Construir el NFA usando el algoritmo de Thompson
nfa, states = thompson_construction(postfix)

# Generar y mostrar la matriz de adyacencia
print("AFN construido.")
adjacency_matrix = generate_adjacency_matrix(states)
print("Matriz de adyacencia:")
print_adjacency_matrix(adjacency_matrix, states)


