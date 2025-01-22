# Generated from POL.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .POLParser import POLParser
else:
    from POLParser import POLParser

# This class defines a complete generic visitor for a parse tree produced by POLParser.

class POLVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by POLParser#program.
    def visitProgram(self, ctx:POLParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by POLParser#block.
    def visitBlock(self, ctx:POLParser.BlockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by POLParser#instruction.
    def visitInstruction(self, ctx:POLParser.InstructionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by POLParser#variable_declaration.
    def visitVariable_declaration(self, ctx:POLParser.Variable_declarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by POLParser#function_definition.
    def visitFunction_definition(self, ctx:POLParser.Function_definitionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by POLParser#parameter.
    def visitParameter(self, ctx:POLParser.ParameterContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by POLParser#loop.
    def visitLoop(self, ctx:POLParser.LoopContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by POLParser#for_loop.
    def visitFor_loop(self, ctx:POLParser.For_loopContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by POLParser#while_loop.
    def visitWhile_loop(self, ctx:POLParser.While_loopContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by POLParser#do_while_loop.
    def visitDo_while_loop(self, ctx:POLParser.Do_while_loopContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by POLParser#expression.
    def visitExpression(self, ctx:POLParser.ExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by POLParser#function_execution.
    def visitFunction_execution(self, ctx:POLParser.Function_executionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by POLParser#conditional.
    def visitConditional(self, ctx:POLParser.ConditionalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by POLParser#condition.
    def visitCondition(self, ctx:POLParser.ConditionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by POLParser#output.
    def visitOutput(self, ctx:POLParser.OutputContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by POLParser#variable_value_change.
    def visitVariable_value_change(self, ctx:POLParser.Variable_value_changeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by POLParser#return_.
    def visitReturn_(self, ctx:POLParser.Return_Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by POLParser#literal.
    def visitLiteral(self, ctx:POLParser.LiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by POLParser#unary_expression.
    def visitUnary_expression(self, ctx:POLParser.Unary_expressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by POLParser#arithmetic_expression.
    def visitArithmetic_expression(self, ctx:POLParser.Arithmetic_expressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by POLParser#operator.
    def visitOperator(self, ctx:POLParser.OperatorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by POLParser#comparison_operator.
    def visitComparison_operator(self, ctx:POLParser.Comparison_operatorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by POLParser#type.
    def visitType(self, ctx:POLParser.TypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by POLParser#identifier.
    def visitIdentifier(self, ctx:POLParser.IdentifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by POLParser#integer.
    def visitInteger(self, ctx:POLParser.IntegerContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by POLParser#float.
    def visitFloat(self, ctx:POLParser.FloatContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by POLParser#char.
    def visitChar(self, ctx:POLParser.CharContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by POLParser#string.
    def visitString(self, ctx:POLParser.StringContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by POLParser#boolean.
    def visitBoolean(self, ctx:POLParser.BooleanContext):
        return self.visitChildren(ctx)



del POLParser