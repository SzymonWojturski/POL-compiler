# Generated from POL.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .POLParser import POLParser
else:
    from POLParser import POLParser

# This class defines a complete listener for a parse tree produced by POLParser.
class POLListener(ParseTreeListener):

    # Enter a parse tree produced by POLParser#program.
    def enterProgram(self, ctx:POLParser.ProgramContext):
        pass

    # Exit a parse tree produced by POLParser#program.
    def exitProgram(self, ctx:POLParser.ProgramContext):
        pass


    # Enter a parse tree produced by POLParser#block.
    def enterBlock(self, ctx:POLParser.BlockContext):
        pass

    # Exit a parse tree produced by POLParser#block.
    def exitBlock(self, ctx:POLParser.BlockContext):
        pass


    # Enter a parse tree produced by POLParser#instruction.
    def enterInstruction(self, ctx:POLParser.InstructionContext):
        pass

    # Exit a parse tree produced by POLParser#instruction.
    def exitInstruction(self, ctx:POLParser.InstructionContext):
        pass


    # Enter a parse tree produced by POLParser#variable_declaration.
    def enterVariable_declaration(self, ctx:POLParser.Variable_declarationContext):
        pass

    # Exit a parse tree produced by POLParser#variable_declaration.
    def exitVariable_declaration(self, ctx:POLParser.Variable_declarationContext):
        pass


    # Enter a parse tree produced by POLParser#function_definition.
    def enterFunction_definition(self, ctx:POLParser.Function_definitionContext):
        pass

    # Exit a parse tree produced by POLParser#function_definition.
    def exitFunction_definition(self, ctx:POLParser.Function_definitionContext):
        pass


    # Enter a parse tree produced by POLParser#parameter.
    def enterParameter(self, ctx:POLParser.ParameterContext):
        pass

    # Exit a parse tree produced by POLParser#parameter.
    def exitParameter(self, ctx:POLParser.ParameterContext):
        pass


    # Enter a parse tree produced by POLParser#loop.
    def enterLoop(self, ctx:POLParser.LoopContext):
        pass

    # Exit a parse tree produced by POLParser#loop.
    def exitLoop(self, ctx:POLParser.LoopContext):
        pass


    # Enter a parse tree produced by POLParser#for_loop.
    def enterFor_loop(self, ctx:POLParser.For_loopContext):
        pass

    # Exit a parse tree produced by POLParser#for_loop.
    def exitFor_loop(self, ctx:POLParser.For_loopContext):
        pass


    # Enter a parse tree produced by POLParser#while_loop.
    def enterWhile_loop(self, ctx:POLParser.While_loopContext):
        pass

    # Exit a parse tree produced by POLParser#while_loop.
    def exitWhile_loop(self, ctx:POLParser.While_loopContext):
        pass


    # Enter a parse tree produced by POLParser#do_while_loop.
    def enterDo_while_loop(self, ctx:POLParser.Do_while_loopContext):
        pass

    # Exit a parse tree produced by POLParser#do_while_loop.
    def exitDo_while_loop(self, ctx:POLParser.Do_while_loopContext):
        pass


    # Enter a parse tree produced by POLParser#expression.
    def enterExpression(self, ctx:POLParser.ExpressionContext):
        pass

    # Exit a parse tree produced by POLParser#expression.
    def exitExpression(self, ctx:POLParser.ExpressionContext):
        pass


    # Enter a parse tree produced by POLParser#function_execution.
    def enterFunction_execution(self, ctx:POLParser.Function_executionContext):
        pass

    # Exit a parse tree produced by POLParser#function_execution.
    def exitFunction_execution(self, ctx:POLParser.Function_executionContext):
        pass


    # Enter a parse tree produced by POLParser#conditional.
    def enterConditional(self, ctx:POLParser.ConditionalContext):
        pass

    # Exit a parse tree produced by POLParser#conditional.
    def exitConditional(self, ctx:POLParser.ConditionalContext):
        pass


    # Enter a parse tree produced by POLParser#condition.
    def enterCondition(self, ctx:POLParser.ConditionContext):
        pass

    # Exit a parse tree produced by POLParser#condition.
    def exitCondition(self, ctx:POLParser.ConditionContext):
        pass


    # Enter a parse tree produced by POLParser#output.
    def enterOutput(self, ctx:POLParser.OutputContext):
        pass

    # Exit a parse tree produced by POLParser#output.
    def exitOutput(self, ctx:POLParser.OutputContext):
        pass


    # Enter a parse tree produced by POLParser#variable_value_change.
    def enterVariable_value_change(self, ctx:POLParser.Variable_value_changeContext):
        pass

    # Exit a parse tree produced by POLParser#variable_value_change.
    def exitVariable_value_change(self, ctx:POLParser.Variable_value_changeContext):
        pass


    # Enter a parse tree produced by POLParser#return_.
    def enterReturn_(self, ctx:POLParser.Return_Context):
        pass

    # Exit a parse tree produced by POLParser#return_.
    def exitReturn_(self, ctx:POLParser.Return_Context):
        pass


    # Enter a parse tree produced by POLParser#literal.
    def enterLiteral(self, ctx:POLParser.LiteralContext):
        pass

    # Exit a parse tree produced by POLParser#literal.
    def exitLiteral(self, ctx:POLParser.LiteralContext):
        pass


    # Enter a parse tree produced by POLParser#unary_expression.
    def enterUnary_expression(self, ctx:POLParser.Unary_expressionContext):
        pass

    # Exit a parse tree produced by POLParser#unary_expression.
    def exitUnary_expression(self, ctx:POLParser.Unary_expressionContext):
        pass


    # Enter a parse tree produced by POLParser#arithmetic_expression.
    def enterArithmetic_expression(self, ctx:POLParser.Arithmetic_expressionContext):
        pass

    # Exit a parse tree produced by POLParser#arithmetic_expression.
    def exitArithmetic_expression(self, ctx:POLParser.Arithmetic_expressionContext):
        pass


    # Enter a parse tree produced by POLParser#operator.
    def enterOperator(self, ctx:POLParser.OperatorContext):
        pass

    # Exit a parse tree produced by POLParser#operator.
    def exitOperator(self, ctx:POLParser.OperatorContext):
        pass


    # Enter a parse tree produced by POLParser#comparison_operator.
    def enterComparison_operator(self, ctx:POLParser.Comparison_operatorContext):
        pass

    # Exit a parse tree produced by POLParser#comparison_operator.
    def exitComparison_operator(self, ctx:POLParser.Comparison_operatorContext):
        pass


    # Enter a parse tree produced by POLParser#type.
    def enterType(self, ctx:POLParser.TypeContext):
        pass

    # Exit a parse tree produced by POLParser#type.
    def exitType(self, ctx:POLParser.TypeContext):
        pass


    # Enter a parse tree produced by POLParser#identifier.
    def enterIdentifier(self, ctx:POLParser.IdentifierContext):
        pass

    # Exit a parse tree produced by POLParser#identifier.
    def exitIdentifier(self, ctx:POLParser.IdentifierContext):
        pass


    # Enter a parse tree produced by POLParser#integer.
    def enterInteger(self, ctx:POLParser.IntegerContext):
        pass

    # Exit a parse tree produced by POLParser#integer.
    def exitInteger(self, ctx:POLParser.IntegerContext):
        pass


    # Enter a parse tree produced by POLParser#float.
    def enterFloat(self, ctx:POLParser.FloatContext):
        pass

    # Exit a parse tree produced by POLParser#float.
    def exitFloat(self, ctx:POLParser.FloatContext):
        pass


    # Enter a parse tree produced by POLParser#char.
    def enterChar(self, ctx:POLParser.CharContext):
        pass

    # Exit a parse tree produced by POLParser#char.
    def exitChar(self, ctx:POLParser.CharContext):
        pass


    # Enter a parse tree produced by POLParser#string.
    def enterString(self, ctx:POLParser.StringContext):
        pass

    # Exit a parse tree produced by POLParser#string.
    def exitString(self, ctx:POLParser.StringContext):
        pass


    # Enter a parse tree produced by POLParser#boolean.
    def enterBoolean(self, ctx:POLParser.BooleanContext):
        pass

    # Exit a parse tree produced by POLParser#boolean.
    def exitBoolean(self, ctx:POLParser.BooleanContext):
        pass



del POLParser