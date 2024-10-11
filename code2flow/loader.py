"""
Module for processors loading related functions.
"""

from enum import Enum
import importlib
import inspect
import os

from code2flow.language import LANGUAGE_EXTENTIONS, Language
from code2flow.model import BaseLanguage


def load_processor(language: Language):
    """
    Find and load processor for specified language.
    Processor is a child class of BaseLanguage.
    :param language Language: language enum.
    :returns: processor class.
    :rtype: the processor class or None.
    """

    try:
        mod = importlib.import_module(f"code2flow.processors.{language}")
        classes = inspect.getmembers(mod, inspect.isclass)
        for c in classes:
            if isinstance(c, BaseLanguage):
                return c
    except Exception as ex:
        # TODO: add logger
        pass


# List of loaded processors
_processors:list[BaseLanguage] = None


def load_all_processors():
    """
    Find and load all processors in processors folder.
    A processor is a child class of BaseLanguage.
    :returns: list of processor classes.
    :rtype list[BaseLanguage]:
    """
    global _processors

    if _processors is not None:
        return _processors

    _processors = []
    try:

        # TODO: replace 'listdir' with 'walk' func so that 
        # We can organize processors in it's own folder.
        cur_dir = os.path.dirname(__file__)
        processor_folder = f"{cur_dir}/processors"
        processor_files = [file for file in os.listdir(processor_folder) 
                           if os.path.isfile(os.path.join(processor_folder, file))]

        # Remove trailing '.py' in file name
        tmp_list = []
        for file in processor_files:
            parts = file.split('.')
            tmp_list.append(parts[0])
        processor_files = tmp_list

        for file in processor_files:
            mod = importlib.import_module(f'code2flow.processors.{file}')
            classes = inspect.getmembers(mod, inspect.isclass)
            for c in classes:
                if issubclass(c[1], BaseLanguage) and c[1] != BaseLanguage:
                    _processors.append(c[1])
        
        return _processors
    
    except Exception as ex:
        # TODO: add logger
        pass

    return _processors
