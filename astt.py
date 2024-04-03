from dataclasses import dataclass
from enum import Enum
from typing import List

class NodeType(Enum):
    "Program"
    "NumericalLiteral"
    "Identifier"
    "BinaryExpr"

@dataclass
class Statement:
    kind: NodeType
    
@dataclass    
class Program(Statement):
    kind = "Program" 
    body: List[Statement]
    
@dataclass  
class Expression(Statement):
    pass
@dataclass
class BinaryExpression(Expression):
    kind = "BinaryExpr"
    left: Expression
    right: Expression
    operator: str

@dataclass
class Identifier(Expression):
    kind = "Identifier"
    symbol: str

@dataclass
class NumericalLiteral(Expression):
    kind = "NumericalLiteral"
    value: int

