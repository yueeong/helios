__author__ = 'yueeong'

import os


def run_tests():
    from proboscis import TestProgram

    '''
    Add more from Tests import file_name to have your tests run by test_controller_example.py
    in the example below import ap_example runs the tests in ap_example.py under the Tests directory

    '''
    from Tests import example

    try:
        TestProgram().run_and_exit()
    except SystemExit:
        os._exit(0)


if __name__ == '__main__':
    run_tests()