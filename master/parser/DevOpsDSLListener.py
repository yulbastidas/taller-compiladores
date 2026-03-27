# Generated from grammar/DevOpsDSL.g4 by ANTLR 4.13.0
from antlr4 import *
if "." in __name__:
    from .DevOpsDSLParser import DevOpsDSLParser
else:
    from DevOpsDSLParser import DevOpsDSLParser

# This class defines a complete listener for a parse tree produced by DevOpsDSLParser.
class DevOpsDSLListener(ParseTreeListener):

    # Enter a parse tree produced by DevOpsDSLParser#program.
    def enterProgram(self, ctx:DevOpsDSLParser.ProgramContext):
        pass

    # Exit a parse tree produced by DevOpsDSLParser#program.
    def exitProgram(self, ctx:DevOpsDSLParser.ProgramContext):
        pass


    # Enter a parse tree produced by DevOpsDSLParser#statement.
    def enterStatement(self, ctx:DevOpsDSLParser.StatementContext):
        pass

    # Exit a parse tree produced by DevOpsDSLParser#statement.
    def exitStatement(self, ctx:DevOpsDSLParser.StatementContext):
        pass


    # Enter a parse tree produced by DevOpsDSLParser#nodeCommand.
    def enterNodeCommand(self, ctx:DevOpsDSLParser.NodeCommandContext):
        pass

    # Exit a parse tree produced by DevOpsDSLParser#nodeCommand.
    def exitNodeCommand(self, ctx:DevOpsDSLParser.NodeCommandContext):
        pass


    # Enter a parse tree produced by DevOpsDSLParser#groupCommand.
    def enterGroupCommand(self, ctx:DevOpsDSLParser.GroupCommandContext):
        pass

    # Exit a parse tree produced by DevOpsDSLParser#groupCommand.
    def exitGroupCommand(self, ctx:DevOpsDSLParser.GroupCommandContext):
        pass


    # Enter a parse tree produced by DevOpsDSLParser#deployCommand.
    def enterDeployCommand(self, ctx:DevOpsDSLParser.DeployCommandContext):
        pass

    # Exit a parse tree produced by DevOpsDSLParser#deployCommand.
    def exitDeployCommand(self, ctx:DevOpsDSLParser.DeployCommandContext):
        pass


    # Enter a parse tree produced by DevOpsDSLParser#rule.
    def enterRule(self, ctx:DevOpsDSLParser.RuleContext):
        pass

    # Exit a parse tree produced by DevOpsDSLParser#rule.
    def exitRule(self, ctx:DevOpsDSLParser.RuleContext):
        pass


    # Enter a parse tree produced by DevOpsDSLParser#condition.
    def enterCondition(self, ctx:DevOpsDSLParser.ConditionContext):
        pass

    # Exit a parse tree produced by DevOpsDSLParser#condition.
    def exitCondition(self, ctx:DevOpsDSLParser.ConditionContext):
        pass


    # Enter a parse tree produced by DevOpsDSLParser#action.
    def enterAction(self, ctx:DevOpsDSLParser.ActionContext):
        pass

    # Exit a parse tree produced by DevOpsDSLParser#action.
    def exitAction(self, ctx:DevOpsDSLParser.ActionContext):
        pass


    # Enter a parse tree produced by DevOpsDSLParser#parallelBlock.
    def enterParallelBlock(self, ctx:DevOpsDSLParser.ParallelBlockContext):
        pass

    # Exit a parse tree produced by DevOpsDSLParser#parallelBlock.
    def exitParallelBlock(self, ctx:DevOpsDSLParser.ParallelBlockContext):
        pass


    # Enter a parse tree produced by DevOpsDSLParser#comparator.
    def enterComparator(self, ctx:DevOpsDSLParser.ComparatorContext):
        pass

    # Exit a parse tree produced by DevOpsDSLParser#comparator.
    def exitComparator(self, ctx:DevOpsDSLParser.ComparatorContext):
        pass



del DevOpsDSLParser