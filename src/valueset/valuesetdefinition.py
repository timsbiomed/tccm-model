# Auto generated from valuesetdefinition.yaml by pythongen.py version: 0.4.0
# Generation date: 2020-08-27 16:22
# Schema: valuesetdefinition
#
# id: https://hotecosystem.org/tccm/valuesetdefinition
# description: A ValueSetDefinition describes the rules that determine which entity references (value meanings)
#              belong to a value set at a given point in time. The definition of what belongs in a value set can
#              evolve over time, and it is possible for there to be multiple definitions active at any given point
#              in time - perhaps one for a system in general use, a second for a newer system, and a third for
#              testing. A ValueSetDefinition may or may not identify a specific version of a code system. The
#              decision of which version is to be used depends on the context and needs of the community.
#              ValueSetDefinition and the supporting model has been designed to allow multiple variations on the
#              “binding” of definitions to value sets, code system versions to definitions, and the combination to
#              concept domains.
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
from src.core.entityreference import EntityReference, EntityReferenceCode, EntityReferenceList, EntityReferenceListNamespaceURI
from src.core.entrydescription import OpaqueData
from src.core.filters import FilterComponent
from src.core.localidentifiers import CodeSystemName
from src.core.references import CodeSystemReference, CodeSystemReferenceName, CodeSystemVersionReference, CodeSystemVersionReferenceName, FormatReference, FormatReferenceName, LanguageReference, LanguageReferenceName, MapReference, MapReferenceName, MatchAlgorithmReference, MatchAlgorithmReferenceName, NameAndMeaningReference, NameAndMeaningReferenceName, OntologyLanguageReference, OntologyLanguageReferenceName, OntologySyntaxReference, OntologySyntaxReferenceName, PredicateReference, PredicateReferenceName, RoleReference, RoleReferenceName, ValueSetDefinitionReference, ValueSetDefinitionReferenceName, ValueSetReference, ValueSetReferenceName, VersionTagReference, VersionTagReferenceName
from src.core.resourcedescription import ResourceVersionDescription, ResourceVersionDescriptionId, SourceAndNotation
from src.core.uritypes import DocumentURI, ExternalURI, LocalURI, PersistentURI, RenderingURI
from biolinkml.utils.metamodelcore import Bool, URIorCURIE, XSDDateTime
from includes.annotations import Annotation
from includes.extensions import Extension
from includes.types import Boolean, String

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
class SpecificEntityListNamespaceURI(EntityReferenceListNamespaceURI):
    pass


class ValueSetDefinitionId(ResourceVersionDescriptionId):
    pass


@dataclass
class ValueSetDefinitionEntry(YAMLRoot):
    """
    An element of a value set definition that, when resolved yields a set of entity references that are to be included
    in, excluded from or intersected with the set of elements that represent the full resolution of the definition.

    Note that only ACTIVE entity references are included. INACTIVE entity references may never be considered for
    inclusion or exclusion in the resolution of a value set definition.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = TCCM.ValueSetDefinitionEntry
    class_class_curie: ClassVar[str] = "tccm:ValueSetDefinitionEntry"
    class_name: ClassVar[str] = "ValueSetDefinitionEntry"
    class_model_uri: ClassVar[URIRef] = TCCM.ValueSetDefinitionEntry

    include: Optional[Union[dict, "FormalDefinition"]] = None
    exclude: Optional[Union[dict, "FormalDefinition"]] = None
    intersect: Optional[Union[dict, "FormalDefinition"]] = None

    def __post_init__(self, **kwargs: Dict[str, Any]):
        if self.include is not None and not isinstance(self.include, FormalDefinition):
            self.include = FormalDefinition(**self.include)
        if self.exclude is not None and not isinstance(self.exclude, FormalDefinition):
            self.exclude = FormalDefinition(**self.exclude)
        if self.intersect is not None and not isinstance(self.intersect, FormalDefinition):
            self.intersect = FormalDefinition(**self.intersect)
        super().__post_init__(**kwargs)


@dataclass
class FormalDefinition(YAMLRoot):
    """
    A value set definition choice
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = TCCM.FormalDefinition
    class_class_curie: ClassVar[str] = "tccm:FormalDefinition"
    class_name: ClassVar[str] = "FormalDefinition"
    class_model_uri: ClassVar[URIRef] = TCCM.FormalDefinition

    entityquery: Optional[Union[dict, "AssociatedEntitiesReference"]] = None
    valuequery: Optional[Union[dict, "PropertyQueryReference"]] = None
    entitylist: Optional[Union[dict, "SpecificEntityList"]] = None
    valueset: Optional[Union[dict, "CompleteValueSetReference"]] = None
    definition: Optional[Union[dict, ValueSetDefinitionEntry]] = None
    codesystem: Optional[Union[dict, "CompleteCodeSystemReference"]] = None
    externaldefinition: Optional[Union[dict, "ExternalValueSetDefinition"]] = None

    def __post_init__(self, **kwargs: Dict[str, Any]):
        if self.entityquery is not None and not isinstance(self.entityquery, AssociatedEntitiesReference):
            self.entityquery = AssociatedEntitiesReference(**self.entityquery)
        if self.valuequery is not None and not isinstance(self.valuequery, PropertyQueryReference):
            self.valuequery = PropertyQueryReference(**self.valuequery)
        if self.entitylist is not None and not isinstance(self.entitylist, SpecificEntityList):
            self.entitylist = SpecificEntityList(self.entitylist)
        if self.valueset is not None and not isinstance(self.valueset, CompleteValueSetReference):
            self.valueset = CompleteValueSetReference(**self.valueset)
        if self.definition is not None and not isinstance(self.definition, ValueSetDefinitionEntry):
            self.definition = ValueSetDefinitionEntry(**self.definition)
        if self.codesystem is not None and not isinstance(self.codesystem, CompleteCodeSystemReference):
            self.codesystem = CompleteCodeSystemReference(**self.codesystem)
        if self.externaldefinition is not None and not isinstance(self.externaldefinition, ExternalValueSetDefinition):
            self.externaldefinition = ExternalValueSetDefinition(**self.externaldefinition)
        super().__post_init__(**kwargs)


