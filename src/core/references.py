# Auto generated from references.yaml by pythongen.py version: 0.4.0
# Generation date: 2020-08-14 09:49
# Schema: references
#
# id: https://hotecosystem.org/tccm/references
# description: his diagram identifies all of the value domains that are used within the TCCM service itself. Each
#              reference has a domain, which frequently isn’t necessary to carry through to PSMs with strong type
#              systems, a name that serves as a unique permissible value within the context of the domain, a uri
#              that references the intended meaning of name, and an optional href that, if present, provides a
#              link to a TCCM EntityDescription that provides definitions, descriptions, etc. of the meaning. The
#              NameAndMeaningReference pattern represents, at the meta-level, one of the key purposes for a TCCM
#              based service to establish lists of value domains (identified here by ReferenceType) from which
#              sets of permissible values and meanings can be drawn. For each specific reference below we attempt
#              to identify an ontology or value set from which the set of possible values could be drawn. We then
#              state whether this set is mandatory, meaning that it must be used in a compliant TCCM
#              implementation, recommended, meaning that, while not required, we anticipate that significant gains
#              in interoperability would result were it used, or simply exemplar, meaning that the set carries
#              examples of what might be used.
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
from biolinkml.utils.metamodelcore import Curie, URIorCURIE
from datatypes import CURIE, LocalIdentifier, URIorCurie
from includes.types import String
from uritypes import ExternalURI, LocalURI, PersistentURI, RenderingURI

metamodel_version = "1.5.3"

# Overwrite dataclasses _init_fn to add **kwargs in __init__
dataclasses._init_fn = dataclasses_init_fn_with_kwargs

# Namespaces
TCCM = CurieNamespace('tccm', 'https://hotecosystem.org/tccm/')
DEFAULT_ = TCCM


# Types

# Class references



@dataclass
class NameAndMeaningReference(YAMLRoot):
    """
    A NameAndMeaningReference consists of a local identifier that references a unique meaning within the context of a
    given domain in a TCCM service instance and a globally unique URI that identifies the intended meaning of the
    identifier.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = TCCM.NameAndMeaningReference
    class_class_curie: ClassVar[str] = "tccm:NameAndMeaningReference"
    class_name: ClassVar[str] = "NameAndMeaningReference"
    class_model_uri: ClassVar[URIRef] = TCCM.NameAndMeaningReference

    name: Union[str, LocalIdentifier]
    uri: Optional[Union[str, ExternalURI]] = None
    href: Optional[Union[str, RenderingURI]] = None

    def __post_init__(self, **kwargs: Dict[str, Any]):
        if self.name is None:
            raise ValueError(f"name must be supplied")
        if not isinstance(self.name, LocalIdentifier):
            self.name = LocalIdentifier(self.name)
        if self.uri is not None and not isinstance(self.uri, ExternalURI):
            self.uri = ExternalURI(self.uri)
        if self.href is not None and not isinstance(self.href, RenderingURI):
            self.href = RenderingURI(self.href)
        super().__post_init__(**kwargs)


@dataclass
class AssociationReference(NameAndMeaningReference):
    """
    A name or identifier that uniquely names an association instance in a code system.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = TCCM.AssociationReference
    class_class_curie: ClassVar[str] = "tccm:AssociationReference"
    class_name: ClassVar[str] = "AssociationReference"
    class_model_uri: ClassVar[URIRef] = TCCM.AssociationReference

    name: Union[str, LocalIdentifier] = None

@dataclass
class BindingQualifierReference(NameAndMeaningReference):
    """
    A reference to an entity that describes the role that a given value set binding plays for a concept domain. T
    ypical values represent “overall,” “minimum” or “maximum,” the significance of which can be found in H L7 Version
    3 documentation.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = TCCM.BindingQualifierReference
    class_class_curie: ClassVar[str] = "tccm:BindingQualifierReference"
    class_name: ClassVar[str] = "BindingQualifierReference"
    class_model_uri: ClassVar[URIRef] = TCCM.BindingQualifierReference

    name: Union[str, LocalIdentifier] = None

@dataclass
class CaseSignificanceReference(NameAndMeaningReference):
    """
    A reference to an entity that describes significance of the case in term or designation.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = TCCM.CaseSignificanceReference
    class_class_curie: ClassVar[str] = "tccm:CaseSignificanceReference"
    class_name: ClassVar[str] = "CaseSignificanceReference"
    class_model_uri: ClassVar[URIRef] = TCCM.CaseSignificanceReference

    name: Union[str, LocalIdentifier] = None

