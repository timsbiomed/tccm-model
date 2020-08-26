# Auto generated from filters.yaml by pythongen.py version: 0.4.0
# Generation date: 2020-08-25 13:58
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
from ...core.references import CodeSystemReference, CodeSystemVersionReference, MapReference, MapVersionReference, MatchAlgorithmReference, NameAndMeaningReference, PredicateReference, RoleReference, SourceAndRoleReference
from ...core.uritypes import ExternalURI, LocalURI, PersistentURI, RenderingURI
from biolinkml.utils.metamodelcore import Curie, URIorCURIE
from includes.types import String

metamodel_version = "1.5.3"

# Overwrite dataclasses _init_fn to add **kwargs in __init__
dataclasses._init_fn = dataclasses_init_fn_with_kwargs

# Namespaces
DEFAULT_ = CurieNamespace('', 'https://hotecosystem.org/tccm/filtersandsorting/')


# Types

# Class references



@dataclass
class Filter(YAMLRoot):
    """
    A collection of one or more filters. The result of applying a Filter component is the intersection of the sets of
    qualifying elements. As an example, a filter having two components - one which says that the rights attribute must
    exist and a second that says that the text “SNOMED” must appear in the synopsis would return all resources having
    BOTH a rights attribute and “SNOMED” in the description.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = TCCM["filtersandsorting/Filter"]
    class_class_curie: ClassVar[str] = "tccm:filtersandsorting/Filter"
    class_name: ClassVar[str] = "Filter"
    class_model_uri: ClassVar[URIRef] = URIRef("https://hotecosystem.org/tccm/filtersandsorting/Filter")

    component: List[Union[dict, "FilterComponent"]] = empty_list()
    description: Optional[str] = None

    def __post_init__(self, **kwargs: Dict[str, Any]):
        if not isinstance(self.component, list) or len(self.component) == 0:
            raise ValueError(f"component must be a non-empty list")
        self.component = [FilterComponent(*e) for e in self.component.items()] if isinstance(self.component, dict) \
                          else [v if isinstance(v, FilterComponent) else FilterComponent(**v)
                                for v in ([self.component] if isinstance(self.component, str) else self.component)]
        super().__post_init__(**kwargs)


@dataclass
class FilterComponent(YAMLRoot):
    """
    A restriction on an attribute, property, or special field.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = TCCM["filtersandsorting/FilterComponent"]
    class_class_curie: ClassVar[str] = "tccm:filtersandsorting/FilterComponent"
    class_name: ClassVar[str] = "FilterComponent"
    class_model_uri: ClassVar[URIRef] = URIRef("https://hotecosystem.org/tccm/filtersandsorting/FilterComponent")

    matchAlgorithm: Union[dict, MatchAlgorithmReference]
    filterComponent: Dict[Union[Curie, PredicateReferenceName], Union[dict, PredicateReference]] = empty_dict()
    matchValue: Optional[str] = None

    def __post_init__(self, **kwargs: Dict[str, Any]):
        for k, v in self.filterComponent.items():
            if not isinstance(v, PredicateReference):
                self.filterComponent[k] = PredicateReference(name=k, **({} if v is None else v))
        if self.matchAlgorithm is None:
            raise ValueError(f"matchAlgorithm must be supplied")
        if not isinstance(self.matchAlgorithm, MatchAlgorithmReference):
            self.matchAlgorithm = MatchAlgorithmReference(**self.matchAlgorithm)
        super().__post_init__(**kwargs)



# Slots
class slots:
    pass

slots.component = Slot(uri=DEFAULT_.component, name="component", curie=DEFAULT_.curie('component'),
                      model_uri=DEFAULT_.component, domain=None, range=List[Union[dict, FilterComponent]])

slots.description = Slot(uri=DEFAULT_.description, name="description", curie=DEFAULT_.curie('description'),
                      model_uri=DEFAULT_.description, domain=None, range=Optional[str])

slots.filterComponent = Slot(uri=DEFAULT_.filterComponent, name="filterComponent", curie=DEFAULT_.curie('filterComponent'),
                      model_uri=DEFAULT_.filterComponent, domain=None, range=Dict[Union[Curie, PredicateReferenceName], Union[dict, PredicateReference]])

slots.matchAlgorithm = Slot(uri=DEFAULT_.matchAlgorithm, name="matchAlgorithm", curie=DEFAULT_.curie('matchAlgorithm'),
                      model_uri=DEFAULT_.matchAlgorithm, domain=None, range=Union[dict, MatchAlgorithmReference])

slots.matchValue = Slot(uri=DEFAULT_.matchValue, name="matchValue", curie=DEFAULT_.curie('matchValue'),
                      model_uri=DEFAULT_.matchValue, domain=None, range=Optional[str])

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

slots.Filter_component = Slot(uri=DEFAULT_.component, name="Filter_component", curie=DEFAULT_.curie('component'),
                      model_uri=DEFAULT_.Filter_component, domain=Filter, range=List[Union[dict, "FilterComponent"]])

slots.Filter_description = Slot(uri=DEFAULT_.description, name="Filter_description", curie=DEFAULT_.curie('description'),
                      model_uri=DEFAULT_.Filter_description, domain=Filter, range=Optional[str])

slots.FilterComponent_filterComponent = Slot(uri=DEFAULT_.filterComponent, name="FilterComponent_filterComponent", curie=DEFAULT_.curie('filterComponent'),
                      model_uri=DEFAULT_.FilterComponent_filterComponent, domain=FilterComponent, range=Dict[Union[Curie, PredicateReferenceName], Union[dict, PredicateReference]])

slots.FilterComponent_matchAlgorithm = Slot(uri=DEFAULT_.matchAlgorithm, name="FilterComponent_matchAlgorithm", curie=DEFAULT_.curie('matchAlgorithm'),
                      model_uri=DEFAULT_.FilterComponent_matchAlgorithm, domain=FilterComponent, range=Union[dict, MatchAlgorithmReference])

slots.FilterComponent_matchValue = Slot(uri=DEFAULT_.matchValue, name="FilterComponent_matchValue", curie=DEFAULT_.curie('matchValue'),
                      model_uri=DEFAULT_.FilterComponent_matchValue, domain=FilterComponent, range=Optional[str])

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
