from dataclasses import dataclass
from enum import Enum
from typing import Optional

from biolinkml.utils.yamlutils import YAMLRoot

from src.tccm import ExternalURI

# TODO: Review FHIR Terminology Services and CTS2 for the appropriate metadata to place here
@dataclass
class Resource(YAMLRoot):
    about:  ExternalURI             # The permanant resource identifier
    name: str                       # The name of the resource
    description: Optional[str] = None   # A description


class FinalizableState(str, Enum):
    """
    Terminology resources frequently depend on immutability
    """
    OPEN = "OPEN"           # Item is not static and its URI is not immutable
    FINAL = "FINAL"          # Item is locked and will not change


class EntryState(str, Enum):
    DEPRECATED = "DEPRECATED"      # Entry should no longer be used -- has been superceded
    ACTIVE = "ACTIVE"          # Entry is active


@dataclass
class VersionedResource(Resource):
    version: str = None                             # Version identifier.  Ideally in semver.org form...
    tag: str = "CURRENT"                            # Tag associated with the resource
    versionOf: Optional[ExternalURI] = None         # Abstract resource that this is a version of
    previousVersion: Optional[ExternalURI] = None   # Previous version that this replaced
    final: FinalizableState = FinalizableState.OPEN    # Indicates that this version is locked and cannot change
    entryState: EntryState = EntryState.ACTIVE         # Indicates whether version is available for use
