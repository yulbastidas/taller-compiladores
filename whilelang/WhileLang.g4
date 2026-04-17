grammar WhileLang;

program: statement+ EOF;

statement
    : declaration
    | assignment
    | ifStatement
    | whileStatement
    | BREAK SEMI
    | CONTINUE SEMI
    ;

declaration
    : type ID (ASSIGN expr)? SEMI
    ;

type
    : INT_TYPE
    | STRING_TYPE
    ;

assignment
    : ID ASSIGN expr SEMI
    ;

ifStatement
    : IF LPAREN expr RPAREN LBRACE statement* RBRACE
      (ELSE LBRACE statement* RBRACE)?
    ;

whileStatement
    : WHILE LPAREN expr RPAREN LBRACE statement* RBRACE
    ;

// 👇 EXPRESIONES CON ETIQUETAS (MUY IMPORTANTE)
expr
    : ID                                       # idExpr
    | NUMBER                                   # numberExpr
    | STRING                                   # stringExpr
    | expr (LT | GT | GE | LE | EQ | NE) expr  # comparisonExpr
    | expr (PLUS | MINUS | MUL | DIV) expr     # arithmeticExpr
    | LPAREN expr RPAREN                       # parenExpr
    ;

// KEYWORDS
IF: 'if';
ELSE: 'else';
WHILE: 'while';
BREAK: 'break';
CONTINUE: 'continue';
INT_TYPE: 'int';
STRING_TYPE: 'string';

// SYMBOLS
LPAREN: '(';
RPAREN: ')';
LBRACE: '{';
RBRACE: '}';
SEMI: ';';
ASSIGN: '=';

// OPERADORES
GE: '>=';
LE: '<=';
EQ: '==';
NE: '!=';
LT: '<';
GT: '>';

PLUS: '+';
MINUS: '-';
MUL: '*';
DIV: '/';

// LITERALES
STRING: '"' (~["\r\n])* '"';
ID: [a-zA-Z_][a-zA-Z_0-9]*;
NUMBER: [0-9]+;

// IGNORAR
COMMENT: '//' ~[\r\n]* -> skip;
WS: [ \t\r\n]+ -> skip;