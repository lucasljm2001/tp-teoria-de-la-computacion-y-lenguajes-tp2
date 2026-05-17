# Generated from MiniPython.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .MiniPythonParser import MiniPythonParser
else:
    from MiniPythonParser import MiniPythonParser

# This class defines a complete listener for a parse tree produced by MiniPythonParser.
class MiniPythonListener(ParseTreeListener):

    # Enter a parse tree produced by MiniPythonParser#program.
    def enterProgram(self, ctx:MiniPythonParser.ProgramContext):
        pass

    # Exit a parse tree produced by MiniPythonParser#program.
    def exitProgram(self, ctx:MiniPythonParser.ProgramContext):
        pass


    # Enter a parse tree produced by MiniPythonParser#functionDef.
    def enterFunctionDef(self, ctx:MiniPythonParser.FunctionDefContext):
        pass

    # Exit a parse tree produced by MiniPythonParser#functionDef.
    def exitFunctionDef(self, ctx:MiniPythonParser.FunctionDefContext):
        pass


    # Enter a parse tree produced by MiniPythonParser#paramList.
    def enterParamList(self, ctx:MiniPythonParser.ParamListContext):
        pass

    # Exit a parse tree produced by MiniPythonParser#paramList.
    def exitParamList(self, ctx:MiniPythonParser.ParamListContext):
        pass


    # Enter a parse tree produced by MiniPythonParser#block.
    def enterBlock(self, ctx:MiniPythonParser.BlockContext):
        pass

    # Exit a parse tree produced by MiniPythonParser#block.
    def exitBlock(self, ctx:MiniPythonParser.BlockContext):
        pass


    # Enter a parse tree produced by MiniPythonParser#statement.
    def enterStatement(self, ctx:MiniPythonParser.StatementContext):
        pass

    # Exit a parse tree produced by MiniPythonParser#statement.
    def exitStatement(self, ctx:MiniPythonParser.StatementContext):
        pass


    # Enter a parse tree produced by MiniPythonParser#ifStat.
    def enterIfStat(self, ctx:MiniPythonParser.IfStatContext):
        pass

    # Exit a parse tree produced by MiniPythonParser#ifStat.
    def exitIfStat(self, ctx:MiniPythonParser.IfStatContext):
        pass


    # Enter a parse tree produced by MiniPythonParser#returnStat.
    def enterReturnStat(self, ctx:MiniPythonParser.ReturnStatContext):
        pass

    # Exit a parse tree produced by MiniPythonParser#returnStat.
    def exitReturnStat(self, ctx:MiniPythonParser.ReturnStatContext):
        pass


    # Enter a parse tree produced by MiniPythonParser#printStat.
    def enterPrintStat(self, ctx:MiniPythonParser.PrintStatContext):
        pass

    # Exit a parse tree produced by MiniPythonParser#printStat.
    def exitPrintStat(self, ctx:MiniPythonParser.PrintStatContext):
        pass


    # Enter a parse tree produced by MiniPythonParser#expr.
    def enterExpr(self, ctx:MiniPythonParser.ExprContext):
        pass

    # Exit a parse tree produced by MiniPythonParser#expr.
    def exitExpr(self, ctx:MiniPythonParser.ExprContext):
        pass



del MiniPythonParser