@dataclass
class CodeSystemCategoryReference(NameAndMeaningReference):
    """
    A reference to information about a paradigm model used to create an ontology (a.k.a. knowledge representation
    paradigm).
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = TCCM.CodeSystemCategoryReference
    class_class_curie: ClassVar[str] = "tccm:CodeSystemCategoryReference"
    class_name: ClassVar[str] = "CodeSystemCategoryReference"
    class_model_uri: ClassVar[URIRef] = TCCM.CodeSystemCategoryReference

    name: Union[str, LocalIdentifier] = None

@dataclass
class CodeSystemReference(NameAndMeaningReference):
    """
    A reference to a code system or ontology.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = TCCM.CodeSystemReference
    class_class_curie: ClassVar[str] = "tccm:CodeSystemReference"
    class_name: ClassVar[str] = "CodeSystemReference"
    class_model_uri: ClassVar[URIRef] = TCCM.CodeSystemReference

    name: Union[str, LocalIdentifier] = None

@dataclass
class CodeSystemVersionReference(NameAndMeaningReference):
    """
    A reference to a specific version of code system and, if known, the code system which it is a version of.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = TCCM.CodeSystemVersionReference
    class_class_curie: ClassVar[str] = "tccm:CodeSystemVersionReference"
    class_name: ClassVar[str] = "CodeSystemVersionReference"
    class_model_uri: ClassVar[URIRef] = TCCM.CodeSystemVersionReference

    name: Union[str, LocalIdentifier] = None
    codeSystem: Optional[Union[dict, CodeSystemReference]] = None

    def __post_init__(self, **kwargs: Dict[str, Any]):
        if self.codeSystem is not None and not isinstance(self.codeSystem, CodeSystemReference):
            self.codeSystem = CodeSystemReference(**self.codeSystem)
        super().__post_init__(**kwargs)


@dataclass
class ConceptDomainReference(NameAndMeaningReference):
    """
    A reference to a concept domain.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = TCCM.ConceptDomainReference
    class_class_curie: ClassVar[str] = "tccm:ConceptDomainReference"
    class_name: ClassVar[str] = "ConceptDomainReference"
    class_model_uri: ClassVar[URIRef] = TCCM.ConceptDomainReference

    name: Union[str, LocalIdentifier] = None

@dataclass
class ContextReference(NameAndMeaningReference):
    """
    A reference to a realm or context.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = TCCM.ContextReference
    class_class_curie: ClassVar[str] = "tccm:ContextReference"
    class_name: ClassVar[str] = "ContextReference"
    class_model_uri: ClassVar[URIRef] = TCCM.ContextReference

    name: Union[str, LocalIdentifier] = None

@dataclass
class DesignationFidelityReference(NameAndMeaningReference):
    """
    A reference to a description about designation faithfulness or accuracy.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = TCCM.DesignationFidelityReference
    class_class_curie: ClassVar[str] = "tccm:DesignationFidelityReference"
    class_name: ClassVar[str] = "DesignationFidelityReference"
    class_model_uri: ClassVar[URIRef] = TCCM.DesignationFidelityReference

    name: Union[str, LocalIdentifier] = None

