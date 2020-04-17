from dataclasses import dataclass
from enum import Enum
from typing import Optional

from src.tccm import ExternalURI

# TODO: Review FHIR Terminology Services and CTS2 for the appropriate metadata to place here
@dataclass
class Resource:
    uri:  ExternalURI               # The resource identifier
    name: str                       # The name of the resource
    description: Optional[str] = None   # A description


class FinalizableState(Enum):
    OPEN = 1            # Item is not static and its URI is not immutable
    FINAL = 2           # Item is locked and will not change


class EntryState(Enum):
    DEPRECATED = 1      # Entry should no longer be used -- has been superceded
    ACTIVE = 2          # Entry is active


@dataclass
class VersionedResource(Resource):
    version: str = None                             # Version identifier.  Ideally in semver.org form...
    tag: str = "CURRENT"                            # Tag associated with the resource
    versionOf: Optional[ExternalURI] = None         # Abstract resource that this is a version of
    previousVersion: Optional[ExternalURI] = None   # Previous version that this replaced
    final: FinalizableState = FinalizableState.OPEN    # Indicates that this version is locked and cannot change
    entryState: EntryState = EntryState.ACTIVE         # Indicates whether version is available for use
