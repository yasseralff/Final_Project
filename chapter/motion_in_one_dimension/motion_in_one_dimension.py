import re
import math


def solve_physics_problem(problem_statement):
    # Define regular expressions to identify different types of physics problems
    circular_regex = r'circular motion'
    projectile_regex = r'projectile motion'
    force_regex = r'forces?|newton\'s laws'

    # Determine the type of problem
    problem_type = None
    if re.search(circular_regex, problem_statement, re.IGNORECASE):
        problem_type = 'circular'
    elif re.search(projectile_regex, problem_statement, re.IGNORECASE):
        problem_type = 'projectile'
    elif re.search(force_regex, problem_statement, re.IGNORECASE):
        problem_type = 'forces'

    # Solve the problem based on its type
    if problem_type == 'circular':
        # Extract variables from the problem statement
        radius_regex = r'radius\s*=\s*([\d\.]+)\s*(\w+)'
        angular_velocity_regex = r'angular velocity\s*=\s*([\d\.]+)\s*(\w+)'
        radius_match = re.search(radius_regex, problem_statement, re.IGNORECASE)
        angular_velocity_match = re.search(angular_velocity_regex, problem_statement, re.IGNORECASE)

        # Check if the necessary variables were found
        if not radius_match or not angular_velocity_match:
            return "Error: Required variables not found in problem statement", radius_match, angular_velocity_match

        # Extract numeric values and units
        radius = float(radius_match.group(1))
        radius_unit = radius_match.group(2)
        angular_velocity = float(angular_velocity_match.group(1))
        angular_velocity_unit = angular_velocity_match.group(2)

        # Check units and convert if necessary
        if radius_unit == 'cm':
            radius /= 100
        elif radius_unit == 'mm':
            radius /= 1000
        elif radius_unit == 'ft':
            radius *= 0.3048
        elif radius_unit == 'yd':
            radius *= 0.9144
        if angular_velocity_unit == 'rpm':
            angular_velocity *= math.pi / 30

        # Calculate and return the solution
        acceleration = (angular_velocity ** 2) * radius
        return f"The centripetal acceleration is {acceleration:.2f} m/s^2."

    elif problem_type == 'projectile':
        # TODO: Implement projectile motion problem solver
        return "Projectile motion problems not yet supported."

    elif problem_type == 'forces':
        # TODO: Implement forces and Newton's laws problem solver
        return "Forces and Newton's laws problems not yet supported."

    else:
        return "Error: Problem type not recognized"


# Example usage
problem_statement = "A car is traveling in a circular motion with a radius = 2 meters at an angular velocity = 10 rad/s. What is the centripetal acceleration of the car?"
solution = solve_physics_problem(problem_statement)
print(solution)
print(type(problem_statement))