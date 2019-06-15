from antlr4.error.ErrorListener  import ErrorListener

class jackErrorListener(ErrorListener):

    def __init__(self):
        super(jackErrorListener, self).__init__()

    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        raise SyntaxError('ERROR: Syntax error in line {} and column {} by token {}'.format(line,column,offendingSymbol.text))
