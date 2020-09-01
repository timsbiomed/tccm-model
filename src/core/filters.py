# Auto generated from filters.yaml by pythongen.py version: 0.4.0
# Generation date: 2020-09-01 13:05
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
from src.core.datatypes import LocalIdentifier
from src.core.entrydescription import OpaqueData
from src.core.references import CodeSystemReference, CodeSystemReferenceName, FormatReference, FormatReferenceName, LanguageReference, LanguageReferenceName, MapReference, MapReferenceName, MatchAlgorithmReference, MatchAlgorithmReferenceName, PredicateReference, RoleReference, RoleReferenceName
from src.core.uritypes import DocumentURI, ExternalURI, LocalURI, PersistentURI, RenderingURI
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
    filterComponent: List[Union[dict, PredicateReference]] = empty_list()
    matchValue: Optional[str] = None

    def __post_init__(self, **kwargs: Dict[str, Any]):
        self.filterComponent = [PredicateReference(*e) for e in self.filterComponent.items()] if isinstance(self.filterComponent, dict) \
                                else [v if isinstance(v, PredicateReference) else PredicateReference(**v)
                                      for v in ([self.filterComponent] if isinstance(self.filterComponent, str) else self.filterComponent)]
        if self.matchAlgorithm is None:
            raise ValueError(f"matchAlgorithm must be supplied")
        if not isinstance(self.matchAlgorithm, MatchAlgorithmReference):
            self.matchAlgorithm = MatchAlgorithmReference(self.matchAlgorithm)
        super().__post_init__(**kwargs)



# Slots
class slots:
    pass

slots.filter__component = Slot(uri=TCCM.component, name="filter__component", curie=TCCM.curie('component'),
                      model_uri=TCCM.filter__component, domain=None, range=List[Union[dict, FilterComponent]])

slots.filter__description = Slot(uri=TCCM.description, name="filter__description", curie=TCCM.curie('description'),
                      model_uri=TCCM.filter__description, domain=None, range=Optional[str])

slots.filterComponent__filterComponent = Slot(uri=TCCM.filterComponent, name="filterComponent__filterComponent", curie=TCCM.curie('filterComponent'),
                      model_uri=TCCM.filterComponent__filterComponent, domain=None, range=List[Union[dict, PredicateReference]])

slots.filterComponent__matchAlgorithm = Slot(uri=TCCM.matchAlgorithm, name="filterComponent__matchAlgorithm", curie=TCCM.curie('matchAlgorithm'),
                      model_uri=TCCM.filterComponent__matchAlgorithm, domain=None, range=Union[dict, MatchAlgorithmReference])

slots.filterComponent__matchValue = Slot(uri=TCCM.matchValue, name="filterComponent__matchValue", curie=TCCM.curie('matchValue'),
                      model_uri=TCCM.filterComponent__matchValue, domain=None, range=Optional[str])

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
