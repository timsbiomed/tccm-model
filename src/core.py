"""
Core TCCM Module.

TODO: Update tccm.yaml to include these elements
"""
from dataclasses import dataclass
from typing import Union, List, Optional, NewType

from biolinkml.utils.yamlutils import YAMLRoot

from src.tccm import ExternalURI, NameAndMeaningReference, EntityReference, PersistentURI, RenderingURI

ExternalURIList = List[ExternalURI]
NameAndMeaningReferenceList = List[NameAndMeaningReference]
EntityReferenceList = List[EntityReference]

EntityList: object = Union[ExternalURIList, EntityReferenceList]


@dataclass
class VersionedReference(NameAndMeaningReference):
    version: Optional[str] = None
    versionURI: Optional[ExternalURI] = None



def ExternalURIToNameAndMeaning(uri: Union[ExternalURI, ExternalURIList]) -> Union[NameAndMeaningReference, NameAndMeaningReferenceList]:
    pass


def NameAndMeaningToExternalURI(nam: Union[NameAndMeaningReference, NameAndMeaningReferenceList]) -> Union[ExternalURI, ExternalURIList]:
    pass


def ExternalURIToEntityReference(uri: Union[ExternalURI, ExternalURIList]) -> Union[EntityReference, ExternalURIList]:
    pass


def EntityReferenceToExternalURI(erl: Union[EntityReference, ExternalURIList]) -> Union[ExternalURI, ExternalURIList]:
    pass


ConceptURI = NewType('ConceptURI', ExternalURI)
CodeSystemURI = NewType('CodeSystemURI', ExternalURI)
CodeSystemVersionURI = NewType('CodeSystemVewrsionURI', ExternalURI)
ValueSetDescriptionURI = NewType('ValueSetDescriptionURI', ExternalURI)
ValueSetDefinitionURI = NewType('ValueSetDefinitionURI', ExternalURI)
ResolvedValueSetURI = NewType('ResolvedValueSetURI', ExternalURI)


@dataclass
class EntityReference(YAMLRoot):
    about: Union[PersistentURI, str]
    code: Optional[str] = None
    href: Optional[Union[RenderingURI, str]] = None
    description: Optional[str] = None


@dataclass
class ConceptReference(EntityReference):
    about: Union[ConceptURI, str]

@dataclass
class CodeSystemSummary(NameAndMeaningReference):
    uri: Optional[CodeSystemURI] = None


@dataclass
class CodeSystemVersionSummary(NameAndMeaningReference):
    uri: Optional[Union[CodeSystemVersionURI]] = None


@dataclass
class ValueSetDescriptionSummary(NameAndMeaningReference):
    uri: Optional[Union[str, ValueSetDescriptionURI]] = None


@dataclass
class ValueSetDefinitionSummary(NameAndMeaningReference):
    uri: Optional[Union[str, ValueSetDefinitionURI]] = None


@dataclass
class ResolvedValueSetSummary(NameAndMeaningReference):
    uri: Optional[Union[str, ResolvedValueSetURI]] = None


CodeSystemReference = Union[CodeSystemURI, CodeSystemSummary]
CodeSystemVersionReference = NewType('CodeSystemVersionReference', Union[CodeSystemVersionURI, CodeSystemVersionSummary])
ValueSetDescriptionReference = NewType('ValueSetDescriptionReference', Union[ValueSetDescriptionURI, ValueSetDescriptionSummary])
ValueSetDefinitionReference = NewType('ValueSetDefinitionReference', Union[ValueSetDefinitionURI, ValueSetDefinitionSummary])
ResolvedValuesetReference = NewType('ResolvedValuesetReference', Union[ResolvedValueSetURI, ResolvedValueSetSummary])
