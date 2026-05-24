grammar MiniPython;

// Reglas sintácticas (Parser)
program    : functionDef* EOF ;

functionDef: 'fn' ID '(' paramList? ')' block ;

paramList  : ID (',' ID)* ;

block      : '{' statement* '}' ;

statement  : ifStat
           | returnStat ';'
           | printStat ';'
           | expr ';' 
           ;

ifStat     : 'if' '(' expr ')' block ('else' block)? ;

returnStat : 'return' expr ;

printStat  : 'print' '(' expr (',' expr)* ')' ;

expr       : ID
           | INT
           | STRING
           | expr op=('>' | '<' | '==' | '+') expr
           ;

// Reglas léxicas (Lexer)
ID         : [a-zA-Z_][a-zA-Z0-9_]* ;
INT        : [0-9]+ ;
STRING     : '"' (~[\r\n"])* '"' ;

WS         : [ \t\r\n]+ -> skip ; // Ignora espacios y saltos de línea