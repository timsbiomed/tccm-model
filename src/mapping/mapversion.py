# Auto generated from mapversion.yaml by pythongen.py version: 0.4.0
# Generation date: 2020-09-01 13:23
# Schema: mapversion
#
# id: https://hotecosystem.org/tccm/mapversion
# description: `MapVersion` contains information about a specific version of a Map, including release information,
#              the particular format of the release being described, etc. It also provides a link to the actual
#              contents of the particular version if the implementation is available.
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
from src.core.datatypes import LocalIdentifier
from src.core.entityreference import EntityExpression, EntityReference, EntityReferenceCode
from src.core.entrydescription import OpaqueData
from src.core.localidentifiers import CodeSystemName, MapVersionName
from src.core.references import CodeSystemReference, CodeSystemReferenceName, CodeSystemVersionReference, CodeSystemVersionReferenceName, ContextReference, ContextReferenceName, FormatReference, FormatReferenceName, LanguageReference, LanguageReferenceName, MapCorrelationReference, MapCorrelationReferenceName, MapReference, MapReferenceName, OntologyLanguageReference, OntologyLanguageReferenceName, RoleReference, RoleReferenceName, ValueSetDefinitionReference, ValueSetDefinitionReferenceName, VersionTagReference, VersionTagReferenceName
from src.core.uritypes import DocumentURI, ExternalURI, LocalURI, PersistentURI, RenderingURI
from biolinkml.utils.metamodelcore import URIorCURIE
from includes.types import String

metamodel_version = "1.5.3"

# Overwrite dataclasses _init_fn to add **kwargs in __init__
dataclasses._init_fn = dataclasses_init_fn_with_kwargs

# Namespaces
BIOLINKML = CurieNamespace('biolinkml', 'https://w3id.org/biolink/biolinkml/')
RDF = CurieNamespace('rdf', 'http://www.w3.org/1999/02/22-rdf-syntax-ns#')
SKOS = CurieNamespace('skos', 'http://www.w3.org/2004/02/skos/core#')
TCCM = CurieNamespace('tccm', 'https://hotecosystem.org/tccm/')
DEFAULT_ = TCCM


# Types

# Class references



