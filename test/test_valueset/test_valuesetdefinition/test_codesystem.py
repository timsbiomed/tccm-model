import unittest

from jsonasobj import as_json

from core import CodeSystemURI, CodeSystemSummary
from resource import FinalizableState
from valueset import ValueSetDefinitionEntry, Include, ValueSetDefinition, Exclude, Intersect


class TestCodeSystemQuery(unittest.TestCase):
    def test_codesystem_elements(self):
        # A single URI
        x = CodeSystemURI("http://purl.bioontology.org/ontology/ICD10CM/")

        # A short summary -- only required field IS the uri
        y = CodeSystemSummary("ICD-10", x, "http://purl.bioontology.org/ontology/ICD10CM/")
        print(as_json(y))

        # A value set definition entry that consists of all concept codes in ICD10CM at an unspecified point
        z = Include(x)
        print(as_json(z))

        d = ValueSetDefinition("http://purl.bioontology.org/ontology/ICD10CM",
                               "ICD10CM-VS", "All active concept codes in ICD-10-CM",
                               final=FinalizableState.FINAL, definition=z)
        print(as_json(d))
        d2 = ValueSetDefinition("urn:uuid:B1B9A74D-2DD1-4CB3-AC90-EE23164110D3",
                                "ICD10CM-Changes", "Concept codes that are in two versions of ICD-10-CM but not both",
                                definition = [
                                    Intersect([
                                        Include("http://purl.bioontology.org/ontology/ICD10CM/2019ab"),
                                        Exclude("http://purl.bioontology.org/ontology/ICD10CM/2018aa")
                                    ],[
                                        Include("http://purl.bioontology.org/ontology/ICD10CM/2018aa"),
                                        Exclude("http://purl.bioontology.org/ontology/ICD10CM/2019ab")

                                    )





if __name__ == '__main__':
    unittest.main()
