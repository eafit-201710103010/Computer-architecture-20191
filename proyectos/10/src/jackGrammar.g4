
grammar jackGrammar;

classNT : 'class' className '{' classVarDec* subroutineDec* '}';

classVarDec : ('static' | 'field') jackType varName(',' varName)*';';

jackType : 'int' | 'char' | 'boolean' | className;

subroutineDec : ('constructor' | 'function' | 'method') ('void' | jackType) subroutineName '(' parameterList ')' subroutineBody;

parameterList :( (jackType varName) (','jackType varName)* )?;

subroutineBody : '{'varDec* statements'}';

varDec : 'var' jackType varName(',' varName)*';';

className : Identifier;

subroutineName : Identifier;

varName : Identifier;



statements : statement*;

statement : letStatement | ifStatement | whileStatement | doStatement | returnStatement;

letStatement :  'let' varName ( '['expression']' )? '=' expression ';';

ifStatement :  'if''('expression ')' '{' statements '}' ('else' '{' statements '}' )?;

whileStatement :  'while' '(' expression ')' '{' statements '}';

doStatement : 'do' subroutineCall ';';

returnStatement :  'return' expression? ';';


expression :  term(op term)*;

term : INTEGER | STRING | keywordConstant | varName | (varName'['expression']') | subroutineCall | ('('expression')') | (unaryOp term);

subroutineCall : ( subroutineName '(' expressionList ')' ) | ( className | varName ) '.' subroutineName '(' expressionList ')' ;

expressionList :  ( expression ( ',' expression )*)?;

op :  '+' | '-' | '*' | '/' | '&' | ' | ' | '<' | '>' | '=';

unaryOp :  '-' | '~';

keywordConstant :  'true' | 'false' | 'null' | 'this';


KEYWORD :  'class' | 'constructor' | 'function' | 'method' | 'field' | 'static' | 'var' | 'int' | 'char' | 'boolean' | 'void' | 'true' | 'false' | 'null' | 'this' | 'let' | 'do' | 'if' | 'else' | 'while' | 'return';
SYMBOL :  '{' | '}' | '(' | ')' | '[' | ']' | '.' | ',' | ';' | '+' | '-' | '*' | '/' | '&' | '|' | '<' | '>' | '=' | '~' | '"';
INTEGER : [0-9]+;
STRING :  ( '"' .*? '"');
COMMENT :   ( '//' ~[\r\n]* '\r'? '\n' | '/**' .*? '*/') -> skip;
Identifier :  [a-zA-Z_][a-zA-Z0-9_]*;
WHITESPACE :  [ \t\r\n]+ -> skip ;

