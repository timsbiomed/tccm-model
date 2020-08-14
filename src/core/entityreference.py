# Auto generated from entityreference.yaml by pythongen.py version: 0.4.0
# Generation date: 2020-08-13 16:16
# Schema: entityreference
#
# id: https://hotecosystem.org/tccm/entityreference
# description: TCCM differentiates between a simple resource reference, such as a code system, code system
#              version, value set, etc. and a reference to an Entity - a class, predicate, or individual. Simple
#              resource references are identified by a single URI. Entity references, however, are subdivided into
#              two parts - a scoping namespace and a name that is unique within the context of the namespace. This
#              model defines three building blocks that are used for referencing entities throughout the
#              specification. The first form, URIAndEntityName provides the URI and local name by which the entity
#              is known within the context of the service. An optional href may also be supplied that resolves to
#              the EntityDescription that is contextually appropriate. The second form, EntityReference, supplies
#              the uri and name but also includes a list of code system versions that make one or more assertions
#              about (or using) the referenced entity. There will be at most one version of any given code system
#              in this list, the choice of which will depend on the context of the query. The third form,
#              EntityExpression, is a description of an Entity in an external language and syntax such as RDF/
#              OWL, Manchester OWL, or SNOMED CT Compositional Grammar.
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
from biolinkml.utils.metamodelcore import URIorCURIE
from datatypes import URIorCurie
from includes.types import String
from uritypes import LocalURI, PersistentURI, RenderingURI

metamodel_version = "1.5.3"

# Overwrite dataclasses _init_fn to add **kwargs in __init__
dataclasses._init_fn = dataclasses_init_fn_with_kwargs

# Namespaces
TCCM = CurieNamespace('tccm', 'https://hotecosystem.org/tccm/')
DEFAULT_ = TCCM


# Types

# Class references



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

    about: Union[str, PersistentURI]
    name: Optional[str] = None
    designation: Optional[str] = None
    href: Optional[Union[str, RenderingURI]] = None

    def __post_init__(self, **kwargs: Dict[str, Any]):
        if self.about is None:
            raise ValueError(f"about must be supplied")
        if not isinstance(self.about, PersistentURI):
            self.about = PersistentURI(self.about)
        if self.href is not None and not isinstance(self.href, RenderingURI):
            self.href = RenderingURI(self.href)
        super().__post_init__(**kwargs)



# Slots
class slots:
    pass

slots.about = Slot(uri=TCCM.about, name="about", curie=TCCM.curie('about'),
                      model_uri=TCCM.about, domain=None, range=Union[str, PersistentURI])

slots.name = Slot(uri=TCCM.name, name="name", curie=TCCM.curie('name'),
                      model_uri=TCCM.name, domain=None, range=Optional[str])

slots.designation = Slot(uri=TCCM.designation, name="designation", curie=TCCM.curie('designation'),
                      model_uri=TCCM.designation, domain=None, range=Optional[str])

slots.href = Slot(uri=TCCM.href, name="href", curie=TCCM.curie('href'),
                      model_uri=TCCM.href, domain=None, range=Optional[Union[str, RenderingURI]])

slots.EntityReference_about = Slot(uri=TCCM.about, name="EntityReference_about", curie=TCCM.curie('about'),
                      model_uri=TCCM.EntityReference_about, domain=EntityReference, range=Union[str, PersistentURI])

slots.EntityReference_name = Slot(uri=TCCM.name, name="EntityReference_name", curie=TCCM.curie('name'),
                      model_uri=TCCM.EntityReference_name, domain=EntityReference, range=Optional[str])

slots.EntityReference_designation = Slot(uri=TCCM.designation, name="EntityReference_designation", curie=TCCM.curie('designation'),
                      model_uri=TCCM.EntityReference_designation, domain=EntityReference, range=Optional[str])

slots.EntityReference_href = Slot(uri=TCCM.href, name="EntityReference_href", curie=TCCM.curie('href'),
                      model_uri=TCCM.EntityReference_href, domain=EntityReference, range=Optional[Union[str, RenderingURI]])
