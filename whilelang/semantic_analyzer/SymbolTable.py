class Symbol:
    def __init__(self, name, type_):
        self.name = name
        self.type = type_


class SymbolTable:
    def __init__(self):
        self.scope_stack = [{}]

    def enter_scope(self):
        self.scope_stack.append({})

    def exit_scope(self):
        if len(self.scope_stack) > 1:
            self.scope_stack.pop()

    def insert(self, name, symbol):
        current_scope = self.scope_stack[-1]
        if name in current_scope:
            print(f"Error Semántico: La variable '{name}' ya ha sido declarada en este ámbito.")
            return False
        current_scope[name] = symbol
        return True

    def lookup(self, name):
        for scope in reversed(self.scope_stack):
            if name in scope:
                return scope[name]
        return None