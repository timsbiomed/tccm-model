from dataclasses import dataclass
from enum import Enum
from typing import Union, Optional

from rdflib import SKOS

from core import EntityList
from tccm import ExternalURI, NameAndMeaningReference


# NOTE: Remember that this is for value set DEFINITION, not concept discovery.  This must be deterministic if it is
#       is used at all
class MatchAlgorithm(str, Enum):
    EXACT = "EXACT"             # Text must match exactly
    STARTS_WITH = "STARTS_WITH" # Text must start with matchValue
    CONTAINS = "CONTAINS"       # Text must contain matchValue
    RE = "RE"                   # Text must match RE in matchValue
    WORD_MATCH = "WORD_MATCH"   # Match all words (e.g. "Appendicitis Acute" --> Acute Appendicitis)
    WORD_START = "WORD_START"   # Match word starts   (e.g. "acu app" --> Acute Appendicitis)
    CUSTOM = "CUSTOM"           # use CustomAlgorithm


MatchAlgorithmReference = Union[ExternalURI, NameAndMeaningReference]


@dataclass
class TextSelector:
    predicates: Optional[EntityList] = None             # Default is SKOS.prefLabel, SKOS.altLabel
    matchValue: Optional[str] = ""
    matchAlgorithm: MatchAlgorithm = MatchAlgorithm.STARTS_WITH
    customAlgorithm: MatchAlgorithmReference = None
