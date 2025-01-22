import sys
from antlr4 import *
from POLLexer import POLLexer
from POLParser import POLParser
from EvalVisitor import EvalVisitor

def main(argv):
    input_file = argv[1]
    input_stream = FileStream(input_file, encoding='utf-8')

    lexer = POLLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = POLParser(stream)

    tree = parser.program()

    visitor = EvalVisitor()
    result = visitor.visit(tree)

    if result is not None:
        output_text = str(result)
        output_file = argv[2]
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(output_text)

        print(f"Translation complete. Output saved to {output_file}")
    else:
        print("Error: Visitor returned None.")

if __name__ == '__main__':
    main(sys.argv)
