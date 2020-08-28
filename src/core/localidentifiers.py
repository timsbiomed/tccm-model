# Auto generated from localidentifiers.yaml by pythongen.py version: 0.4.0
# Generation date: 2020-08-27 15:27
# Schema: localidentifiers
#
# id: https://hotecosystem.org/tccm/localidentifiers
# description: This sub clause lists the specific types of local identifiers that are used within the TCCM
#              specification. Instances of each type of local identifier must be unique within the context of the
#              service instance. As an example, “SCT” might uniquely name the SNOMED-CT code system within the
#              context of one service, while another service might use “SMD-CT.” As a consequence, local
#              identifiers can never be used in interchanges between services - URIs must be used instead. Note,
#              also, that it is okay to have the same local identifier for different types of resource. As an
#              example, the identifier “SCT” could be a CodeSystemName for the SNOMED-CT code system and a
#              ValueSetName for the “ Standardized Category Terms” value set.
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
from includes.types import String

metamodel_version = "1.5.3"

# Overwrite dataclasses _init_fn to add **kwargs in __init__
dataclasses._init_fn = dataclasses_init_fn_with_kwargs

# Namespaces
TCCM = CurieNamespace('tccm', 'https://hotecosystem.org/tccm/')
XSD = CurieNamespace('xsd', 'http://www.w3.org/2001/XMLSchema#')
DEFAULT_ = TCCM


# Types
class CodeSystemName(LocalIdentifier):
    """ A local identifier for a CodeSystem. """
    type_class_uri = XSD.string
    type_class_curie = "xsd:string"
    type_name = "CodeSystemName"
    type_model_uri = TCCM.CodeSystemName


class CodeSystemVersionName(LocalIdentifier):
    """ A local identifier for a CodeSystemVersion. """
    type_class_uri = XSD.string
    type_class_curie = "xsd:string"
    type_name = "CodeSystemVersionName"
    type_model_uri = TCCM.CodeSystemVersionName


class ConceptDomainName(LocalIdentifier):
    """ A local identifier for a ConceptDomain. """
    type_class_uri = XSD.string
    type_class_curie = "xsd:string"
    type_name = "ConceptDomainName"
    type_model_uri = TCCM.ConceptDomainName


class MapName(LocalIdentifier):
    """ A local identifier for a Map. """
    type_class_uri = XSD.string
    type_class_curie = "xsd:string"
    type_name = "MapName"
    type_model_uri = TCCM.MapName


class MapVersionName(LocalIdentifier):
    """ A local identifier for a MapVersion. """
    type_class_uri = XSD.string
    type_class_curie = "xsd:string"
    type_name = "MapVersionName"
    type_model_uri = TCCM.MapVersionName


class ValueSetName(LocalIdentifier):
    """ A local identifier for a ValueSet. """
    type_class_uri = XSD.string
    type_class_curie = "xsd:string"
    type_name = "ValueSetName"
    type_model_uri = TCCM.ValueSetName


class VersionTagName(LocalIdentifier):
    """ A local identifier for a VersionTag. """
    type_class_uri = XSD.string
    type_class_curie = "xsd:string"
    type_name = "VersionTagName"
    type_model_uri = TCCM.VersionTagName


# Class references





# Slots
class slots:
    pass


