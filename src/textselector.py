from dataclasses import dataclass
from enum import Enum
from typing import Union, Optional

from rdflib import SKOS

from core import EntityList
from tccm import ExternalURI, NameAndMeaningReference


class MatchAlgorithm(Enum):
    EXACT_MATCH = 1             # Text must match exactly
    STARTS_WITH = 2             # Text must start with matchValue
    CONTAINS = 3                # Text must contain matchValue
    REGULAR_EXPRESSION = 4      # Text must match RE in matchValue
    CUSTOM = 99                 # use CustomAlgorithm


MatchAlgorithmReference = Union[ExternalURI, NameAndMeaningReference]


@dataclass
class TextSelector:
    predicates: Optional[EntityList] = None             # Default is SKOS.prefLabel, SKOS.altLabel
    matchValue: Optional[str] = ""
    matchAlgorithm: MatchAlgorithm = MatchAlgorithm.STARTS_WITH
    customAlgorithm: MatchAlgorithmReference = None
