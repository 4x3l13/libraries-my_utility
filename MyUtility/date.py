# -*- coding: utf-8 -*-
"""
Created on Fri Dic 02 10:12:00 2022

@author: Jhonatan Martínez
"""

from datetime import datetime, timedelta
import logging


def get_date(days_offset: int = 0, separator: str = "-") -> str:
    """Obtiene la fecha actual en formato string con un desfase de día opcional y un separador especificado

    Args:
        days_offset (int, optional): Agrega o resta días a la fecha actual.
        separator (String, optional): Separador para formato de fecha

    Returns:
        str: fecha
    """
    try:
        now = datetime.now() + timedelta(days=days_offset)
        return now.strftime(f'%Y{separator}%m{separator}%d')
    except ValueError as exc:
        logging.error(str(exc),
                      exc_info=True)
        raise


def get_time() -> str:
    """Obtener la hora actual en string con formato hh:mm:ss.

    Returns:
        str: hora
    """

    try:
        now = datetime.now()
        return now.strftime('%H:%M:%S')
    except ValueError as exc:
        logging.error(str(exc),
                      exc_info=True)
        raise


def timestamp_to_date(timestamp: datetime.timestamp, separator: str = "-") -> str:
    """Convierte de timestamp a date

    Args:
        timestamp (timestamp): fecha en timestamp.
        separator (str, optional): Separador para dar formato a la fecha

    Returns:
            str:

    """

    try:
        date = datetime.fromtimestamp(timestamp)
        return date.strftime(f'%Y{separator}%m{separator}%d')
    except ValueError as exc:
        logging.error(str(exc),
                      exc_info=True)
        raise


def string_to_date(date: str) -> datetime:
    """Convierte un string a date

    Args:
        date (str): fecha a convertir en date.

    Returns:
        datetime:
    """

    try:
        return datetime.strptime(date, '%Y-%m-%d')
    except ValueError as exc:
        logging.error(str(exc),
                      exc_info=True)
        raise
