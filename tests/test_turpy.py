from turpy import __version__
from turpy.io.load_yaml import load_yaml

def test_version():
    assert __version__ == '0.1.1'

def test_load_yaml(filepath: str = 'tests/test_yaml.yaml'):
    """ Tests load_yaml for `filepath` string"""
    assert filepath is not None
    assert isinstance(filepath, str)
    assert load_yaml(filepath=filepath)
    my_dict = load_yaml(filepath=filepath)
    assert my_dict is not None
    assert isinstance(my_dict, dict)
