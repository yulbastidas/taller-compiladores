# Generated from grammar/DevOpsDSL.g4 by ANTLR 4.13.0
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,21,86,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,1,0,5,0,22,8,0,10,0,12,0,25,9,0,1,0,1,
        0,1,1,1,1,1,1,1,1,1,1,3,1,34,8,1,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,3,
        1,3,1,3,1,3,1,3,1,3,1,4,1,4,1,4,1,4,1,4,1,5,1,5,1,5,1,5,1,6,1,6,
        1,6,1,6,1,6,1,6,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,3,7,73,8,7,1,
        8,1,8,1,8,4,8,78,8,8,11,8,12,8,79,1,8,1,8,1,9,1,9,1,9,0,0,10,0,2,
        4,6,8,10,12,14,16,18,0,1,1,0,12,17,82,0,23,1,0,0,0,2,33,1,0,0,0,
        4,35,1,0,0,0,6,42,1,0,0,0,8,48,1,0,0,0,10,53,1,0,0,0,12,57,1,0,0,
        0,14,72,1,0,0,0,16,74,1,0,0,0,18,83,1,0,0,0,20,22,3,2,1,0,21,20,
        1,0,0,0,22,25,1,0,0,0,23,21,1,0,0,0,23,24,1,0,0,0,24,26,1,0,0,0,
        25,23,1,0,0,0,26,27,5,0,0,1,27,1,1,0,0,0,28,34,3,4,2,0,29,34,3,6,
        3,0,30,34,3,8,4,0,31,34,3,10,5,0,32,34,3,16,8,0,33,28,1,0,0,0,33,
        29,1,0,0,0,33,30,1,0,0,0,33,31,1,0,0,0,33,32,1,0,0,0,34,3,1,0,0,
        0,35,36,5,18,0,0,36,37,5,1,0,0,37,38,5,2,0,0,38,39,5,3,0,0,39,40,
        5,19,0,0,40,41,5,4,0,0,41,5,1,0,0,0,42,43,5,18,0,0,43,44,5,1,0,0,
        44,45,5,5,0,0,45,46,5,3,0,0,46,47,5,4,0,0,47,7,1,0,0,0,48,49,5,6,
        0,0,49,50,5,18,0,0,50,51,5,7,0,0,51,52,5,18,0,0,52,9,1,0,0,0,53,
        54,3,12,6,0,54,55,5,8,0,0,55,56,3,14,7,0,56,11,1,0,0,0,57,58,5,18,
        0,0,58,59,5,1,0,0,59,60,5,18,0,0,60,61,3,18,9,0,61,62,5,20,0,0,62,
        13,1,0,0,0,63,64,5,18,0,0,64,65,5,3,0,0,65,73,5,4,0,0,66,67,5,18,
        0,0,67,68,5,1,0,0,68,69,5,2,0,0,69,70,5,3,0,0,70,71,5,19,0,0,71,
        73,5,4,0,0,72,63,1,0,0,0,72,66,1,0,0,0,73,15,1,0,0,0,74,75,5,9,0,
        0,75,77,5,10,0,0,76,78,3,2,1,0,77,76,1,0,0,0,78,79,1,0,0,0,79,77,
        1,0,0,0,79,80,1,0,0,0,80,81,1,0,0,0,81,82,5,11,0,0,82,17,1,0,0,0,
        83,84,7,0,0,0,84,19,1,0,0,0,4,23,33,72,79
    ]

