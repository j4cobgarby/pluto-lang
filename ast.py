class Node(object):
    def literal(self):
        return self.token.literal
        

class Statement(Node): pass
class Expression(Node): pass
        
        
tree_indent = 2


def _(amount):
    return " " * tree_indent * amount
    
    
def n(name):
    return "" if name == "" else name + " ‣ "
    

def make_list_tree(indent, list, name = ""):
    string = "%s [" % _(indent) + n(name)
    
    for item in list:
        string += "\n%s%s" % (
            _(indent),
            item.tree(indent + 1, "")
        )
        
    return "string\n%s]" % _(indent)
    

class Program(object):    
    """a program. contains a list of statements to be executed"""
    def __init__(self, statements = []):
        self.statements = statements
        
    def tree(self):
        return "program\n" + "".join(stmt.tree(1) + "\n" for stmt in self.statements)
        
        
## Expressions ##

class Identifier(Expression):
    """an identifier node"""
    def __init__(self, token):
        self.token = token
        self.value = token.literal
        
    def tree(self, indent, name = ""):
        return "%s%s" % (_(indent) + n(name), self.value)
        

class Number(Expression):
    """a number literal node"""
    def __init__(self, token, value):
        self.token = token
        self.value = value
        
    def tree(self, indent, name = ""):
        return "%s%s" % (_(indent) + n(name), self.value)
        

class Boolean(Expression):
    """a boolean literal node"""
    def __init__(self, token, value):
        self.token = token
        self.value = value
        
    def tree(self, indent, name = ""):
        return "%s%s" % (_(indent) + n(name), str(self.value).lower())
        
        
class Null(Expression):
    """a null literal node"""
    def __init__(self, token):
        self.token = token
        
    def tree(self, indent, name = ""):
        return "%snull" % _(indent) + n(name)
        
        
class Array(Expression):
    """an array literal: [a, b, ..., n]"""
    def __init__(self, token, elements):
        self.token = token
        self.elements = elements
        
    def tree(self, indent, name = ""):
        return "%sarray\n%s" % (
            _(indent) + n(name),
            make_list_tree(indent + 1, self.elements, "elements")
        )
        
        
class AssignExpression(Expression):
    """an assign expression"""
    def __init__(self, token, name, value):
        self.token = token
        self.name = name
        self.value = value
        
    def tree(self, indent, name = ""):
        return "%sassign\n%s\n%s" % (
            _(indent) + n(name),
            self.name.tree(indent + 1, "name"),
            self.value.tree(indent + 1, "value")
        )
        
        
class PrefixExpression(Expression):
    """a prefix operator expression"""
    def __init__(self, token, operator, right):
        self.token = token
        self.operator = operator
        self.right = right

    def tree(self, indent, name = ""):
        return "%sprefix (%s)\n%s" % (
            _(indent) + n(name),
            self.operator,
            self.right.tree(indent + 1, "right")
        )
        
        
class Parameter(Expression):
    """a parameter in a function definition"""
    def __init__(self, name):
        self.name = name
        
    def tree(self, indent, name = ""):
        return "%s<%s>" % (_(indent) + n(name), self.name)
        
        
class Argument(Expression):
    """an argument in a function call"""
    def __init__(self, value):
        self.value = value
        
    def tree(self, indent, name = ""):
        return "%sarg\n%s" % (
            _(indent) + n(name),
            self.value.tree(indent + 1, "value")
        )
        
        
class FunctionCall(Expression):
    """calls a function, using a pattern"""
    def __init__(self, pattern):
        self.pattern = pattern
        
    def tree(self, indent, name = ""):
        return "%sfn call\n%s" % (
            _(indent) + n(name),
            make_list_tree(indent + 1, self.pattern, "pattern")
        )
        
        
## Statements ##
        
class ExpressionStatement(Statement):
    """a statement containing a single expression"""
    def __init__(self, token, expr):
        self.token = token
        self.expr = expr
    
    def tree(self, indent, name = ""):
        expr = "none" if self.expr == None else self.expr.tree(indent + 1)
        return "%sexpression statement\n%s" % (_(indent) + n(name), expr)
        
        
class ReturnStatement(Statement):
    """returns a value from a function"""
    def __init__(self, token, expr):
        self.token = token
        self.expr = expr
        
    def tree(self, indent, name = ""):
        return "%sreturn\n%s" % (
            _(indent) + n(name),
            self.expr.tree(indent + 1, "expr")
        )


class BlockStatement(Statement):
    """a list of statements"""
    def __init__(self, token, statements = []):
        self.token = token
        self.statements = statements
    
    def tree(self, indent, name = ""):
        return make_list_tree(indent, self.statements, "statements")
        
        
class FunctionDefinition(Statement):
    """
        defines a function.
        the pattern is an array, where each
        element is either an Identifier or
        a Parameter
    """
    def __init__(self, pattern, body):
        self.pattern = pattern
        self.body = body
        
    def tree(self, indent, name = ""):
        return "%sfunction\n%s\n%s" % (
            _(indent) + n(name),
            make_list_tree(indent + 1, self.pattern, "pattern"),
            self.body.tree(indent + 1, "body")
        )
        
        
class IfStatement(Statement):
    """an if statement"""
    def __init__(self, token, condition, consequence, alternative):
        self.token = token
        self.condition = condition
        self.consequence = consequence
        self.alternative = alternative
        
    def tree(self, indent, name = ""):
        return "%sif stmt\n%s\n%s\n%s" % (
            _(indent) + n(name),
            self.condition.tree(indent + 1, "condition"),
            self.consequence.tree(indent + 1, "consequence"),
            self.alternative.tree(indent + 1, "alternative")
        )
        