@dataclass
class MapVersion(YAMLRoot):
    """
    A specific version of a Map. MapVersion is bound to specific code system versions and/or value set
    versions andreferences a set of mapping entries (mapSet) that, if the resource is FINAL, are fixed with respect
    to this version.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = TCCM.MapVersion
    class_class_curie: ClassVar[str] = "tccm:MapVersion"
    class_name: ClassVar[str] = "MapVersion"
    class_model_uri: ClassVar[URIRef] = TCCM.MapVersion

    mapVersionName: Union[str, MapVersionName]
    versionOf: Union[dict, MapReference]
    fromValueSetDefinition: Union[dict, ValueSetDefinitionReference]
    toValueSetDefinition: Union[dict, ValueSetDefinitionReference]
    fromCodeSystemVersion: Optional[Union[dict, CodeSystemVersionReference]] = None
    toCodeSystemVersion: Optional[Union[dict, CodeSystemVersionReference]] = None
    useCodeSystemVersion: Dict[Union[str, CodeSystemVersionReferenceName], Union[dict, CodeSystemVersionReference]] = empty_dict()
    applicableContext: Dict[Union[str, ContextReferenceName], Union[dict, ContextReference]] = empty_dict()
    versionTag: Dict[Union[str, VersionTagReferenceName], Union[dict, VersionTagReference]] = empty_dict()

    def __post_init__(self, **kwargs: Dict[str, Any]):
        if self.mapVersionName is None:
            raise ValueError(f"mapVersionName must be supplied")
        if not isinstance(self.mapVersionName, MapVersionName):
            self.mapVersionName = MapVersionName(self.mapVersionName)
        if self.versionOf is None:
            raise ValueError(f"versionOf must be supplied")
        if not isinstance(self.versionOf, MapReference):
            self.versionOf = MapReference(self.versionOf)
        if self.fromValueSetDefinition is None:
            raise ValueError(f"fromValueSetDefinition must be supplied")
        if not isinstance(self.fromValueSetDefinition, ValueSetDefinitionReference):
            self.fromValueSetDefinition = ValueSetDefinitionReference(self.fromValueSetDefinition)
        if self.fromCodeSystemVersion is not None and not isinstance(self.fromCodeSystemVersion, CodeSystemVersionReference):
            self.fromCodeSystemVersion = CodeSystemVersionReference(self.fromCodeSystemVersion)
        if self.toValueSetDefinition is None:
            raise ValueError(f"toValueSetDefinition must be supplied")
        if not isinstance(self.toValueSetDefinition, ValueSetDefinitionReference):
            self.toValueSetDefinition = ValueSetDefinitionReference(self.toValueSetDefinition)
        if self.toCodeSystemVersion is not None and not isinstance(self.toCodeSystemVersion, CodeSystemVersionReference):
            self.toCodeSystemVersion = CodeSystemVersionReference(self.toCodeSystemVersion)
        for k, v in self.useCodeSystemVersion.items():
            if not isinstance(v, CodeSystemVersionReference):
                self.useCodeSystemVersion[k] = CodeSystemVersionReference(name=k, **({} if v is None else v))
        for k, v in self.applicableContext.items():
            if not isinstance(v, ContextReference):
                self.applicableContext[k] = ContextReference(name=k, **({} if v is None else v))
        for k, v in self.versionTag.items():
            if not isinstance(v, VersionTagReference):
                self.versionTag[k] = VersionTagReference(name=k, **({} if v is None else v))
        super().__post_init__(**kwargs)


@dataclass
class SimpleMapVersion(MapVersion):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = TCCM.SimpleMapVersion
    class_class_curie: ClassVar[str] = "tccm:SimpleMapVersion"
    class_name: ClassVar[str] = "SimpleMapVersion"
    class_model_uri: ClassVar[URIRef] = TCCM.SimpleMapVersion

    mapVersionName: Union[str, MapVersionName] = None
    versionOf: Union[dict, MapReference] = None
    fromValueSetDefinition: Union[dict, ValueSetDefinitionReference] = None
    toValueSetDefinition: Union[dict, ValueSetDefinitionReference] = None
    entries: List[Union[dict, "SimpleMapEntry"]] = empty_list()

    def __post_init__(self, **kwargs: Dict[str, Any]):
        self.entries = [SimpleMapEntry(*e) for e in self.entries.items()] if isinstance(self.entries, dict) \
                        else [v if isinstance(v, SimpleMapEntry) else SimpleMapEntry(**v)
                              for v in ([self.entries] if isinstance(self.entries, str) else self.entries)]
        super().__post_init__(**kwargs)


@dataclass
class SimpleMapEntry(YAMLRoot):
    """
    A map entry represents the set of mappings that share the same mapFrom entity identifier. There may be at most
    one MapEntry for any unique EntityDescription within the context of a given MapVersion. Note also that is
    considered unidirectional from the perspective of the TCCM model. If one wishes that, class A in code system C1
    maps to class T in code system C2, and visa versa, one needs to create two map versions - the first from a
    version of C1 to a version of C2 and the second from a version of C2 to a version of C1.

    "`SimpleMapEntry`" is used to represent simple maps that don't involve cascading rules, target expressions, etc.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = TCCM.SimpleMapEntry
    class_class_curie: ClassVar[str] = "tccm:SimpleMapEntry"
    class_name: ClassVar[str] = "SimpleMapEntry"
    class_model_uri: ClassVar[URIRef] = TCCM.SimpleMapEntry

    mapFrom: Union[dict, EntityReference]
    mapTo: Optional[Union[dict, EntityReference]] = None
    correlation: Optional[Union[dict, MapCorrelationReference]] = None

    def __post_init__(self, **kwargs: Dict[str, Any]):
        if self.mapFrom is None:
            raise ValueError(f"mapFrom must be supplied")
        if not isinstance(self.mapFrom, EntityReference):
            self.mapFrom = EntityReference(self.mapFrom)
        if self.mapTo is not None and not isinstance(self.mapTo, EntityReference):
            self.mapTo = EntityReference(self.mapTo)
        if self.correlation is not None and not isinstance(self.correlation, MapCorrelationReference):
            self.correlation = MapCorrelationReference(self.correlation)
        super().__post_init__(**kwargs)


