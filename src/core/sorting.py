# Auto generated from sorting.yaml by pythongen.py version: 0.4.0
# Generation date: 2020-08-25 14:00
# Schema: filtersandsorting
#
# id: https://hotecosystem.org/tccm/filtersandsorting
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
from ...core.datatypes import CURIE, LocalIdentifier, URIorCurie
from ...core.references import CodeSystemReference, CodeSystemVersionReference, MapReference, MapVersionReference, NameAndMeaningReference, PredicateReference, RoleReference, SourceAndRoleReference
from ...core.uritypes import ExternalURI, LocalURI, PersistentURI, RenderingURI
from biolinkml.utils.metamodelcore import Bool, Curie, URIorCURIE
from includes.types import Boolean, String

metamodel_version = "1.5.3"

# Overwrite dataclasses _init_fn to add **kwargs in __init__
dataclasses._init_fn = dataclasses_init_fn_with_kwargs

# Namespaces
DEFAULT_ = CurieNamespace('', 'https://hotecosystem.org/tccm/filtersandsorting/')


# Types

# Class references



@dataclass
class SortCriteria(YAMLRoot):
    """
    An ordered list of sort criterion. The first entry in the list identifies the primary sort order, the second
    entry the sub sort order, etc.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = TCCM["filtersandsorting/SortCriteria"]
    class_class_curie: ClassVar[str] = "tccm:filtersandsorting/SortCriteria"
    class_name: ClassVar[str] = "SortCriteria"
    class_model_uri: ClassVar[URIRef] = URIRef("https://hotecosystem.org/tccm/filtersandsorting/SortCriteria")

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

    class_class_uri: ClassVar[URIRef] = TCCM["filtersandsorting/SortCriterion"]
    class_class_curie: ClassVar[str] = "tccm:filtersandsorting/SortCriterion"
    class_name: ClassVar[str] = "SortCriterion"
    class_model_uri: ClassVar[URIRef] = URIRef("https://hotecosystem.org/tccm/filtersandsorting/SortCriterion")

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

slots.entry = Slot(uri=DEFAULT_.entry, name="entry", curie=DEFAULT_.curie('entry'),
                      model_uri=DEFAULT_.entry, domain=None, range=List[Union[dict, SortCriterion]])

slots.sortElement = Slot(uri=DEFAULT_.sortElement, name="sortElement", curie=DEFAULT_.curie('sortElement'),
                      model_uri=DEFAULT_.sortElement, domain=None, range=Union[dict, PredicateReference])

slots.sortDescending = Slot(uri=DEFAULT_.sortDescending, name="sortDescending", curie=DEFAULT_.curie('sortDescending'),
                      model_uri=DEFAULT_.sortDescending, domain=None, range=Optional[Bool])

slots.name = Slot(uri=DEFAULT_.name, name="name", curie=DEFAULT_.curie('name'),
                      model_uri=DEFAULT_.name, domain=None, range=URIRef)

slots.synopsis = Slot(uri=DEFAULT_.synopsis, name="synopsis", curie=DEFAULT_.curie('synopsis'),
                      model_uri=DEFAULT_.synopsis, domain=None, range=Optional[str])

slots.uri = Slot(uri=DEFAULT_.uri, name="uri", curie=DEFAULT_.curie('uri'),
                      model_uri=DEFAULT_.uri, domain=None, range=Optional[Union[str, ExternalURI]])

slots.href = Slot(uri=DEFAULT_.href, name="href", curie=DEFAULT_.curie('href'),
                      model_uri=DEFAULT_.href, domain=None, range=Optional[Union[str, RenderingURI]])

slots.codeSystem = Slot(uri=DEFAULT_.codeSystem, name="codeSystem", curie=DEFAULT_.curie('codeSystem'),
                      model_uri=DEFAULT_.codeSystem, domain=None, range=Optional[Union[dict, CodeSystemReference]])

slots.map = Slot(uri=DEFAULT_.map, name="map", curie=DEFAULT_.curie('map'),
                      model_uri=DEFAULT_.map, domain=None, range=Optional[Union[dict, MapReference]])

slots.designation = Slot(uri=DEFAULT_.designation, name="designation", curie=DEFAULT_.curie('designation'),
                      model_uri=DEFAULT_.designation, domain=None, range=Optional[str])

slots.role = Slot(uri=DEFAULT_.role, name="role", curie=DEFAULT_.curie('role'),
                      model_uri=DEFAULT_.role, domain=None, range=Optional[Union[dict, RoleReference]])

slots.SortCriteria_entry = Slot(uri=DEFAULT_.entry, name="SortCriteria_entry", curie=DEFAULT_.curie('entry'),
                      model_uri=DEFAULT_.SortCriteria_entry, domain=SortCriteria, range=List[Union[dict, "SortCriterion"]])

slots.SortCriterion_sortElement = Slot(uri=DEFAULT_.sortElement, name="SortCriterion_sortElement", curie=DEFAULT_.curie('sortElement'),
                      model_uri=DEFAULT_.SortCriterion_sortElement, domain=SortCriterion, range=Union[dict, PredicateReference])

slots.SortCriterion_sortDescending = Slot(uri=DEFAULT_.sortDescending, name="SortCriterion_sortDescending", curie=DEFAULT_.curie('sortDescending'),
                      model_uri=DEFAULT_.SortCriterion_sortDescending, domain=SortCriterion, range=Optional[Bool])

slots.NameAndMeaningReference_name = Slot(uri=DEFAULT_.name, name="NameAndMeaningReference_name", curie=DEFAULT_.curie('name'),
                      model_uri=DEFAULT_.NameAndMeaningReference_name, domain=NameAndMeaningReference, range=Union[str, NameAndMeaningReferenceName])

slots.NameAndMeaningReference_synopsis = Slot(uri=DEFAULT_.synopsis, name="NameAndMeaningReference_synopsis", curie=DEFAULT_.curie('synopsis'),
                      model_uri=DEFAULT_.NameAndMeaningReference_synopsis, domain=NameAndMeaningReference, range=Optional[str])

slots.NameAndMeaningReference_uri = Slot(uri=DEFAULT_.uri, name="NameAndMeaningReference_uri", curie=DEFAULT_.curie('uri'),
                      model_uri=DEFAULT_.NameAndMeaningReference_uri, domain=NameAndMeaningReference, range=Optional[Union[str, ExternalURI]])

slots.NameAndMeaningReference_href = Slot(uri=DEFAULT_.href, name="NameAndMeaningReference_href", curie=DEFAULT_.curie('href'),
                      model_uri=DEFAULT_.NameAndMeaningReference_href, domain=NameAndMeaningReference, range=Optional[Union[str, RenderingURI]])

slots.CodeSystemVersionReference_codeSystem = Slot(uri=DEFAULT_.codeSystem, name="CodeSystemVersionReference_codeSystem", curie=DEFAULT_.curie('codeSystem'),
                      model_uri=DEFAULT_.CodeSystemVersionReference_codeSystem, domain=CodeSystemVersionReference, range=Optional[Union[dict, CodeSystemReference]])

slots.MapVersionReference_map = Slot(uri=DEFAULT_.map, name="MapVersionReference_map", curie=DEFAULT_.curie('map'),
                      model_uri=DEFAULT_.MapVersionReference_map, domain=MapVersionReference, range=Optional[Union[dict, MapReference]])

slots.PredicateReference_uri = Slot(uri=DEFAULT_.uri, name="PredicateReference_uri", curie=DEFAULT_.curie('uri'),
                      model_uri=DEFAULT_.PredicateReference_uri, domain=PredicateReference, range=Union[str, ExternalURI])

slots.PredicateReference_name = Slot(uri=DEFAULT_.name, name="PredicateReference_name", curie=DEFAULT_.curie('name'),
                      model_uri=DEFAULT_.PredicateReference_name, domain=PredicateReference, range=Union[Curie, PredicateReferenceName])

slots.PredicateReference_href = Slot(uri=DEFAULT_.href, name="PredicateReference_href", curie=DEFAULT_.curie('href'),
                      model_uri=DEFAULT_.PredicateReference_href, domain=PredicateReference, range=Optional[Union[str, RenderingURI]])

slots.PredicateReference_designation = Slot(uri=DEFAULT_.designation, name="PredicateReference_designation", curie=DEFAULT_.curie('designation'),
                      model_uri=DEFAULT_.PredicateReference_designation, domain=PredicateReference, range=Optional[str])

slots.SourceAndRoleReference_role = Slot(uri=DEFAULT_.role, name="SourceAndRoleReference_role", curie=DEFAULT_.curie('role'),
                      model_uri=DEFAULT_.SourceAndRoleReference_role, domain=SourceAndRoleReference, range=Optional[Union[dict, RoleReference]])
