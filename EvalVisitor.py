from POLVisitor import POLVisitor
from POLParser import POLParser


class EvalVisitor(POLVisitor):
    def visitProgram(self, ctx: POLParser.ProgramContext):
        c_code = []
        self.functions = []
        c_code.append("int main() {")

        for child in ctx.children:
            result = self.visit(child)
            if result is not None:
                c_code.append(result)

        c_code.append("    return 0;")
        c_code.append("}")

        return "#include <stdio.h>\n" + '\n'.join(self.functions) + '\n'.join(c_code)

    def visitBlock(self, ctx: POLParser.ProgramContext):
        c_code = []
        for child in ctx.children:
            result = self.visit(child)
            if result is not None:
                c_code.append(result)
        return '\n'.join(c_code)

    def visitInstruction(self, ctx: POLParser.InstructionContext):
        if ctx.variable_declaration():
            return self.visit(ctx.variable_declaration())
        elif ctx.function_definition():
            return self.visit(ctx.function_definition())
        elif ctx.loop():
            return self.visit(ctx.loop())
        elif ctx.conditional():
            return self.visit(ctx.conditional())
        elif ctx.output():
            return self.visit(ctx.output())
        elif ctx.variable_value_change():
            return self.visit(ctx.variable_value_change())
        elif ctx.return_():
            return self.visit(ctx.return_())

    def visitArithmetic_expression(self, ctx: POLParser.Arithmetic_expressionContext):
        if ctx.unary_expression():
            return self.visitUnary_expression(ctx.unary_expression())
        elif ctx.operator() and ctx.arithmetic_expression():
            left = self.visitArithmetic_expression(ctx.arithmetic_expression(0))
            right = self.visitArithmetic_expression(ctx.arithmetic_expression(1))
            operator = ctx.operator().getText()

            return f"({left} {operator} {right})"
        return ""

    def visitUnary_expression(self, ctx: POLParser.Unary_expressionContext):
        if ctx.literal():
            return self.visit(ctx.literal())
        elif ctx.children[0].getText() == "-":
            return f"-{self.visit(ctx.literal())}"
        else:
            return self.visit(ctx.identifier())

    def visitLiteral(self, ctx: POLParser.LiteralContext):
        return ctx.getText()

    def visitVariable_declaration(self, ctx: POLParser.Variable_declarationContext):
        identifier = ctx.identifier().getText()
        var_type = self.visit(ctx.type_())
        value = self.visit(ctx.arithmetic_expression())

        return f"{var_type} {identifier} = {value};"

    def visitComparison_operator(self, ctx: POLParser.Comparison_operatorContext):
        if ctx.LT():
            return ">"
        elif ctx.GT():
            return "<"
        elif ctx.EQ():
            return "=="
        elif ctx.NEQ():
            return "!="
        elif ctx.LOE():
            return ">="
        elif ctx.GOE():
            return "<="

    def visitVariable_value_change(self, ctx: POLParser.Variable_value_changeContext):
        identifier = ctx.identifier().getText()
        expression = self.visit(ctx.expression())
        return f"{identifier} = {expression};"

    def visitLoop(self, ctx: POLParser.LoopContext):
        if ctx.for_loop():
            return self.visit(ctx.for_loop())
        if ctx.while_loop():
            return self.visit(ctx.while_loop())
        if ctx.do_while_loop():
            return self.visit(ctx.do_while_loop())

    def visitFor_loop(self, ctx: POLParser.For_loopContext):
        identifier = ctx.identifier().getText()
        initial_value = self.visit(ctx.expression(0))
        max_value = self.visit(ctx.expression(1))
        block = self.visit(ctx.block())
        return f"for (int {identifier} = {initial_value}; {identifier} < {max_value}; {identifier}++) {{\n{block}\n}}"

    def visitWhile_loop(self, ctx: POLParser.While_loopContext):
        condition = self.visit(ctx.condition())
        block = self.visit(ctx.block())
        return f"While ({condition}){{\n{block}\n}}"

    def visitDo_while_loop(self, ctx: POLParser.Do_while_loopContext):
        condition = self.visit(ctx.condition())
        block = self.visit(ctx.block())
        return f"Do {{\n{block}\n}} Wile({condition})"

    def visitConditional(self, ctx: POLParser.ConditionalContext):
        condition = self.visit(ctx.condition())
        block = self.visit(ctx.block(0))

        code = ""
        if ctx.block(1):
            block = self.visit(ctx.block(1))
            code += f"else {{\n{block}\n}}"
        return f"if ({condition}){{\n {block} \n}}{code}"

    def visitOutput(self, ctx: POLParser.OutputContext):
        expression = self.visit(ctx.expression())
        return f'printf({expression});'

    def visitCondition(self, ctx: POLParser.ConditionContext):
        left = self.visit(ctx.expression(0))
        right = self.visit(ctx.expression(1))
        operator = self.visit(ctx.comparison_operator())
        return f"{left} {operator} {right}"

    def visitType(self, ctx: POLParser.TypeContext):
        type_map = {
            "liczba całkowita": "int",
            "liczba zmiennoprzecinkowa": "float",
            "znak": "char",
            "łańcuch znaków": "str[]",
            "wartość logiczna": "bool"
        }
        return type_map[ctx.getText()]

    def visitReturn_(self, ctx):
        expression = self.visit(ctx.expression())
        return f'return {expression};'

    def visitIdentifier(self, ctx: POLParser.IdentifierContext):
        return ctx.getText()

    def visitFunction_execution(self, ctx: POLParser.Function_executionContext):
        function_name = ctx.identifier().getText()

        parameters = []
        if ctx.parameter():
            parameters = [self.visit(param) for param in ctx.parameter()]

        param_list = ", ".join(parameters)
        return f"{function_name}({param_list})"

    def visitFunction_definition(self, ctx: POLParser.Function_definitionContext):
        return_type = self.visit(ctx.type_())
        function_name = ctx.identifier().getText()

        parameters = []
        if ctx.parameter():
            parameters = [self.visit(param) for param in ctx.parameter()]
        param_list = ", ".join(parameters)

        function_body = self.visit(ctx.block())
        self.functions.append(f"{return_type} {function_name}({param_list}) {{\n{function_body}\n}}")
