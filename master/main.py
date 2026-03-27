import json
from antlr4 import FileStream, CommonTokenStream
from parser.DevOpsDSLLexer import DevOpsDSLLexer
from parser.DevOpsDSLParser import DevOpsDSLParser
from interpreter.interpreter import DevOpsInterpreter
from executor.executor import Executor


def load_json(path):
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def main():
    nodes = load_json("config/nodes.json")
    groups = load_json("config/groups.json")

    # Cambia a False cuando tengas acceso real por SSH a las Raspberry
    executor = Executor(nodes, simulate=True)

    input_stream = FileStream("script.dsl", encoding="utf-8")
    lexer = DevOpsDSLLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = DevOpsDSLParser(stream)
    tree = parser.program()

    interpreter = DevOpsInterpreter(executor, groups)
    results = interpreter.visit(tree)

    print("\n===== RESULTADOS =====")
    for item in results:
        print(item)


if __name__ == "__main__":
    main()