@dataclass
class AssociatedEntitiesReference(YAMLRoot):
    """
    The description of a set of entities that are associated with a referenced entity. This description names a
    reference entity and an association predicate, which identifies a set of entities that are related to the
    reference entity according to a given code system. The description can reference the direct targets of the
    association (children), the direct sources of the association (parents), the transitive closure of the
    association targets (descendants), the transitive closure of the association sources (ancestors) and can state
    whether all intermediate nodes are included in the closure or just the leaf nodes.

    Note that the terms “parent” and “children” are asserted in reference to the predicate itself. As an example, in
    the association “arm subClassOf bodyPart,” the “parent” is arm and the “child” is bodyPart.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = TCCM.AssociatedEntitiesReference
    class_class_curie: ClassVar[str] = "tccm:AssociatedEntitiesReference"
    class_name: ClassVar[str] = "AssociatedEntitiesReference"
    class_model_uri: ClassVar[URIRef] = TCCM.AssociatedEntitiesReference

    referencedEntity: Union[dict, EntityReference]
    codeSystem: Union[dict, CodeSystemReference]
    predicate: Union[dict, PredicateReference]
    codeSystemVersion: Optional[Union[dict, CodeSystemVersionReference]] = None
    objectToSubject: Optional[Bool] = None
    transitiveClosure: Optional[Bool] = None
    leafOnly: Optional[Bool] = None

    def __post_init__(self, **kwargs: Dict[str, Any]):
        if self.referencedEntity is None:
            raise ValueError(f"referencedEntity must be supplied")
        if not isinstance(self.referencedEntity, EntityReference):
            self.referencedEntity = EntityReference(self.referencedEntity)
        if self.codeSystem is None:
            raise ValueError(f"codeSystem must be supplied")
        if not isinstance(self.codeSystem, CodeSystemReference):
            self.codeSystem = CodeSystemReference(self.codeSystem)
        if self.codeSystemVersion is not None and not isinstance(self.codeSystemVersion, CodeSystemVersionReference):
            self.codeSystemVersion = CodeSystemVersionReference(self.codeSystemVersion)
        if self.predicate is None:
            raise ValueError(f"predicate must be supplied")
        if not isinstance(self.predicate, PredicateReference):
            self.predicate = PredicateReference(self.predicate)
        super().__post_init__(**kwargs)


@dataclass
class PropertyQueryReference(YAMLRoot):
    """
    A description of a set of entity references that are determined by applying a filter to the attribute(s) or
    property(s) that appear in an EntityDescription in a specified code system.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = TCCM.PropertyQueryReference
    class_class_curie: ClassVar[str] = "tccm:PropertyQueryReference"
    class_name: ClassVar[str] = "PropertyQueryReference"
    class_model_uri: ClassVar[URIRef] = TCCM.PropertyQueryReference

    codeSystem: Union[dict, CodeSystemReference]
    filter: Union[dict, FilterComponent]
    codeSystemVersion: Optional[Union[dict, CodeSystemVersionReference]] = None

    def __post_init__(self, **kwargs: Dict[str, Any]):
        if self.codeSystem is None:
            raise ValueError(f"codeSystem must be supplied")
        if not isinstance(self.codeSystem, CodeSystemReference):
            self.codeSystem = CodeSystemReference(self.codeSystem)
        if self.codeSystemVersion is not None and not isinstance(self.codeSystemVersion, CodeSystemVersionReference):
            self.codeSystemVersion = CodeSystemVersionReference(self.codeSystemVersion)
        if self.filter is None:
            raise ValueError(f"filter must be supplied")
        if not isinstance(self.filter, FilterComponent):
            self.filter = FilterComponent(**self.filter)
        super().__post_init__(**kwargs)