@dataclass
class FullMapVersion(MapVersion):
    """
    A "complex map" that defines an ordered set of rules for mapping from "`mapFrom`" to one or more targets
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = TCCM.FullMapVersion
    class_class_curie: ClassVar[str] = "tccm:FullMapVersion"
    class_name: ClassVar[str] = "FullMapVersion"
    class_model_uri: ClassVar[URIRef] = TCCM.FullMapVersion

    mapVersionName: Union[str, MapVersionName] = None
    versionOf: Union[dict, MapReference] = None
    fromValueSetDefinition: Union[dict, ValueSetDefinitionReference] = None
    toValueSetDefinition: Union[dict, ValueSetDefinitionReference] = None
    entries: List[Union[dict, "MapEntry"]] = empty_list()

    def __post_init__(self, **kwargs: Dict[str, Any]):
        self.entries = [MapEntry(*e) for e in self.entries.items()] if isinstance(self.entries, dict) \
                        else [v if isinstance(v, MapEntry) else MapEntry(**v)
                              for v in ([self.entries] if isinstance(self.entries, str) else self.entries)]
        super().__post_init__(**kwargs)


@dataclass
class MapEntry(YAMLRoot):
    """
    A "complex map" that defines an ordered set of rules for mapping from "`mapFrom`" to one or more targets
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = TCCM.MapEntry
    class_class_curie: ClassVar[str] = "tccm:MapEntry"
    class_name: ClassVar[str] = "MapEntry"
    class_model_uri: ClassVar[URIRef] = TCCM.MapEntry

    mapFrom: Union[dict, EntityReference]
    allMatchesFrom: List[Union[dict, "MapSet"]] = empty_list()
    firstMatchFrom: List[Union[dict, "MapSet"]] = empty_list()

    def __post_init__(self, **kwargs: Dict[str, Any]):
        if self.mapFrom is None:
            raise ValueError(f"mapFrom must be supplied")
        if not isinstance(self.mapFrom, EntityReference):
            self.mapFrom = EntityReference(self.mapFrom)
        self.allMatchesFrom = [MapSet(*e) for e in self.allMatchesFrom.items()] if isinstance(self.allMatchesFrom, dict) \
                               else [v if isinstance(v, MapSet) else MapSet(**v)
                                     for v in ([self.allMatchesFrom] if isinstance(self.allMatchesFrom, str) else self.allMatchesFrom)]
        self.firstMatchFrom = [MapSet(*e) for e in self.firstMatchFrom.items()] if isinstance(self.firstMatchFrom, dict) \
                               else [v if isinstance(v, MapSet) else MapSet(**v)
                                     for v in ([self.firstMatchFrom] if isinstance(self.firstMatchFrom, str) else self.firstMatchFrom)]
        super().__post_init__(**kwargs)


