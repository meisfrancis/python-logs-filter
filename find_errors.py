#!/usr/bin/env python3
import sys
import os
import re
from get_system_argument import get_args


def error_search(log_file):
    """
    Require input from user and return result after searching throughout the log file
    :param str log_file: Path to log file
    :return list[str]:
    """
    error = input('What is the error? ')
    returned_errors = []
    with open(log_file, mode='r', encoding='UTF-8') as file:
        for log in file.readlines():
            error_patterns = ["error"]
            for str in error.split(' '):
                error_patterns.append(rf"{str.lower()}")
            if all(re.search(error_pattern, log.lower()) for error_pattern in error_patterns):
                returned_errors.append(log)
        file.close()
    return returned_errors


def file_output(returned_errors, output_file_path, output_file_name):
    """
    Write error to output file
    :param list[str] returned_errors: List error get from func error_search
    :param str output_file_path: Path to output file
    :param str output_file_name: name of output file
    """
    with open(f'{output_file_path}/{output_file_name}', 'w') as file:
        for error in returned_errors:
            file.write(error)
        file.close()


if __name__ == '__main__':
    log_file = get_args(1)
    output_path = get_args(2, os.getcwd())
    output_name = get_args(3, 'errors_found.log')
    returned_errors = error_search(log_file)
    file_output(returned_errors, output_path, output_name)
    sys.exit(0)
