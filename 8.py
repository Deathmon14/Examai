class Substitution:
    def __init__(self):
        self.substitution = {}

    def add(self, variable, term):
        self.substitution[variable] = term

    def apply(self, expression):
        if isinstance(expression, Variable):
            return self.substitution.get(expression.name, expression)
        elif isinstance(expression, Function):
            return Function(expression.name, [self.apply(arg) for arg in expression.arguments])
        else:
            return expression


class Variable:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name

    def __eq__(self, other):
        return isinstance(other, Variable) and self.name == other.name


class Function:
    def __init__(self, name, arguments):
        self.name = name
        self.arguments = arguments

    def __str__(self):
        if not self.arguments:
            return self.name
        return f"{self.name}({', '.join(map(str, self.arguments))})"

    def __eq__(self, other):
        return (
            isinstance(other, Function) and
            self.name == other.name and
            self.arguments == other.arguments
        )


def unify(expr1, expr2, substitution):
    if substitution is None:
        return None
    elif expr1 == expr2:
        return substitution
    elif isinstance(expr1, Variable):
        return unify_variable(expr1, expr2, substitution)
    elif isinstance(expr2, Variable):
        return unify_variable(expr2, expr1, substitution)
    elif isinstance(expr1, Function) and isinstance(expr2, Function):
        return unify(expr1.arguments, expr2.arguments, unify(expr1.name, expr2.name, substitution))
    else:
        return None


def unify_variable(var, expr, substitution):
    if var.name in substitution.substitution:
        return unify(substitution.substitution[var.name], expr, substitution)
    elif expr_contains_var(expr, var):
        return None
    else:
        new_substitution = Substitution()
        new_substitution.add(var.name, expr)
        substitution.substitution.update(new_substitution.substitution)
        return substitution


def expr_contains_var(expr, var):
    if expr == var:
        return True
    elif isinstance(expr, Function):
        return any(expr_contains_var(arg, var) for arg in expr.arguments)
    else:
        return False


# Example usage:
x = Variable('x')
y = Variable('y')
z = Variable('z')
f = Function('f', [x, y])
g = Function('g', [y, z])
h = Function('h', [z, x])

s = Substitution()
result = unify(f, g, s)
if result is not None:
    print(f"Unification successful: {result.apply(f)}")
else:
    print("Unification failed.")
