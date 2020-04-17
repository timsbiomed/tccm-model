from dataclasses import dataclass
from enum import Enum

from rdflib import SKOS

from src.tccm import EntityReference


class AssociationDirection(Enum):
    SOURCE_TO_TARGET = 1            # Follow predicate from source to target direction
    TARGET_TO_SOURCE = 2            # Follow predicate from target to source


class TransitiveClosure(Enum):
    DIRECTLY_ASSOCIATED = 1         # Follow predicate one level
    TRANSITIVE_CLOSURE = 2          # Follow transitive closure of predicate


class IncludeElements(Enum):
    CHILDREN = 0                    # Include only direct children (same as DIRECTLY_ASSOCIATED)
    CHILDREN_AND_SELF = 1           # Include both children and referencedEntity
    DESCENDENTS = 2                 # Include all elements in closure
    DESCENDENTS_AND_SELF = 3        # Include referencedEntity in closure
    LEAVES = 4                      # Only include elements in the leaves of the closure


@dataclass
class GraphSelector:
    referencedEntity: EntityReference
    predicate: EntityReference = SKOS.broader
    direction: AssociationDirection = AssociationDirection.TARGET_TO_SOURCE
    transitive: TransitiveClosure = TransitiveClosure.DIRECTLY_ASSOCIATED
    include: IncludeElements = IncludeElements.DESCENDENTS
