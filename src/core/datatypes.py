# Auto generated from datatypes.yaml by pythongen.py version: 0.4.0
# Generation date: 2020-08-13 16:16
# Schema: datatypes
#
# id: https://hotecosystem.org/tccm/datatype
# description: Ths module identifies the core data types that are used in the TCCM. The term “data type” refers to
#              “a type whose instances are identified only by their value".
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
from biolinkml.utils.metamodelcore import Curie, NCName, URI, URIorCURIE, XSDDateTime
from includes.types import String

metamodel_version = "1.5.3"

# Overwrite dataclasses _init_fn to add **kwargs in __init__
dataclasses._init_fn = dataclasses_init_fn_with_kwargs

# Namespaces
TCCM = CurieNamespace('tccm', 'https://hotecosystem.org/tccm/')
XSD = CurieNamespace('xsd', 'http://www.w3.org/2001/XMLSchema#')
DEFAULT_ = TCCM


# Types
class DateAndTime(XSDDateTime):
    """ Represents an “Instant” as defined in the OWL Time Specification . Implementations must be able to support temporal units of second, minute, hour, day, month, and year, and be able to represent and compare instances represented in any of these units. DateAndTime can only provide a partial ordering and, as a consequence, i s never used as an index, unique identifier, or to sequence data or events. """
    type_class_uri = XSD.dateTime
    type_class_curie = "xsd:dateTime"
    type_name = "DateAndTime"
    type_model_uri = TCCM.DateAndTime


class NaturalNumber(int):
    """ A non-negative integer (N). NatrualNumber is used exclusively for representing quantities. """
    type_class_uri = XSD.nonNegativeInteger
    type_class_curie = "xsd:nonNegativeInteger"
    type_name = "NaturalNumber"
    type_model_uri = TCCM.NaturalNumber


class LocalIdentifier(String):
    """ An identifier that uniquely references a class, individual, property, or other resource within the context of a specific TCCM service implementation. LocalIdentifier syntax must match the PNAME production as defined in the SPARQL Query Specification . LocalIdentifiers may begin with leading digits, where XML Local Identifiers and NameSpaceIdentifiers may not. """
    type_class_uri = XSD.string
    type_class_curie = "xsd:string"
    type_name = "LocalIdentifier"
    type_model_uri = TCCM.LocalIdentifier


class NamespaceIdentifier(NCName):
    """ An identifier that uniquely references the scoping namespace of an Entity (class, role, or individual) within the context of a TCCM service. NameSpaceIdentifier syntax must match the PNAME NS production as defined in the SPARQL Query Specification - meaning that it must begin with an alphabetic character """
    type_class_uri = XSD.NMTOKEN
    type_class_curie = "xsd:NMTOKEN"
    type_name = "NamespaceIdentifier"
    type_model_uri = TCCM.NamespaceIdentifier


class URI(URI):
    """ A Universal Resource Identifier (URI) as defined in IETF RFC 3986. TCCM implementations are encouraged to consider implementing this data type using the IRI (RFC3987) specification """
    type_class_uri = XSD.anyURI
    type_class_curie = "xsd:anyURI"
    type_name = "URI"
    type_model_uri = TCCM.URI


class CURIE(Curie):
    type_class_uri = XSD.anyURI
    type_class_curie = "xsd:anyURI"
    type_name = "CURIE"
    type_model_uri = TCCM.CURIE


class URIorCurie(URIorCURIE):
    """ a URI or a CURIE """
    type_class_uri = XSD.anyURI
    type_class_curie = "xsd:anyURI"
    type_name = "URIorCurie"
    type_model_uri = TCCM.URIorCurie


# Class references





# Slots
class slots:
    pass


