# Auto generated from entityreference.yaml by pythongen.py version: 0.4.0
# Generation date: 2020-09-01 13:04
# Schema: entityreference
#
# id: https://hotecosystem.org/tccm/entityreference
# description: TCCM differentiates between a simple resource reference, such as a code system, code system
#              version, value set, etc. and a reference to an Entity - a class, predicate, or individual. Simple
#              resource references are identified by a single URI. Entity references, however, are subdivided into
#              two parts - a scoping namespace and an identifier that is unique within the context of the
#              namespace. This model defines three building blocks that are used for referencing entities
#              throughout the specification. The first form, URIAndEntityName provides the URI and local name by
#              which the entity is known within the context of the service. An optional href may also be supplied
#              that resolves to the EntityDescription that is contextually appropriate. The second form,
#              EntityReference, supplies the uri and name but also includes a list of code system versions that
#              make one or more assertions about (or using) the referenced entity. There will be at most one
#              version of any given code system in this list, the choice of which will depend on the context of
#              the query. The third form, EntityExpression, is a description of an Entity in an external language
#              and syntax such as RDF/ OWL, Manchester OWL, or SNOMED CT Compositional Grammar.
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
from src.core.entrydescription import OpaqueData
from src.core.localidentifiers import CodeSystemName
from src.core.references import CodeSystemReference, CodeSystemReferenceName, FormatReference, FormatReferenceName, LanguageReference, LanguageReferenceName, MapReference, MapReferenceName, OntologyLanguageReference, OntologyLanguageReferenceName, RoleReference, RoleReferenceName
from src.core.uritypes import DocumentURI, ExternalURI, LocalURI, PersistentURI, RenderingURI
from biolinkml.utils.metamodelcore import URIorCURIE
from includes.types import String

metamodel_version = "1.5.3"

# Overwrite dataclasses _init_fn to add **kwargs in __init__
dataclasses._init_fn = dataclasses_init_fn_with_kwargs

# Namespaces
RDF = CurieNamespace('rdf', 'http://www.w3.org/1999/02/22-rdf-syntax-ns#')
SKOS = CurieNamespace('skos', 'http://www.w3.org/2004/02/skos/core#')
TCCM = CurieNamespace('tccm', 'https://hotecosystem.org/tccm/')
DEFAULT_ = TCCM


# Types

# Class references
class EntityReferenceListNamespaceURI(ExternalURI):
    pass


class EntityReferenceCode(extended_str):
    pass


@dataclass
class EntityReferenceList(YAMLRoot):
    """
    A collection (set) of zero or more entity references that belong to the same scoping namespace
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = TCCM.EntityReferenceList
    class_class_curie: ClassVar[str] = "tccm:EntityReferenceList"
    class_name: ClassVar[str] = "EntityReferenceList"
    class_model_uri: ClassVar[URIRef] = TCCM.EntityReferenceList

    namespaceURI: Union[URIorCURIE, EntityReferenceListNamespaceURI]
    namespaceName: Optional[Union[str, CodeSystemName]] = None
    entities: Dict[Union[str, EntityReferenceCode], Union[dict, "EntityReference"]] = empty_dict()

    def __post_init__(self, **kwargs: Dict[str, Any]):
        if self.namespaceURI is None:
            raise ValueError(f"namespaceURI must be supplied")
        if not isinstance(self.namespaceURI, EntityReferenceListNamespaceURI):
            self.namespaceURI = EntityReferenceListNamespaceURI(self.namespaceURI)
        if self.namespaceName is not None and not isinstance(self.namespaceName, CodeSystemName):
            self.namespaceName = CodeSystemName(self.namespaceName)
        for k, v in self.entities.items():
            if not isinstance(v, EntityReference):
                self.entities[k] = EntityReference(code=k, **({} if v is None else v))
        super().__post_init__(**kwargs)


@dataclass
class EntityReference(YAMLRoot):
    """
    The URI, namespace/name (if known) and a list of code systems that make assertions about the entity.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = TCCM.EntityReference
    class_class_curie: ClassVar[str] = "tccm:EntityReference"
    class_name: ClassVar[str] = "EntityReference"
    class_model_uri: ClassVar[URIRef] = TCCM.EntityReference

    code: Union[str, EntityReferenceCode]
    about: Optional[URIorCURIE] = None
    designation: Optional[str] = None
    description: Optional[str] = None
    href: Optional[Union[URIorCURIE, RenderingURI]] = None
    see_also: List[Union[URIorCURIE, RenderingURI]] = empty_list()

    def __post_init__(self, **kwargs: Dict[str, Any]):
        if self.code is None:
            raise ValueError(f"code must be supplied")
        if not isinstance(self.code, EntityReferenceCode):
            self.code = EntityReferenceCode(self.code)
        if self.href is not None and not isinstance(self.href, RenderingURI):
            self.href = RenderingURI(self.href)
        self.see_also = [v if isinstance(v, RenderingURI)
                         else RenderingURI(v) for v in ([self.see_also] if isinstance(self.see_also, str) else self.see_also)]
        super().__post_init__(**kwargs)


@dataclass
class EntityExpression(YAMLRoot):
    """
    An expression in a given ontology language and syntax that describes or defines an entity. Examples might include
    descriptions of entities in Manchester OWL Syntax, RDF, SNOMED Concept Expression, etc.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = TCCM.EntityExpression
    class_class_curie: ClassVar[str] = "tccm:EntityExpression"
    class_name: ClassVar[str] = "EntityExpression"
    class_model_uri: ClassVar[URIRef] = TCCM.EntityExpression

    ontologyLanguage: Union[dict, OntologyLanguageReference]
    expression: Union[dict, OpaqueData]

    def __post_init__(self, **kwargs: Dict[str, Any]):
        if self.ontologyLanguage is None:
            raise ValueError(f"ontologyLanguage must be supplied")
        if not isinstance(self.ontologyLanguage, OntologyLanguageReference):
            self.ontologyLanguage = OntologyLanguageReference(self.ontologyLanguage)
        if self.expression is None:
            raise ValueError(f"expression must be supplied")
        if not isinstance(self.expression, OpaqueData):
            self.expression = OpaqueData(**self.expression)
        super().__post_init__(**kwargs)



# Slots
class slots:
    pass

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

slots.opaqueData__format = Slot(uri=TCCM.format, name="opaqueData__format", curie=TCCM.curie('format'),
                      model_uri=TCCM.opaqueData__format, domain=None, range=Optional[Union[dict, FormatReference]])

slots.opaqueData__schema = Slot(uri=TCCM.schema, name="opaqueData__schema", curie=TCCM.curie('schema'),
                      model_uri=TCCM.opaqueData__schema, domain=None, range=Optional[Union[URIorCURIE, DocumentURI]])

slots.opaqueData__language = Slot(uri=TCCM.language, name="opaqueData__language", curie=TCCM.curie('language'),
                      model_uri=TCCM.opaqueData__language, domain=None, range=Optional[Union[dict, LanguageReference]])

slots.opaqueData__value = Slot(uri=TCCM.value, name="opaqueData__value", curie=TCCM.curie('value'),
                      model_uri=TCCM.opaqueData__value, domain=None, range=str)
