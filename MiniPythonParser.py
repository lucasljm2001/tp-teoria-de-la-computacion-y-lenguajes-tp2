# Generated from MiniPython.g4 by ANTLR 4.13.1
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
        4,1,19,103,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,1,0,5,0,20,8,0,10,0,12,0,23,9,0,1,0,1,0,1,1,1,
        1,1,1,1,1,3,1,31,8,1,1,1,1,1,1,1,1,2,1,2,1,2,5,2,39,8,2,10,2,12,
        2,42,9,2,1,3,1,3,5,3,46,8,3,10,3,12,3,49,9,3,1,3,1,3,1,4,1,4,1,4,
        1,4,1,4,1,4,1,4,1,4,1,4,1,4,3,4,63,8,4,1,5,1,5,1,5,1,5,1,5,1,5,1,
        5,3,5,72,8,5,1,6,1,6,1,6,1,7,1,7,1,7,1,7,1,7,5,7,82,8,7,10,7,12,
        7,85,9,7,1,7,1,7,1,8,1,8,1,8,1,8,3,8,93,8,8,1,8,1,8,1,8,5,8,98,8,
        8,10,8,12,8,101,9,8,1,8,0,1,16,9,0,2,4,6,8,10,12,14,16,0,1,1,0,12,
        15,105,0,21,1,0,0,0,2,26,1,0,0,0,4,35,1,0,0,0,6,43,1,0,0,0,8,62,
        1,0,0,0,10,64,1,0,0,0,12,73,1,0,0,0,14,76,1,0,0,0,16,92,1,0,0,0,
        18,20,3,2,1,0,19,18,1,0,0,0,20,23,1,0,0,0,21,19,1,0,0,0,21,22,1,
        0,0,0,22,24,1,0,0,0,23,21,1,0,0,0,24,25,5,0,0,1,25,1,1,0,0,0,26,
        27,5,1,0,0,27,28,5,16,0,0,28,30,5,2,0,0,29,31,3,4,2,0,30,29,1,0,
        0,0,30,31,1,0,0,0,31,32,1,0,0,0,32,33,5,3,0,0,33,34,3,6,3,0,34,3,
        1,0,0,0,35,40,5,16,0,0,36,37,5,4,0,0,37,39,5,16,0,0,38,36,1,0,0,
        0,39,42,1,0,0,0,40,38,1,0,0,0,40,41,1,0,0,0,41,5,1,0,0,0,42,40,1,
        0,0,0,43,47,5,5,0,0,44,46,3,8,4,0,45,44,1,0,0,0,46,49,1,0,0,0,47,
        45,1,0,0,0,47,48,1,0,0,0,48,50,1,0,0,0,49,47,1,0,0,0,50,51,5,6,0,
        0,51,7,1,0,0,0,52,63,3,10,5,0,53,54,3,12,6,0,54,55,5,7,0,0,55,63,
        1,0,0,0,56,57,3,14,7,0,57,58,5,7,0,0,58,63,1,0,0,0,59,60,3,16,8,
        0,60,61,5,7,0,0,61,63,1,0,0,0,62,52,1,0,0,0,62,53,1,0,0,0,62,56,
        1,0,0,0,62,59,1,0,0,0,63,9,1,0,0,0,64,65,5,8,0,0,65,66,5,2,0,0,66,
        67,3,16,8,0,67,68,5,3,0,0,68,71,3,6,3,0,69,70,5,9,0,0,70,72,3,6,
        3,0,71,69,1,0,0,0,71,72,1,0,0,0,72,11,1,0,0,0,73,74,5,10,0,0,74,
        75,3,16,8,0,75,13,1,0,0,0,76,77,5,11,0,0,77,78,5,2,0,0,78,83,3,16,
        8,0,79,80,5,4,0,0,80,82,3,16,8,0,81,79,1,0,0,0,82,85,1,0,0,0,83,
        81,1,0,0,0,83,84,1,0,0,0,84,86,1,0,0,0,85,83,1,0,0,0,86,87,5,3,0,
        0,87,15,1,0,0,0,88,89,6,8,-1,0,89,93,5,16,0,0,90,93,5,17,0,0,91,
        93,5,18,0,0,92,88,1,0,0,0,92,90,1,0,0,0,92,91,1,0,0,0,93,99,1,0,
        0,0,94,95,10,1,0,0,95,96,7,0,0,0,96,98,3,16,8,2,97,94,1,0,0,0,98,
        101,1,0,0,0,99,97,1,0,0,0,99,100,1,0,0,0,100,17,1,0,0,0,101,99,1,
        0,0,0,9,21,30,40,47,62,71,83,92,99
    ]

