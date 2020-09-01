import unittest

from biolinkml.utils.yamlutils import as_yaml

from valueset.valuesetdefinition import *
from yaml import dump


class DefinitionFormTestCase(unittest.TestCase):
    def test_minimal_definition(self):
        entry = SpecificEntityList("http://loinc.org/", entities={'abc': None, 'def': None})
        vde = ValueSetDefinitionEntry(include=entry)
        defn = ValueSetDefinition(resourceID="SIMPLE", about="http://something.org/smthing", entry=[vde])
        print(as_yaml(defn))

    def test_code_system(self):
        hpo = CodeSystemReference('HPO', 'Human Phenotype Ontology', href='https://hpo.jax.org/app/')
        entry = CompleteCodeSystemReference(hpo)
        vde = ValueSetDefinitionEntry(include=entry)
        defn = ValueSetDefinition('HPO', about="http://ontologies.r.us/valueset/allofHPO", entry=[vde])
        print(as_yaml(defn))
        print(dump(defn))


if __name__ == '__main__':
    unittest.main()
