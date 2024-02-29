def satisfies_constraint(A, B, C, D, E, F, G, H, I, J):
    # Constraint (C5)
    if H*J + E*16 != (G+I)**2 - 48:
        return False

    # Constraint (C6)
    if A-C != (H-F)**2 + 4:
        return False

    # Constraint (C7)
    if 4*J != G**2 + 7:
        return False

    # Constraint (C8)
    if H+I >= D:
        return False

    # Constraint (C9)
    if E**2 >= G**2 + J**2:
        return False

    # All constraints are satisfied
    return True


def solve_problem_B():
    # Define the domains for the variables
    domain = range(1, 126)

    # Define the variables
    variables = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"]

    # Initialize the assignments dictionary with empty assignments for each variable
    assignments = {var: None for var in variables}

    # Start the backtracking search
    return backtrack_search(assignments, domain)


def backtrack_search(assignments, domain):
    # Check if all variables have been assigned a value
    if all(assignments.values()):
        # Check if the current assignment satisfies all constraints
        if satisfies_constraint(*list(assignments.values())):
            # Return the valid assignment
            return assignments
        else:
            # Backtrack
            return None

    # Select the next unassigned variable
    var = next((var for var, val in assignments.items() if val is None), None)

    # Loop through all values in the domain for the selected variable
    for val in domain:
        # Make a copy of the current assignments dictionary
        new_assignments = dict(assignments)

        # Assign the value to the selected variable
        new_assignments[var] = val

        # Check if the new assignment satisfies all constraints
        if satisfies_constraint(*list(new_assignments.values())):
            # Recursively search for a solution with the new assignment
            result = backtrack_search(new_assignments, domain)
            if result is not None:
                # A solution was found, so return it
                return result

    # No solution was found with the current assignments, so backtrack
    return None


# Call the solve_problem_B function to find a solution to Problem B
    solution = solve_problem_B()

    # Print the solution
    if solution is not None:
        print("Solution found:")
        for var, val in solution.items():
            print(var, "=", val)
    else:
        print("No solution found.")
