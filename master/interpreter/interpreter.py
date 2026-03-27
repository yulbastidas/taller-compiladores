import threading
from parser.DevOpsDSLVisitor import DevOpsDSLVisitor


class DevOpsInterpreter(DevOpsDSLVisitor):
    def __init__(self, executor, groups):
        self.executor = executor
        self.groups = groups

    def strip_quotes(self, text):
        if text.startswith('"') and text.endswith('"'):
            return text[1:-1]
        return text

    def visitProgram(self, ctx):
        results = []
        for statement in ctx.statement():
            result = self.visit(statement)
            if result is not None:
                results.append(result)
        return results

    def visitStatement(self, ctx):
        return self.visitChildren(ctx)

    def visitNodeCommand(self, ctx):
        node_name = ctx.ID().getText()
        script_name = self.strip_quotes(ctx.STRING().getText())
        return self.executor.run_remote_script(node_name, script_name)

    def visitGroupCommand(self, ctx):
        group_name = ctx.ID().getText()
        return self.executor.update_group(group_name, self.groups)

    def visitDeployCommand(self, ctx):
        app_name = ctx.ID(0).getText()
        group_name = ctx.ID(1).getText()
        return self.executor.deploy_app(app_name, group_name, self.groups)

    def visitRule(self, ctx):
        condition_text = ctx.condition().getText()
        action_text = ctx.action().getText()
        return {
            "type": "rule",
            "condition": condition_text,
            "action": action_text,
            "status": "registered"
        }

    def visitParallelBlock(self, ctx):
        results = []
        threads = []

        def run_statement(statement_ctx):
            result = self.visit(statement_ctx)
            results.append(result)

        for statement in ctx.statement():
            t = threading.Thread(target=run_statement, args=(statement,))
            threads.append(t)
            t.start()

        for t in threads:
            t.join()

        return {
            "type": "parallel",
            "results": results
        }
        