@dataclass
class CompleteCodeSystemReference(FormalDefinition):
    """
    An entry that, when resolved, returns all of the active entity references in a given code system. This includes
    all entity references that appear as the source of one or more statements in the code system, whether the
    assertions are made directly by a version of the code system or indirectly by a version of a different code
    system that is imported. Note that targets are not included to prevent codes from rdf, rdfs, owl, etc. being
    included in this resolution set.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = TCCM.CompleteCodeSystemReference
    class_class_curie: ClassVar[str] = "tccm:CompleteCodeSystemReference"
    class_name: ClassVar[str] = "CompleteCodeSystemReference"
    class_model_uri: ClassVar[URIRef] = TCCM.CompleteCodeSystemReference

    codeSystem: Union[dict, CodeSystemReference] = None
    codeSystemVersion: Optional[Union[dict, CodeSystemVersionReference]] = None

    def __post_init__(self, **kwargs: Dict[str, Any]):
        if self.codeSystem is None:
            raise ValueError(f"codeSystem must be supplied")
        if not isinstance(self.codeSystem, CodeSystemReference):
            self.codeSystem = CodeSystemReference(self.codeSystem)
        if self.codeSystemVersion is not None and not isinstance(self.codeSystemVersion, CodeSystemVersionReference):
            self.codeSystemVersion = CodeSystemVersionReference(self.codeSystemVersion)
        super().__post_init__(**kwargs)


@dataclass
class CompleteValueSetReference(YAMLRoot):
    """
    A reference to a value set that, when resolved, results in a set of entity references that are included in this
    entry. An entry of this type can just name a value set, meaning that the specific definition is determined in the
    resolve value set call, can name both a value set and value set definition, meaning that the specific definition
    is always used in the resolution. It can also specify one or more code system versions to be used in the
    resolution of the named value set.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = TCCM.CompleteValueSetReference
    class_class_curie: ClassVar[str] = "tccm:CompleteValueSetReference"
    class_name: ClassVar[str] = "CompleteValueSetReference"
    class_model_uri: ClassVar[URIRef] = TCCM.CompleteValueSetReference

    valueSet: Union[dict, ValueSetReference]
    valueSetDefinition: Optional[Union[dict, ValueSetDefinitionReference]] = None
    referenceCodeSystemVersion: Optional[Union[dict, CodeSystemVersionReference]] = None

    def __post_init__(self, **kwargs: Dict[str, Any]):
        if self.valueSet is None:
            raise ValueError(f"valueSet must be supplied")
        if not isinstance(self.valueSet, ValueSetReference):
            self.valueSet = ValueSetReference(self.valueSet)
        if self.valueSetDefinition is not None and not isinstance(self.valueSetDefinition, ValueSetDefinitionReference):
            self.valueSetDefinition = ValueSetDefinitionReference(self.valueSetDefinition)
        if self.referenceCodeSystemVersion is not None and not isinstance(self.referenceCodeSystemVersion, CodeSystemVersionReference):
            self.referenceCodeSystemVersion = CodeSystemVersionReference(self.referenceCodeSystemVersion)
        super().__post_init__(**kwargs)


