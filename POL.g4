grammar POL;
// - - - Scanner rules - - -
VARRIABLE:'niech';
BE:'będzie';
ASSIGN:'równe';
EOS:';';
FUNCTION:'niech będzie funkcja zwracająca';
BE_NAMED:'nazywa się';
LPAREN: '(';
RPAREN: ')';
LBRACKET: '[';
RBRACKET: ']';
BEGIN: '{';
END: '}';
COMMA: ',';
DOT:'.';

FOR:'dla';
START:'należącego od';
FINISH:'do';
WHILE:'Dopóki';
DO:'wykonnuj';
LOWER_CASE_WHILE:'dopóki';

IF:'jeżeli';
ELSE:'w przeciwnym wypadku';

PRINTF:'wypisz na konsolę';
CHANGE:'zmień';
TO:'na';

RETURN_:'zwróć';

PLUS: '+';
MINUS: '-';
MULT: '*';
DIV: '/';
LT: 'większe od';
GT: 'mniejsze od';
LOE: 'większe bądź równe od';
GOE: 'mniejsze bądź równe od';
EQ: 'wynosi';
NEQ: 'różne od';

INT: 'liczba całkowita';
FLOAT: 'liczba zmiennoprzecinkowa';
CHAR:'znak';
STR: 'łańcuch znaków';
BOOL: 'wartość logiczna';

UPPER_CASE_LETTER: [A-Z];
LOWER_CASE_LETTER: [a-z];
LETTER:(UPPER_CASE_LETTER|LOWER_CASE_LETTER);
NUMBER: [0-9];
WS: [\t\r\n ]+ -> skip;

// - - - Parser rules - - -
program: (instruction)+;

block: (instruction)+;

instruction
    :variable_declaration
    |function_definition
    |loop
    |conditional
    |output
    |variable_value_change
    |return_
    ;
variable_declaration: VARRIABLE identifier BE type ASSIGN arithmetic_expression EOS;

function_definition: FUNCTION type BE_NAMED identifier LPAREN (parameter (COMMA parameter)*)? RPAREN BEGIN block END;

function_execution:identifier LPAREN (parameter (COMMA parameter)*)? RPAREN ;

parameter:type identifier;

loop
    : for_loop
    | while_loop
    | do_while_loop
    ;

for_loop: FOR identifier START expression FINISH expression BEGIN block END;
while_loop: WHILE condition BEGIN block END;
do_while_loop: DO BEGIN block END LOWER_CASE_WHILE condition ;

expression
    :arithmetic_expression
    |identifier
    |function_execution
    ;


conditional: IF condition BEGIN block END (ELSE BEGIN block END)?;
condition: expression comparison_operator expression;

output: PRINTF LPAREN expression RPAREN;

variable_value_change: CHANGE identifier TO expression EOS;

return_: RETURN_ expression EOS;

literal
    :integer
    |float
    |char
    |string
    |boolean
    ;

unary_expression
    : literal
    | MINUS literal
    | identifier
    ;

arithmetic_expression
    :unary_expression
    |operator arithmetic_expression arithmetic_expression
    ;

operator
    : PLUS
    | MINUS
    | MULT
    | DIV
    ;

comparison_operator
    :LT
    |GT
    |EQ
    |NEQ
    |LOE
    |GOE
    ;

type
    :INT
    |FLOAT
    |CHAR
    |STR
    |BOOL
    ;

identifier: UPPER_CASE_LETTER (LOWER_CASE_LETTER|NUMBER)* ;
//LITERALS
integer:NUMBER+;
float:NUMBER+ DOT NUMBER*;
char: '\''LETTER'\'';
string: '"'LETTER*'"';
boolean: 'prawda'|'fałsz';

