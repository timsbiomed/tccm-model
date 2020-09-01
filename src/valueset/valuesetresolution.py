# Auto generated from valuesetresolution.yaml by pythongen.py version: 0.4.0
# Generation date: 2020-09-01 13:13
# Schema: valuesetresolution
#
# id: https://hotecosystem.org/tccm/valuesetresolution
# description: ValueSet definitions can be resolved dynamically on an as needed basis, but they also can be
#              transferred between systems without the necessity of maintaining complete copies of the code system
#              versions that are used to resolve them. This model defines the output of a value set resolution
#              request. It contains sufficient information that the request can be completely reproduced against a
#              service instance the mirrors the state of the system doing the resolution. It also carries the
#              result of the resolution that can be transferred and loaded into a system that does not mirror the
#              source system state.
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
from src.core.entityreference import EntityReference, EntityReferenceCode
from src.core.entrydescription import OpaqueData
from src.core.filters import FilterComponent
from src.core.localidentifiers import CodeSystemName
from src.core.references import CodeSystemReference, CodeSystemReferenceName, CodeSystemVersionReference, CodeSystemVersionReferenceName, FormatReference, FormatReferenceName, LanguageReference, LanguageReferenceName, MapReference, MapReferenceName, MatchAlgorithmReference, MatchAlgorithmReferenceName, NameAndMeaningReference, NameAndMeaningReferenceName, OntologyLanguageReference, OntologyLanguageReferenceName, OntologySyntaxReference, OntologySyntaxReferenceName, PredicateReference, RoleReference, RoleReferenceName, ValueSetDefinitionReference, ValueSetDefinitionReferenceName
from src.core.resourcedescription import SourceAndNotation
from src.core.uritypes import DocumentURI, ExternalURI, LocalURI, PersistentURI, RenderingURI
from biolinkml.utils.metamodelcore import URIorCURIE, XSDDateTime
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
class ResolvedValueSetHeader(YAMLRoot):
    """
    The information required to completely resolve a value set definition.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = TCCM.ResolvedValueSetHeader
    class_class_curie: ClassVar[str] = "tccm:ResolvedValueSetHeader"
    class_name: ClassVar[str] = "ResolvedValueSetHeader"
    class_model_uri: ClassVar[URIRef] = TCCM.ResolvedValueSetHeader

    resolutionOf: Union[dict, ValueSetDefinitionReference]
    resolvedUsingCodeSystem: Dict[Union[str, CodeSystemVersionReferenceName], Union[dict, CodeSystemVersionReference]] = empty_dict()
    includesResolvedValueSet: List[Union[dict, "ResolvedValueSetHeader"]] = empty_list()

    def __post_init__(self, **kwargs: Dict[str, Any]):
        if self.resolutionOf is None:
            raise ValueError(f"resolutionOf must be supplied")
        if not isinstance(self.resolutionOf, ValueSetDefinitionReference):
            self.resolutionOf = ValueSetDefinitionReference(self.resolutionOf)
        for k, v in self.resolvedUsingCodeSystem.items():
            if not isinstance(v, CodeSystemVersionReference):
                self.resolvedUsingCodeSystem[k] = CodeSystemVersionReference(name=k, **({} if v is None else v))
        self.includesResolvedValueSet = [ResolvedValueSetHeader(*e) for e in self.includesResolvedValueSet.items()] if isinstance(self.includesResolvedValueSet, dict) \
                                         else [v if isinstance(v, ResolvedValueSetHeader) else ResolvedValueSetHeader(**v)
                                               for v in ([self.includesResolvedValueSet] if isinstance(self.includesResolvedValueSet, str) else self.includesResolvedValueSet)]
        super().__post_init__(**kwargs)



# Slots
class slots:
    pass

slots.resolvedValueSetHeader__resolutionOf = Slot(uri=TCCM.resolutionOf, name="resolvedValueSetHeader__resolutionOf", curie=TCCM.curie('resolutionOf'),
                      model_uri=TCCM.resolvedValueSetHeader__resolutionOf, domain=None, range=Union[dict, ValueSetDefinitionReference])

slots.resolvedValueSetHeader__resolvedUsingCodeSystem = Slot(uri=TCCM.resolvedUsingCodeSystem, name="resolvedValueSetHeader__resolvedUsingCodeSystem", curie=TCCM.curie('resolvedUsingCodeSystem'),
                      model_uri=TCCM.resolvedValueSetHeader__resolvedUsingCodeSystem, domain=None, range=Dict[Union[str, CodeSystemVersionReferenceName], Union[dict, CodeSystemVersionReference]])

slots.resolvedValueSetHeader__includesResolvedValueSet = Slot(uri=TCCM.includesResolvedValueSet, name="resolvedValueSetHeader__includesResolvedValueSet", curie=TCCM.curie('includesResolvedValueSet'),
                      model_uri=TCCM.resolvedValueSetHeader__includesResolvedValueSet, domain=None, range=List[Union[dict, ResolvedValueSetHeader]])

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

slots.resourceDescription__describedResourceType = Slot(uri=TCCM.describedResourceType, name="resourceDescription__describedResourceType", curie=TCCM.curie('describedResourceType'),
                      model_uri=TCCM.resourceDescription__describedResourceType, domain=None, range=Optional[str])

slots.resourceDescription__resourceSynopsis = Slot(uri=TCCM.resourceSynopsis, name="resourceDescription__resourceSynopsis", curie=TCCM.curie('resourceSynopsis'),
                      model_uri=TCCM.resourceDescription__resourceSynopsis, domain=None, range=Optional[str])

slots.resourceDescription__resourceID = Slot(uri=TCCM.id, name="resourceDescription__resourceID", curie=TCCM.curie('id'),
                      model_uri=TCCM.resourceDescription__resourceID, domain=None, range=URIRef)

slots.resourceDescription__about = Slot(uri=TCCM.about, name="resourceDescription__about", curie=TCCM.curie('about'),
                      model_uri=TCCM.resourceDescription__about, domain=None, range=Union[URIorCURIE, ExternalURI])

slots.resourceDescription__formalName = Slot(uri=TCCM.formalName, name="resourceDescription__formalName", curie=TCCM.curie('formalName'),
                      model_uri=TCCM.resourceDescription__formalName, domain=None, range=Optional[str])

slots.resourceDescription__keyword = Slot(uri=TCCM.keyword, name="resourceDescription__keyword", curie=TCCM.curie('keyword'),
                      model_uri=TCCM.resourceDescription__keyword, domain=None, range=List[str])

slots.resourceDescription__additionalDocumentation = Slot(uri=TCCM.additionalDocumentation, name="resourceDescription__additionalDocumentation", curie=TCCM.curie('additionalDocumentation'),
                      model_uri=TCCM.resourceDescription__additionalDocumentation, domain=None, range=List[URIorCURIE])

slots.resourceDescription__rights = Slot(uri=TCCM.rights, name="resourceDescription__rights", curie=TCCM.curie('rights'),
                      model_uri=TCCM.resourceDescription__rights, domain=None, range=Optional[str])

slots.resourceDescription__alternateID = Slot(uri=TCCM.alternateID, name="resourceDescription__alternateID", curie=TCCM.curie('alternateID'),
                      model_uri=TCCM.resourceDescription__alternateID, domain=None, range=Optional[str])

slots.sourceAndNotation__sourceAndNotationDescription = Slot(uri=TCCM.sourceAndNotationDescription, name="sourceAndNotation__sourceAndNotationDescription", curie=TCCM.curie('sourceAndNotationDescription'),
                      model_uri=TCCM.sourceAndNotation__sourceAndNotationDescription, domain=None, range=Optional[str])

slots.sourceAndNotation__sourceDocument = Slot(uri=TCCM.sourceDocument, name="sourceAndNotation__sourceDocument", curie=TCCM.curie('sourceDocument'),
                      model_uri=TCCM.sourceAndNotation__sourceDocument, domain=None, range=Optional[URIorCURIE])

slots.sourceAndNotation__sourceLanguage = Slot(uri=TCCM.sourceLanguage, name="sourceAndNotation__sourceLanguage", curie=TCCM.curie('sourceLanguage'),
                      model_uri=TCCM.sourceAndNotation__sourceLanguage, domain=None, range=Optional[Union[dict, OntologyLanguageReference]])

slots.sourceAndNotation__sourceDocumentSyntax = Slot(uri=TCCM.sourceDocumentSyntax, name="sourceAndNotation__sourceDocumentSyntax", curie=TCCM.curie('sourceDocumentSyntax'),
                      model_uri=TCCM.sourceAndNotation__sourceDocumentSyntax, domain=None, range=Optional[Union[dict, OntologySyntaxReference]])

slots.abstractResourceDescription__releaseDocumentation = Slot(uri=TCCM.releaseDocumentation, name="abstractResourceDescription__releaseDocumentation", curie=TCCM.curie('releaseDocumentation'),
                      model_uri=TCCM.abstractResourceDescription__releaseDocumentation, domain=None, range=Optional[str])

slots.abstractResourceDescription__releaseFormat = Slot(uri=TCCM.releaseFormat, name="abstractResourceDescription__releaseFormat", curie=TCCM.curie('releaseFormat'),
                      model_uri=TCCM.abstractResourceDescription__releaseFormat, domain=None, range=List[Union[dict, SourceAndNotation]])

slots.resourceVersionDescription__documentURI = Slot(uri=TCCM.documentURI, name="resourceVersionDescription__documentURI", curie=TCCM.curie('documentURI'),
                      model_uri=TCCM.resourceVersionDescription__documentURI, domain=None, range=Optional[Union[URIorCURIE, DocumentURI]])

slots.resourceVersionDescription__sourceAndNotation = Slot(uri=TCCM.sourceAndNotation, name="resourceVersionDescription__sourceAndNotation", curie=TCCM.curie('sourceAndNotation'),
                      model_uri=TCCM.resourceVersionDescription__sourceAndNotation, domain=None, range=Optional[Union[dict, SourceAndNotation]])

slots.resourceVersionDescription__predecessor = Slot(uri=TCCM.predecessor, name="resourceVersionDescription__predecessor", curie=TCCM.curie('predecessor'),
                      model_uri=TCCM.resourceVersionDescription__predecessor, domain=None, range=Optional[Union[dict, NameAndMeaningReference]])

slots.resourceVersionDescription__officialResourceVersionID = Slot(uri=TCCM.officialResourceVersionID, name="resourceVersionDescription__officialResourceVersionID", curie=TCCM.curie('officialResourceVersionID'),
                      model_uri=TCCM.resourceVersionDescription__officialResourceVersionID, domain=None, range=Optional[str])

slots.resourceVersionDescription__officialReleaseDate = Slot(uri=TCCM.officialReleaseDate, name="resourceVersionDescription__officialReleaseDate", curie=TCCM.curie('officialReleaseDate'),
                      model_uri=TCCM.resourceVersionDescription__officialReleaseDate, domain=None, range=Optional[Union[str, XSDDateTime]])

slots.resourceVersionDescription__officialActivationDate = Slot(uri=TCCM.officialActivationDate, name="resourceVersionDescription__officialActivationDate", curie=TCCM.curie('officialActivationDate'),
                      model_uri=TCCM.resourceVersionDescription__officialActivationDate, domain=None, range=Optional[Union[str, XSDDateTime]])

slots.opaqueData__format = Slot(uri=TCCM.format, name="opaqueData__format", curie=TCCM.curie('format'),
                      model_uri=TCCM.opaqueData__format, domain=None, range=Optional[Union[dict, FormatReference]])

slots.opaqueData__schema = Slot(uri=TCCM.schema, name="opaqueData__schema", curie=TCCM.curie('schema'),
                      model_uri=TCCM.opaqueData__schema, domain=None, range=Optional[Union[URIorCURIE, DocumentURI]])

slots.opaqueData__language = Slot(uri=TCCM.language, name="opaqueData__language", curie=TCCM.curie('language'),
                      model_uri=TCCM.opaqueData__language, domain=None, range=Optional[Union[dict, LanguageReference]])

slots.opaqueData__value = Slot(uri=TCCM.value, name="opaqueData__value", curie=TCCM.curie('value'),
                      model_uri=TCCM.opaqueData__value, domain=None, range=str)
