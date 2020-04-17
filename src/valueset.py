"""
TCCM Value Set services model
"""
from dataclasses import dataclass, field, InitVar
from enum import Enum
from typing import Optional, List, Tuple, Union, Dict

from rdflib import URIRef, Literal
from sparql_slurper import SlurpyGraph

from core import EntityList, CodeSystemReference, CodeSystemVersionReference, ValueSetDefinitionReference, \
    ValueSetReference
from graphselector import GraphSelector
from resource import VersionedResource, Resource
from src.tccm import ExternalURI, NameAndMeaningReference, LocalURI
from textselector import TextSelector


@dataclass
class PropertySelector:
    predicates: EntityList
    matchPropery: Optional[Union[Literal, List[Literal]], "ValueSetReference"] = None


ExternalPredicate = Union[ExternalURI, NameAndMeaningReference]

CompoundDefinition = List["ValueSetDefinitionEntry"]


class SetOperator(Enum):
    UNION = 1               # Add the resolution of the
    SUBTRACT = 2
    INTERSECT = 3


# A DefinitionElement is one of the following
#    * EntityList -- a list of entity URI's or EntityReferences -- these are NOT validated and added verbatim
#    * CodeSystemReference -- represents all URIRefs that appear in the subject role in the CodeSystemVersionReference
#                             that CodeSystemReference is bound to
#    * CodeSystemVersionReference -- represents all URIRefs that appear in the subject role of this ontology version
#    * ValueSetReference -- the resolution of this value set using the accompanying bindings
#    * GraphSelector --
DefinitionElement = Union[EntityList, CodeSystemReference, CodeSystemVersionReference, "ValueSetReference",
                          GraphSelector, TextSelector, PropertySelector, ExternalPredicate, CompoundDefinition]


@dataclass
class ValueSetDefinitionEntry:
    operator: SetOperator
    element: DefinitionElement


ValueSetDefinitionEntryList = List[ValueSetDefinitionEntry]


@dataclass
class ValueSetDefinition(VersionedResource):
    """
    A named value set definition.
    """
    definition: CompoundDefinition = field(default_factory=list)


CodeSystemBinding = Dict[ExternalURI, CodeSystemVersionReference]
ValueSetBinding = Dict[ExternalURI, ValueSetDefinitionReference]


@dataclass
class ValueSetResolution(Resource):
    definition: Union[ValueSetReference, ValueSetDefinitionEntryList] = None
    codeSystemBindings: CodeSystemBinding = field(default_factory=dict)
    valueSetBindings: ValueSetBinding = field(default_factory=dict)
    num_elements: InitVar[int] = None
    resolution: InitVar[EntityList] = None

# Parameters for Resolve
class EntityExpansions(Enum):
    URI = 1
    PREFNAME = 2
    ALTNAMES = 3
    DEFINITIONS = 4

language = str


def valueset_resolution_put(res: ValueSetResolution, expansions: Optional[EntityExpansions], language: Optional[str]) -> ValueSetResolution:
    """
    PUT operation on value set resolution.  Follows the standard resource rules -- if the resource URI is not supplied, it is generated, otherwise
    it follows REST rules
    :param res:
    :param expansions:
    :param language:
    :return:
    """



x = ResolvedValueSet(bindings=[(URIRef("https://ncatswiki.dbmi.pitt.edu/acts/ACT/Diagnosis/ICD9"),
                                URIRef("https://ncatswiki.dbmi.pitt.edu/acts/ACT/Diagnosis/ICD9/2018AA"))])

g = SlurpyGraph("http://graph.hotecosystem.org:7200/repositories/ACT_ONTOLOGY_2")
x.resolution = [URIRef(o) for o in g.objects(ACT.A18090652, ISO['enumeratedConceptualDomain.hasMember'])]

print(x)





RuleAdd = DefinitionElement
RuleSubtract = DefinitionElement
RuleIntersect = DefinitionElement
