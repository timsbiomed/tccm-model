import os
import unittest

from biolinkml.generators.pythongen import PythonGenerator
from biolinkml.generators.yamlgen import YAMLGenerator

from test import BASE_DIR

MODULE = "mapping"
SCHEMA = "mapversion"


class ModelBuildTestCase(unittest.TestCase):
    """ A Python entry point to the model build process to allow debugging of biolinkml from here """

    def test_build_python(self):
        python = PythonGenerator(os.path.join(BASE_DIR, f'model/{MODULE}/{SCHEMA}.yaml'), mergeimports=False).serialize()
        print(python)

    def test_build_yaml(self):
        yaml = YAMLGenerator(os.path.join(BASE_DIR, f'model/{MODULE}/{SCHEMA}.yaml'),
                               mergeimports=False).serialize()
        print(yaml)


if __name__ == '__main__':
    unittest.main()
