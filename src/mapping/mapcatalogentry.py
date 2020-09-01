# Auto generated from mapcatalogentry.yaml by pythongen.py version: 0.4.0
# Generation date: 2020-09-01 13:22
# Schema: mapcatalogentry
#
# id: https://hotecosystem.org/tccm/mapcatalogentry
# description: MapCatalogEntry is an entry in a catalog of maps that are known to a service implementation. They
#              contain basic information about the resource including who created it, what it is for, etc. We
#              anticipate that this particular model will be extended in subsequent versions to include
#              information about the rule languages and interface requirements of the various maps but, at the
#              moment this represents a core set of properties.
# license: https://creativecommons.org/publicdomain/zero/1.0/

import dataclasses
import sys
from typing import Optional, List, Union, Dict, ClassVar, Any
from dataclasses import dataclass
from biolinkml.utils.slot import Slot
from biolinkml.utils.metamodelcore import empty_list, empty_dict, bnode
from biolinkml.utils.yamlutils import YAMLRoot, extended_str, extended_float, extended_int
if sys.version_info < (3, 7, 6):
    from biolinkml.utils.dataclass_extensions_375 import dataclasses_init_fn_with_kwargs
else:
    from biolinkml.utils.dataclass_extensions_376 import dataclasses_init_fn_with_kwargs
from biolinkml.utils.formatutils import camelcase, underscore, sfx
from rdflib import Namespace, URIRef
from biolinkml.utils.curienamespace import CurieNamespace
from src.core.datatypes import DateAndTime, LocalIdentifier
from src.core.directorytypes import MapVersionDirectoryURI
from src.core.entrydescription import OpaqueData
from src.core.localidentifiers import MapName
from src.core.references import CodeSystemReference, CodeSystemReferenceName, FormatReference, FormatReferenceName, LanguageReference, LanguageReferenceName, MapReference, MapReferenceName, MapVersionReference, MapVersionReferenceName, NameAndMeaningReference, NameAndMeaningReferenceName, OntologyLanguageReference, OntologyLanguageReferenceName, OntologySyntaxReference, OntologySyntaxReferenceName, RoleReference, RoleReferenceName, ValueSetReference, ValueSetReferenceName
from src.core.resourcedescription import AbstractResourceDescription, AbstractResourceDescriptionId, SourceAndNotation
from src.core.uritypes import DirectoryURI, DocumentURI, ExternalURI, LocalURI, PersistentURI, RenderingURI
from biolinkml.utils.metamodelcore import URIorCURIE, XSDDateTime
from includes.annotations import Annotation
from includes.extensions import Extension
from includes.types import String

metamodel_version = "1.5.3"

# Overwrite dataclasses _init_fn to add **kwargs in __init__
dataclasses._init_fn = dataclasses_init_fn_with_kwargs

# Namespaces
BIOLINKML = CurieNamespace('biolinkml', 'https://w3id.org/biolink/biolinkml/')
TCCM = CurieNamespace('tccm', 'https://hotecosystem.org/tccm/')
DEFAULT_ = TCCM


# Types

# Class references
class MapcatalogentryId(AbstractResourceDescriptionId):
    pass


