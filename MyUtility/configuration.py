# -*- coding: utf-8 -*-
"""
Created on Fri Dic 02 10:12:00 2022

@author: Jhonatan Martínez
"""

import configparser
import logging
from typing import Dict
from .security import decrypt


def read(filename: str, key_decrypt: str) -> Dict:
    """Leer archivo de configuración.

    Args:
        filename (str): Nombre del archivo de configuración. \n
        key_decrypt (str): Clave para desencriptar.

    Returns:
        Dict: Valores leídos del archivo de configuración.
    """
    config_data = {}
    try:
        config = configparser.RawConfigParser()
        config.read(filename)
        for section in config.sections():
            subsection = {}
            for key, value in config.items(section):
                if key.lower() in ['user', 'password']:
                    subsection[key] = decrypt(value=value, key=key_decrypt)
                else:
                    subsection[key] = value
            config_data[section] = subsection
    except (ValueError, Exception) as exc:
        logging.error(str(exc),
                      exc_info=True)
    return config_data


def edit(filename: str, section: str, key: str, value: str) -> None:
    """Editar archivo de configuración .

    Args:
        filename (str): Nombre del archivo de configuración. \n
        section (str): Seccion del archivo de configuración. \n
        key (str): Clave a modificar. \n
        value (str): Valor a modificar. \n
    """
    config = configparser.ConfigParser()
    config.read(filename)
    if section not in config:
        config.add_section(section)
    config[section][key] = value
    with open(filename, 'w', encoding='utf-8') as file:
        config.write(file)
