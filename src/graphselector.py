from dataclasses import dataclass
from enum import Enum
from typing import Optional

from rdflib import SKOS

from core import ConceptReference
from src.tccm import EntityReference


# TODO: find appropriate wording for this concept (in / out from graph theory) (down / up from hierarchy, look at ShEx nomenclature)
class AssociationDirection(str, Enum):
    INBOUND = "INBOUND"             # Follow predicate from source to target direction
    OUTBOUND = "OUTBOUND"           # Follow predicate from target to source


# TODO: Need different words (or synonyms) to cover the ancestor case
class IncludeElements(str, Enum):
    ALL = "ALL"                      # All nodes
    ALL_BUT_FOCUS = "ALL_BUT_FOCUS"  # All nodes except the focus node
    DISTAL = "DISTAL"                # Most distal nodes only
    EDGE_NODE = "EDGE_NODE"          # Synonym for DISTAL


@dataclass
class GraphSelector:
    focus: ConceptReference
    predicate: EntityReference = SKOS.broader
    direction: AssociationDirection = AssociationDirection.INBOUND
    max_hops: Optional[int] = None
    include_elements: IncludeElements = IncludeElements.ALL_BUT_FOCUS

# TODO: we have to define what this means in an OWL environment