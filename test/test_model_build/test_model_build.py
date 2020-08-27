import os
import unittest

from biolinkml.generators.pythongen import PythonGenerator
from biolinkml.generators.yamlgen import YAMLGenerator

from test import BASE_DIR


class ModelBuildTestCase(unittest.TestCase):
    """ A Python entry point to the model build process to allow debugging of biolinkml from here """
    def test_build_valueset(self):
        model = YAMLGenerator(os.path.join(BASE_DIR, 'model/valueset/valuesetdefinition.yaml'), mergeimports=False)
        python = PythonGenerator(model).serialize()
        print(python)

    def test_build_entityreference(self):
        python = PythonGenerator(os.path.join(BASE_DIR, 'model/core/filters.yaml'), mergeimports=False).serialize()
        print(python)


if __name__ == '__main__':
    unittest.main()
