# -*- coding: utf-8 -*-
"""
Created on Fri Dic 02 10:12:00 2022

@author: Jhonatan Martínez
"""

from typing import List
import logging
import os
from shutil import move, rmtree


def get_current_path() -> str:
    """Obtiene el directorio actual de la aplicación.

    Returns:
        str: Directorio actual.
    """

    try:
        return os.getcwd()
    except OSError as exc:
        logging.error(str(exc),
                      exc_info=True)
        raise


def create_folder(folder_names: List[str], directory: str = '') -> None:
    """Crear carpeta(s).

    Args:
        folder_names (List[str]): Nombre de carpeta(s) a crear.
        directory (str): Directorio dónde se creará la carpeta, default raíz dónde se encuentra la aplicación.
    """

    if not directory:
        directory = get_current_path()

    for folder in folder_names:
        try:
            folder_path = os.path.join(directory, folder)
            if not path_exists(folder_path):
                os.mkdir(folder_path)
                logging.info('Folder %s created successfully', folder)
            else:
                logging.info('Folder %s already exists', folder)
        except (OSError, Exception) as exc:
            logging.error(str(exc),
                          exc_info=True)
            raise


def delete_folder(*folders: str) -> None:
    """Delete folder, path, directory

    Args:
        *folders (str): Full path(s) to delete
    """
    for folder in folders:
        try:
            if path_exists(folder):
                rmtree(folder)
                logging.info('Folder %s deleted successfully', folder)
            else:
                logging.info('Folder %s not exists', folder)
        except (OSError, Exception) as exc:
            logging.error(str(exc),
                          exc_info=True)
            raise


def move_file(file: str, destination_directory: str) -> bool:
    """Copiar los archivos de una carpeta a otra

    Args:
        file (str): Ruta completa del archivo a mover.\n
        destination_directory (str): Carpeta a la que se moverán el o los archivos.

    Returns:
        bool: El valor de retorno es True si se pudo mover el archivo, False en caso contrario.
    """
    try:
        destination_file = os.path.join(destination_directory, os.path.basename(file))
        move(file, destination_file)
        return True
    except (OSError, Exception) as exc:
        logging.error(str(exc),
                      exc_info=True)
        raise


def move_directory(directory: str, destination_directory: str) -> bool:
    """Copiar los archivos de una carpeta a otra

        Args:
            directory (str): Carpeta dónde se encuentran los archivos o archivo a mover.\n
            destination_directory (str): Carpeta a la que se moverán el o los archivos.
        """
    try:
        if os.path.isdir(directory):
            for file_name in os.listdir(directory):
                move_file(file_name, destination_directory)
        return True
    except (OSError, Exception) as exc:
        logging.error(str(exc),
                      exc_info=True)
        raise


def path_exists(path: str) -> bool:
    """Verificar el directorio existe

    Args:
        path (str):

    Returns:
        bool: El valor de retorno es True si se existe el directorio, False en caso contrario.
    """
    return os.path.exists(path)
