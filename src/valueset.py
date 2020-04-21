"""
TCCM Value Set services model
"""
from dataclasses import dataclass, field, InitVar
from enum import Enum
from typing import Optional, List, Tuple, Union, Dict, NewType

from biolinkml.utils.yamlutils import YAMLRoot
from rdflib import URIRef, Literal
from sparql_slurper import SlurpyGraph

from core import EntityList, CodeSystemReference, CodeSystemVersionReference, ValueSetDefinitionReference
from graphselector import GraphSelector
from resource import VersionedResource, Resource
from src.tccm import ExternalURI, NameAndMeaningReference, LocalURI
from textselector import TextSelector


@dataclass
class PropertySelector:
    predicates: EntityList
    matchPropery: Optional[Union[Literal, List[Literal], "ValueSetReference"]] = None


ExternalPredicate = Union[ExternalURI, NameAndMeaningReference]

CompoundDefinition = List["ValueSetDefinitionEntry"]



# A DefinitionElement is one of the following
#    * EntityList -- a list of entity URI's or EntityReferences -- these are NOT validated and added verbatim
#    * CodeSystemReference -- represents all URIRefs that appear in the subject role in the CodeSystemVersionReference
#                             that CodeSystemReference is bound to
#    * CodeSystemVersionReference -- represents all URIRefs that appear in the subject role of this ontology version
#    * ValueSetReference -- the resolution of this value set using the accompanying bindings
#    * GraphSelector --

DefinitionElement = Union[EntityList, CodeSystemReference, CodeSystemVersionReference, "ValueSetReference",
                          GraphSelector, TextSelector, PropertySelector, ExternalPredicate, "ValueSet"]


@dataclass
class DefinitionElement(YAMLRoot):
    code: Optional[EntityURI] = None
    codes: Optional[EntityList] = None
    codesystem: Optional[CodeSystemReference] = None
    codesystemversion: Optional[CodeSystemVersionReference] = None
    valueset: Optional[ValueSetReference] = None

@dataclass
class ValueSet(YAMLRoot):
    include: DefinitionElement
    except_for: DefinitionElement


@dataclass
class Exclude(YAMLRoot):
    subtract: DefinitionElement


@dataclass
class Intersect(YAMLRoot):
    intersect: DefinitionElement


ValueSetDefinitionEntry = Union[Include, Exclude, Intersect]


CompoundDefinition = List[ValueSetDefinitionEntry]


@dataclass
class ValueSetDefinition(VersionedResource):
    """
    A named value set definition.
    """
    definition: CompoundDefinition = field(default_factory=list)


CodeSystemBinding = Dict[CodeSystemDescriptionURI, CodeSystemVersionReference]
ValueSetBinding = Dict[ValueSetDescriptionURI, ValueSetDefinitionReference]


class ValueSetReference(object):
    pass


@dataclass
class ValueSetResolution(Resource):
    definition: Union[ValueSetDescriptionReference, ValueSetDefinitionReference, "Valueset"] = None
    codeSystemBindings: CodeSystemBinding = field(default_factory=dict)
    valueSetBindings: ValueSetBinding = field(default_factory=dict)
    num_elements: InitVar[int] = None
    resolution: InitVar[EntityList] = None

# Parameters for Resolve
class EntityExpansions(str, Enum):
    URI = "URI"
    PREFNAME = "PREFNAME"
    ALTNAMES = "ALTNAMES"
    DEFINITIONS = "DEFINITIONS"

language = str

#
# def valueset_resolution_put(res: ValueSetResolution, expansions: Optional[EntityExpansions], language: Optional[str]) -> ValueSetResolution:
#     """
#     PUT operation on value set resolution.  Follows the standard resource rules -- if the resource URI is not supplied, it is generated, otherwise
#     it follows REST rules
#     :param res:
#     :param expansions:
#     :param language:
#     :return:
#     """
#
#
#
# x = ResolvedValueSet(bindings=[(URIRef("https://ncatswiki.dbmi.pitt.edu/acts/ACT/Diagnosis/ICD9"),
#                                 URIRef("https://ncatswiki.dbmi.pitt.edu/acts/ACT/Diagnosis/ICD9/2018AA"))])
#
# g = SlurpyGraph("http://graph.hotecosystem.org:7200/repositories/ACT_ONTOLOGY_2")
# x.resolution = [URIRef(o) for o in g.objects(ACT.A18090652, ISO['enumeratedConceptualDomain.hasMember'])]
#
# print(x)
#
#
#
#
#
# RuleAdd = DefinitionElement
# RuleSubtract = DefinitionElement
# RuleIntersect = DefinitionElement