@dataclass
class SpecificEntityList(EntityReferenceList):
    """
    A list of specific entity references that are to be included in the definition. When specified in this form,
    the service must include all entities in this list whether they are known to the service or not, and whether
    they are currently ACTIVE or not.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = TCCM.SpecificEntityList
    class_class_curie: ClassVar[str] = "tccm:SpecificEntityList"
    class_name: ClassVar[str] = "SpecificEntityList"
    class_model_uri: ClassVar[URIRef] = TCCM.SpecificEntityList

    namespaceURI: Union[URIorCURIE, SpecificEntityListNamespaceURI] = None

    def __post_init__(self, **kwargs: Dict[str, Any]):
        if self.namespaceURI is None:
            raise ValueError(f"namespaceURI must be supplied")
        if not isinstance(self.namespaceURI, SpecificEntityListNamespaceURI):
            self.namespaceURI = SpecificEntityListNamespaceURI(self.namespaceURI)
        super().__post_init__(**kwargs)


@dataclass
class ValueSetDefinition(ResourceVersionDescription):
    """
    A ValueSetDefinition describes the rules that determine which entity references (value meanings) belong to a
    value set at a given point in time. The definition of what belongs in a value set can evolve over time, and it
    is possible for there to be multiple definitions active at any given point in time - perhaps one for a system
    in general use, a second for a newer system, and a third for testing. A ValueSetDefinition may or may not
    identify a specific version of a code system. The decision of which version is to be used depends on the context
    and needs of the community. ValueSetDefinition and the supporting model has been designed to allow multiple
    variations on the “binding” of definitions to value sets, code system versions to definitions, and the
    combination to concept domains.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = TCCM.ValueSetDefinition
    class_class_curie: ClassVar[str] = "tccm:ValueSetDefinition"
    class_name: ClassVar[str] = "ValueSetDefinition"
    class_model_uri: ClassVar[URIRef] = TCCM.ValueSetDefinition

    id: Union[str, ValueSetDefinitionId] = None
    about: Union[URIorCURIE, ExternalURI] = None
    entry: List[Union[dict, "ValueSetDefinitionEntry"]] = empty_list()
    definitionOf: Optional[Union[dict, ValueSetReference]] = None
    versionTag: Dict[Union[str, VersionTagReferenceName], Union[dict, VersionTagReference]] = empty_dict()

    def __post_init__(self, **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError(f"id must be supplied")
        if not isinstance(self.id, ValueSetDefinitionId):
            self.id = ValueSetDefinitionId(self.id)
        if self.definitionOf is not None and not isinstance(self.definitionOf, ValueSetReference):
            self.definitionOf = ValueSetReference(self.definitionOf)
        for k, v in self.versionTag.items():
            if not isinstance(v, VersionTagReference):
                self.versionTag[k] = VersionTagReference(name=k, **({} if v is None else v))
        if not isinstance(self.entry, list) or len(self.entry) == 0:
            raise ValueError(f"entry must be a non-empty list")
        self.entry = [ValueSetDefinitionEntry(*e) for e in self.entry.items()] if isinstance(self.entry, dict) \
                      else [v if isinstance(v, ValueSetDefinitionEntry) else ValueSetDefinitionEntry(**v)
                            for v in ([self.entry] if isinstance(self.entry, str) else self.entry)]
        super().__post_init__(**kwargs)


@dataclass
class ExternalValueSetDefinition(OpaqueData):
    """
    A definition of a value set whose format and semantics is specified outside of the core
    TCCM specification. If a given CTTCCMS2 service recognizes the syntax and semantics of this definition, it may
    call the appropriate process to resolve it. If the definition is not recognized, a TCCM service implementation
    must not process the containing value set definition and, instead, return an error.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = TCCM.ExternalValueSetDefinition
    class_class_curie: ClassVar[str] = "tccm:ExternalValueSetDefinition"
    class_name: ClassVar[str] = "ExternalValueSetDefinition"
    class_model_uri: ClassVar[URIRef] = TCCM.ExternalValueSetDefinition

    value: str = None


# Slots
class slots:
    pass

slots.definitionOf = Slot(uri=TCCM.definitionOf, name="definitionOf", curie=TCCM.curie('definitionOf'),
                      model_uri=TCCM.definitionOf, domain=None, range=Optional[Union[dict, ValueSetReference]])

slots.versionTag = Slot(uri=TCCM.versionTag, name="versionTag", curie=TCCM.curie('versionTag'),
                      model_uri=TCCM.versionTag, domain=None, range=Dict[Union[str, VersionTagReferenceName], Union[dict, VersionTagReference]])

slots.entry = Slot(uri=TCCM.entry, name="entry", curie=TCCM.curie('entry'),
                      model_uri=TCCM.entry, domain=None, range=List[Union[dict, ValueSetDefinitionEntry]])

slots.include = Slot(uri=TCCM.include, name="include", curie=TCCM.curie('include'),
                      model_uri=TCCM.include, domain=None, range=Optional[Union[dict, FormalDefinition]])

slots.exclude = Slot(uri=TCCM.exclude, name="exclude", curie=TCCM.curie('exclude'),
                      model_uri=TCCM.exclude, domain=None, range=Optional[Union[dict, FormalDefinition]])

slots.intersect = Slot(uri=TCCM.intersect, name="intersect", curie=TCCM.curie('intersect'),
                      model_uri=TCCM.intersect, domain=None, range=Optional[Union[dict, FormalDefinition]])

slots.associated_entities = Slot(uri=TCCM.entityquery, name="associated_entities", curie=TCCM.curie('entityquery'),
                      model_uri=TCCM.associated_entities, domain=None, range=Optional[Union[dict, AssociatedEntitiesReference]])

slots.property_query = Slot(uri=TCCM.valuequery, name="property_query", curie=TCCM.curie('valuequery'),
                      model_uri=TCCM.property_query, domain=None, range=Optional[Union[dict, PropertyQueryReference]])

slots.entity_list = Slot(uri=TCCM.entitylist, name="entity_list", curie=TCCM.curie('entitylist'),
                      model_uri=TCCM.entity_list, domain=None, range=Optional[Union[dict, SpecificEntityList]])

slots.complete_value_set = Slot(uri=TCCM.valueset, name="complete_value_set", curie=TCCM.curie('valueset'),
                      model_uri=TCCM.complete_value_set, domain=None, range=Optional[Union[dict, CompleteValueSetReference]])

slots.complete_code_system = Slot(uri=TCCM.codesystem, name="complete_code_system", curie=TCCM.curie('codesystem'),
                      model_uri=TCCM.complete_code_system, domain=None, range=Optional[Union[dict, CompleteCodeSystemReference]])

slots.external_value_set_definition = Slot(uri=TCCM.externaldefinition, name="external_value_set_definition", curie=TCCM.curie('externaldefinition'),
                      model_uri=TCCM.external_value_set_definition, domain=None, range=Optional[Union[dict, ExternalValueSetDefinition]])

slots.value_set_definition = Slot(uri=TCCM.definition, name="value_set_definition", curie=TCCM.curie('definition'),
                      model_uri=TCCM.value_set_definition, domain=None, range=Optional[Union[dict, ValueSetDefinitionEntry]])

slots.about = Slot(uri=TCCM.about, name="about", curie=TCCM.curie('about'),
                      model_uri=TCCM.about, domain=None, range=Union[URIorCURIE, ExternalURI])

slots.formalName = Slot(uri=TCCM.formalName, name="formalName", curie=TCCM.curie('formalName'),
                      model_uri=TCCM.formalName, domain=None, range=Optional[str])

slots.keyword = Slot(uri=TCCM.keyword, name="keyword", curie=TCCM.curie('keyword'),
                      model_uri=TCCM.keyword, domain=None, range=List[str])

slots.additionalDocumentation = Slot(uri=TCCM.additionalDocumentation, name="additionalDocumentation", curie=TCCM.curie('additionalDocumentation'),
                      model_uri=TCCM.additionalDocumentation, domain=None, range=List[URIorCURIE])

slots.rights = Slot(uri=TCCM.rights, name="rights", curie=TCCM.curie('rights'),
                      model_uri=TCCM.rights, domain=None, range=Optional[str])

slots.alternateID = Slot(uri=TCCM.alternateID, name="alternateID", curie=TCCM.curie('alternateID'),
                      model_uri=TCCM.alternateID, domain=None, range=Optional[str])

slots.documentURI = Slot(uri=TCCM.documentURI, name="documentURI", curie=TCCM.curie('documentURI'),
                      model_uri=TCCM.documentURI, domain=None, range=Optional[Union[URIorCURIE, DocumentURI]])

slots.sourceAndNotation = Slot(uri=TCCM.sourceAndNotation, name="sourceAndNotation", curie=TCCM.curie('sourceAndNotation'),
                      model_uri=TCCM.sourceAndNotation, domain=None, range=Optional[Union[dict, SourceAndNotation]])

slots.predecessor = Slot(uri=TCCM.predecessor, name="predecessor", curie=TCCM.curie('predecessor'),
                      model_uri=TCCM.predecessor, domain=None, range=Optional[Union[dict, NameAndMeaningReference]])

slots.officialResourceVersionID = Slot(uri=TCCM.officialResourceVersionID, name="officialResourceVersionID", curie=TCCM.curie('officialResourceVersionID'),
                      model_uri=TCCM.officialResourceVersionID, domain=None, range=Optional[str])

slots.officialReleaseDate = Slot(uri=TCCM.officialReleaseDate, name="officialReleaseDate", curie=TCCM.curie('officialReleaseDate'),
                      model_uri=TCCM.officialReleaseDate, domain=None, range=Optional[Union[str, XSDDateTime]])

slots.officialActivationDate = Slot(uri=TCCM.officialActivationDate, name="officialActivationDate", curie=TCCM.curie('officialActivationDate'),
                      model_uri=TCCM.officialActivationDate, domain=None, range=Optional[Union[str, XSDDateTime]])

slots.referencedEntity = Slot(uri=TCCM.referencedEntity, name="referencedEntity", curie=TCCM.curie('referencedEntity'),
                      model_uri=TCCM.referencedEntity, domain=None, range=Union[dict, EntityReference])

slots.codeSystem = Slot(uri=TCCM.codeSystem, name="codeSystem", curie=TCCM.curie('codeSystem'),
                      model_uri=TCCM.codeSystem, domain=None, range=Union[dict, CodeSystemReference])

slots.codeSystemVersion = Slot(uri=TCCM.codeSystemVersion, name="codeSystemVersion", curie=TCCM.curie('codeSystemVersion'),
                      model_uri=TCCM.codeSystemVersion, domain=None, range=Optional[Union[dict, CodeSystemVersionReference]])

slots.predicate = Slot(uri=TCCM.predicate, name="predicate", curie=TCCM.curie('predicate'),
                      model_uri=TCCM.predicate, domain=None, range=Union[dict, PredicateReference])

slots.objectToSubject = Slot(uri=TCCM.objectToSubject, name="objectToSubject", curie=TCCM.curie('objectToSubject'),
                      model_uri=TCCM.objectToSubject, domain=None, range=Optional[Bool])

slots.transitiveClosure = Slot(uri=TCCM.transitiveClosure, name="transitiveClosure", curie=TCCM.curie('transitiveClosure'),
                      model_uri=TCCM.transitiveClosure, domain=None, range=Optional[Bool])

slots.leafOnly = Slot(uri=TCCM.leafOnly, name="leafOnly", curie=TCCM.curie('leafOnly'),
                      model_uri=TCCM.leafOnly, domain=None, range=Optional[Bool])

slots.namespaceURI = Slot(uri=TCCM.namespaceURI, name="namespaceURI", curie=TCCM.curie('namespaceURI'),
                      model_uri=TCCM.namespaceURI, domain=None, range=URIRef)

slots.namespaceName = Slot(uri=TCCM.namespaceName, name="namespaceName", curie=TCCM.curie('namespaceName'),
                      model_uri=TCCM.namespaceName, domain=None, range=Optional[Union[str, CodeSystemName]])

slots.entities = Slot(uri=TCCM.entities, name="entities", curie=TCCM.curie('entities'),
                      model_uri=TCCM.entities, domain=None, range=Dict[Union[str, EntityReferenceCode], Union[dict, EntityReference]])

slots.filter = Slot(uri=TCCM.filter, name="filter", curie=TCCM.curie('filter'),
                      model_uri=TCCM.filter, domain=None, range=Union[dict, FilterComponent])

slots.valueSet = Slot(uri=TCCM.valueSet, name="valueSet", curie=TCCM.curie('valueSet'),
                      model_uri=TCCM.valueSet, domain=None, range=Union[dict, ValueSetReference])

slots.valueSetDefinition = Slot(uri=TCCM.valueSetDefinition, name="valueSetDefinition", curie=TCCM.curie('valueSetDefinition'),
                      model_uri=TCCM.valueSetDefinition, domain=None, range=Optional[Union[dict, ValueSetDefinitionReference]])

slots.referenceCodeSystemVersion = Slot(uri=TCCM.referenceCodeSystemVersion, name="referenceCodeSystemVersion", curie=TCCM.curie('referenceCodeSystemVersion'),
                      model_uri=TCCM.referenceCodeSystemVersion, domain=None, range=Optional[Union[dict, CodeSystemVersionReference]])

slots.format = Slot(uri=TCCM.format, name="format", curie=TCCM.curie('format'),
                      model_uri=TCCM.format, domain=None, range=Optional[Union[dict, FormatReference]])

slots.schema = Slot(uri=TCCM.schema, name="schema", curie=TCCM.curie('schema'),
                      model_uri=TCCM.schema, domain=None, range=Optional[Union[URIorCURIE, DocumentURI]])

slots.language = Slot(uri=TCCM.language, name="language", curie=TCCM.curie('language'),
                      model_uri=TCCM.language, domain=None, range=Optional[Union[dict, LanguageReference]])

slots.value = Slot(uri=TCCM.value, name="value", curie=TCCM.curie('value'),
                      model_uri=TCCM.value, domain=None, range=str)

slots.code = Slot(uri=RDF.id, name="code", curie=RDF.curie('id'),
                      model_uri=TCCM.code, domain=None, range=URIRef)

slots.designation = Slot(uri=SKOS.prefLabel, name="designation", curie=SKOS.curie('prefLabel'),
                      model_uri=TCCM.designation, domain=None, range=Optional[str])

slots.description = Slot(uri=SKOS.definition, name="description", curie=SKOS.curie('definition'),
                      model_uri=TCCM.description, domain=None, range=Optional[str])

slots.href = Slot(uri=TCCM.href, name="href", curie=TCCM.curie('href'),
                      model_uri=TCCM.href, domain=None, range=Optional[Union[URIorCURIE, RenderingURI]])

slots.see_also = Slot(uri=TCCM.see_also, name="see_also", curie=TCCM.curie('see_also'),
                      model_uri=TCCM.see_also, domain=None, range=List[Union[URIorCURIE, RenderingURI]])

slots.name = Slot(uri=TCCM.name, name="name", curie=TCCM.curie('name'),
                      model_uri=TCCM.name, domain=None, range=URIRef)

slots.synopsis = Slot(uri=TCCM.synopsis, name="synopsis", curie=TCCM.curie('synopsis'),
                      model_uri=TCCM.synopsis, domain=None, range=Optional[str])

slots.uri = Slot(uri=TCCM.uri, name="uri", curie=TCCM.curie('uri'),
                      model_uri=TCCM.uri, domain=None, range=Optional[Union[URIorCURIE, ExternalURI]])

slots.map = Slot(uri=TCCM.map, name="map", curie=TCCM.curie('map'),
                      model_uri=TCCM.map, domain=None, range=Optional[Union[dict, MapReference]])

slots.role = Slot(uri=TCCM.role, name="role", curie=TCCM.curie('role'),
                      model_uri=TCCM.role, domain=None, range=Optional[Union[dict, RoleReference]])

slots.component = Slot(uri=TCCM.component, name="component", curie=TCCM.curie('component'),
                      model_uri=TCCM.component, domain=None, range=List[Union[dict, FilterComponent]])

slots.filterComponent = Slot(uri=TCCM.filterComponent, name="filterComponent", curie=TCCM.curie('filterComponent'),
                      model_uri=TCCM.filterComponent, domain=None, range=Dict[Union[str, PredicateReferenceName], Union[dict, PredicateReference]])

slots.matchAlgorithm = Slot(uri=TCCM.matchAlgorithm, name="matchAlgorithm", curie=TCCM.curie('matchAlgorithm'),
                      model_uri=TCCM.matchAlgorithm, domain=None, range=Union[dict, MatchAlgorithmReference])

slots.matchValue = Slot(uri=TCCM.matchValue, name="matchValue", curie=TCCM.curie('matchValue'),
                      model_uri=TCCM.matchValue, domain=None, range=Optional[str])

slots.sourceAndNotationDescription = Slot(uri=TCCM.sourceAndNotationDescription, name="sourceAndNotationDescription", curie=TCCM.curie('sourceAndNotationDescription'),
                      model_uri=TCCM.sourceAndNotationDescription, domain=None, range=Optional[str])

slots.sourceDocument = Slot(uri=TCCM.sourceDocument, name="sourceDocument", curie=TCCM.curie('sourceDocument'),
                      model_uri=TCCM.sourceDocument, domain=None, range=Optional[URIorCURIE])

slots.sourceLanguage = Slot(uri=TCCM.sourceLanguage, name="sourceLanguage", curie=TCCM.curie('sourceLanguage'),
                      model_uri=TCCM.sourceLanguage, domain=None, range=Optional[Union[dict, OntologyLanguageReference]])

slots.sourceDocumentSyntax = Slot(uri=TCCM.sourceDocumentSyntax, name="sourceDocumentSyntax", curie=TCCM.curie('sourceDocumentSyntax'),
                      model_uri=TCCM.sourceDocumentSyntax, domain=None, range=Optional[Union[dict, OntologySyntaxReference]])

slots.releaseDocumentation = Slot(uri=TCCM.releaseDocumentation, name="releaseDocumentation", curie=TCCM.curie('releaseDocumentation'),
                      model_uri=TCCM.releaseDocumentation, domain=None, range=Optional[str])

slots.releaseFormat = Slot(uri=TCCM.releaseFormat, name="releaseFormat", curie=TCCM.curie('releaseFormat'),
                      model_uri=TCCM.releaseFormat, domain=None, range=List[Union[dict, SourceAndNotation]])

slots.AssociatedEntitiesReference_referencedEntity = Slot(uri=TCCM.referencedEntity, name="AssociatedEntitiesReference_referencedEntity", curie=TCCM.curie('referencedEntity'),
                      model_uri=TCCM.AssociatedEntitiesReference_referencedEntity, domain=AssociatedEntitiesReference, range=Union[dict, EntityReference])

slots.AssociatedEntitiesReference_codeSystem = Slot(uri=TCCM.codeSystem, name="AssociatedEntitiesReference_codeSystem", curie=TCCM.curie('codeSystem'),
                      model_uri=TCCM.AssociatedEntitiesReference_codeSystem, domain=AssociatedEntitiesReference, range=Union[dict, CodeSystemReference])

slots.AssociatedEntitiesReference_codeSystemVersion = Slot(uri=TCCM.codeSystemVersion, name="AssociatedEntitiesReference_codeSystemVersion", curie=TCCM.curie('codeSystemVersion'),
                      model_uri=TCCM.AssociatedEntitiesReference_codeSystemVersion, domain=AssociatedEntitiesReference, range=Optional[Union[dict, CodeSystemVersionReference]])

slots.AssociatedEntitiesReference_predicate = Slot(uri=TCCM.predicate, name="AssociatedEntitiesReference_predicate", curie=TCCM.curie('predicate'),
                      model_uri=TCCM.AssociatedEntitiesReference_predicate, domain=AssociatedEntitiesReference, range=Union[dict, PredicateReference])

slots.AssociatedEntitiesReference_objectToSubject = Slot(uri=TCCM.objectToSubject, name="AssociatedEntitiesReference_objectToSubject", curie=TCCM.curie('objectToSubject'),
                      model_uri=TCCM.AssociatedEntitiesReference_objectToSubject, domain=AssociatedEntitiesReference, range=Optional[Bool])

slots.AssociatedEntitiesReference_transitiveClosure = Slot(uri=TCCM.transitiveClosure, name="AssociatedEntitiesReference_transitiveClosure", curie=TCCM.curie('transitiveClosure'),
                      model_uri=TCCM.AssociatedEntitiesReference_transitiveClosure, domain=AssociatedEntitiesReference, range=Optional[Bool])

slots.AssociatedEntitiesReference_leafOnly = Slot(uri=TCCM.leafOnly, name="AssociatedEntitiesReference_leafOnly", curie=TCCM.curie('leafOnly'),
                      model_uri=TCCM.AssociatedEntitiesReference_leafOnly, domain=AssociatedEntitiesReference, range=Optional[Bool])

slots.PropertyQueryReference_codeSystem = Slot(uri=TCCM.codeSystem, name="PropertyQueryReference_codeSystem", curie=TCCM.curie('codeSystem'),
                      model_uri=TCCM.PropertyQueryReference_codeSystem, domain=PropertyQueryReference, range=Union[dict, CodeSystemReference])

slots.PropertyQueryReference_codeSystemVersion = Slot(uri=TCCM.codeSystemVersion, name="PropertyQueryReference_codeSystemVersion", curie=TCCM.curie('codeSystemVersion'),
                      model_uri=TCCM.PropertyQueryReference_codeSystemVersion, domain=PropertyQueryReference, range=Optional[Union[dict, CodeSystemVersionReference]])

slots.PropertyQueryReference_filter = Slot(uri=TCCM.filter, name="PropertyQueryReference_filter", curie=TCCM.curie('filter'),
                      model_uri=TCCM.PropertyQueryReference_filter, domain=PropertyQueryReference, range=Union[dict, FilterComponent])

slots.CompleteCodeSystemReference_codeSystem = Slot(uri=TCCM.codeSystem, name="CompleteCodeSystemReference_codeSystem", curie=TCCM.curie('codeSystem'),
                      model_uri=TCCM.CompleteCodeSystemReference_codeSystem, domain=CompleteCodeSystemReference, range=Union[dict, CodeSystemReference])

slots.CompleteCodeSystemReference_codeSystemVersion = Slot(uri=TCCM.codeSystemVersion, name="CompleteCodeSystemReference_codeSystemVersion", curie=TCCM.curie('codeSystemVersion'),
                      model_uri=TCCM.CompleteCodeSystemReference_codeSystemVersion, domain=CompleteCodeSystemReference, range=Optional[Union[dict, CodeSystemVersionReference]])

slots.CompleteValueSetReference_valueSet = Slot(uri=TCCM.valueSet, name="CompleteValueSetReference_valueSet", curie=TCCM.curie('valueSet'),
                      model_uri=TCCM.CompleteValueSetReference_valueSet, domain=CompleteValueSetReference, range=Union[dict, ValueSetReference])

slots.CompleteValueSetReference_valueSetDefinition = Slot(uri=TCCM.valueSetDefinition, name="CompleteValueSetReference_valueSetDefinition", curie=TCCM.curie('valueSetDefinition'),
                      model_uri=TCCM.CompleteValueSetReference_valueSetDefinition, domain=CompleteValueSetReference, range=Optional[Union[dict, ValueSetDefinitionReference]])

slots.CompleteValueSetReference_referenceCodeSystemVersion = Slot(uri=TCCM.referenceCodeSystemVersion, name="CompleteValueSetReference_referenceCodeSystemVersion", curie=TCCM.curie('referenceCodeSystemVersion'),
                      model_uri=TCCM.CompleteValueSetReference_referenceCodeSystemVersion, domain=CompleteValueSetReference, range=Optional[Union[dict, CodeSystemVersionReference]])
