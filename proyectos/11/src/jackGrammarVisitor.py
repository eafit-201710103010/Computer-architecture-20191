# Generated from jackGrammar.g4 by ANTLR 4.7.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .jackGrammarParser import jackGrammarParser
else:
    from jackGrammarParser import jackGrammarParser

# This class defines a complete generic visitor for a parse tree produced by jackGrammarParser.

class jackGrammarVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by jackGrammarParser#classes.
    def visitClasses(self, ctx:jackGrammarParser.ClassesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by jackGrammarParser#classVarDec.
    def visitClassVarDec(self, ctx:jackGrammarParser.ClassVarDecContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by jackGrammarParser#types.
    def visitTypes(self, ctx:jackGrammarParser.TypesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by jackGrammarParser#subroutineDec.
    def visitSubroutineDec(self, ctx:jackGrammarParser.SubroutineDecContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by jackGrammarParser#parameterList.
    def visitParameterList(self, ctx:jackGrammarParser.ParameterListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by jackGrammarParser#subroutineBody.
    def visitSubroutineBody(self, ctx:jackGrammarParser.SubroutineBodyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by jackGrammarParser#varDec.
    def visitVarDec(self, ctx:jackGrammarParser.VarDecContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by jackGrammarParser#className.
    def visitClassName(self, ctx:jackGrammarParser.ClassNameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by jackGrammarParser#subroutineName.
    def visitSubroutineName(self, ctx:jackGrammarParser.SubroutineNameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by jackGrammarParser#varName.
    def visitVarName(self, ctx:jackGrammarParser.VarNameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by jackGrammarParser#statements.
    def visitStatements(self, ctx:jackGrammarParser.StatementsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by jackGrammarParser#statement.
    def visitStatement(self, ctx:jackGrammarParser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by jackGrammarParser#letStatement.
    def visitLetStatement(self, ctx:jackGrammarParser.LetStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by jackGrammarParser#ifStatement.
    def visitIfStatement(self, ctx:jackGrammarParser.IfStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by jackGrammarParser#whileStatement.
    def visitWhileStatement(self, ctx:jackGrammarParser.WhileStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by jackGrammarParser#doStatement.
    def visitDoStatement(self, ctx:jackGrammarParser.DoStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by jackGrammarParser#returnStatement.
    def visitReturnStatement(self, ctx:jackGrammarParser.ReturnStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by jackGrammarParser#expression.
    def visitExpression(self, ctx:jackGrammarParser.ExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by jackGrammarParser#term.
    def visitTerm(self, ctx:jackGrammarParser.TermContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by jackGrammarParser#subroutineCall.
    def visitSubroutineCall(self, ctx:jackGrammarParser.SubroutineCallContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by jackGrammarParser#expressionList.
    def visitExpressionList(self, ctx:jackGrammarParser.ExpressionListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by jackGrammarParser#op.
    def visitOp(self, ctx:jackGrammarParser.OpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by jackGrammarParser#unaryop.
    def visitUnaryop(self, ctx:jackGrammarParser.UnaryopContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by jackGrammarParser#keywordconstant.
    def visitKeywordconstant(self, ctx:jackGrammarParser.KeywordconstantContext):
        return self.visitChildren(ctx)



del jackGrammarParser