class DevOpsDSLParser ( Parser ):

    grammarFileName = "DevOpsDSL.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'.'", "'run'", "'('", "')'", "'update'", 
                     "'deploy'", "'to'", "'->'", "'parallel'", "'{'", "'}'", 
                     "'>'", "'<'", "'>='", "'<='", "'=='", "'!='" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "ID", "STRING", "NUMBER", 
                      "WS" ]

    RULE_program = 0
    RULE_statement = 1
    RULE_nodeCommand = 2
    RULE_groupCommand = 3
    RULE_deployCommand = 4
    RULE_rule = 5
    RULE_condition = 6
    RULE_action = 7
    RULE_parallelBlock = 8
    RULE_comparator = 9

    ruleNames =  [ "program", "statement", "nodeCommand", "groupCommand", 
                   "deployCommand", "rule", "condition", "action", "parallelBlock", 
                   "comparator" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    T__7=8
    T__8=9
    T__9=10
    T__10=11
    T__11=12
    T__12=13
    T__13=14
    T__14=15
    T__15=16
    T__16=17
    ID=18
    STRING=19
    NUMBER=20
    WS=21

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.0")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(DevOpsDSLParser.EOF, 0)

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(DevOpsDSLParser.StatementContext)
            else:
                return self.getTypedRuleContext(DevOpsDSLParser.StatementContext,i)


        def getRuleIndex(self):
            return DevOpsDSLParser.RULE_program

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProgram" ):
                listener.enterProgram(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProgram" ):
                listener.exitProgram(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProgram" ):
                return visitor.visitProgram(self)
            else:
                return visitor.visitChildren(self)




    def program(self):

        localctx = DevOpsDSLParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 23
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 262720) != 0):
                self.state = 20
                self.statement()
                self.state = 25
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 26
            self.match(DevOpsDSLParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def nodeCommand(self):
            return self.getTypedRuleContext(DevOpsDSLParser.NodeCommandContext,0)


        def groupCommand(self):
            return self.getTypedRuleContext(DevOpsDSLParser.GroupCommandContext,0)


        def deployCommand(self):
            return self.getTypedRuleContext(DevOpsDSLParser.DeployCommandContext,0)


        def rule_(self):
            return self.getTypedRuleContext(DevOpsDSLParser.RuleContext,0)


        def parallelBlock(self):
            return self.getTypedRuleContext(DevOpsDSLParser.ParallelBlockContext,0)


        def getRuleIndex(self):
            return DevOpsDSLParser.RULE_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStatement" ):
                listener.enterStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStatement" ):
                listener.exitStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStatement" ):
                return visitor.visitStatement(self)
            else:
                return visitor.visitChildren(self)




    def statement(self):

        localctx = DevOpsDSLParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_statement)
        try:
            self.state = 33
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 28
                self.nodeCommand()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 29
                self.groupCommand()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 30
                self.deployCommand()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 31
                self.rule_()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 32
                self.parallelBlock()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class NodeCommandContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(DevOpsDSLParser.ID, 0)

        def STRING(self):
            return self.getToken(DevOpsDSLParser.STRING, 0)

        def getRuleIndex(self):
            return DevOpsDSLParser.RULE_nodeCommand

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNodeCommand" ):
                listener.enterNodeCommand(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNodeCommand" ):
                listener.exitNodeCommand(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNodeCommand" ):
                return visitor.visitNodeCommand(self)
            else:
                return visitor.visitChildren(self)




    def nodeCommand(self):

        localctx = DevOpsDSLParser.NodeCommandContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_nodeCommand)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 35
            self.match(DevOpsDSLParser.ID)
            self.state = 36
            self.match(DevOpsDSLParser.T__0)
            self.state = 37
            self.match(DevOpsDSLParser.T__1)
            self.state = 38
            self.match(DevOpsDSLParser.T__2)
            self.state = 39
            self.match(DevOpsDSLParser.STRING)
            self.state = 40
            self.match(DevOpsDSLParser.T__3)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class GroupCommandContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(DevOpsDSLParser.ID, 0)

        def getRuleIndex(self):
            return DevOpsDSLParser.RULE_groupCommand

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterGroupCommand" ):
                listener.enterGroupCommand(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitGroupCommand" ):
                listener.exitGroupCommand(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitGroupCommand" ):
                return visitor.visitGroupCommand(self)
            else:
                return visitor.visitChildren(self)




    def groupCommand(self):

        localctx = DevOpsDSLParser.GroupCommandContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_groupCommand)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 42
            self.match(DevOpsDSLParser.ID)
            self.state = 43
            self.match(DevOpsDSLParser.T__0)
            self.state = 44
            self.match(DevOpsDSLParser.T__4)
            self.state = 45
            self.match(DevOpsDSLParser.T__2)
            self.state = 46
            self.match(DevOpsDSLParser.T__3)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DeployCommandContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(DevOpsDSLParser.ID)
            else:
                return self.getToken(DevOpsDSLParser.ID, i)

        def getRuleIndex(self):
            return DevOpsDSLParser.RULE_deployCommand

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDeployCommand" ):
                listener.enterDeployCommand(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDeployCommand" ):
                listener.exitDeployCommand(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDeployCommand" ):
                return visitor.visitDeployCommand(self)
            else:
                return visitor.visitChildren(self)




    def deployCommand(self):

        localctx = DevOpsDSLParser.DeployCommandContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_deployCommand)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 48
            self.match(DevOpsDSLParser.T__5)
            self.state = 49
            self.match(DevOpsDSLParser.ID)
            self.state = 50
            self.match(DevOpsDSLParser.T__6)
            self.state = 51
            self.match(DevOpsDSLParser.ID)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class RuleContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def condition(self):
            return self.getTypedRuleContext(DevOpsDSLParser.ConditionContext,0)


        def action(self):
            return self.getTypedRuleContext(DevOpsDSLParser.ActionContext,0)


        def getRuleIndex(self):
            return DevOpsDSLParser.RULE_rule

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRule" ):
                listener.enterRule(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRule" ):
                listener.exitRule(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRule" ):
                return visitor.visitRule(self)
            else:
                return visitor.visitChildren(self)




    def rule_(self):

        localctx = DevOpsDSLParser.RuleContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_rule)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 53
            self.condition()
            self.state = 54
            self.match(DevOpsDSLParser.T__7)
            self.state = 55
            self.action()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ConditionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(DevOpsDSLParser.ID)
            else:
                return self.getToken(DevOpsDSLParser.ID, i)

        def comparator(self):
            return self.getTypedRuleContext(DevOpsDSLParser.ComparatorContext,0)


        def NUMBER(self):
            return self.getToken(DevOpsDSLParser.NUMBER, 0)

        def getRuleIndex(self):
            return DevOpsDSLParser.RULE_condition

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCondition" ):
                listener.enterCondition(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCondition" ):
                listener.exitCondition(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCondition" ):
                return visitor.visitCondition(self)
            else:
                return visitor.visitChildren(self)




    def condition(self):

        localctx = DevOpsDSLParser.ConditionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_condition)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 57
            self.match(DevOpsDSLParser.ID)
            self.state = 58
            self.match(DevOpsDSLParser.T__0)
            self.state = 59
            self.match(DevOpsDSLParser.ID)
            self.state = 60
            self.comparator()
            self.state = 61
            self.match(DevOpsDSLParser.NUMBER)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ActionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(DevOpsDSLParser.ID, 0)

        def STRING(self):
            return self.getToken(DevOpsDSLParser.STRING, 0)

        def getRuleIndex(self):
            return DevOpsDSLParser.RULE_action

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAction" ):
                listener.enterAction(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAction" ):
                listener.exitAction(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAction" ):
                return visitor.visitAction(self)
            else:
                return visitor.visitChildren(self)




    def action(self):

        localctx = DevOpsDSLParser.ActionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_action)
        try:
            self.state = 72
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 63
                self.match(DevOpsDSLParser.ID)
                self.state = 64
                self.match(DevOpsDSLParser.T__2)
                self.state = 65
                self.match(DevOpsDSLParser.T__3)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 66
                self.match(DevOpsDSLParser.ID)
                self.state = 67
                self.match(DevOpsDSLParser.T__0)
                self.state = 68
                self.match(DevOpsDSLParser.T__1)
                self.state = 69
                self.match(DevOpsDSLParser.T__2)
                self.state = 70
                self.match(DevOpsDSLParser.STRING)
                self.state = 71
                self.match(DevOpsDSLParser.T__3)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParallelBlockContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(DevOpsDSLParser.StatementContext)
            else:
                return self.getTypedRuleContext(DevOpsDSLParser.StatementContext,i)


        def getRuleIndex(self):
            return DevOpsDSLParser.RULE_parallelBlock

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParallelBlock" ):
                listener.enterParallelBlock(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParallelBlock" ):
                listener.exitParallelBlock(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParallelBlock" ):
                return visitor.visitParallelBlock(self)
            else:
                return visitor.visitChildren(self)




    def parallelBlock(self):

        localctx = DevOpsDSLParser.ParallelBlockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_parallelBlock)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 74
            self.match(DevOpsDSLParser.T__8)
            self.state = 75
            self.match(DevOpsDSLParser.T__9)
            self.state = 77 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 76
                self.statement()
                self.state = 79 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 262720) != 0)):
                    break

            self.state = 81
            self.match(DevOpsDSLParser.T__10)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ComparatorContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return DevOpsDSLParser.RULE_comparator

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterComparator" ):
                listener.enterComparator(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitComparator" ):
                listener.exitComparator(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitComparator" ):
                return visitor.visitComparator(self)
            else:
                return visitor.visitChildren(self)




    def comparator(self):

        localctx = DevOpsDSLParser.ComparatorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_comparator)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 83
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 258048) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