@dataclass
class DesignationTypeReference(NameAndMeaningReference):
    """
    A reference to a designation type or form such as “short name,” “abbreviation,” “eponym.”
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = TCCM.DesignationTypeReference
    class_class_curie: ClassVar[str] = "tccm:DesignationTypeReference"
    class_name: ClassVar[str] = "DesignationTypeReference"
    class_model_uri: ClassVar[URIRef] = TCCM.DesignationTypeReference

    name: Union[str, LocalIdentifier] = None

@dataclass
class FormalityLevelReference(NameAndMeaningReference):
    """
    A reference to a description of the relative formality an ontology.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = TCCM.FormalityLevelReference
    class_class_curie: ClassVar[str] = "tccm:FormalityLevelReference"
    class_name: ClassVar[str] = "FormalityLevelReference"
    class_model_uri: ClassVar[URIRef] = TCCM.FormalityLevelReference

    name: Union[str, LocalIdentifier] = None

@dataclass
class FormatReference(NameAndMeaningReference):
    """
    A reference to a particular way that information is encoded for storage or transmission.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = TCCM.FormatReference
    class_class_curie: ClassVar[str] = "tccm:FormatReference"
    class_name: ClassVar[str] = "FormatReference"
    class_model_uri: ClassVar[URIRef] = TCCM.FormatReference

    name: Union[str, LocalIdentifier] = None

@dataclass
class LanguageReference(NameAndMeaningReference):
    """
    A reference to a spoken or written human language.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = TCCM.LanguageReference
    class_class_curie: ClassVar[str] = "tccm:LanguageReference"
    class_name: ClassVar[str] = "LanguageReference"
    class_model_uri: ClassVar[URIRef] = TCCM.LanguageReference

    name: Union[str, LocalIdentifier] = None

@dataclass
class MapCorrelationReference(NameAndMeaningReference):
    """
    A reference to a way that the source and target in a map can be related or assessed.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = TCCM.MapCorrelationReference
    class_class_curie: ClassVar[str] = "tccm:MapCorrelationReference"
    class_name: ClassVar[str] = "MapCorrelationReference"
    class_model_uri: ClassVar[URIRef] = TCCM.MapCorrelationReference

    name: Union[str, LocalIdentifier] = None

@dataclass
class MapReference(NameAndMeaningReference):
    """
    A reference to an abstract map.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = TCCM.MapReference
    class_class_curie: ClassVar[str] = "tccm:MapReference"
    class_name: ClassVar[str] = "MapReference"
    class_model_uri: ClassVar[URIRef] = TCCM.MapReference

    name: Union[str, LocalIdentifier] = None

@dataclass
class MapVersionReference(NameAndMeaningReference):
    """
    A reference to a map version and the corresponding map, if known.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = TCCM.MapVersionReference
    class_class_curie: ClassVar[str] = "tccm:MapVersionReference"
    class_name: ClassVar[str] = "MapVersionReference"
    class_model_uri: ClassVar[URIRef] = TCCM.MapVersionReference

    name: Union[str, LocalIdentifier] = None
    map: Optional[Union[dict, MapReference]] = None

    def __post_init__(self, **kwargs: Dict[str, Any]):
        if self.map is not None and not isinstance(self.map, MapReference):
            self.map = MapReference(**self.map)
        super().__post_init__(**kwargs)


@dataclass
class MatchAlgorithmReference(NameAndMeaningReference):
    """
    A reference to an algorithm used for selecting and filtering data.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = TCCM.MatchAlgorithmReference
    class_class_curie: ClassVar[str] = "tccm:MatchAlgorithmReference"
    class_name: ClassVar[str] = "MatchAlgorithmReference"
    class_model_uri: ClassVar[URIRef] = TCCM.MatchAlgorithmReference

    name: Union[str, LocalIdentifier] = None

@dataclass
class ModelAttributeReference(NameAndMeaningReference):
    """
    A reference to an attribute defined in the CTS2 specification.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = TCCM.ModelAttributeReference
    class_class_curie: ClassVar[str] = "tccm:ModelAttributeReference"
    class_name: ClassVar[str] = "ModelAttributeReference"
    class_model_uri: ClassVar[URIRef] = TCCM.ModelAttributeReference

    name: Union[str, LocalIdentifier] = None

@dataclass
class NamespaceReference(NameAndMeaningReference):
    """
    A reference to a conceptual space that groups identifiers to avoid conflict with items that have the same name but
    different meanings.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = TCCM.NamespaceReference
    class_class_curie: ClassVar[str] = "tccm:NamespaceReference"
    class_name: ClassVar[str] = "NamespaceReference"
    class_model_uri: ClassVar[URIRef] = TCCM.NamespaceReference

    name: Union[str, LocalIdentifier] = None

