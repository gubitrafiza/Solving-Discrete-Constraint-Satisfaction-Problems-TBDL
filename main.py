
def solve_a():
    variables = ['A', 'B', 'C', 'D', 'E', 'F']
    domain = range(1,126)
    assing = {var: 0 for var in variables}

    def satisfy_constraint_of_a(A, B, C, D, E, F):
        if A != B + C + E + F:
            return False
        if F <= E - B:
            return False
        if D != E + F + 21:
            return False
        if D ** 2 != E ** 2 * A + 694:
            return False
        return True

    for A in domain:
        for B in domain:
            for C in domain:
                for D in domain:
                    for E in domain:
                        for F in domain:
                            values = [A, B, C, D, E, F]
                            if satisfy_constraint_of_a(A, B, C, D, E, F):
                                return values

def solve_b():
    variables = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
    domain = range(1, 126)
    # initially assign 0 to all variables
    assign = {var: 0 for var in variables}

    def satisfies_constraint(A, B, C, D, E, F, G, H, I, J):
        # Constraint (C5)
        if H * J + E * 16 != (G + I) ** 2 - 48:
            return False

        # Constraint (C6)
        if A - C != (H - F) ** 2 + 4:
            return False

        # Constraint (C7)
        if 4 * J != G ** 2 + 7:
            return False

        # Constraint (C8)
        if H + I >= D:
            return False

        # Constraint (C9)
        if E ** 2 >= G ** 2 + J ** 2:
            return False
        # All constraints are satisfied
        return True

    def backtracking():
        A, B, C, D, E, F, G, H, I, J = [assign[v] for v in variables]
        #function to return the next item in an iterator next().
        var = next((v for v in variables if assign[v] == 0), None)
        if var is None:
            return True
        for val in domain:
            if satisfies_constraint(A, B, C, D, E, F, G, H, I, J):
                assign[var] = val

                if backtracking():
                    return True
                assign[var] = 0
        return False

    if backtracking():
        return assign
    else:
        return None


def solve_c():
    variables = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P']
    #126 becuase the variables can take numbers 1-125 inclusive, range(1,125) only goes till 124.
    domain = range(1, 126)
    #initially assign 0 to all variables
    assign = {var: 0 for var in variables}

    def satisfies_constraints(var, val):
        #assigning 0 to all variables
        A, B, C, D, E, F, G, H, I, J, K, L, M, N, O, P = [assign[v] for v in variables]
        assign[var] = val
        if var == 'A':
            return True
        elif var == 'B':
            return B != D and B != F and B != H and B != J and B != L and B != N and B != P
        elif var == 'C':
            return True
        elif var == 'D':
            return B != D and D != F and D != H and D != J and D != L and D != N and D != P
        elif var == 'E':
            return True
        elif var == 'F':
            return B != F and D != F and F != H and F != J and F != L and F != N and F != P and (N-O)**2 == (F-J)*O*2+360
        elif var == 'G':
            return True
        elif var == 'H':
            return B != H and D != H and F != H and H != J and H != L and H != N and H != P
        elif var == 'I':
            return True
        elif var == 'J':
            return (N**2-135) == M*J+A**2 and B != J and D != J and F != J and H != J and J != L and J != N and J != P
        elif var == 'K':
            return 2*M == K**2 - A*8 and K != L and K != N and K != P
        elif var == 'L':
            return K != L and J != L and L != N and L != P and (L+N)**2+445 == (B+F)*(K+M+N+(A*E))
        elif var == 'M':
            return 2*M == K**2 - A*8 and (K**3-900) == (O*F*A)+M**2
        elif var == 'N':
            return J != N and L != N and N != P and (P-N)**2-(P-O)**2 == A**2+K*L-M**2-1425
        elif var == 'O':
            return True
        elif var == 'P':
            return J != P and L != P and N != P and (P-N)**2-(P-O)**2 == A**2+K*L-M**2-1425
        else:
            return True

    #use backtracking to find a satisfiable solution
    def backtracking():
        var = next((v for v in variables if assign[v] == 0), None)
        if var is None:
            return True
        for val in domain:
            if satisfies_constraints(var, val):
                assign[var] = val
                if backtracking():
                    return True
                assign[var] = 0
        return False

    if backtracking():
        return assign
    else:
        return None

if __name__ == '__main__':



    print('Solution for Problem B:')

    sol2 = solve_b()
    # Print the solution
    if sol2 is not None:
        print("Solution found:")

        for var, val in sol2.items():
            print(var, "=", val)
    else:
        print("No solution found.")

#printing solutions for c
    print('Solution for Problem C:')

    sol3 = solve_c()
    if sol3 is not None:
        print(sol3)

    else:
        print("No solution found.")

    print('Solution for Problem A:')
    print('And this never prints :/')
    sol1 = solve_a()
    # Print the solution
    if sol1 is not None:
        print(sol1)
    else:
        print("No solution found.")
