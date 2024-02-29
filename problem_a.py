# Define the constraints
def c1(a, b, c, d, e, f):
    return a == b + c + e + f

def c2(a, b, c, d, e, f):
    return f > e - b

def c3(a, b, c, d, e, f):
    return d == e + f + 21

def c4(a, b, c, d, e, f):
    return d ** 2 == e ** 2 * a + 694

# Define the backtracking function
def backtrack_A(assignment, variables):
    if len(assignment) == len(variables):
        return assignment

    var = select_unassigned_variable(variables, assignment)
    domain = order_domain_values(var, assignment)

    for value in domain:
        assignment[var] = value

        if is_consistent(assignment):
            result = backtrack_A(assignment, variables)
            if result is not None:
                return result

        del assignment[var]

    return None

# Helper functions for backtracking
def select_unassigned_variable(variables, assignment):
    for var in variables:
        if var not in assignment:
            return var

def order_domain_values(var, assignment):
    values = [i for i in range(1, 126)]
    return values

def is_consistent(assignment):
    a = assignment.get('A')
    b = assignment.get('B')
    c = assignment.get('C')
    d = assignment.get('D')
    e = assignment.get('E')
    f = assignment.get('F')

    if a is not None and b is not None and c is not None and d is not None and e is not None and f is not None:
        if not c1(a, b, c, d, e, f):
            return False
        if not c2(a, b, c, d, e, f):
            return False
        if not c3(a, b, c, d, e, f):
            return False
        if not c4(a, b, c, d, e, f):
            return False

    return True

# Run the backtracking function
variables_A = ['A', 'B', 'C', 'D', 'E', 'F']
assignment_A = {}
solution_A = backtrack_A(assignment_A, variables_A)

if solution_A is not None:
    print("Solution found:")
    print(solution_A)
    print("Number of variable assignments:", len(solution_A))
else:
    print("No solution found.")
