# run_doctest.py

import doctest
import importlib
import argparse


def run_doctests_for_function(module_name, func_name):
    """
    Run doctests for the given function in the specified module.
    """
    module = importlib.import_module(module_name)
    func = getattr(module, func_name)

    finder = doctest.DocTestFinder()
    runner = doctest.DocTestRunner()

    # Find the doctests for the specific function
    tests = finder.find(func)

    # Run each test
    for test in tests:
        runner.run(test)

    # Summarize results
    runner.summarize()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Run doctests for a specific function.")
    parser.add_argument('module', help="The module containing the function.")
    parser.add_argument('function', help="The function to test.")

    args = parser.parse_args()

    run_doctests_for_function(args.module, args.function)