class MiniPythonParser ( Parser ):

    grammarFileName = "MiniPython.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'fn'", "'('", "')'", "','", "'{'", "'}'", 
                     "';'", "'if'", "'else'", "'return'", "'print'", "'>'", 
                     "'<'", "'=='", "'+'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "ID", "INT", "STRING", "WS" ]

    RULE_program = 0
    RULE_functionDef = 1
    RULE_paramList = 2
    RULE_block = 3
    RULE_statement = 4
    RULE_ifStat = 5
    RULE_returnStat = 6
    RULE_printStat = 7
    RULE_expr = 8

    ruleNames =  [ "program", "functionDef", "paramList", "block", "statement", 
                   "ifStat", "returnStat", "printStat", "expr" ]

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
    ID=16
    INT=17
    STRING=18
    WS=19

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(MiniPythonParser.EOF, 0)

        def functionDef(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniPythonParser.FunctionDefContext)
            else:
                return self.getTypedRuleContext(MiniPythonParser.FunctionDefContext,i)


        def getRuleIndex(self):
            return MiniPythonParser.RULE_program

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProgram" ):
                listener.enterProgram(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProgram" ):
                listener.exitProgram(self)




    def program(self):

        localctx = MiniPythonParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 21
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==1:
                self.state = 18
                self.functionDef()
                self.state = 23
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 24
            self.match(MiniPythonParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FunctionDefContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MiniPythonParser.ID, 0)

        def block(self):
            return self.getTypedRuleContext(MiniPythonParser.BlockContext,0)


        def paramList(self):
            return self.getTypedRuleContext(MiniPythonParser.ParamListContext,0)


        def getRuleIndex(self):
            return MiniPythonParser.RULE_functionDef

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFunctionDef" ):
                listener.enterFunctionDef(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFunctionDef" ):
                listener.exitFunctionDef(self)




    def functionDef(self):

        localctx = MiniPythonParser.FunctionDefContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_functionDef)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 26
            self.match(MiniPythonParser.T__0)
            self.state = 27
            self.match(MiniPythonParser.ID)
            self.state = 28
            self.match(MiniPythonParser.T__1)
            self.state = 30
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==16:
                self.state = 29
                self.paramList()


            self.state = 32
            self.match(MiniPythonParser.T__2)
            self.state = 33
            self.block()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParamListContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(MiniPythonParser.ID)
            else:
                return self.getToken(MiniPythonParser.ID, i)

        def getRuleIndex(self):
            return MiniPythonParser.RULE_paramList

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParamList" ):
                listener.enterParamList(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParamList" ):
                listener.exitParamList(self)




    def paramList(self):

        localctx = MiniPythonParser.ParamListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_paramList)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 35
            self.match(MiniPythonParser.ID)
            self.state = 40
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==4:
                self.state = 36
                self.match(MiniPythonParser.T__3)
                self.state = 37
                self.match(MiniPythonParser.ID)
                self.state = 42
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BlockContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniPythonParser.StatementContext)
            else:
                return self.getTypedRuleContext(MiniPythonParser.StatementContext,i)


        def getRuleIndex(self):
            return MiniPythonParser.RULE_block

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBlock" ):
                listener.enterBlock(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBlock" ):
                listener.exitBlock(self)




    def block(self):

        localctx = MiniPythonParser.BlockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_block)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 43
            self.match(MiniPythonParser.T__4)
            self.state = 47
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 462080) != 0):
                self.state = 44
                self.statement()
                self.state = 49
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 50
            self.match(MiniPythonParser.T__5)
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

        def ifStat(self):
            return self.getTypedRuleContext(MiniPythonParser.IfStatContext,0)


        def returnStat(self):
            return self.getTypedRuleContext(MiniPythonParser.ReturnStatContext,0)


        def printStat(self):
            return self.getTypedRuleContext(MiniPythonParser.PrintStatContext,0)


        def expr(self):
            return self.getTypedRuleContext(MiniPythonParser.ExprContext,0)


        def getRuleIndex(self):
            return MiniPythonParser.RULE_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStatement" ):
                listener.enterStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStatement" ):
                listener.exitStatement(self)




    def statement(self):

        localctx = MiniPythonParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_statement)
        try:
            self.state = 62
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [8]:
                self.enterOuterAlt(localctx, 1)
                self.state = 52
                self.ifStat()
                pass
            elif token in [10]:
                self.enterOuterAlt(localctx, 2)
                self.state = 53
                self.returnStat()
                self.state = 54
                self.match(MiniPythonParser.T__6)
                pass
            elif token in [11]:
                self.enterOuterAlt(localctx, 3)
                self.state = 56
                self.printStat()
                self.state = 57
                self.match(MiniPythonParser.T__6)
                pass
            elif token in [16, 17, 18]:
                self.enterOuterAlt(localctx, 4)
                self.state = 59
                self.expr(0)
                self.state = 60
                self.match(MiniPythonParser.T__6)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IfStatContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self):
            return self.getTypedRuleContext(MiniPythonParser.ExprContext,0)


        def block(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniPythonParser.BlockContext)
            else:
                return self.getTypedRuleContext(MiniPythonParser.BlockContext,i)


        def getRuleIndex(self):
            return MiniPythonParser.RULE_ifStat

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIfStat" ):
                listener.enterIfStat(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIfStat" ):
                listener.exitIfStat(self)




    def ifStat(self):

        localctx = MiniPythonParser.IfStatContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_ifStat)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 64
            self.match(MiniPythonParser.T__7)
            self.state = 65
            self.match(MiniPythonParser.T__1)
            self.state = 66
            self.expr(0)
            self.state = 67
            self.match(MiniPythonParser.T__2)
            self.state = 68
            self.block()
            self.state = 71
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==9:
                self.state = 69
                self.match(MiniPythonParser.T__8)
                self.state = 70
                self.block()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ReturnStatContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self):
            return self.getTypedRuleContext(MiniPythonParser.ExprContext,0)


        def getRuleIndex(self):
            return MiniPythonParser.RULE_returnStat

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterReturnStat" ):
                listener.enterReturnStat(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitReturnStat" ):
                listener.exitReturnStat(self)




    def returnStat(self):

        localctx = MiniPythonParser.ReturnStatContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_returnStat)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 73
            self.match(MiniPythonParser.T__9)
            self.state = 74
            self.expr(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PrintStatContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniPythonParser.ExprContext)
            else:
                return self.getTypedRuleContext(MiniPythonParser.ExprContext,i)


        def getRuleIndex(self):
            return MiniPythonParser.RULE_printStat

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrintStat" ):
                listener.enterPrintStat(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrintStat" ):
                listener.exitPrintStat(self)




    def printStat(self):

        localctx = MiniPythonParser.PrintStatContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_printStat)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 76
            self.match(MiniPythonParser.T__10)
            self.state = 77
            self.match(MiniPythonParser.T__1)
            self.state = 78
            self.expr(0)
            self.state = 83
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==4:
                self.state = 79
                self.match(MiniPythonParser.T__3)
                self.state = 80
                self.expr(0)
                self.state = 85
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 86
            self.match(MiniPythonParser.T__2)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.op = None # Token

        def ID(self):
            return self.getToken(MiniPythonParser.ID, 0)

        def INT(self):
            return self.getToken(MiniPythonParser.INT, 0)

        def STRING(self):
            return self.getToken(MiniPythonParser.STRING, 0)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniPythonParser.ExprContext)
            else:
                return self.getTypedRuleContext(MiniPythonParser.ExprContext,i)


        def getRuleIndex(self):
            return MiniPythonParser.RULE_expr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpr" ):
                listener.enterExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpr" ):
                listener.exitExpr(self)



    def expr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MiniPythonParser.ExprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 16
        self.enterRecursionRule(localctx, 16, self.RULE_expr, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 92
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [16]:
                self.state = 89
                self.match(MiniPythonParser.ID)
                pass
            elif token in [17]:
                self.state = 90
                self.match(MiniPythonParser.INT)
                pass
            elif token in [18]:
                self.state = 91
                self.match(MiniPythonParser.STRING)
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 99
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,8,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MiniPythonParser.ExprContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                    self.state = 94
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 95
                    localctx.op = self._input.LT(1)
                    _la = self._input.LA(1)
                    if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 61440) != 0)):
                        localctx.op = self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 96
                    self.expr(2) 
                self.state = 101
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,8,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[8] = self.expr_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expr_sempred(self, localctx:ExprContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 1)
         