@dataclass
class OntologyDomainReference(NameAndMeaningReference):
    """
    A reference to a subject domain for an ontology.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = TCCM.OntologyDomainReference
    class_class_curie: ClassVar[str] = "tccm:OntologyDomainReference"
    class_name: ClassVar[str] = "OntologyDomainReference"
    class_model_uri: ClassVar[URIRef] = TCCM.OntologyDomainReference

    name: Union[str, LocalIdentifier] = None

@dataclass
class OntologyEngineeringMethodologyReference(NameAndMeaningReference):
    """
    A reference to a method model that can be used to create an ontology.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = TCCM.OntologyEngineeringMethodologyReference
    class_class_curie: ClassVar[str] = "tccm:OntologyEngineeringMethodologyReference"
    class_name: ClassVar[str] = "OntologyEngineeringMethodologyReference"
    class_model_uri: ClassVar[URIRef] = TCCM.OntologyEngineeringMethodologyReference

    name: Union[str, LocalIdentifier] = None

@dataclass
class OntologyEngineeringToolReference(NameAndMeaningReference):
    """
    A reference to a tool that can be used to create an ontology.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = TCCM.OntologyEngineeringToolReference
    class_class_curie: ClassVar[str] = "tccm:OntologyEngineeringToolReference"
    class_name: ClassVar[str] = "OntologyEngineeringToolReference"
    class_model_uri: ClassVar[URIRef] = TCCM.OntologyEngineeringToolReference

    name: Union[str, LocalIdentifier] = None

@dataclass
class OntologyLanguageReference(NameAndMeaningReference):
    """
    A reference to a language in which an ontology may be implemented.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = TCCM.OntologyLanguageReference
    class_class_curie: ClassVar[str] = "tccm:OntologyLanguageReference"
    class_name: ClassVar[str] = "OntologyLanguageReference"
    class_model_uri: ClassVar[URIRef] = TCCM.OntologyLanguageReference

    name: Union[str, LocalIdentifier] = None

@dataclass
class OntologySyntaxReference(NameAndMeaningReference):
    """
    A reference to a syntax in which an ontology may be represented.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = TCCM.OntologySyntaxReference
    class_class_curie: ClassVar[str] = "tccm:OntologySyntaxReference"
    class_name: ClassVar[str] = "OntologySyntaxReference"
    class_model_uri: ClassVar[URIRef] = TCCM.OntologySyntaxReference

    name: Union[str, LocalIdentifier] = None

@dataclass
class OntologyTaskReference(NameAndMeaningReference):
    """
    A reference to a purpose for which an ontology can be designed.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = TCCM.OntologyTaskReference
    class_class_curie: ClassVar[str] = "tccm:OntologyTaskReference"
    class_name: ClassVar[str] = "OntologyTaskReference"
    class_model_uri: ClassVar[URIRef] = TCCM.OntologyTaskReference

    name: Union[str, LocalIdentifier] = None

