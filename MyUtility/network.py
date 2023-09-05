# -*- coding: utf-8 -*-
"""
Created on Tue Sep 05 16:02:00 2023

@author: Jhonatan Martínez
"""

import logging
import socket


def get_hostname() -> str:
    """Obtener el nombre del equipo

    Returns:
        str: Nombre del equipo
    """
    try:
        return socket.gethostname()
    except (socket.error, Exception) as exc:
        logging.error(str(exc),
                      exc_info=True)
        raise


def get_ip() -> str:
    """Obtener la IP del equipo

    Returns:
        str: IP
    """
    try:
        return socket.gethostbyname(get_hostname())
    except (socket.error, Exception) as exc:
        logging.error(str(exc),
                      exc_info=True)
        raise
