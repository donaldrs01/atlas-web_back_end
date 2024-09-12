#!/usr/bin/env python3
"""
Module for filter_datum function that uses regex
to obfuscate certain user information
"""
import re
import logging
from typing import List


def filter_datum(fields: List[str], redaction: str, message: str,
                 separator: str) -> str:
    """
    Function that returns a log message with key information
    obfuscated

    Args:
        fields (List[str]): list of strings containing all fields to obfuscate
        redaction (str): str containing the symbol which will obfuscate PII
        message (str): str that represents the log line
        separator (str): str that represents the character that separates
        each field in log line

    Returns:
        str: log message with certain fields obfuscated
    """
    # construct regex pattern to match field=value format
    for field in fields:
        #  re.escape(field) and re.escape(separator)
        # treats each field string value and separator literally
        pattern = rf"{re.escape(field)}=.*?{re.escape(separator)}"
    #  re.sub to replace field values with redaction symbols
        message = re.sub(pattern, f"{field}={redaction}{separator}", message)
    return message


class RedactingFormatter(logging.Formatter):
    """ Redacting Formatter class
        """

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: List[str]):
        #  Each RedactingFormatter object initialized with fields
        super(RedactingFormatter, self).__init__(self.FORMAT)
        self.fields = fields  # store list of fields in object instance

    def format(self, record: logging.LogRecord) -> str:
        NotImplementedError
