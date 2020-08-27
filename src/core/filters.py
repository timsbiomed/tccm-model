# Auto generated from filters.yaml by pythongen.py version: 0.4.0
# Generation date: 2020-08-26 15:38
# Schema: filters
#
# id: https://hotecosystem.org/tccm/filters
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
from src.core.datatypes import LocalIdentifier, URIorCurie
from src.core.references import CodeSystemReference, CodeSystemReferenceName, MapReference, MapReferenceName, MatchAlgorithmReference, MatchAlgorithmReferenceName, PredicateReference, PredicateReferenceName, RoleReference, RoleReferenceName
from src.core.uritypes import ExternalURI, LocalURI, PersistentURI, RenderingURI
from biolinkml.utils.metamodelcore import URIorCURIE
from includes.types import String

metamodel_version = "1.5.3"

# Overwrite dataclasses _init_fn to add **kwargs in __init__
dataclasses._init_fn = dataclasses_init_fn_with_kwargs

# Namespaces
TCCM = CurieNamespace('tccm', 'https://hotecosystem.org/tccm/')
DEFAULT_ = TCCM


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

    class_class_uri: ClassVar[URIRef] = TCCM.Filter
    class_class_curie: ClassVar[str] = "tccm:Filter"
    class_name: ClassVar[str] = "Filter"
    class_model_uri: ClassVar[URIRef] = TCCM.Filter

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

    class_class_uri: ClassVar[URIRef] = TCCM.FilterComponent
    class_class_curie: ClassVar[str] = "tccm:FilterComponent"
    class_name: ClassVar[str] = "FilterComponent"
    class_model_uri: ClassVar[URIRef] = TCCM.FilterComponent

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
            self.matchAlgorithm = MatchAlgorithmReference(self.matchAlgorithm)
        super().__post_init__(**kwargs)



# Slots
class slots:
    pass

slots.component = Slot(uri=TCCM.component, name="component", curie=TCCM.curie('component'),
                      model_uri=TCCM.component, domain=None, range=List[Union[dict, FilterComponent]])

slots.description = Slot(uri=TCCM.description, name="description", curie=TCCM.curie('description'),
                      model_uri=TCCM.description, domain=None, range=Optional[str])

slots.filterComponent = Slot(uri=TCCM.filterComponent, name="filterComponent", curie=TCCM.curie('filterComponent'),
                      model_uri=TCCM.filterComponent, domain=None, range=Dict[Union[Curie, PredicateReferenceName], Union[dict, PredicateReference]])

slots.matchAlgorithm = Slot(uri=TCCM.matchAlgorithm, name="matchAlgorithm", curie=TCCM.curie('matchAlgorithm'),
                      model_uri=TCCM.matchAlgorithm, domain=None, range=Union[dict, MatchAlgorithmReference])

slots.matchValue = Slot(uri=TCCM.matchValue, name="matchValue", curie=TCCM.curie('matchValue'),
                      model_uri=TCCM.matchValue, domain=None, range=Optional[str])

slots.name = Slot(uri=TCCM.name, name="name", curie=TCCM.curie('name'),
                      model_uri=TCCM.name, domain=None, range=URIRef)

slots.synopsis = Slot(uri=TCCM.synopsis, name="synopsis", curie=TCCM.curie('synopsis'),
                      model_uri=TCCM.synopsis, domain=None, range=Optional[str])

slots.uri = Slot(uri=TCCM.uri, name="uri", curie=TCCM.curie('uri'),
                      model_uri=TCCM.uri, domain=None, range=Optional[Union[str, ExternalURI]])

slots.href = Slot(uri=TCCM.href, name="href", curie=TCCM.curie('href'),
                      model_uri=TCCM.href, domain=None, range=Optional[Union[str, RenderingURI]])

slots.codeSystem = Slot(uri=TCCM.codeSystem, name="codeSystem", curie=TCCM.curie('codeSystem'),
                      model_uri=TCCM.codeSystem, domain=None, range=Optional[Union[dict, CodeSystemReference]])

slots.map = Slot(uri=TCCM.map, name="map", curie=TCCM.curie('map'),
                      model_uri=TCCM.map, domain=None, range=Optional[Union[dict, MapReference]])

slots.designation = Slot(uri=TCCM.designation, name="designation", curie=TCCM.curie('designation'),
                      model_uri=TCCM.designation, domain=None, range=Optional[str])

slots.role = Slot(uri=TCCM.role, name="role", curie=TCCM.curie('role'),
                      model_uri=TCCM.role, domain=None, range=Optional[Union[dict, RoleReference]])

slots.Filter_component = Slot(uri=TCCM.component, name="Filter_component", curie=TCCM.curie('component'),
                      model_uri=TCCM.Filter_component, domain=Filter, range=List[Union[dict, "FilterComponent"]])

slots.Filter_description = Slot(uri=TCCM.description, name="Filter_description", curie=TCCM.curie('description'),
                      model_uri=TCCM.Filter_description, domain=Filter, range=Optional[str])

slots.FilterComponent_filterComponent = Slot(uri=TCCM.filterComponent, name="FilterComponent_filterComponent", curie=TCCM.curie('filterComponent'),
                      model_uri=TCCM.FilterComponent_filterComponent, domain=FilterComponent, range=Dict[Union[Curie, PredicateReferenceName], Union[dict, PredicateReference]])

slots.FilterComponent_matchAlgorithm = Slot(uri=TCCM.matchAlgorithm, name="FilterComponent_matchAlgorithm", curie=TCCM.curie('matchAlgorithm'),
                      model_uri=TCCM.FilterComponent_matchAlgorithm, domain=FilterComponent, range=Union[dict, MatchAlgorithmReference])

slots.FilterComponent_matchValue = Slot(uri=TCCM.matchValue, name="FilterComponent_matchValue", curie=TCCM.curie('matchValue'),
                      model_uri=TCCM.FilterComponent_matchValue, domain=FilterComponent, range=Optional[str])
