from enum import Enum
from typing import List

class TokenType(Enum):
    Number = 0
    Identifier = 1
    Equals = 2
    OpenParen = 3
    CloseParen = 4
    BinaryOperator = 5
    Let = 6
KEYWORDS = {}
KEYWORDS["let"] = TokenType.Let

class Token:
    def __init__(self, value: str, Ttype: TokenType) -> None:
        self.value = value
        self.Ttype = Ttype

    def __str__(self) -> str:
        return f'Token({self.value}, {self.Ttype})'
    
    def __repr__(self) -> str:
        return f'(\'{self.value}\', {self.Ttype})'
    
def isint(str: str) -> bool:
    bounds = (ord("0"), ord("9"))
    return ord(str) >= bounds[0] and ord(str) <= bounds[1]

def isalp(str: str) -> bool:
    return str.upper != str.lower

def isignorable(str: str) -> bool:
    return str == ' ' or str == '\n' or str == '\t'
    
def tokenize(sourceCode: str) -> List[Token]:
    tokens = []
    src = list(sourceCode)

    while len(src):
        match src[0]:
            case "(":
                token = Token(src.pop(0), TokenType.OpenParen)
                tokens.append(token)
            case ")":
                token = Token(src.pop(0), TokenType.CloseParen)
                tokens.append(token)
            case "-" | "+" | "*" | "/":
                token = Token(src.pop(0), TokenType.BinaryOperator)
                tokens.append(token)
            case "=":
                token = Token(src.pop(0), TokenType.Equals)
                tokens.append(token)
            case _:
                #Handles multi-character tokens.

                if isignorable(src[0]):
                    src.pop(0)
                    continue

                elif isint(src[0]):
                    num = ''
        
                    while len(src) > 0 and isint(src[0]) and src[0] != ' ':
                        num += src.pop(0)

                    token = Token(num, TokenType.Number)
                    tokens.append(token)
                
                elif isalp(src[0]):
                    ident = ''
                    
                    while len(src) > 0 and isalp(src[0]) and src[0] != ' ':
                        ident += src.pop(0)


                    reserved = KEYWORDS.get(ident)
                    if reserved is None:
                        token = Token(ident, TokenType.Identifier)
                        tokens.append(token)
                    else:
                        token = Token(ident, reserved)
                        tokens.append(token)
                else:
                    raise ValueError(f"Unrecognized Character: {src[0]}")
                
    return tokens
