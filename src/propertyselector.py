from dataclasses import dataclass
from typing import List, Optional, Union

from rdflib import Literal

from core import ConceptReference, ValueSetDescriptionReference, ValueSetDefinitionReference
from tccm import ExternalURI, NameAndMeaningReference


@dataclass
class PropertySelector:
    predicate: Optional[ConceptReference] = None
    predicates: Optional[List[ConceptReference]] = None # Does a list of predicates ever make sense
    matchPropery: Optional[Union[Literal, List[Literal], ValueSetDescriptionReference, ValueSetDefinitionReference, "ValueSet"]] = None




ExternalPredicate = Union[ExternalURI, NameAndMeaningReference]