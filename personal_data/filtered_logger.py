#!/usr/bin/env python3
"""
Module for filter_datum function that uses regex
to obfuscate certain user information
"""
import re
import logging
from typing import List, Tuple

PII_FIELDS: Tuple[str, ...] = ("name", "email", "phone", "ssn", "password")


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

    #  Each RedactingFormatter instance initialized with fields
    def __init__(self, fields: List[str]):
        super(RedactingFormatter, self).__init__(self.FORMAT)
        self.fields = fields  # store list of fields in object instance

    def format(self, record: logging.LogRecord) -> str:
        """Formats the message log, redacting certain PII

        Args:
            record (logging.LogRecord): log record to be formatted

        Returns:
            str: the redacted log message
        """
        no_redact = super(RedactingFormatter, self).format(record)
        # use filter_datum to create redacted message
        redacted_message = filter_datum(self.fields, self.REDACTION,
                                        no_redact, self.SEPARATOR)
        return redacted_message


def get_logger() -> logging.Logger:
    """
    Creates and returns a logger that redacts information flagged as PII
    """
    # Create logger "user_data"
    logger = logging.getLogger("user_data")
    logger.setLevel(logging.INFO)
    logger.propagate = False  # stop logging propogation to parent loggers
    #  stream_handler sends log messages to console
    stream_handler = logging.StreamHandler()
    #  formats log message to redact PII
    redact_format = RedactingFormatter(list(PII_FIELDS))
    stream_handler.setFormatter(redact_format)
    logger.addHandler(stream_handler)

    return logger
