# -*- coding: utf-8 -*-
"""
Created on Fri Dic 02 10:12:00 2022

@author: Jhonatan Martínez
"""


import json
import logging
from typing import Any, Dict


def dictionary_to_json(dictionary: Dict) -> Dict:
    """Convertir datos de diccionario a json

    Args:
        dictionary (Dict): diccionario a convertir a Json. \n

    Returns:
        json:
    """
    data = None
    try:
        data = json.dumps(dictionary)
    except ValueError as exc:
        logging.error(str(exc),
                      exc_info=True)
    return data


def json_to_dict(json_: Any) -> Dict:
    """Convertir datos de json a diccionario

    Args:
        json_ (json): json a convertir a diccionario. \n

    Returns:
        Dict:
    """
    data = None
    try:
        data = json.loads(json_)
    except ValueError as exc:
        logging.error(str(exc),
                      exc_info=True)
    return data


def json_file_to_dict(json_file: Any) -> Dict:
    """Convertir datos de json a diccionario

    Args:
        json_file (json): json_file a convertir a diccionario. \n

    Returns:
        Dict:
    """
    data = None
    try:
        data = json.load(json_file)
    except ValueError as exc:
        logging.error(str(exc),
                      exc_info=True)
    return data
