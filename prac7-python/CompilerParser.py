from ParseTree import *


class ParseException(Exception):
    def __init__(self, message):
        super().__init__(message)
        
class CompilerParser :

    def __init__(self,tokens):
        """
        Constructor for the CompilerParser
        @param tokens A list of tokens to be parsed
        """
        self.tokens = tokens
        self.current_token_index = 0
    

    def compileProgram(self):
        """
        Generates a parse tree for the entire program, which may consist of multiple classes.
        """
        program_node = ParseTree("program", None)
        while self.current() is not None:  # Continue until all tokens are processed
            if self.have('keyword', 'class'):
                program_node.addChild(self.compileClass())
            else:
                raise ParseException("Class definition expected.")
        return program_node

    
    
    def compileType(self):
        """
        Generates a parse tree for a type, which could be a primitive type or a class type (identifier).
        @return a ParseTree that represents the type
        """
        if self.have('keyword') and self.current().getValue() in ['int', 'char', 'boolean']:
            # Primitive type
            type_token = self.mustBe('keyword', None)
            return ParseTree('keyword', type_token.getValue())
        elif self.have('identifier'):
            # Class type
            type_token = self.mustBe('identifier', None)
            return ParseTree('keyword', type_token.getValue())
        else:
            raise ParseException(f"Keyword expected but found {self.current().getType()} with value '{self.current().getValue()}'")
    
    
    def compileClass(self):
        class_node = ParseTree("class", None)
        self.mustBe('keyword', 'class')
        class_name_token = self.mustBe('identifier')
        class_node.addChild(ParseTree('identifier', class_name_token.getValue()))
        self.mustBe('symbol', '{')

        # Check for class variable declarations or subroutine declarations
        while not self.have('symbol', '}'):
            if self.have('keyword', 'static') or self.have('keyword', 'field'):
                class_var_dec_node = self.compileClassVarDec()
                class_node.addChild(class_var_dec_node)
            elif self.have('keyword', 'constructor') or self.have('keyword', 'function') or self.have('keyword', 'method'):
                subroutine_dec_node = self.compileSubroutine()
                class_node.addChild(subroutine_dec_node)
            else:
                raise ParseException("Unexpected token in class body, expecting 'static', 'field', 'constructor', 'function', or 'method'.")

        self.mustBe('symbol', '}')
        return class_node
    

    def compileClassVarDec(self):
        """
        Generates a parse tree for a static variable declaration or field declaration
        @return a ParseTree that represents a static variable declaration or field declaration
        """
        class_var_dec_node = ParseTree("classVarDec", None)

        # Check if the current token is 'static' or 'field'
        var_kind_token = self.mustBe('keyword', None)  # 'static' or 'field' expected
        if var_kind_token.getValue() not in ['static', 'field']:
            raise ParseException(f"Expected 'static' or 'field', found '{var_kind_token.getValue()}'")
        
        class_var_dec_node.addChild(ParseTree('keyword', var_kind_token.getValue()))

        # Parse the type
        type_node = self.compileType()  # Assuming this method will parse and return a type node
        class_var_dec_node.addChild(type_node)

        # Parse the variable names
        var_name_token = self.mustBe('identifier', None)
        class_var_dec_node.addChild(ParseTree('identifier', var_name_token.getValue()))
        while self.have('symbol', ','):
            self.next()  # Consume the comma
            var_name_token = self.mustBe('identifier', None)
            class_var_dec_node.addChild(ParseTree('identifier', var_name_token.getValue()))

        # Confirm and consume the semicolon
        self.mustBe('symbol', ';')

        return class_var_dec_node

    

    def compileSubroutine(self):
        """
        Generates a parse tree for a method, function, or constructor
        @return a ParseTree that represents the method, function, or constructor
        """
        subroutine_dec_node = ParseTree("subroutineDec", None)

        subroutine_kind_token = self.mustBe('keyword')  # The keyword could be 'constructor', 'function', or 'method'
        subroutine_dec_node.addChild(ParseTree('keyword', subroutine_kind_token.getValue()))

        # This is a simplified version of return type parsing
        if self.have('keyword', 'void'):
            return_type_token = self.mustBe('keyword', 'void')
        else:
            return_type_token = self.compileType()
        subroutine_dec_node.addChild(ParseTree('keyword', return_type_token.getValue()))

        subroutine_name_token = self.mustBe('identifier')
        subroutine_dec_node.addChild(ParseTree('identifier', subroutine_name_token.getValue()))

        self.mustBe('symbol', '(')
        # Placeholder for parameter list parsing
        # In a complete implementation, this would involve more complex logic
        parameter_list_node = self.compileParameterList()
        subroutine_dec_node.addChild(parameter_list_node)
        self.mustBe('symbol', ')')

        # Placeholder for subroutine body parsing
        # In a complete implementation, this would involve more complex logic
        subroutine_body_node = self.compileSubroutineBody()
        subroutine_dec_node.addChild(subroutine_body_node)

        return subroutine_dec_node    
    
    def compileParameterList(self):
        """
        Generates a parse tree for a subroutine's parameters
        @return a ParseTree that represents a subroutine's parameters
        """
        parameters_node = ParseTree("parameterList", None)
        
        # Check if there is at least one parameter
        if not self.have('symbol', ')'):  # Assuming ')' follows the parameter list
            while True:
                type_node = self.compileType()
                parameters_node.addChild(type_node)
                
                var_name_token = self.mustBe('identifier', None)
                parameters_node.addChild(ParseTree('identifier', var_name_token.getValue()))
                
                # Check if there's another parameter after a comma
                if not self.have('symbol', ','):
                    break
                self.next()  # Consume the comma
        
        return parameters_node

    
    
    def compileSubroutineBody(self):
        """
        Generates a parse tree for a subroutine's body
        @return a ParseTree that represents a subroutine's body
        """
        body_node = ParseTree("subroutineBody", None)

        self.mustBe('symbol', '{')

        # Compile variable declarations if any
        while self.have('keyword', 'var'):
            var_dec_node = self.compileVarDec()
            body_node.addChild(var_dec_node)
        
        # Compile statements
        statements_node = self.compileStatements()
        body_node.addChild(statements_node)
        
        self.mustBe('symbol', '}')

        return body_node

    
    
    def compileVarDec(self):
        """
        Generates a parse tree for a variable declaration
        @return a ParseTree that represents a var declaration
        """
        var_dec_node = ParseTree("varDec", None)
        self.mustBe('keyword', 'var')
        type_node = self.compileType()
        var_dec_node.addChild(type_node)

        var_names = []
        var_names.append(self.mustBe('identifier').getValue())

        while self.have('symbol', ','):
            self.next()  # Consume the comma
            var_names.append(self.mustBe('identifier').getValue())

        for var_name in var_names:
            var_dec_node.addChild(ParseTree('identifier', var_name))

        self.mustBe('symbol', ';')
        return var_dec_node


    def compileStatements(self):
        """
        Generates a parse tree for a series of statements
        @return a ParseTree that represents the series of statements
        """
        statements_node = ParseTree("statements", None)
        valid_statement_keywords = ['let', 'if', 'while', 'do', 'return']
        
        # Process all statements until no valid statement keyword is found
        while self.current() is not None and self.have('keyword') and self.current().getValue() in valid_statement_keywords:
            if self.have('keyword', 'let'):
                statements_node.addChild(self.compileLet())
            elif self.have('keyword', 'if'):
                statements_node.addChild(self.compileIf())
            elif self.have('keyword', 'while'):
                statements_node.addChild(self.compileWhile())
            elif self.have('keyword', 'do'):
                statements_node.addChild(self.compileDo())
            elif self.have('keyword', 'return'):
                statements_node.addChild(self.compileReturn())
            else:
                # If the current token doesn't match any known statement, raise an exception
                raise ParseException(f"Unexpected statement type {self.current().getType()} with value '{self.current().getValue()}'")
        
        return statements_node
    
    
    def compileLet(self):
        """
        Generates a parse tree for a let statement
        @return a ParseTree that represents the statement
        """
        let_node = ParseTree("letStatement", None)
        self.mustBe('keyword', 'let')
        var_name_token = self.mustBe('identifier', None)
        let_node.addChild(ParseTree('identifier', var_name_token.getValue()))
        # Handle possible array indexing
        if self.have('symbol', '['):
            self.next()
            let_node.addChild(self.compileExpression())
            self.mustBe('symbol', ']')
        self.mustBe('symbol', '=')
        let_node.addChild(self.compileExpression())
        self.mustBe('symbol', ';')
        return let_node


    def compileIf(self):
        """
        Generates a parse tree for an if statement
        @return a ParseTree that represents the statement
        """
        if_node = ParseTree("ifStatement", None)
        self.mustBe('keyword', 'if')
        self.mustBe('symbol', '(')
        if_node.addChild(self.compileExpression())
        self.mustBe('symbol', ')')
        self.mustBe('symbol', '{')
        if_node.addChild(self.compileStatements())
        self.mustBe('symbol', '}')
        if self.have('keyword', 'else'):
            self.next()
            self.mustBe('symbol', '{')
            if_node.addChild(self.compileStatements())
            self.mustBe('symbol', '}')
        return if_node

    
    def compileWhile(self):
        """
        Generates a parse tree for a while statement
        @return a ParseTree that represents the statement
        """
        while_node = ParseTree("whileStatement", None)
        self.mustBe('keyword', 'while')
        self.mustBe('symbol', '(')
        while_node.addChild(self.compileExpression())
        self.mustBe('symbol', ')')
        self.mustBe('symbol', '{')
        while_node.addChild(self.compileStatements())
        self.mustBe('symbol', '}')
        return while_node



    def compileDo(self):
        """
        Generates a parse tree for a do statement
        @return a ParseTree that represents the statement
        """
        do_node = ParseTree("doStatement", None)
        self.mustBe('keyword', 'do')
        
        do_node.addChild(ParseTree('keyword', 'do'))

        # Assuming 'skip' is used as a placeholder for a subroutine call
        if self.have('keyword', 'skip'):
            do_node.addChild(ParseTree('keyword', 'skip'))
            self.next()  # Consume the 'skip' token
        else:

            # Assume that a subroutine call starts with an identifier (function name or object name)
            subroutine_name_token = self.mustBe('identifier', None)
            subroutine_call_node = ParseTree("subroutineCall", None)
            subroutine_call_node.addChild(ParseTree('identifier', subroutine_name_token.getValue()))

            # Handle class methods or functions (e.g., someObject.someMethod or someFunction)
            if self.have('symbol', '.'):
                self.mustBe('symbol', '.')
                method_name_token = self.mustBe('identifier', None)
                subroutine_call_node.addChild(ParseTree('identifier', method_name_token.getValue()))

            # Next, expect an opening parenthesis
            self.mustBe('symbol', '(')

            # Compile the expression list if any arguments are present
            subroutine_call_node.addChild(self.compileExpressionList())

            # Expect a closing parenthesis after the expression list
            self.mustBe('symbol', ')')

            # Add the compiled subroutine call to the do statement node
            do_node.addChild(subroutine_call_node)

        # A semicolon is expected to terminate the do statement
        self.mustBe('symbol', ';')
        return do_node



    def compileReturn(self):
        """
        Generates a parse tree for a return statement
        @return a ParseTree that represents the statement
        """
        return_node = ParseTree("returnStatement", None)
        # Confirm the 'return' keyword is present
        self.mustBe('keyword', 'return')
        
        # Check if there is an expression after the 'return'
        if not self.have('symbol', ';'):
            # If there is an expression, compile it and add to the return node
            return_node.addChild(self.compileExpression())
        
        # Confirm the presence of the semicolon to end the return statement
        self.mustBe('symbol', ';')
        return return_node



    def compileExpression(self):
        """
        Generates a parse tree for an expression
        @return a ParseTree that represents the expression
        """
        expression_node = ParseTree("expression", None)
        
        # Check if 'skip' is used as a placeholder for an expression
        if self.have('keyword', 'skip'):
            expression_node.addChild(ParseTree('keyword', 'skip'))
            self.next()  # Consume the 'skip' token
        else:
            # An expression starts with a term
            expression_node.addChild(self.compileTerm())
            
            # After a term, there might be zero or more (op term) pair
            ops = ['+', '-', '*', '/', '&', '|', '<', '>', '=']
            while self.have('symbol') and self.current().getValue() in ops:
                op_token = self.mustBe('symbol', None)
                expression_node.addChild(ParseTree('op', op_token.getValue()))
                expression_node.addChild(self.compileTerm())
            
        return expression_node


    def compileTerm(self):
        """
        Generates a parse tree for an expression term
        @return a ParseTree that represents the expression term
        """
        term_node = ParseTree("term", None)
    
        if self.have('integerConstant'):
            term_node.addChild(ParseTree('integerConstant', self.mustBe('integerConstant', None).getValue()))
        elif self.have('stringConstant'):
            term_node.addChild(ParseTree('stringConstant', self.mustBe('stringConstant', None).getValue()))
        elif self.have('keyword'):
            term_node.addChild(ParseTree('keywordConstant', self.mustBe('keyword', None).getValue()))
        # Handle more complex terms like variable names, array indexing, and subroutine calls
        # This is a placeholder for more complex term parsing logic
        
        return term_node


    def compileExpressionList(self):
        """
        Generates a parse tree for an expression list
        @return a ParseTree that represents the expression list
        """
        expression_list_node = ParseTree("expressionList", None)
    
        # If the next token isn't ')', there's at least one expression
        if not self.have('symbol', ')'):
            expression_list_node.addChild(self.compileExpression())
            while self.have('symbol', ','):
                self.mustBe('symbol', ',')
                expression_list_node.addChild(self.compileExpression())
        
        return expression_list_node


    def next(self):
        """
        Advance to the next token
        """
        self.current_token_index += 1


    def current(self):
        """
        Return the current token
        @return the token
        """
        if self.current_token_index < len(self.tokens):
            return self.tokens[self.current_token_index]
        else:
            return None  # No more tokens


    def have(self, expectedType, expectedValue=None):
        current_token = self.current()
        if current_token is None:
            return False
        if expectedValue is None:
            return current_token.getType() == expectedType
        else:
            return current_token.getType() == expectedType and current_token.getValue() == expectedValue


    def mustBe(self,expectedType,expectedValue=None):
        """
        Check if the current token matches the expected type and expectedValue.
        If so, advance to the next token, returning the current token, otherwise throw/raise a ParseException.
        @return token that was current prior to advancing.
        """
        if self.current() is None:
            raise ParseException(f"Unexpected end of token stream. Expected {expectedType} with value '{expectedValue}'")
        
        if self.have(expectedType, expectedValue):
            current_token = self.current()
            self.next()
            return current_token
        else:
            current_value = self.current().getValue() if self.current() else "None"
            raise ParseException(f"Expected {expectedType} with value '{expectedValue}', but found {self.current().getType()} with value '{current_value}'")
    

