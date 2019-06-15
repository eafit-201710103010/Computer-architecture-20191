# Generated from jackGrammar.g4 by ANTLR 4.7.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .jackGrammarParser import jackGrammarParser
else:
    from jackGrammarParser import jackGrammarParser

# This class defines a complete listener for a parse tree produced by jackGrammarParser.
class jackGrammarListener(ParseTreeListener):

    # Enter a parse tree produced by jackGrammarParser#classNT.
    def enterClassNT(self, ctx:jackGrammarParser.ClassNTContext):
        pass

    # Exit a parse tree produced by jackGrammarParser#classNT.
    def exitClassNT(self, ctx:jackGrammarParser.ClassNTContext):
        pass


    # Enter a parse tree produced by jackGrammarParser#classVarDec.
    def enterClassVarDec(self, ctx:jackGrammarParser.ClassVarDecContext):
        pass

    # Exit a parse tree produced by jackGrammarParser#classVarDec.
    def exitClassVarDec(self, ctx:jackGrammarParser.ClassVarDecContext):
        pass


    # Enter a parse tree produced by jackGrammarParser#jackType.
    def enterJackType(self, ctx:jackGrammarParser.JackTypeContext):
        pass

    # Exit a parse tree produced by jackGrammarParser#jackType.
    def exitJackType(self, ctx:jackGrammarParser.JackTypeContext):
        pass


    # Enter a parse tree produced by jackGrammarParser#subroutineDec.
    def enterSubroutineDec(self, ctx:jackGrammarParser.SubroutineDecContext):
        pass

    # Exit a parse tree produced by jackGrammarParser#subroutineDec.
    def exitSubroutineDec(self, ctx:jackGrammarParser.SubroutineDecContext):
        pass


    # Enter a parse tree produced by jackGrammarParser#parameterList.
    def enterParameterList(self, ctx:jackGrammarParser.ParameterListContext):
        pass

    # Exit a parse tree produced by jackGrammarParser#parameterList.
    def exitParameterList(self, ctx:jackGrammarParser.ParameterListContext):
        pass


    # Enter a parse tree produced by jackGrammarParser#subroutineBody.
    def enterSubroutineBody(self, ctx:jackGrammarParser.SubroutineBodyContext):
        pass

    # Exit a parse tree produced by jackGrammarParser#subroutineBody.
    def exitSubroutineBody(self, ctx:jackGrammarParser.SubroutineBodyContext):
        pass


    # Enter a parse tree produced by jackGrammarParser#varDec.
    def enterVarDec(self, ctx:jackGrammarParser.VarDecContext):
        pass

    # Exit a parse tree produced by jackGrammarParser#varDec.
    def exitVarDec(self, ctx:jackGrammarParser.VarDecContext):
        pass


    # Enter a parse tree produced by jackGrammarParser#className.
    def enterClassName(self, ctx:jackGrammarParser.ClassNameContext):
        pass

    # Exit a parse tree produced by jackGrammarParser#className.
    def exitClassName(self, ctx:jackGrammarParser.ClassNameContext):
        pass


    # Enter a parse tree produced by jackGrammarParser#subroutineName.
    def enterSubroutineName(self, ctx:jackGrammarParser.SubroutineNameContext):
        pass

    # Exit a parse tree produced by jackGrammarParser#subroutineName.
    def exitSubroutineName(self, ctx:jackGrammarParser.SubroutineNameContext):
        pass


    # Enter a parse tree produced by jackGrammarParser#varName.
    def enterVarName(self, ctx:jackGrammarParser.VarNameContext):
        pass

    # Exit a parse tree produced by jackGrammarParser#varName.
    def exitVarName(self, ctx:jackGrammarParser.VarNameContext):
        pass


    # Enter a parse tree produced by jackGrammarParser#statements.
    def enterStatements(self, ctx:jackGrammarParser.StatementsContext):
        pass

    # Exit a parse tree produced by jackGrammarParser#statements.
    def exitStatements(self, ctx:jackGrammarParser.StatementsContext):
        pass


    # Enter a parse tree produced by jackGrammarParser#statement.
    def enterStatement(self, ctx:jackGrammarParser.StatementContext):
        pass

    # Exit a parse tree produced by jackGrammarParser#statement.
    def exitStatement(self, ctx:jackGrammarParser.StatementContext):
        pass


    # Enter a parse tree produced by jackGrammarParser#letStatement.
    def enterLetStatement(self, ctx:jackGrammarParser.LetStatementContext):
        pass

    # Exit a parse tree produced by jackGrammarParser#letStatement.
    def exitLetStatement(self, ctx:jackGrammarParser.LetStatementContext):
        pass


    # Enter a parse tree produced by jackGrammarParser#ifStatement.
    def enterIfStatement(self, ctx:jackGrammarParser.IfStatementContext):
        pass

    # Exit a parse tree produced by jackGrammarParser#ifStatement.
    def exitIfStatement(self, ctx:jackGrammarParser.IfStatementContext):
        pass


    # Enter a parse tree produced by jackGrammarParser#whileStatement.
    def enterWhileStatement(self, ctx:jackGrammarParser.WhileStatementContext):
        pass

    # Exit a parse tree produced by jackGrammarParser#whileStatement.
    def exitWhileStatement(self, ctx:jackGrammarParser.WhileStatementContext):
        pass


    # Enter a parse tree produced by jackGrammarParser#doStatement.
    def enterDoStatement(self, ctx:jackGrammarParser.DoStatementContext):
        pass

    # Exit a parse tree produced by jackGrammarParser#doStatement.
    def exitDoStatement(self, ctx:jackGrammarParser.DoStatementContext):
        pass


    # Enter a parse tree produced by jackGrammarParser#returnStatement.
    def enterReturnStatement(self, ctx:jackGrammarParser.ReturnStatementContext):
        pass

    # Exit a parse tree produced by jackGrammarParser#returnStatement.
    def exitReturnStatement(self, ctx:jackGrammarParser.ReturnStatementContext):
        pass


    # Enter a parse tree produced by jackGrammarParser#expression.
    def enterExpression(self, ctx:jackGrammarParser.ExpressionContext):
        pass

    # Exit a parse tree produced by jackGrammarParser#expression.
    def exitExpression(self, ctx:jackGrammarParser.ExpressionContext):
        pass


    # Enter a parse tree produced by jackGrammarParser#term.
    def enterTerm(self, ctx:jackGrammarParser.TermContext):
        pass

    # Exit a parse tree produced by jackGrammarParser#term.
    def exitTerm(self, ctx:jackGrammarParser.TermContext):
        pass


    # Enter a parse tree produced by jackGrammarParser#subroutineCall.
    def enterSubroutineCall(self, ctx:jackGrammarParser.SubroutineCallContext):
        pass

    # Exit a parse tree produced by jackGrammarParser#subroutineCall.
    def exitSubroutineCall(self, ctx:jackGrammarParser.SubroutineCallContext):
        pass


    # Enter a parse tree produced by jackGrammarParser#expressionList.
    def enterExpressionList(self, ctx:jackGrammarParser.ExpressionListContext):
        pass

    # Exit a parse tree produced by jackGrammarParser#expressionList.
    def exitExpressionList(self, ctx:jackGrammarParser.ExpressionListContext):
        pass


    # Enter a parse tree produced by jackGrammarParser#op.
    def enterOp(self, ctx:jackGrammarParser.OpContext):
        pass

    # Exit a parse tree produced by jackGrammarParser#op.
    def exitOp(self, ctx:jackGrammarParser.OpContext):
        pass


    # Enter a parse tree produced by jackGrammarParser#unaryOp.
    def enterUnaryOp(self, ctx:jackGrammarParser.UnaryOpContext):
        pass

    # Exit a parse tree produced by jackGrammarParser#unaryOp.
    def exitUnaryOp(self, ctx:jackGrammarParser.UnaryOpContext):
        pass


    # Enter a parse tree produced by jackGrammarParser#keywordConstant.
    def enterKeywordConstant(self, ctx:jackGrammarParser.KeywordConstantContext):
        pass

    # Exit a parse tree produced by jackGrammarParser#keywordConstant.
    def exitKeywordConstant(self, ctx:jackGrammarParser.KeywordConstantContext):
        pass


