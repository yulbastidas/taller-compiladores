# Generated from grammar/DevOpsDSL.g4 by ANTLR 4.13.0
from antlr4 import *
if "." in __name__:
    from .DevOpsDSLParser import DevOpsDSLParser
else:
    from DevOpsDSLParser import DevOpsDSLParser

# This class defines a complete generic visitor for a parse tree produced by DevOpsDSLParser.

class DevOpsDSLVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by DevOpsDSLParser#program.
    def visitProgram(self, ctx:DevOpsDSLParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DevOpsDSLParser#statement.
    def visitStatement(self, ctx:DevOpsDSLParser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DevOpsDSLParser#nodeCommand.
    def visitNodeCommand(self, ctx:DevOpsDSLParser.NodeCommandContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DevOpsDSLParser#groupCommand.
    def visitGroupCommand(self, ctx:DevOpsDSLParser.GroupCommandContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DevOpsDSLParser#deployCommand.
    def visitDeployCommand(self, ctx:DevOpsDSLParser.DeployCommandContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DevOpsDSLParser#rule.
    def visitRule(self, ctx:DevOpsDSLParser.RuleContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DevOpsDSLParser#condition.
    def visitCondition(self, ctx:DevOpsDSLParser.ConditionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DevOpsDSLParser#action.
    def visitAction(self, ctx:DevOpsDSLParser.ActionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DevOpsDSLParser#parallelBlock.
    def visitParallelBlock(self, ctx:DevOpsDSLParser.ParallelBlockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DevOpsDSLParser#comparator.
    def visitComparator(self, ctx:DevOpsDSLParser.ComparatorContext):
        return self.visitChildren(ctx)



del DevOpsDSLParser