@dataclass
class Mapcatalogentry(AbstractResourceDescription):
    """
    An entry in a catalog of maps - organized collections of rules that describe how information encoded using one
    set of value meanings can be transformed into a second, related set of meanings. A map catalog contains
    information about who is responsible for creating and distributing the rules, the source code system or value set,
    the target code system or value set, how often the rules are updated, how they are distributed, etc.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = TCCM.Mapcatalogentry
    class_class_curie: ClassVar[str] = "tccm:Mapcatalogentry"
    class_name: ClassVar[str] = "mapcatalogentry"
    class_model_uri: ClassVar[URIRef] = TCCM.Mapcatalogentry

    id: Union[str, MapcatalogentryId] = None
    about: Union[URIorCURIE, ExternalURI] = None
    mapName: Union[str, MapName] = None
    fromValueSet: Union[dict, ValueSetReference] = None
    toValueSet: Union[dict, ValueSetReference] = None
    fromCodeSystem: Optional[Union[dict, CodeSystemReference]] = None
    toCodeSystem: Optional[Union[dict, CodeSystemReference]] = None
    versions: Optional[Union[URIorCURIE, MapVersionDirectoryURI]] = None
    currentVersion: Optional[Union[dict, MapVersionReference]] = None

    def __post_init__(self, **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError(f"id must be supplied")
        if not isinstance(self.id, MapcatalogentryId):
            self.id = MapcatalogentryId(self.id)
        if self.mapName is None:
            raise ValueError(f"mapName must be supplied")
        if not isinstance(self.mapName, MapName):
            self.mapName = MapName(self.mapName)
        if self.fromCodeSystem is not None and not isinstance(self.fromCodeSystem, CodeSystemReference):
            self.fromCodeSystem = CodeSystemReference(self.fromCodeSystem)
        if self.fromValueSet is None:
            raise ValueError(f"fromValueSet must be supplied")
        if not isinstance(self.fromValueSet, ValueSetReference):
            self.fromValueSet = ValueSetReference(self.fromValueSet)
        if self.toCodeSystem is not None and not isinstance(self.toCodeSystem, CodeSystemReference):
            self.toCodeSystem = CodeSystemReference(self.toCodeSystem)
        if self.toValueSet is None:
            raise ValueError(f"toValueSet must be supplied")
        if not isinstance(self.toValueSet, ValueSetReference):
            self.toValueSet = ValueSetReference(self.toValueSet)
        if self.versions is not None and not isinstance(self.versions, MapVersionDirectoryURI):
            self.versions = MapVersionDirectoryURI(self.versions)
        if self.currentVersion is not None and not isinstance(self.currentVersion, MapVersionReference):
            self.currentVersion = MapVersionReference(self.currentVersion)
        super().__post_init__(**kwargs)



# Slots
class slots:
    pass

slots.mapcatalogentry__mapName = Slot(uri=TCCM.mapName, name="mapcatalogentry__mapName", curie=TCCM.curie('mapName'),
                      model_uri=TCCM.mapcatalogentry__mapName, domain=None, range=Union[str, MapName])

slots.mapcatalogentry__fromCodeSystem = Slot(uri=TCCM.fromCodeSystem, name="mapcatalogentry__fromCodeSystem", curie=TCCM.curie('fromCodeSystem'),
                      model_uri=TCCM.mapcatalogentry__fromCodeSystem, domain=None, range=Optional[Union[dict, CodeSystemReference]])

slots.mapcatalogentry__fromValueSet = Slot(uri=TCCM.fromValueSet, name="mapcatalogentry__fromValueSet", curie=TCCM.curie('fromValueSet'),
                      model_uri=TCCM.mapcatalogentry__fromValueSet, domain=None, range=Union[dict, ValueSetReference])

slots.mapcatalogentry__toCodeSystem = Slot(uri=TCCM.toCodeSystem, name="mapcatalogentry__toCodeSystem", curie=TCCM.curie('toCodeSystem'),
                      model_uri=TCCM.mapcatalogentry__toCodeSystem, domain=None, range=Optional[Union[dict, CodeSystemReference]])

slots.mapcatalogentry__toValueSet = Slot(uri=TCCM.toValueSet, name="mapcatalogentry__toValueSet", curie=TCCM.curie('toValueSet'),
                      model_uri=TCCM.mapcatalogentry__toValueSet, domain=None, range=Union[dict, ValueSetReference])

slots.mapcatalogentry__versions = Slot(uri=TCCM.versions, name="mapcatalogentry__versions", curie=TCCM.curie('versions'),
                      model_uri=TCCM.mapcatalogentry__versions, domain=None, range=Optional[Union[URIorCURIE, MapVersionDirectoryURI]])

slots.mapcatalogentry__currentVersion = Slot(uri=TCCM.currentVersion, name="mapcatalogentry__currentVersion", curie=TCCM.curie('currentVersion'),
                      model_uri=TCCM.mapcatalogentry__currentVersion, domain=None, range=Optional[Union[dict, MapVersionReference]])

slots.nameAndMeaningReference__name = Slot(uri=TCCM.name, name="nameAndMeaningReference__name", curie=TCCM.curie('name'),
                      model_uri=TCCM.nameAndMeaningReference__name, domain=None, range=URIRef)

slots.nameAndMeaningReference__synopsis = Slot(uri=TCCM.synopsis, name="nameAndMeaningReference__synopsis", curie=TCCM.curie('synopsis'),
                      model_uri=TCCM.nameAndMeaningReference__synopsis, domain=None, range=Optional[str])

slots.nameAndMeaningReference__uri = Slot(uri=TCCM.uri, name="nameAndMeaningReference__uri", curie=TCCM.curie('uri'),
                      model_uri=TCCM.nameAndMeaningReference__uri, domain=None, range=Optional[Union[URIorCURIE, ExternalURI]])

slots.nameAndMeaningReference__href = Slot(uri=TCCM.href, name="nameAndMeaningReference__href", curie=TCCM.curie('href'),
                      model_uri=TCCM.nameAndMeaningReference__href, domain=None, range=Optional[Union[URIorCURIE, RenderingURI]])

slots.codeSystemVersionReference__codeSystem = Slot(uri=TCCM.codeSystem, name="codeSystemVersionReference__codeSystem", curie=TCCM.curie('codeSystem'),
                      model_uri=TCCM.codeSystemVersionReference__codeSystem, domain=None, range=Union[dict, CodeSystemReference])

slots.mapVersionReference__map = Slot(uri=TCCM.map, name="mapVersionReference__map", curie=TCCM.curie('map'),
                      model_uri=TCCM.mapVersionReference__map, domain=None, range=Optional[Union[dict, MapReference]])

slots.predicateReference__uri = Slot(uri=TCCM.uri, name="predicateReference__uri", curie=TCCM.curie('uri'),
                      model_uri=TCCM.predicateReference__uri, domain=None, range=Union[URIorCURIE, ExternalURI])

slots.predicateReference__name = Slot(uri=TCCM.name, name="predicateReference__name", curie=TCCM.curie('name'),
                      model_uri=TCCM.predicateReference__name, domain=None, range=Optional[Union[str, LocalIdentifier]])

slots.predicateReference__href = Slot(uri=TCCM.href, name="predicateReference__href", curie=TCCM.curie('href'),
                      model_uri=TCCM.predicateReference__href, domain=None, range=Optional[Union[URIorCURIE, RenderingURI]])

slots.predicateReference__designation = Slot(uri=TCCM.designation, name="predicateReference__designation", curie=TCCM.curie('designation'),
                      model_uri=TCCM.predicateReference__designation, domain=None, range=Optional[str])

slots.sourceAndRoleReference__role = Slot(uri=TCCM.role, name="sourceAndRoleReference__role", curie=TCCM.curie('role'),
                      model_uri=TCCM.sourceAndRoleReference__role, domain=None, range=Optional[Union[dict, RoleReference]])

slots.sourceAndRoleReference__bibliographicLink = Slot(uri=TCCM.bibliographicLink, name="sourceAndRoleReference__bibliographicLink", curie=TCCM.curie('bibliographicLink'),
                      model_uri=TCCM.sourceAndRoleReference__bibliographicLink, domain=None, range=Optional[Union[dict, OpaqueData]])

slots.resourceDescription__describedResourceType = Slot(uri=TCCM.describedResourceType, name="resourceDescription__describedResourceType", curie=TCCM.curie('describedResourceType'),
                      model_uri=TCCM.resourceDescription__describedResourceType, domain=None, range=Optional[str])

slots.resourceDescription__resourceSynopsis = Slot(uri=TCCM.resourceSynopsis, name="resourceDescription__resourceSynopsis", curie=TCCM.curie('resourceSynopsis'),
                      model_uri=TCCM.resourceDescription__resourceSynopsis, domain=None, range=Optional[str])

slots.resourceDescription__resourceID = Slot(uri=TCCM.id, name="resourceDescription__resourceID", curie=TCCM.curie('id'),
                      model_uri=TCCM.resourceDescription__resourceID, domain=None, range=URIRef)

slots.resourceDescription__about = Slot(uri=TCCM.about, name="resourceDescription__about", curie=TCCM.curie('about'),
                      model_uri=TCCM.resourceDescription__about, domain=None, range=Union[URIorCURIE, ExternalURI])

slots.resourceDescription__formalName = Slot(uri=TCCM.formalName, name="resourceDescription__formalName", curie=TCCM.curie('formalName'),
                      model_uri=TCCM.resourceDescription__formalName, domain=None, range=Optional[str])

slots.resourceDescription__keyword = Slot(uri=TCCM.keyword, name="resourceDescription__keyword", curie=TCCM.curie('keyword'),
                      model_uri=TCCM.resourceDescription__keyword, domain=None, range=List[str])

slots.resourceDescription__additionalDocumentation = Slot(uri=TCCM.additionalDocumentation, name="resourceDescription__additionalDocumentation", curie=TCCM.curie('additionalDocumentation'),
                      model_uri=TCCM.resourceDescription__additionalDocumentation, domain=None, range=List[URIorCURIE])

slots.resourceDescription__rights = Slot(uri=TCCM.rights, name="resourceDescription__rights", curie=TCCM.curie('rights'),
                      model_uri=TCCM.resourceDescription__rights, domain=None, range=Optional[str])

slots.resourceDescription__alternateID = Slot(uri=TCCM.alternateID, name="resourceDescription__alternateID", curie=TCCM.curie('alternateID'),
                      model_uri=TCCM.resourceDescription__alternateID, domain=None, range=Optional[str])

slots.sourceAndNotation__sourceAndNotationDescription = Slot(uri=TCCM.sourceAndNotationDescription, name="sourceAndNotation__sourceAndNotationDescription", curie=TCCM.curie('sourceAndNotationDescription'),
                      model_uri=TCCM.sourceAndNotation__sourceAndNotationDescription, domain=None, range=Optional[str])

slots.sourceAndNotation__sourceDocument = Slot(uri=TCCM.sourceDocument, name="sourceAndNotation__sourceDocument", curie=TCCM.curie('sourceDocument'),
                      model_uri=TCCM.sourceAndNotation__sourceDocument, domain=None, range=Optional[URIorCURIE])

slots.sourceAndNotation__sourceLanguage = Slot(uri=TCCM.sourceLanguage, name="sourceAndNotation__sourceLanguage", curie=TCCM.curie('sourceLanguage'),
                      model_uri=TCCM.sourceAndNotation__sourceLanguage, domain=None, range=Optional[Union[dict, OntologyLanguageReference]])

slots.sourceAndNotation__sourceDocumentSyntax = Slot(uri=TCCM.sourceDocumentSyntax, name="sourceAndNotation__sourceDocumentSyntax", curie=TCCM.curie('sourceDocumentSyntax'),
                      model_uri=TCCM.sourceAndNotation__sourceDocumentSyntax, domain=None, range=Optional[Union[dict, OntologySyntaxReference]])

slots.abstractResourceDescription__releaseDocumentation = Slot(uri=TCCM.releaseDocumentation, name="abstractResourceDescription__releaseDocumentation", curie=TCCM.curie('releaseDocumentation'),
                      model_uri=TCCM.abstractResourceDescription__releaseDocumentation, domain=None, range=Optional[str])

slots.abstractResourceDescription__releaseFormat = Slot(uri=TCCM.releaseFormat, name="abstractResourceDescription__releaseFormat", curie=TCCM.curie('releaseFormat'),
                      model_uri=TCCM.abstractResourceDescription__releaseFormat, domain=None, range=List[Union[dict, SourceAndNotation]])

slots.resourceVersionDescription__documentURI = Slot(uri=TCCM.documentURI, name="resourceVersionDescription__documentURI", curie=TCCM.curie('documentURI'),
                      model_uri=TCCM.resourceVersionDescription__documentURI, domain=None, range=Optional[Union[URIorCURIE, DocumentURI]])

slots.resourceVersionDescription__sourceAndNotation = Slot(uri=TCCM.sourceAndNotation, name="resourceVersionDescription__sourceAndNotation", curie=TCCM.curie('sourceAndNotation'),
                      model_uri=TCCM.resourceVersionDescription__sourceAndNotation, domain=None, range=Optional[Union[dict, SourceAndNotation]])

slots.resourceVersionDescription__predecessor = Slot(uri=TCCM.predecessor, name="resourceVersionDescription__predecessor", curie=TCCM.curie('predecessor'),
                      model_uri=TCCM.resourceVersionDescription__predecessor, domain=None, range=Optional[Union[dict, NameAndMeaningReference]])

slots.resourceVersionDescription__officialResourceVersionID = Slot(uri=TCCM.officialResourceVersionID, name="resourceVersionDescription__officialResourceVersionID", curie=TCCM.curie('officialResourceVersionID'),
                      model_uri=TCCM.resourceVersionDescription__officialResourceVersionID, domain=None, range=Optional[str])

slots.resourceVersionDescription__officialReleaseDate = Slot(uri=TCCM.officialReleaseDate, name="resourceVersionDescription__officialReleaseDate", curie=TCCM.curie('officialReleaseDate'),
                      model_uri=TCCM.resourceVersionDescription__officialReleaseDate, domain=None, range=Optional[Union[str, XSDDateTime]])

slots.resourceVersionDescription__officialActivationDate = Slot(uri=TCCM.officialActivationDate, name="resourceVersionDescription__officialActivationDate", curie=TCCM.curie('officialActivationDate'),
                      model_uri=TCCM.resourceVersionDescription__officialActivationDate, domain=None, range=Optional[Union[str, XSDDateTime]])

slots.opaqueData__format = Slot(uri=TCCM.format, name="opaqueData__format", curie=TCCM.curie('format'),
                      model_uri=TCCM.opaqueData__format, domain=None, range=Optional[Union[dict, FormatReference]])

slots.opaqueData__schema = Slot(uri=TCCM.schema, name="opaqueData__schema", curie=TCCM.curie('schema'),
                      model_uri=TCCM.opaqueData__schema, domain=None, range=Optional[Union[URIorCURIE, DocumentURI]])

slots.opaqueData__language = Slot(uri=TCCM.language, name="opaqueData__language", curie=TCCM.curie('language'),
                      model_uri=TCCM.opaqueData__language, domain=None, range=Optional[Union[dict, LanguageReference]])

slots.opaqueData__value = Slot(uri=TCCM.value, name="opaqueData__value", curie=TCCM.curie('value'),
                      model_uri=TCCM.opaqueData__value, domain=None, range=str)