@dataclass
class MapSet(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = TCCM.MapSet
    class_class_curie: ClassVar[str] = "tccm:MapSet"
    class_name: ClassVar[str] = "MapSet"
    class_model_uri: ClassVar[URIRef] = TCCM.MapSet

    allMatchesFrom: List[Union[dict, "MapTarget"]] = empty_list()
    firstMatchFrom: List[Union[dict, "MapTarget"]] = empty_list()

    def __post_init__(self, **kwargs: Dict[str, Any]):
        self.allMatchesFrom = [MapTarget(*e) for e in self.allMatchesFrom.items()] if isinstance(self.allMatchesFrom, dict) \
                               else [v if isinstance(v, MapTarget) else MapTarget(**v)
                                     for v in ([self.allMatchesFrom] if isinstance(self.allMatchesFrom, str) else self.allMatchesFrom)]
        self.firstMatchFrom = [MapTarget(*e) for e in self.firstMatchFrom.items()] if isinstance(self.firstMatchFrom, dict) \
                               else [v if isinstance(v, MapTarget) else MapTarget(**v)
                                     for v in ([self.firstMatchFrom] if isinstance(self.firstMatchFrom, str) else self.firstMatchFrom)]
        super().__post_init__(**kwargs)


@dataclass
class MapTarget(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = TCCM.MapTarget
    class_class_curie: ClassVar[str] = "tccm:MapTarget"
    class_name: ClassVar[str] = "MapTarget"
    class_model_uri: ClassVar[URIRef] = TCCM.MapTarget

    rule: Optional[Union[dict, "MapRule"]] = None
    mapTo: Optional[Union[dict, EntityReference]] = None
    targetDescription: Optional[Union[dict, OpaqueData]] = None
    targetExpression: Optional[Union[dict, EntityExpression]] = None
    correlation: Optional[Union[dict, MapCorrelationReference]] = None

    def __post_init__(self, **kwargs: Dict[str, Any]):
        if self.rule is not None and not isinstance(self.rule, MapRule):
            self.rule = MapRule(**self.rule)
        if self.mapTo is not None and not isinstance(self.mapTo, EntityReference):
            self.mapTo = EntityReference(self.mapTo)
        if self.targetDescription is not None and not isinstance(self.targetDescription, OpaqueData):
            self.targetDescription = OpaqueData(**self.targetDescription)
        if self.targetExpression is not None and not isinstance(self.targetExpression, EntityExpression):
            self.targetExpression = EntityExpression(**self.targetExpression)
        if self.correlation is not None and not isinstance(self.correlation, MapCorrelationReference):
            self.correlation = MapCorrelationReference(self.correlation)
        super().__post_init__(**kwargs)


@dataclass
class MapRule(OpaqueData):
    """
    A set of instructions that, when interpreted in the proper context, returns a true/false value, where true means
    that the context meets the requirements set forth by the rule and false means that it doesn’t. Neither the syntax
    nor the semantics of map rules are included as part of the TCCM specification.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = TCCM.MapRule
    class_class_curie: ClassVar[str] = "tccm:MapRule"
    class_name: ClassVar[str] = "MapRule"
    class_model_uri: ClassVar[URIRef] = TCCM.MapRule

    value: str = None


# Slots
class slots:
    pass

slots.mapVersion__mapVersionName = Slot(uri=TCCM.mapVersionName, name="mapVersion__mapVersionName", curie=TCCM.curie('mapVersionName'),
                      model_uri=TCCM.mapVersion__mapVersionName, domain=None, range=Union[str, MapVersionName])

slots.mapVersion__versionOf = Slot(uri=TCCM.versionOf, name="mapVersion__versionOf", curie=TCCM.curie('versionOf'),
                      model_uri=TCCM.mapVersion__versionOf, domain=None, range=Union[dict, MapReference])

slots.mapVersion__fromValueSetDefinition = Slot(uri=TCCM.fromValueSetDefinition, name="mapVersion__fromValueSetDefinition", curie=TCCM.curie('fromValueSetDefinition'),
                      model_uri=TCCM.mapVersion__fromValueSetDefinition, domain=None, range=Union[dict, ValueSetDefinitionReference])

slots.mapVersion__fromCodeSystemVersion = Slot(uri=TCCM.fromCodeSystemVersion, name="mapVersion__fromCodeSystemVersion", curie=TCCM.curie('fromCodeSystemVersion'),
                      model_uri=TCCM.mapVersion__fromCodeSystemVersion, domain=None, range=Optional[Union[dict, CodeSystemVersionReference]])

slots.mapVersion__toValueSetDefinition = Slot(uri=TCCM.toValueSetDefinition, name="mapVersion__toValueSetDefinition", curie=TCCM.curie('toValueSetDefinition'),
                      model_uri=TCCM.mapVersion__toValueSetDefinition, domain=None, range=Union[dict, ValueSetDefinitionReference])

slots.mapVersion__toCodeSystemVersion = Slot(uri=TCCM.toCodeSystemVersion, name="mapVersion__toCodeSystemVersion", curie=TCCM.curie('toCodeSystemVersion'),
                      model_uri=TCCM.mapVersion__toCodeSystemVersion, domain=None, range=Optional[Union[dict, CodeSystemVersionReference]])

slots.mapVersion__useCodeSystemVersion = Slot(uri=TCCM.useCodeSystemVersion, name="mapVersion__useCodeSystemVersion", curie=TCCM.curie('useCodeSystemVersion'),
                      model_uri=TCCM.mapVersion__useCodeSystemVersion, domain=None, range=Dict[Union[str, CodeSystemVersionReferenceName], Union[dict, CodeSystemVersionReference]])

slots.mapVersion__applicableContext = Slot(uri=TCCM.applicableContext, name="mapVersion__applicableContext", curie=TCCM.curie('applicableContext'),
                      model_uri=TCCM.mapVersion__applicableContext, domain=None, range=Dict[Union[str, ContextReferenceName], Union[dict, ContextReference]])

slots.mapVersion__versionTag = Slot(uri=TCCM.versionTag, name="mapVersion__versionTag", curie=TCCM.curie('versionTag'),
                      model_uri=TCCM.mapVersion__versionTag, domain=None, range=Dict[Union[str, VersionTagReferenceName], Union[dict, VersionTagReference]])

slots.simpleMapVersion__entries = Slot(uri=TCCM.entries, name="simpleMapVersion__entries", curie=TCCM.curie('entries'),
                      model_uri=TCCM.simpleMapVersion__entries, domain=None, range=List[Union[dict, SimpleMapEntry]])

slots.simpleMapEntry__mapFrom = Slot(uri=TCCM.mapFrom, name="simpleMapEntry__mapFrom", curie=TCCM.curie('mapFrom'),
                      model_uri=TCCM.simpleMapEntry__mapFrom, domain=None, range=Union[dict, EntityReference])

slots.simpleMapEntry__mapTo = Slot(uri=TCCM.mapTo, name="simpleMapEntry__mapTo", curie=TCCM.curie('mapTo'),
                      model_uri=TCCM.simpleMapEntry__mapTo, domain=None, range=Optional[Union[dict, EntityReference]])

slots.simpleMapEntry__correlation = Slot(uri=TCCM.correlation, name="simpleMapEntry__correlation", curie=TCCM.curie('correlation'),
                      model_uri=TCCM.simpleMapEntry__correlation, domain=None, range=Optional[Union[dict, MapCorrelationReference]])

slots.fullMapVersion__entries = Slot(uri=TCCM.entries, name="fullMapVersion__entries", curie=TCCM.curie('entries'),
                      model_uri=TCCM.fullMapVersion__entries, domain=None, range=List[Union[dict, MapEntry]])

slots.mapEntry__mapFrom = Slot(uri=TCCM.mapFrom, name="mapEntry__mapFrom", curie=TCCM.curie('mapFrom'),
                      model_uri=TCCM.mapEntry__mapFrom, domain=None, range=Union[dict, EntityReference])

slots.mapEntry__allMatchesFrom = Slot(uri=TCCM.allMatchesFrom, name="mapEntry__allMatchesFrom", curie=TCCM.curie('allMatchesFrom'),
                      model_uri=TCCM.mapEntry__allMatchesFrom, domain=None, range=List[Union[dict, MapSet]])

slots.mapEntry__firstMatchFrom = Slot(uri=TCCM.firstMatchFrom, name="mapEntry__firstMatchFrom", curie=TCCM.curie('firstMatchFrom'),
                      model_uri=TCCM.mapEntry__firstMatchFrom, domain=None, range=List[Union[dict, MapSet]])

slots.mapSet__allMatchesFrom = Slot(uri=TCCM.allMatchesFrom, name="mapSet__allMatchesFrom", curie=TCCM.curie('allMatchesFrom'),
                      model_uri=TCCM.mapSet__allMatchesFrom, domain=None, range=List[Union[dict, MapTarget]])

slots.mapSet__firstMatchFrom = Slot(uri=TCCM.firstMatchFrom, name="mapSet__firstMatchFrom", curie=TCCM.curie('firstMatchFrom'),
                      model_uri=TCCM.mapSet__firstMatchFrom, domain=None, range=List[Union[dict, MapTarget]])

slots.mapTarget__rule = Slot(uri=TCCM.rule, name="mapTarget__rule", curie=TCCM.curie('rule'),
                      model_uri=TCCM.mapTarget__rule, domain=None, range=Optional[Union[dict, MapRule]])

slots.mapTarget__mapTo = Slot(uri=TCCM.mapTo, name="mapTarget__mapTo", curie=TCCM.curie('mapTo'),
                      model_uri=TCCM.mapTarget__mapTo, domain=None, range=Optional[Union[dict, EntityReference]])

slots.mapTarget__targetDescription = Slot(uri=TCCM.targetDescription, name="mapTarget__targetDescription", curie=TCCM.curie('targetDescription'),
                      model_uri=TCCM.mapTarget__targetDescription, domain=None, range=Optional[Union[dict, OpaqueData]])

slots.mapTarget__targetExpression = Slot(uri=TCCM.targetExpression, name="mapTarget__targetExpression", curie=TCCM.curie('targetExpression'),
                      model_uri=TCCM.mapTarget__targetExpression, domain=None, range=Optional[Union[dict, EntityExpression]])

slots.mapTarget__correlation = Slot(uri=TCCM.correlation, name="mapTarget__correlation", curie=TCCM.curie('correlation'),
                      model_uri=TCCM.mapTarget__correlation, domain=None, range=Optional[Union[dict, MapCorrelationReference]])

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

slots.entityReferenceList__namespaceURI = Slot(uri=TCCM.namespaceURI, name="entityReferenceList__namespaceURI", curie=TCCM.curie('namespaceURI'),
                      model_uri=TCCM.entityReferenceList__namespaceURI, domain=None, range=URIRef)

slots.entityReferenceList__namespaceName = Slot(uri=TCCM.namespaceName, name="entityReferenceList__namespaceName", curie=TCCM.curie('namespaceName'),
                      model_uri=TCCM.entityReferenceList__namespaceName, domain=None, range=Optional[Union[str, CodeSystemName]])

slots.entityReferenceList__entities = Slot(uri=TCCM.entities, name="entityReferenceList__entities", curie=TCCM.curie('entities'),
                      model_uri=TCCM.entityReferenceList__entities, domain=None, range=Dict[Union[str, EntityReferenceCode], Union[dict, EntityReference]])

slots.entityReference__about = Slot(uri=TCCM.about, name="entityReference__about", curie=TCCM.curie('about'),
                      model_uri=TCCM.entityReference__about, domain=None, range=Optional[URIorCURIE])

slots.entityReference__code = Slot(uri=RDF.id, name="entityReference__code", curie=RDF.curie('id'),
                      model_uri=TCCM.entityReference__code, domain=None, range=URIRef)

slots.entityReference__designation = Slot(uri=SKOS.prefLabel, name="entityReference__designation", curie=SKOS.curie('prefLabel'),
                      model_uri=TCCM.entityReference__designation, domain=None, range=Optional[str])

slots.entityReference__description = Slot(uri=SKOS.definition, name="entityReference__description", curie=SKOS.curie('definition'),
                      model_uri=TCCM.entityReference__description, domain=None, range=Optional[str])

slots.entityReference__href = Slot(uri=TCCM.href, name="entityReference__href", curie=TCCM.curie('href'),
                      model_uri=TCCM.entityReference__href, domain=None, range=Optional[Union[URIorCURIE, RenderingURI]])

slots.entityReference__see_also = Slot(uri=TCCM.see_also, name="entityReference__see_also", curie=TCCM.curie('see_also'),
                      model_uri=TCCM.entityReference__see_also, domain=None, range=List[Union[URIorCURIE, RenderingURI]])

slots.entityExpression__ontologyLanguage = Slot(uri=TCCM.ontologyLanguage, name="entityExpression__ontologyLanguage", curie=TCCM.curie('ontologyLanguage'),
                      model_uri=TCCM.entityExpression__ontologyLanguage, domain=None, range=Union[dict, OntologyLanguageReference])

slots.entityExpression__expression = Slot(uri=TCCM.expression, name="entityExpression__expression", curie=TCCM.curie('expression'),
                      model_uri=TCCM.entityExpression__expression, domain=None, range=Union[dict, OpaqueData])

slots.opaqueData__format = Slot(uri=TCCM.format, name="opaqueData__format", curie=TCCM.curie('format'),
                      model_uri=TCCM.opaqueData__format, domain=None, range=Optional[Union[dict, FormatReference]])

slots.opaqueData__schema = Slot(uri=TCCM.schema, name="opaqueData__schema", curie=TCCM.curie('schema'),
                      model_uri=TCCM.opaqueData__schema, domain=None, range=Optional[Union[URIorCURIE, DocumentURI]])

slots.opaqueData__language = Slot(uri=TCCM.language, name="opaqueData__language", curie=TCCM.curie('language'),
                      model_uri=TCCM.opaqueData__language, domain=None, range=Optional[Union[dict, LanguageReference]])

slots.opaqueData__value = Slot(uri=TCCM.value, name="opaqueData__value", curie=TCCM.curie('value'),
                      model_uri=TCCM.opaqueData__value, domain=None, range=str)
