# Auto generated from entityreference.yaml by pythongen.py version: 0.4.0
# Generation date: 2020-08-26 15:38
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
from src.core.datatypes import LocalIdentifier, URIorCurie
from src.core.localidentifiers import CodeSystemName
from src.core.uritypes import ExternalURI, LocalURI, PersistentURI, RenderingURI
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

    namespaceURI: Union[str, EntityReferenceListNamespaceURI]
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
    about: Optional[Union[str, PersistentURI]] = None
    designation: Optional[str] = None
    description: Optional[str] = None
    href: Optional[Union[str, RenderingURI]] = None
    see_also: List[Union[str, RenderingURI]] = empty_list()

    def __post_init__(self, **kwargs: Dict[str, Any]):
        if self.code is None:
            raise ValueError(f"code must be supplied")
        if not isinstance(self.code, EntityReferenceCode):
            self.code = EntityReferenceCode(self.code)
        if self.about is not None and not isinstance(self.about, PersistentURI):
            self.about = PersistentURI(self.about)
        if self.href is not None and not isinstance(self.href, RenderingURI):
            self.href = RenderingURI(self.href)
        self.see_also = [v if isinstance(v, RenderingURI)
                         else RenderingURI(v) for v in ([self.see_also] if isinstance(self.see_also, str) else self.see_also)]
        super().__post_init__(**kwargs)



# Slots
class slots:
    pass

slots.namespaceURI = Slot(uri=TCCM.namespaceURI, name="namespaceURI", curie=TCCM.curie('namespaceURI'),
                      model_uri=TCCM.namespaceURI, domain=None, range=URIRef)

slots.namespaceName = Slot(uri=TCCM.namespaceName, name="namespaceName", curie=TCCM.curie('namespaceName'),
                      model_uri=TCCM.namespaceName, domain=None, range=Optional[Union[str, CodeSystemName]])

slots.entities = Slot(uri=TCCM.entities, name="entities", curie=TCCM.curie('entities'),
                      model_uri=TCCM.entities, domain=None, range=Dict[Union[str, EntityReferenceCode], Union[dict, EntityReference]])

slots.about = Slot(uri=TCCM.about, name="about", curie=TCCM.curie('about'),
                      model_uri=TCCM.about, domain=None, range=Optional[Union[str, PersistentURI]])

slots.code = Slot(uri=RDF.id, name="code", curie=RDF.curie('id'),
                      model_uri=TCCM.code, domain=None, range=URIRef)

slots.designation = Slot(uri=SKOS.prefLabel, name="designation", curie=SKOS.curie('prefLabel'),
                      model_uri=TCCM.designation, domain=None, range=Optional[str])

slots.description = Slot(uri=SKOS.definition, name="description", curie=SKOS.curie('definition'),
                      model_uri=TCCM.description, domain=None, range=Optional[str])

slots.href = Slot(uri=TCCM.href, name="href", curie=TCCM.curie('href'),
                      model_uri=TCCM.href, domain=None, range=Optional[Union[str, RenderingURI]])

slots.see_also = Slot(uri=TCCM.see_also, name="see_also", curie=TCCM.curie('see_also'),
                      model_uri=TCCM.see_also, domain=None, range=List[Union[str, RenderingURI]])

slots.EntityReferenceList_namespaceURI = Slot(uri=TCCM.namespaceURI, name="EntityReferenceList_namespaceURI", curie=TCCM.curie('namespaceURI'),
                      model_uri=TCCM.EntityReferenceList_namespaceURI, domain=EntityReferenceList, range=Union[str, EntityReferenceListNamespaceURI])

slots.EntityReferenceList_namespaceName = Slot(uri=TCCM.namespaceName, name="EntityReferenceList_namespaceName", curie=TCCM.curie('namespaceName'),
                      model_uri=TCCM.EntityReferenceList_namespaceName, domain=EntityReferenceList, range=Optional[Union[str, CodeSystemName]])

slots.EntityReferenceList_entities = Slot(uri=TCCM.entities, name="EntityReferenceList_entities", curie=TCCM.curie('entities'),
                      model_uri=TCCM.EntityReferenceList_entities, domain=EntityReferenceList, range=Dict[Union[str, EntityReferenceCode], Union[dict, "EntityReference"]])

slots.EntityReference_about = Slot(uri=TCCM.about, name="EntityReference_about", curie=TCCM.curie('about'),
                      model_uri=TCCM.EntityReference_about, domain=EntityReference, range=Optional[Union[str, PersistentURI]])

slots.EntityReference_code = Slot(uri=RDF.id, name="EntityReference_code", curie=RDF.curie('id'),
                      model_uri=TCCM.EntityReference_code, domain=EntityReference, range=Union[str, EntityReferenceCode])

slots.EntityReference_designation = Slot(uri=SKOS.prefLabel, name="EntityReference_designation", curie=SKOS.curie('prefLabel'),
                      model_uri=TCCM.EntityReference_designation, domain=EntityReference, range=Optional[str])

slots.EntityReference_description = Slot(uri=SKOS.definition, name="EntityReference_description", curie=SKOS.curie('definition'),
                      model_uri=TCCM.EntityReference_description, domain=EntityReference, range=Optional[str])

slots.EntityReference_href = Slot(uri=TCCM.href, name="EntityReference_href", curie=TCCM.curie('href'),
                      model_uri=TCCM.EntityReference_href, domain=EntityReference, range=Optional[Union[str, RenderingURI]])

slots.EntityReference_see_also = Slot(uri=TCCM.see_also, name="EntityReference_see_also", curie=TCCM.curie('see_also'),
                      model_uri=TCCM.EntityReference_see_also, domain=EntityReference, range=List[Union[str, RenderingURI]])