if __name__ == "__main__":


    """ First testcase
    Tokens for:
        class MyClass {
        
        }
    """
    # tokens = []
    # tokens.append(Token("keyword","class"))
    # tokens.append(Token("identifier","MyClass"))
    # tokens.append(Token("symbol","{"))
    # tokens.append(Token("symbol","}"))
    
    """ Second testcase
        class Main {
        static int a ;
    }
    """
    # tokens = []
    # tokens.append(Token("keyword","class"))
    # tokens.append(Token("identifier","Main"))
    # tokens.append(Token("symbol","{"))
    # tokens.append(Token("keyword","static"))
    # tokens.append(Token("keyword","int"))
    # tokens.append(Token("identifier","a"))
    # tokens.append(Token("symbol",";"))
    # tokens.append(Token("symbol","}"))
    
    """ Third testcase
        function void myFunc ( int a ) {
        var int a ;
        let a = 1 ;
    }
    """
    # tokens = []
    # tokens.append(Token("keyword","class"))
    # tokens.append(Token("identifier","Main"))
    # tokens.append(Token("symbol","{"))
    # tokens.append(Token("keyword","function"))
    # tokens.append(Token("keyword","void"))
    # tokens.append(Token("identifier","myFunc"))
    # tokens.append(Token("symbol","("))
    # tokens.append(Token("keyword","int"))
    # tokens.append(Token("identifier","a"))
    # tokens.append(Token("symbol",")"))
    # tokens.append(Token("symbol","{"))
    # tokens.append(Token("keyword","var"))
    # tokens.append(Token("keyword","int"))
    # tokens.append(Token("identifier","a"))
    # tokens.append(Token("symbol",";"))
    # tokens.append(Token("keyword","let"))
    # tokens.append(Token("identifier","a"))
    # tokens.append(Token("symbol","="))
    # tokens.append(Token("integerConstant","1"))
    # tokens.append(Token("symbol",";"))
    # tokens.append(Token("symbol","}"))
    # tokens.append(Token("symbol","}"))
    
    """ Fourth testcase
        let a = skip ;
        do skip ;
        return ;
    """
    tokens = []
    tokens.append(Token("keyword","class"))
    tokens.append(Token("identifier","Main"))
    tokens.append(Token("symbol","{"))
    tokens.append(Token("keyword","let"))
    tokens.append(Token("identifier","a"))
    tokens.append(Token("symbol","="))
    tokens.append(Token("keyword","skip"))
    tokens.append(Token("symbol",";"))
    tokens.append(Token("keyword","do"))
    tokens.append(Token("keyword","skip"))
    tokens.append(Token("symbol",";"))
    tokens.append(Token("keyword","return"))
    tokens.append(Token("symbol",";"))
    tokens.append(Token("symbol","}"))

    parser = CompilerParser(tokens)
    try:
        result = parser.compileProgram()
        print(result)
    except ParseException as e:
        print(f"Error Parsing: {str(e)}")
