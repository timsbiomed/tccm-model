# Auto generated from sorting.yaml by pythongen.py version: 0.4.0
# Generation date: 2020-08-31 11:40
# Schema: sorting
#
# id: https://hotecosystem.org/tccm/sorting
# description: The elements that are used in the construction of query filters and return sort criteria.
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
from src.core.references import CodeSystemReference, CodeSystemReferenceName, FormatReference, FormatReferenceName, LanguageReference, LanguageReferenceName, MapReference, MapReferenceName, PredicateReference, RoleReference, RoleReferenceName
from src.core.uritypes import DocumentURI, ExternalURI, LocalURI, PersistentURI, RenderingURI
from biolinkml.utils.metamodelcore import Bool, URIorCURIE
from includes.types import Boolean, String

metamodel_version = "1.5.3"

# Overwrite dataclasses _init_fn to add **kwargs in __init__
dataclasses._init_fn = dataclasses_init_fn_with_kwargs

# Namespaces
TCCM = CurieNamespace('tccm', 'https://hotecosystem.org/tccm/')
DEFAULT_ = CurieNamespace('', 'https://hotecosystem.org/tccm/sorting/')


# Types

# Class references



@dataclass
class SortCriteria(YAMLRoot):
    """
    An ordered list of sort criterion. The first entry in the list identifies the primary sort order, the second
    entry the sub sort order, etc.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = TCCM["sorting/SortCriteria"]
    class_class_curie: ClassVar[str] = "tccm:sorting/SortCriteria"
    class_name: ClassVar[str] = "SortCriteria"
    class_model_uri: ClassVar[URIRef] = URIRef("https://hotecosystem.org/tccm/sorting/SortCriteria")

    entry: List[Union[dict, "SortCriterion"]] = empty_list()

    def __post_init__(self, **kwargs: Dict[str, Any]):
        self.entry = [SortCriterion(*e) for e in self.entry.items()] if isinstance(self.entry, dict) \
                      else [v if isinstance(v, SortCriterion) else SortCriterion(**v)
                            for v in ([self.entry] if isinstance(self.entry, str) else self.entry)]
        super().__post_init__(**kwargs)


@dataclass
class SortCriterion(YAMLRoot):
    """
    The particular attribute, property, or special element to be sorted along with the sort direction.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = TCCM["sorting/SortCriterion"]
    class_class_curie: ClassVar[str] = "tccm:sorting/SortCriterion"
    class_name: ClassVar[str] = "SortCriterion"
    class_model_uri: ClassVar[URIRef] = URIRef("https://hotecosystem.org/tccm/sorting/SortCriterion")

    sortElement: Union[dict, PredicateReference]
    sortDescending: Optional[Bool] = None

    def __post_init__(self, **kwargs: Dict[str, Any]):
        if self.sortElement is None:
            raise ValueError(f"sortElement must be supplied")
        if not isinstance(self.sortElement, PredicateReference):
            self.sortElement = PredicateReference(**self.sortElement)
        super().__post_init__(**kwargs)



# Slots
class slots:
    pass

slots.sortCriteria__entry = Slot(uri=DEFAULT_.entry, name="sortCriteria__entry", curie=DEFAULT_.curie('entry'),
                      model_uri=DEFAULT_.sortCriteria__entry, domain=None, range=List[Union[dict, SortCriterion]])

slots.sortCriterion__sortElement = Slot(uri=DEFAULT_.sortElement, name="sortCriterion__sortElement", curie=DEFAULT_.curie('sortElement'),
                      model_uri=DEFAULT_.sortCriterion__sortElement, domain=None, range=Union[dict, PredicateReference])

slots.sortCriterion__sortDescending = Slot(uri=DEFAULT_.sortDescending, name="sortCriterion__sortDescending", curie=DEFAULT_.curie('sortDescending'),
                      model_uri=DEFAULT_.sortCriterion__sortDescending, domain=None, range=Optional[Bool])

slots.nameAndMeaningReference__name = Slot(uri=DEFAULT_.name, name="nameAndMeaningReference__name", curie=DEFAULT_.curie('name'),
                      model_uri=DEFAULT_.nameAndMeaningReference__name, domain=None, range=URIRef)

