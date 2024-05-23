# author: alf64
# This is a script that searches for dirs (cases) in folder1\\folder2\\ and executes exec_command within each of them.
# In this case, pytest command is shown as an example.
import os, sys


def main():
    # This scripts exit codes.
    EXIT_CODE_SUCCESS = 0
    EXIT_CODE_FAILURE = -1

    script_name = os.path.basename(__file__)
    print("Welcome to "+str(script_name)+" script.")
    this_script_path = os.path.realpath(__file__) # includes name of the .py script
    this_dir_path = os.path.dirname(this_script_path) #excludes name of the .py script
    folder2_path = os.path.join(this_dir_path, "folder1\\folder2")
    cases_list = os.listdir(folder2_path)
    number_of_cases = len(cases_list)
    exec_command = ("pytest -s {}\SomePytestTestFile.py::()::SomePytestTestFunction")

    print("Number of cases found: "+str(number_of_cases))

    if number_of_cases == 0:
        print("No cases to be executed. Terminating script.")
        sys.exit(EXIT_CODE_SUCCESS)

    cases_cnt = 0
    for case in cases_list:
        print("Executing case {} out of {}. ".format(str(cases_cnt+1), str(number_of_cases)), end='') # end = '' ensures no new-line at the end of print
        print("Case name is: "+case)
        case_path = os.path.join(folder2_path, case)
        case_cmd_call = exec_command.format(case_path)
        # print("Exec cmd is: "+case_cmd_call)
        pytest_result = os.system(case_cmd_call)
        print_pytest_exit_result(pytest_result)
        cases_cnt += 1


def print_pytest_exit_result(pytest_exit_code = 0):
    PYTEST_EXIT_CODE_0 = "SUCCESS!"
    PYTEST_EXIT_CODE_1 = "ERROR! pytest has returned test failures!"
    PYTEST_EXIT_CODE_2 = "ERROR! pytest execution was interrupted by user!"
    PYTEST_EXIT_CODE_3 = "ERROR! pytest internal error occured!"
    PYTEST_EXIT_CODE_4 = "ERROR! pytest cmd line usage error occured!"
    PYTEST_EXIT_CODE_5 = "ERROR! pytest did not collect any tests!"

    pytest_exit_codes = {
        PYTEST_EXIT_CODE_0 : 0,
        PYTEST_EXIT_CODE_1 : 1,
        PYTEST_EXIT_CODE_2 : 2,
        PYTEST_EXIT_CODE_3 : 3,
        PYTEST_EXIT_CODE_4 : 4,
        PYTEST_EXIT_CODE_5 : 5
    }

    print("pytest returned exit code: "+str(pytest_exit_code)+" ", end="")
    if pytest_exit_code in pytest_exit_codes.values():
        py_e_codes_keys = list(pytest_exit_codes.keys())
        print("("+py_e_codes_keys[pytest_exit_code]+")")
    else:
        print("(unknown code)")


if __name__ == '__main__':
    main()
