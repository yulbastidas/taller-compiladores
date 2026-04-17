from generated.WhileLangVisitor import WhileLangVisitor
from generated.WhileLangParser import WhileLangParser
from .SymbolTable import SymbolTable, Symbol


class SemanticVisitor(WhileLangVisitor):
    def __init__(self):
        super().__init__()
        self.table = SymbolTable()
        self.loop_depth = 0

    # Programa
    def visitProgram(self, ctx: WhileLangParser.ProgramContext):
        for stmt in ctx.statement():
            self.visit(stmt)
        return None

    # Declaración
    def visitDeclaration(self, ctx: WhileLangParser.DeclarationContext):
        var_name = ctx.ID().getText()
        type_name = ctx.type_().getText()

        inserted = self.table.insert(var_name, Symbol(var_name, type_name))

        if ctx.expr():
            expr_type = self.visit(ctx.expr())
            if inserted and expr_type != 'error_type' and expr_type != type_name:
                print(
                    f"Error Semántico: No se puede asignar tipo '{expr_type}' a variable '{var_name}' de tipo '{type_name}'."
                )
        return None

    # Asignación
    def visitAssignment(self, ctx: WhileLangParser.AssignmentContext):
        var_name = ctx.ID().getText()
        symbol = self.table.lookup(var_name)

        if symbol is None:
            print(f"Error Semántico: La variable '{var_name}' a la que se intenta asignar no ha sido declarada.")
            return None

        expr_type = self.visit(ctx.expr())

        if expr_type != 'error_type' and expr_type is not None and symbol.type != expr_type:
            print(
                f"Error Semántico: No se puede asignar tipo '{expr_type}' a variable '{var_name}' de tipo '{symbol.type}'."
            )
        return None

    # If
    def visitIfStatement(self, ctx: WhileLangParser.IfStatementContext):
        cond_type = self.visit(ctx.expr())
        if cond_type != 'error_type' and cond_type != 'int':
            print(f"Error Semántico: La condición del if debe ser de tipo 'int', no '{cond_type}'.")

        then_count = len(ctx.statement())
        else_exists = ctx.ELSE() is not None

        if else_exists:
            mid = then_count // 2

            self.table.enter_scope()
            for stmt in ctx.statement()[:mid]:
                self.visit(stmt)
            self.table.exit_scope()

            self.table.enter_scope()
            for stmt in ctx.statement()[mid:]:
                self.visit(stmt)
            self.table.exit_scope()
        else:
            self.table.enter_scope()
            for stmt in ctx.statement():
                self.visit(stmt)
            self.table.exit_scope()

        return None

    # While
    def visitWhileStatement(self, ctx: WhileLangParser.WhileStatementContext):
        cond_type = self.visit(ctx.expr())
        if cond_type != 'error_type' and cond_type != 'int':
            print(f"Error Semántico: La condición del while debe ser de tipo 'int', no '{cond_type}'.")

        self.loop_depth += 1
        self.table.enter_scope()

        for stmt in ctx.statement():
            self.visit(stmt)

        self.table.exit_scope()
        self.loop_depth -= 1
        return None

    # Expresión: ID
    def visitIdExpr(self, ctx: WhileLangParser.IdExprContext):
        var_name = ctx.ID().getText()
        symbol = self.table.lookup(var_name)

        if symbol is None:
            print(f"Error Semántico: La variable '{var_name}' no ha sido declarada.")
            return 'error_type'

        return symbol.type

    # Expresión: número
    def visitNumberExpr(self, ctx: WhileLangParser.NumberExprContext):
        return 'int'

    # Expresión: string
    def visitStringExpr(self, ctx: WhileLangParser.StringExprContext):
        return 'string'

    # Expresión: paréntesis
    def visitParenExpr(self, ctx: WhileLangParser.ParenExprContext):
        return self.visit(ctx.expr())

    # Expresión: comparación
    def visitComparisonExpr(self, ctx: WhileLangParser.ComparisonExprContext):
        left_type = self.visit(ctx.expr(0))
        right_type = self.visit(ctx.expr(1))
        op = ctx.getChild(1).getText()

        if left_type == 'error_type' or right_type == 'error_type':
            return 'error_type'

        if left_type != right_type:
            print(f"Error Semántico: Comparación entre tipos incompatibles ({left_type} vs {right_type}).")
            return 'error_type'

        if op in ['<', '>', '<=', '>='] and (left_type != 'int' or right_type != 'int'):
            print(f"Error Semántico: Operador '{op}' solo permitido entre enteros.")
            return 'error_type'

        return 'int'

    # Expresión: aritmética
    def visitArithmeticExpr(self, ctx: WhileLangParser.ArithmeticExprContext):
        left_type = self.visit(ctx.expr(0))
        right_type = self.visit(ctx.expr(1))
        op = ctx.getChild(1).getText()

        if left_type == 'error_type' or right_type == 'error_type':
            return 'error_type'

        if op == '+':
            if left_type == right_type == 'int':
                return 'int'
            if left_type == right_type == 'string':
                return 'string'
            print(f"Error Semántico: Operación '+' incompatible entre {left_type} y {right_type}.")
            return 'error_type'

        if left_type != 'int' or right_type != 'int':
            print(f"Error Semántico: Operación aritmética solo permitida con enteros, no con {left_type} y {right_type}.")
            return 'error_type'

        return 'int'