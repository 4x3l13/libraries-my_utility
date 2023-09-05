# -*- coding: utf-8 -*-
"""
Created on Thu Mar 09 10:10:00 2023

@author: Jhonatan Martínez
"""
import cryptocode


def decrypt(value: str, key: str) -> str:
    """Desencriptar un valor

    Args:
        value (str): Valor a desencriptar.
        key (str): Clave para desencriptar.

    Returns:
        str: valor desencriptado
    """
    return cryptocode.decrypt(value, key)


def encrypt(value: str, key: str) -> str:
    """Encriptar un valor

    Args:
        value (str): Valor a encriptar.
        key (str): Clave para encriptar.

    Returns:
        str: valor encriptado
    """

    return cryptocode.encrypt(value, key)
