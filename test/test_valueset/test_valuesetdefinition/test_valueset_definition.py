import unittest
from dataclasses import dataclass
from typing import Optional, List, Union

from biolinkml.utils.yamlutils import YAMLRoot
from jsonasobj import as_json

from core import ConceptReference, CodeSystemReference, CodeSystemVersionReference, ValueSetDefinitionReference, \
    ValueSetDescriptionReference, ValueSetDescriptionSummary
from graphselector import GraphSelector, TransitiveClosure
from propertyselector import PropertySelector
from textselector import TextSelector


#DefinitionElement = Union[EntityList, CodeSystemReference, CodeSystemVersionReference, "ValueSetReference",
                          # GraphSelector, TextSelector, PropertySelector, ExternalPredicate, "ValueSet"]



@dataclass
class ValueSet(YAMLRoot):
    code: Optional[Union[ConceptReference, str]] = None
    codes: Optional[List[Union[ConceptReference, str]]] = None
    activecodesfrom: Optional[Union[CodeSystemReference, CodeSystemVersionReference, str]] = None
    in_definition: Optional[Union[ValueSetDescriptionReference, ValueSetDefinitionReference, str]] = None
    having_text: Optional[TextSelector] = None
    having_property: Optional[PropertySelector] = None
    in_tree: Optional[GraphSelector] = None
    plus: Optional["ValueSet"] = None
    minus: Optional["ValueSet"] = None
    intersect: Optional["ValueSet"] = None


x = ValueSet(in_definition=ValueSet(code="GO:GENE"))
# x is equivalent to
x = ValueSet(code="GO:GENE")


class ValueSetDefinitionUnitTest(unittest.TestCase):
    def test_code_lists(self):
        # A value set with a single code ("Appendicitis")
        vsd1 = ValueSet(codes=[ConceptReference("NCIt:C35145", description="Appendicitis")], minus=ValueSet(activecodesfrom="http://snomed.info/sct/"))
        print(as_json(vsd1))
        # A value set with three codes - "Appendicitis",
        vsd2 = ValueSet(codes=["http://ncicb.nci.nih.gov/xml/owl/EVS/Thesaurus.owl#C35145", "NCIt:C78178",
                               ConceptReference(about="http://ncicb.nci.nih.gov/xml/owl/EVS/Thesaurus.owl#C53500",
                                                code="C53500",
                                                href="https://ncit.nci.nih.gov/ncitbrowser/ConceptReport.jsp?dictionary=NCI_Thesaurus&code=C53500&ns=ncit",
                                                description="Non-Neoplastic Intestinal Disorder")])
        print(as_json(vsd2))

    def test_code_systems(self):
        # A value set with all codes from a particular code system
        # vscs1 = ValueSet(activecodesfrom=)

        pass

    def test_valueset_description(self):
        vsdr = ValueSetDescriptionReference(ValueSetDescriptionSummary("SNOMED CT Virus Organisms", "http://valuesets.org/sctvirus/"))
        vsd = ValueSet(in_tree=GraphSelector("sct:725894000", transitive=TransitiveClosure.TRANSITIVE_CLOSURE))
        snomedviraldiseases = ValueSet(having_property=PropertySelector("sct:246075003", matchPropery=vsdr))




if __name__ == '__main__':
    unittest.main()
