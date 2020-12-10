import os
# from turpy import __version__
from turpy.io.load_yaml import load_yaml
from turpy.utils import script_as_module

from io import BytesIO, StringIO, IOBase
from typing import Union

# def test_version():
#    assert __version__ == 0.1.3


def test_load_yaml(file: Union[str, BytesIO, StringIO] = 'tests/test_yaml.yaml'):
    """ Tests load_yaml for `filepath` string"""
    assert file is not None
    assert isinstance(file, str)
    assert load_yaml(file=file)
    my_dict = load_yaml(file=file)
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

