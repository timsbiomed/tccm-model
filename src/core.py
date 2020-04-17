"""
Core TCCM Module.

TODO: Update tccm.yaml to include these elements
"""
from dataclasses import dataclass
from typing import Union, List, Optional

from src.tccm import ExternalURI, NameAndMeaningReference, EntityReference

ExternalURIList = List[ExternalURI]
NameAndMeaningReferenceList = List[NameAndMeaningReference]
EntityReferenceList = List[EntityReference]

EntityList = Union[ExternalURIList, EntityReferenceList]


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


CodeSystemReference = Union[ExternalURI, NameAndMeaningReference]
CodeSystemVersionReference = Union[ExternalURI, VersionedReference]
ValueSetDescriptionReference = Union[ExternalURI, NameAndMeaningReference]
ValueSetDefinitionReference = Union[ExternalURI, NameAndMeaningReference]
ValueSetReference = Union[ValueSetDefinitionReference, ValueSetDescriptionReference]