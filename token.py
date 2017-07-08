# etc...
EOF     = "EOF"
ILLEGAL = "ILLEGAL"

# Literals
NUM   = "number"
STR   = "string"
ID    = "identifier"
PARAM = "param"

# Punctuation
PLUS   = "plus"
MINUS  = "minus"
STAR   = "star"
SLASH  = "slash"
HASH   = "hash"
LPAREN = "lparen"
RPAREN = "rparen"
LT     = "less-than"
GT     = "greater-than"
LBRACE = "lbrace"
RBRACE = "rbrace"
SEMI   = "semi"
EQ     = "equal"
N_EQ   = "not equal"
OR     = "or"
AND    = "and"
B_OR   = "bitwise or"
B_AND  = "bitwise and"

# Keywords
DEF    = "def"
RETURN = "return"
TRUE   = "true"  
FALSE  = "false"
NULL   = "null"

class Token(object):
    """a single lexical token"""
    def __init__(self, t, literal, start = (0, 0), end = (0, 0)):
        self.type = t          # "type"
        self.literal = literal # "literal"
        self.start = start     # (line, col)
        self.end = end         # (line, col)
    
    def __str__(self):
        return "%s '%s' from %s:%s to %s:%s" % (
            self.type, self.literal,
            self.start[0], self.start[1],
            self.end[0], self.end[1]
        )
        
    def __repr__(self):
        return self.__str__()
        
keywords = {
    "def":    DEF,
    "return": RETURN,
    "true":   TRUE,
    "yes":    TRUE,
    "false":  FALSE,
    "no":     FALSE,
    "null":   NULL
}
        