slots.nameAndMeaningReference__synopsis = Slot(uri=DEFAULT_.synopsis, name="nameAndMeaningReference__synopsis", curie=DEFAULT_.curie('synopsis'),
                      model_uri=DEFAULT_.nameAndMeaningReference__synopsis, domain=None, range=Optional[str])

slots.nameAndMeaningReference__uri = Slot(uri=DEFAULT_.uri, name="nameAndMeaningReference__uri", curie=DEFAULT_.curie('uri'),
                      model_uri=DEFAULT_.nameAndMeaningReference__uri, domain=None, range=Optional[Union[URIorCURIE, ExternalURI]])

slots.nameAndMeaningReference__href = Slot(uri=DEFAULT_.href, name="nameAndMeaningReference__href", curie=DEFAULT_.curie('href'),
                      model_uri=DEFAULT_.nameAndMeaningReference__href, domain=None, range=Optional[Union[URIorCURIE, RenderingURI]])

slots.codeSystemVersionReference__codeSystem = Slot(uri=DEFAULT_.codeSystem, name="codeSystemVersionReference__codeSystem", curie=DEFAULT_.curie('codeSystem'),
                      model_uri=DEFAULT_.codeSystemVersionReference__codeSystem, domain=None, range=Optional[Union[dict, CodeSystemReference]])

slots.mapVersionReference__map = Slot(uri=DEFAULT_.map, name="mapVersionReference__map", curie=DEFAULT_.curie('map'),
                      model_uri=DEFAULT_.mapVersionReference__map, domain=None, range=Optional[Union[dict, MapReference]])

slots.predicateReference__uri = Slot(uri=DEFAULT_.uri, name="predicateReference__uri", curie=DEFAULT_.curie('uri'),
                      model_uri=DEFAULT_.predicateReference__uri, domain=None, range=Union[URIorCURIE, ExternalURI])

slots.predicateReference__name = Slot(uri=DEFAULT_.name, name="predicateReference__name", curie=DEFAULT_.curie('name'),
                      model_uri=DEFAULT_.predicateReference__name, domain=None, range=Optional[Union[str, LocalIdentifier]])

slots.predicateReference__href = Slot(uri=DEFAULT_.href, name="predicateReference__href", curie=DEFAULT_.curie('href'),
                      model_uri=DEFAULT_.predicateReference__href, domain=None, range=Optional[Union[URIorCURIE, RenderingURI]])

slots.predicateReference__designation = Slot(uri=DEFAULT_.designation, name="predicateReference__designation", curie=DEFAULT_.curie('designation'),
                      model_uri=DEFAULT_.predicateReference__designation, domain=None, range=Optional[str])

slots.sourceAndRoleReference__role = Slot(uri=DEFAULT_.role, name="sourceAndRoleReference__role", curie=DEFAULT_.curie('role'),
                      model_uri=DEFAULT_.sourceAndRoleReference__role, domain=None, range=Optional[Union[dict, RoleReference]])

slots.sourceAndRoleReference__bibliographicLink = Slot(uri=DEFAULT_.bibliographicLink, name="sourceAndRoleReference__bibliographicLink", curie=DEFAULT_.curie('bibliographicLink'),
                      model_uri=DEFAULT_.sourceAndRoleReference__bibliographicLink, domain=None, range=Optional[Union[dict, OpaqueData]])

slots.opaqueData__format = Slot(uri=DEFAULT_.format, name="opaqueData__format", curie=DEFAULT_.curie('format'),
                      model_uri=DEFAULT_.opaqueData__format, domain=None, range=Optional[Union[dict, FormatReference]])

slots.opaqueData__schema = Slot(uri=DEFAULT_.schema, name="opaqueData__schema", curie=DEFAULT_.curie('schema'),
                      model_uri=DEFAULT_.opaqueData__schema, domain=None, range=Optional[Union[URIorCURIE, DocumentURI]])

slots.opaqueData__language = Slot(uri=DEFAULT_.language, name="opaqueData__language", curie=DEFAULT_.curie('language'),
                      model_uri=DEFAULT_.opaqueData__language, domain=None, range=Optional[Union[dict, LanguageReference]])

slots.opaqueData__value = Slot(uri=DEFAULT_.value, name="opaqueData__value", curie=DEFAULT_.curie('value'),
                      model_uri=DEFAULT_.opaqueData__value, domain=None, range=str)
