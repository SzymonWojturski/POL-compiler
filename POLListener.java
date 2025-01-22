// Generated from POL.g4 by ANTLR 4.13.2
import org.antlr.v4.runtime.tree.ParseTreeListener;

/**
 * This interface defines a complete listener for a parse tree produced by
 * {@link POLParser}.
 */
public interface POLListener extends ParseTreeListener {
	/**
	 * Enter a parse tree produced by {@link POLParser#program}.
	 * @param ctx the parse tree
	 */
	void enterProgram(POLParser.ProgramContext ctx);
	/**
	 * Exit a parse tree produced by {@link POLParser#program}.
	 * @param ctx the parse tree
	 */
	void exitProgram(POLParser.ProgramContext ctx);
	/**
	 * Enter a parse tree produced by {@link POLParser#block}.
	 * @param ctx the parse tree
	 */
	void enterBlock(POLParser.BlockContext ctx);
	/**
	 * Exit a parse tree produced by {@link POLParser#block}.
	 * @param ctx the parse tree
	 */
	void exitBlock(POLParser.BlockContext ctx);
	/**
	 * Enter a parse tree produced by {@link POLParser#instruction}.
	 * @param ctx the parse tree
	 */
	void enterInstruction(POLParser.InstructionContext ctx);
	/**
	 * Exit a parse tree produced by {@link POLParser#instruction}.
	 * @param ctx the parse tree
	 */
	void exitInstruction(POLParser.InstructionContext ctx);
	/**
	 * Enter a parse tree produced by {@link POLParser#variable_declaration}.
	 * @param ctx the parse tree
	 */
	void enterVariable_declaration(POLParser.Variable_declarationContext ctx);
	/**
	 * Exit a parse tree produced by {@link POLParser#variable_declaration}.
	 * @param ctx the parse tree
	 */
	void exitVariable_declaration(POLParser.Variable_declarationContext ctx);
	/**
	 * Enter a parse tree produced by {@link POLParser#function_definition}.
	 * @param ctx the parse tree
	 */
	void enterFunction_definition(POLParser.Function_definitionContext ctx);
	/**
	 * Exit a parse tree produced by {@link POLParser#function_definition}.
	 * @param ctx the parse tree
	 */
	void exitFunction_definition(POLParser.Function_definitionContext ctx);
	/**
	 * Enter a parse tree produced by {@link POLParser#parameter}.
	 * @param ctx the parse tree
	 */
	void enterParameter(POLParser.ParameterContext ctx);
	/**
	 * Exit a parse tree produced by {@link POLParser#parameter}.
	 * @param ctx the parse tree
	 */
	void exitParameter(POLParser.ParameterContext ctx);
	/**
	 * Enter a parse tree produced by {@link POLParser#loop}.
	 * @param ctx the parse tree
	 */
	void enterLoop(POLParser.LoopContext ctx);
	/**
	 * Exit a parse tree produced by {@link POLParser#loop}.
	 * @param ctx the parse tree
	 */
	void exitLoop(POLParser.LoopContext ctx);
	/**
	 * Enter a parse tree produced by {@link POLParser#for_loop}.
	 * @param ctx the parse tree
	 */
	void enterFor_loop(POLParser.For_loopContext ctx);
	/**
	 * Exit a parse tree produced by {@link POLParser#for_loop}.
	 * @param ctx the parse tree
	 */
	void exitFor_loop(POLParser.For_loopContext ctx);
	/**
	 * Enter a parse tree produced by {@link POLParser#while_loop}.
	 * @param ctx the parse tree
	 */
	void enterWhile_loop(POLParser.While_loopContext ctx);
	/**
	 * Exit a parse tree produced by {@link POLParser#while_loop}.
	 * @param ctx the parse tree
	 */
	void exitWhile_loop(POLParser.While_loopContext ctx);
	/**
	 * Enter a parse tree produced by {@link POLParser#do_while_loop}.
	 * @param ctx the parse tree
	 */
	void enterDo_while_loop(POLParser.Do_while_loopContext ctx);
	/**
	 * Exit a parse tree produced by {@link POLParser#do_while_loop}.
	 * @param ctx the parse tree
	 */
	void exitDo_while_loop(POLParser.Do_while_loopContext ctx);
	/**
	 * Enter a parse tree produced by {@link POLParser#condition}.
	 * @param ctx the parse tree
	 */
	void enterCondition(POLParser.ConditionContext ctx);
	/**
	 * Exit a parse tree produced by {@link POLParser#condition}.
	 * @param ctx the parse tree
	 */
	void exitCondition(POLParser.ConditionContext ctx);
	/**
	 * Enter a parse tree produced by {@link POLParser#expression}.
	 * @param ctx the parse tree
	 */
	void enterExpression(POLParser.ExpressionContext ctx);
	/**
	 * Exit a parse tree produced by {@link POLParser#expression}.
	 * @param ctx the parse tree
	 */
	void exitExpression(POLParser.ExpressionContext ctx);
	/**
	 * Enter a parse tree produced by {@link POLParser#conditional}.
	 * @param ctx the parse tree
	 */
	void enterConditional(POLParser.ConditionalContext ctx);
	/**
	 * Exit a parse tree produced by {@link POLParser#conditional}.
	 * @param ctx the parse tree
	 */
	void exitConditional(POLParser.ConditionalContext ctx);
	/**
	 * Enter a parse tree produced by {@link POLParser#output}.
	 * @param ctx the parse tree
	 */
	void enterOutput(POLParser.OutputContext ctx);
	/**
	 * Exit a parse tree produced by {@link POLParser#output}.
	 * @param ctx the parse tree
	 */
	void exitOutput(POLParser.OutputContext ctx);
	/**
	 * Enter a parse tree produced by {@link POLParser#variable_value_change}.
	 * @param ctx the parse tree
	 */
	void enterVariable_value_change(POLParser.Variable_value_changeContext ctx);
	/**
	 * Exit a parse tree produced by {@link POLParser#variable_value_change}.
	 * @param ctx the parse tree
	 */
	void exitVariable_value_change(POLParser.Variable_value_changeContext ctx);
	/**
	 * Enter a parse tree produced by {@link POLParser#return_}.
	 * @param ctx the parse tree
	 */
	void enterReturn_(POLParser.Return_Context ctx);
	/**
	 * Exit a parse tree produced by {@link POLParser#return_}.
	 * @param ctx the parse tree
	 */
	void exitReturn_(POLParser.Return_Context ctx);
	/**
	 * Enter a parse tree produced by {@link POLParser#literal}.
	 * @param ctx the parse tree
	 */
	void enterLiteral(POLParser.LiteralContext ctx);
	/**
	 * Exit a parse tree produced by {@link POLParser#literal}.
	 * @param ctx the parse tree
	 */
	void exitLiteral(POLParser.LiteralContext ctx);
	/**
	 * Enter a parse tree produced by {@link POLParser#arithmetic_expression}.
	 * @param ctx the parse tree
	 */
	void enterArithmetic_expression(POLParser.Arithmetic_expressionContext ctx);
	/**
	 * Exit a parse tree produced by {@link POLParser#arithmetic_expression}.
	 * @param ctx the parse tree
	 */
	void exitArithmetic_expression(POLParser.Arithmetic_expressionContext ctx);
	/**
	 * Enter a parse tree produced by {@link POLParser#operator}.
	 * @param ctx the parse tree
	 */
	void enterOperator(POLParser.OperatorContext ctx);
	/**
	 * Exit a parse tree produced by {@link POLParser#operator}.
	 * @param ctx the parse tree
	 */
	void exitOperator(POLParser.OperatorContext ctx);
	/**
	 * Enter a parse tree produced by {@link POLParser#comparison_operator}.
	 * @param ctx the parse tree
	 */
	void enterComparison_operator(POLParser.Comparison_operatorContext ctx);
	/**
	 * Exit a parse tree produced by {@link POLParser#comparison_operator}.
	 * @param ctx the parse tree
	 */
	void exitComparison_operator(POLParser.Comparison_operatorContext ctx);
	/**
	 * Enter a parse tree produced by {@link POLParser#type}.
	 * @param ctx the parse tree
	 */
	void enterType(POLParser.TypeContext ctx);
	/**
	 * Exit a parse tree produced by {@link POLParser#type}.
	 * @param ctx the parse tree
	 */
	void exitType(POLParser.TypeContext ctx);
	/**
	 * Enter a parse tree produced by {@link POLParser#identifier}.
	 * @param ctx the parse tree
	 */
	void enterIdentifier(POLParser.IdentifierContext ctx);
	/**
	 * Exit a parse tree produced by {@link POLParser#identifier}.
	 * @param ctx the parse tree
	 */
	void exitIdentifier(POLParser.IdentifierContext ctx);
	/**
	 * Enter a parse tree produced by {@link POLParser#integer}.
	 * @param ctx the parse tree
	 */
	void enterInteger(POLParser.IntegerContext ctx);
	/**
	 * Exit a parse tree produced by {@link POLParser#integer}.
	 * @param ctx the parse tree
	 */
	void exitInteger(POLParser.IntegerContext ctx);
	/**
	 * Enter a parse tree produced by {@link POLParser#float}.
	 * @param ctx the parse tree
	 */
	void enterFloat(POLParser.FloatContext ctx);
	/**
	 * Exit a parse tree produced by {@link POLParser#float}.
	 * @param ctx the parse tree
	 */
	void exitFloat(POLParser.FloatContext ctx);
	/**
	 * Enter a parse tree produced by {@link POLParser#char}.
	 * @param ctx the parse tree
	 */
	void enterChar(POLParser.CharContext ctx);
	/**
	 * Exit a parse tree produced by {@link POLParser#char}.
	 * @param ctx the parse tree
	 */
	void exitChar(POLParser.CharContext ctx);
	/**
	 * Enter a parse tree produced by {@link POLParser#string}.
	 * @param ctx the parse tree
	 */
	void enterString(POLParser.StringContext ctx);
	/**
	 * Exit a parse tree produced by {@link POLParser#string}.
	 * @param ctx the parse tree
	 */
	void exitString(POLParser.StringContext ctx);
	/**
	 * Enter a parse tree produced by {@link POLParser#boolean}.
	 * @param ctx the parse tree
	 */
	void enterBoolean(POLParser.BooleanContext ctx);
	/**
	 * Exit a parse tree produced by {@link POLParser#boolean}.
	 * @param ctx the parse tree
	 */
	void exitBoolean(POLParser.BooleanContext ctx);
}