@dataclass
class OntologyTypeReference(NameAndMeaningReference):
    """
    A reference to the nature of the content of an ontology.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = TCCM.OntologyTypeReference
    class_class_curie: ClassVar[str] = "tccm:OntologyTypeReference"
    class_name: ClassVar[str] = "OntologyTypeReference"
    class_model_uri: ClassVar[URIRef] = TCCM.OntologyTypeReference

    name: Union[str, LocalIdentifier] = None

@dataclass
class PredicateReference(YAMLRoot):
    """
    An EntityReference that serves the role of predicate. Note that this varies slightly from the base class of
    NameAndMeaningReference because the name attribute is a namespace/name combination rather than a simple name
    scoped exclusively by the domain.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = TCCM.PredicateReference
    class_class_curie: ClassVar[str] = "tccm:PredicateReference"
    class_name: ClassVar[str] = "PredicateReference"
    class_model_uri: ClassVar[URIRef] = TCCM.PredicateReference

    uri: Union[str, ExternalURI]
    name: Curie
    href: Optional[Union[str, RenderingURI]] = None
    designation: Optional[str] = None

    def __post_init__(self, **kwargs: Dict[str, Any]):
        if self.uri is None:
            raise ValueError(f"uri must be supplied")
        if not isinstance(self.uri, ExternalURI):
            self.uri = ExternalURI(self.uri)
        if self.name is None:
            raise ValueError(f"name must be supplied")
        if self.href is not None and not isinstance(self.href, RenderingURI):
            self.href = RenderingURI(self.href)
        super().__post_init__(**kwargs)


@dataclass
class ReasoningAlgorithmReference(NameAndMeaningReference):
    """
    A reference to a formal algorithm for making inferences about an ontology.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = TCCM.ReasoningAlgorithmReference
    class_class_curie: ClassVar[str] = "tccm:ReasoningAlgorithmReference"
    class_name: ClassVar[str] = "ReasoningAlgorithmReference"
    class_model_uri: ClassVar[URIRef] = TCCM.ReasoningAlgorithmReference

    name: Union[str, LocalIdentifier] = None

@dataclass
class RoleReference(NameAndMeaningReference):
    """
    A reference to a role that an individual, organization, or bibliographic reference can play in the construction of
    a resource or resource component.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = TCCM.RoleReference
    class_class_curie: ClassVar[str] = "tccm:RoleReference"
    class_name: ClassVar[str] = "RoleReference"
    class_model_uri: ClassVar[URIRef] = TCCM.RoleReference

    name: Union[str, LocalIdentifier] = None

@dataclass
class SourceAndRoleReference(NameAndMeaningReference):
    """
    A reference to a source that also includes the role that the source played and/or fixes the particular chapter,
    page, or other element within the reference.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = TCCM.SourceAndRoleReference
    class_class_curie: ClassVar[str] = "tccm:SourceAndRoleReference"
    class_name: ClassVar[str] = "SourceAndRoleReference"
    class_model_uri: ClassVar[URIRef] = TCCM.SourceAndRoleReference

    name: Union[str, LocalIdentifier] = None
    role: Optional[Union[dict, RoleReference]] = None

    def __post_init__(self, **kwargs: Dict[str, Any]):
        if self.role is not None and not isinstance(self.role, RoleReference):
            self.role = RoleReference(**self.role)
        super().__post_init__(**kwargs)


@dataclass
class SourceReference(NameAndMeaningReference):
    """
    A reference to an individual, organization of bibliographic reference.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = TCCM.SourceReference
    class_class_curie: ClassVar[str] = "tccm:SourceReference"
    class_name: ClassVar[str] = "SourceReference"
    class_model_uri: ClassVar[URIRef] = TCCM.SourceReference

    name: Union[str, LocalIdentifier] = None

@dataclass
class StatusReference(NameAndMeaningReference):
    """
    A reference to a state in an external ontology authoring workflow.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = TCCM.StatusReference
    class_class_curie: ClassVar[str] = "tccm:StatusReference"
    class_name: ClassVar[str] = "StatusReference"
    class_model_uri: ClassVar[URIRef] = TCCM.StatusReference

    name: Union[str, LocalIdentifier] = None

@dataclass
class ValueSetDefinitionReference(NameAndMeaningReference):
    """
    A reference to a set of rules for constructing a value set along with the corresponding value set if known.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = TCCM.ValueSetDefinitionReference
    class_class_curie: ClassVar[str] = "tccm:ValueSetDefinitionReference"
    class_name: ClassVar[str] = "ValueSetDefinitionReference"
    class_model_uri: ClassVar[URIRef] = TCCM.ValueSetDefinitionReference

    name: Union[str, LocalIdentifier] = None

