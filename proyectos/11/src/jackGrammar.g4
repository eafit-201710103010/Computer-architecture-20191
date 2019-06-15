grammar jackGrammar;


classes   : 'class' className '{' classVarDec* subroutineDec*'}';
classVarDec : ('static'|'field') types varName (','varName)* ';';
types    : 'int'|'char'|'boolean'|className;
subroutineDec   : ('constructor'|'function'|'method') ('void'|types)subroutineName '('parameterList')' subroutineBody;
parameterList: ((types varName) (',' types varName)*)?;
subroutineBody: '{'varDec* statements'}';
varDec: 'var'types varName(','varName)*';';
className   : IDENTIFIER;
subroutineName  : IDENTIFIER;
varName : IDENTIFIER;



statements  : statement*;
statement   : letStatement |ifStatement|whileStatement|doStatement|returnStatement;
letStatement : 'let' varName ('[' expression ']')? '=' expression ';' ; 
ifStatement : 'if' '(' expression ')' '{' statements '}' ('else' '{' statements '}')? ;
whileStatement  : 'while''('expression')''{'statements'}';
doStatement : 'do' subroutineCall';';
returnStatement : 'return' expression? ';';



expression  : term(op term)*;
term    : INTEGERCONSTANT | STRINGCONSTANT | keywordconstant | varName
           |varName '['expression']'|subroutineCall|'(' expression')'|unaryop term;
subroutineCall  : subroutineName '('expressionList')' | (className | varName)'.' 
                subroutineName '('expressionList')';
expressionList  : (expression(','expression)*)?;
  
op  : '+'|'-'|'*'|'/'|'&'|'|'|'<'|'>'|'=';
unaryop : '-'|'~';
keywordconstant : 'true'|'false'|'null'|'this';

KEYWORD : 'class'|'constructor'|'function'|'method'|'field'|'static'|'var'|'int'|
          'char'|'boolean'|'void'|'true'|'false'|'null'|'this'|'let'|'do'|'if'|
          'else'|'while'|'return' ;
SYMBOL  : '{'|'}'|'('|')'|'['|']'|'.'|','|';'|'+'|'-'|'*'|'/'|'&'|'|'|'<'|'>'|
          '='|'~';
INTEGERCONSTANT : ('1'..'9')('0'..'9')* | '0';
STRINGCONSTANT  : '"' ~('"'|'\n')* '"';
IDENTIFIER  :  ('A'..'Z'|'a'..'z'|'_') ('A'..'Z'|'a'..'z'|'0'..'9'|'_')*;
WHITESPACE  : (' ' | '\t') -> skip ;
NEWLINE : ('\r'? '\n' | '\r')+ -> skip ; 
COMMENT : ('/*' .*? '*/' | '/**' .*? '*/' | '//' ~[\r\n]* '\r'? '\n') ->skip ;   
