import re
import math
# import numpy as np

with open('keywords.txt', 'r') as f:
    circular_keywords = [line.strip() for line in f.readlines()]

with open('keywords2.txt', 'r') as f:
    projectile_keywords = [line.strip() for line in f.readlines()]

with open('keywords3.txt', 'r') as f:
    force_keywords = [line.strip() for line in f.readlines()]

class AngularMomentum:
    def __init__(self):
        pass

    def problem_type(self, problem_statement):
        problem_type = None

        # Check for circular-related problems
        for keyword in circular_keywords:
            if re.search(keyword, problem_statement, re.IGNORECASE):
                problem_type = 'circular'
                break

        # Check for projectile-related problems
        if not problem_type:
            for keyword in projectile_keywords:
                if re.search(keyword, problem_statement, re.IGNORECASE):
                    problem_type = 'projectile'
                    break

        # Check for force-related problems
        if not problem_type:
            for keyword in force_keywords:
                if re.search(keyword, problem_statement, re.IGNORECASE):
                    problem_type = 'forces'
                    break

        return problem_type


    def getCircular(self, problem_statement):
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

    def getProjectile(self):
        pass

    def getForces(self):
        pass

    def solve_physics_problem(self, problem_statement):
        problem_type = self.problem_type(problem_statement)
        # Solve the problem based on its type
        if problem_type == 'circular':
            return self.getCircular(problem_statement)

        elif problem_type == 'projectile':
            # TODO: Implement projectile motion problem solver
            return "Projectile motion problems not yet supported."

        elif problem_type == 'forces':
            # TODO: Implement forces and Newton's laws problem solver
            return "Forces and Newton's laws problems not yet supported."

        else:
            return "Error: Problem type not recognized"


# Example usage
# problem_statement = "A car is traveling in a circular path with a radius = 2 meters at an angular velocity = 10 rad/s. What is the centripetal acceleration of the car?"
problem_statement = "n the Bohr model of the hydrogen atom, an electron \
moves in a around a proton. The speed \
of the electron is approximately angular velocity = 106 m/s. Find \
(a) the force acting on the electron as it revolves  in a \ of radius = 10210m and (b) the centripetal acceleration of the electron."
am = AngularMomentum()
solution = am.solve_physics_problem(problem_statement)
print(solution)
print(am.problem_type(problem_statement))