@dataclass
class ValueSetReference(NameAndMeaningReference):
    """
    A reference to a named set of entity references.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = TCCM.ValueSetReference
    class_class_curie: ClassVar[str] = "tccm:ValueSetReference"
    class_name: ClassVar[str] = "ValueSetReference"
    class_model_uri: ClassVar[URIRef] = TCCM.ValueSetReference

    name: Union[str, LocalIdentifier] = None

@dataclass
class VersionTagReference(NameAndMeaningReference):
    """
    A reference to a tag that can be assigned to versionable resources within the context of a service implementation.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = TCCM.VersionTagReference
    class_class_curie: ClassVar[str] = "tccm:VersionTagReference"
    class_name: ClassVar[str] = "VersionTagReference"
    class_model_uri: ClassVar[URIRef] = TCCM.VersionTagReference

    name: Union[str, LocalIdentifier] = None


# Slots
class slots:
    pass

slots.name = Slot(uri=TCCM.name, name="name", curie=TCCM.curie('name'),
                      model_uri=TCCM.name, domain=None, range=Union[str, LocalIdentifier])

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

slots.NameAndMeaningReference_name = Slot(uri=TCCM.name, name="NameAndMeaningReference_name", curie=TCCM.curie('name'),
                      model_uri=TCCM.NameAndMeaningReference_name, domain=NameAndMeaningReference, range=Union[str, LocalIdentifier])

slots.NameAndMeaningReference_uri = Slot(uri=TCCM.uri, name="NameAndMeaningReference_uri", curie=TCCM.curie('uri'),
                      model_uri=TCCM.NameAndMeaningReference_uri, domain=NameAndMeaningReference, range=Optional[Union[str, ExternalURI]])

slots.NameAndMeaningReference_href = Slot(uri=TCCM.href, name="NameAndMeaningReference_href", curie=TCCM.curie('href'),
                      model_uri=TCCM.NameAndMeaningReference_href, domain=NameAndMeaningReference, range=Optional[Union[str, RenderingURI]])

slots.CodeSystemVersionReference_codeSystem = Slot(uri=TCCM.codeSystem, name="CodeSystemVersionReference_codeSystem", curie=TCCM.curie('codeSystem'),
                      model_uri=TCCM.CodeSystemVersionReference_codeSystem, domain=CodeSystemVersionReference, range=Optional[Union[dict, CodeSystemReference]])

slots.MapVersionReference_map = Slot(uri=TCCM.map, name="MapVersionReference_map", curie=TCCM.curie('map'),
                      model_uri=TCCM.MapVersionReference_map, domain=MapVersionReference, range=Optional[Union[dict, MapReference]])

slots.PredicateReference_uri = Slot(uri=TCCM.uri, name="PredicateReference_uri", curie=TCCM.curie('uri'),
                      model_uri=TCCM.PredicateReference_uri, domain=PredicateReference, range=Union[str, ExternalURI])

slots.PredicateReference_name = Slot(uri=TCCM.name, name="PredicateReference_name", curie=TCCM.curie('name'),
                      model_uri=TCCM.PredicateReference_name, domain=PredicateReference, range=Curie)

slots.PredicateReference_href = Slot(uri=TCCM.href, name="PredicateReference_href", curie=TCCM.curie('href'),
                      model_uri=TCCM.PredicateReference_href, domain=PredicateReference, range=Optional[Union[str, RenderingURI]])

slots.PredicateReference_designation = Slot(uri=TCCM.designation, name="PredicateReference_designation", curie=TCCM.curie('designation'),
                      model_uri=TCCM.PredicateReference_designation, domain=PredicateReference, range=Optional[str])

slots.SourceAndRoleReference_role = Slot(uri=TCCM.role, name="SourceAndRoleReference_role", curie=TCCM.curie('role'),
                      model_uri=TCCM.SourceAndRoleReference_role, domain=SourceAndRoleReference, range=Optional[Union[dict, RoleReference]])
