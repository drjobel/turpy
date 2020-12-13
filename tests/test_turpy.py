import os
# from turpy import __version__
from turpy.io.load_yaml import load_yaml
from turpy.utils import script_as_module, string_search_in_list
from turpy import Metadata

from io import BytesIO, StringIO
from typing import Union

# def test_version():
#    assert __version__ == 0.1.6


def test_load_yaml_file(file: Union[str, BytesIO, StringIO] = StringIO("test: Ok")):
    """ Tests load_yaml for `filepath` string"""
    
    assert file is not None
    assert isinstance(file, BytesIO) or isinstance(file, StringIO)
    my_dict = load_yaml(file=file)
    assert my_dict is not None
    assert isinstance(my_dict, dict)


def test_load_yaml_filepath(filepath: str = 'tests/test_yaml.yaml'):
    """ Tests load_yaml for `filepath` string"""

    assert filepath is not None
    assert os.path.isfile(os.path.abspath(filepath))

    my_dict = load_yaml(filepath=filepath)
    assert my_dict is not None
    assert isinstance(my_dict, dict)


def test_script_as_module(
        module_filepath=os.path.abspath('./src/turpy/io/load_yaml.py'),
        package_path=os.path.abspath('./src/turpy/')):

    print(os.path.abspath('./src/turpy/io/load_yaml.py'))
    assert module_filepath is not None
    assert os.path.isfile(module_filepath)
    assert package_path is not None
    assert os.path.isdir(package_path)

def test_metadata():
    context = Metadata(metadata={})
    metadata = context.metadata
    assert isinstance(metadata, dict)
    metadata.update({'test': True})
    assert metadata['test'] == True


def test_string_search_in_list(
    input_string='one', 
    searching_list=['There is ONE', 'two times']):
    assert string_search_in_list(
        input_string=input_string,
        searching_list = searching_list
        )[0] == 'There is ONE'



