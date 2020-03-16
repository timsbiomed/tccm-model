# Auto generated from tccm.yaml by pythongen.py version: 0.4.0
# Generation date: 2020-03-16 09:06
# Schema: tccm
#
# id: https://hotecosystem.org/tccm
# description: Terminology Core Common Model
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
from biolinkml.utils.metamodelcore import URI, URIorCURIE, XSDDateTime

metamodel_version = "1.4.3"

# Overwrite dataclasses _init_fn to add **kwargs in __init__
dataclasses._init_fn = dataclasses_init_fn_with_kwargs

# Namespaces
TCCM = CurieNamespace('tccm', 'https://hotecosystem.org/tccm')
XSD = CurieNamespace('xsd', 'http://www.w3.org/2001/XMLSchema#')
DEFAULT_ = TCCM


# Types
class String(str):
    """ A character string """
    type_class_uri = XSD.string
    type_class_curie = "xsd:string"
    type_name = "string"
    type_model_uri = TCCM.String


class Datetime(XSDDateTime):
    """ The combination of a date and time """
    type_class_uri = XSD.dateTime
    type_class_curie = "xsd:dateTime"
    type_name = "datetime"
    type_model_uri = TCCM.Datetime


class NaturalNumber(int):
    """ An integer """
    type_class_uri = XSD.nonNegativeInteger
    type_class_curie = "xsd:nonNegativeInteger"
    type_name = "naturalNumber"
    type_model_uri = TCCM.NaturalNumber


class LocalIdentifier(String):
    """ An identifier that uniquely references a class, individual, property, or other resource """
    type_class_uri = XSD.string
    type_class_curie = "xsd:string"
    type_name = "localIdentifier"
    type_model_uri = TCCM.LocalIdentifier


class NamespaceIdentifier(str):
    """ An identifier that uniquely references the scoping namespace of an Entity (class, role, or individual) """
    type_class_uri = XSD.NMTOKEN
    type_class_curie = "xsd:NMTOKEN"
    type_name = "namespaceIdentifier"
    type_model_uri = TCCM.NamespaceIdentifier


class Uri(URI):
    """ A Universal Resource Identifier (URI) as defined in IETF RFC 3986 """
    type_class_uri = XSD.anyURI
    type_class_curie = "xsd:anyURI"
    type_name = "uri"
    type_model_uri = TCCM.Uri


class Uriorcurie(URIorCURIE):
    """ a URI or a CURIE """
    type_class_uri = XSD.anyURI
    type_class_curie = "xsd:anyURI"
    type_name = "uriorcurie"
    type_model_uri = TCCM.Uriorcurie


class DesignationRole(String):
    type_class_uri = XSD.string
    type_class_curie = "xsd:string"
    type_name = "designationRole"
    type_model_uri = TCCM.DesignationRole


class PersistentURI(Uriorcurie):
    type_class_uri = XSD.anyURI
    type_class_curie = "xsd:anyURI"
    type_name = "persistentURI"
    type_model_uri = TCCM.PersistentURI


class LocalURI(Uriorcurie):
    type_class_uri = XSD.anyURI
    type_class_curie = "xsd:anyURI"
    type_name = "localURI"
    type_model_uri = TCCM.LocalURI


class ChangeSetURI(PersistentURI):
    type_class_uri = XSD.anyURI
    type_class_curie = "xsd:anyURI"
    type_name = "changeSetURI"
    type_model_uri = TCCM.ChangeSetURI


class DocumentURI(PersistentURI):
    type_class_uri = XSD.anyURI
    type_class_curie = "xsd:anyURI"
    type_name = "documentURI"
    type_model_uri = TCCM.DocumentURI


class ExternalURI(PersistentURI):
    type_class_uri = XSD.anyURI
    type_class_curie = "xsd:anyURI"
    type_name = "externalURI"
    type_model_uri = TCCM.ExternalURI


class ServiceURI(LocalURI):
    type_class_uri = XSD.anyURI
    type_class_curie = "xsd:anyURI"
    type_name = "serviceURI"
    type_model_uri = TCCM.ServiceURI


class RenderingURI(LocalURI):
    type_class_uri = XSD.anyURI
    type_class_curie = "xsd:anyURI"
    type_name = "renderingURI"
    type_model_uri = TCCM.RenderingURI


class DirectoryURI(LocalURI):
    type_class_uri = XSD.anyURI
    type_class_curie = "xsd:anyURI"
    type_name = "directoryURI"
    type_model_uri = TCCM.DirectoryURI


# Class references



@dataclass
class OpaqueData(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = TCCM.OpaqueData
    class_class_curie: ClassVar[str] = "tccm:OpaqueData"
    class_name: ClassVar[str] = "opaqueData"
    class_model_uri: ClassVar[URIRef] = TCCM.OpaqueData

    value: str
    language: Optional[str] = None

    def __post_init__(self, **kwargs: Dict[str, Any]):
        if self.value is None:
            raise ValueError(f"value must be supplied")
        super().__post_init__(**kwargs)


@dataclass
class NameAndMeaningReference(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = TCCM.NameAndMeaningReference
    class_class_curie: ClassVar[str] = "tccm:NameAndMeaningReference"
    class_name: ClassVar[str] = "nameAndMeaningReference"
    class_model_uri: ClassVar[URIRef] = TCCM.NameAndMeaningReference

    name: str
    uri: Optional[Union[str, ExternalURI]] = None
    href: Optional[Union[str, RenderingURI]] = None

    def __post_init__(self, **kwargs: Dict[str, Any]):
        if self.name is None:
            raise ValueError(f"name must be supplied")
        if self.uri is not None and not isinstance(self.uri, ExternalURI):
            self.uri = ExternalURI(self.uri)
        if self.href is not None and not isinstance(self.href, RenderingURI):
            self.href = RenderingURI(self.href)
        super().__post_init__(**kwargs)


@dataclass
class EntityReference(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = TCCM.EntityReference
    class_class_curie: ClassVar[str] = "tccm:EntityReference"
    class_name: ClassVar[str] = "entityReference"
    class_model_uri: ClassVar[URIRef] = TCCM.EntityReference

    about: Union[str, PersistentURI]
    code: Optional[str] = None
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

slots.language = Slot(uri=TCCM.language, name="language", curie=TCCM.curie('language'),
                      model_uri=TCCM.language, domain=OpaqueData, range=Optional[str])

slots.value = Slot(uri=TCCM.value, name="value", curie=TCCM.curie('value'),
                      model_uri=TCCM.value, domain=OpaqueData, range=str)

slots.name = Slot(uri=TCCM.name, name="name", curie=TCCM.curie('name'),
                      model_uri=TCCM.name, domain=NameAndMeaningReference, range=str)

slots.uri = Slot(uri=TCCM.uri, name="uri", curie=TCCM.curie('uri'),
                      model_uri=TCCM.uri, domain=NameAndMeaningReference, range=Optional[Union[str, ExternalURI]])

slots.href = Slot(uri=TCCM.href, name="href", curie=TCCM.curie('href'),
                      model_uri=TCCM.href, domain=None, range=Optional[Union[str, RenderingURI]])

slots.meaningHref = Slot(uri=TCCM.href, name="meaningHref", curie=TCCM.curie('href'),
                      model_uri=TCCM.meaningHref, domain=None, range=Optional[Union[str, RenderingURI]])

slots.about = Slot(uri=TCCM.about, name="about", curie=TCCM.curie('about'),
                      model_uri=TCCM.about, domain=EntityReference, range=Union[str, PersistentURI])

slots.code = Slot(uri=TCCM.code, name="code", curie=TCCM.curie('code'),
                      model_uri=TCCM.code, domain=EntityReference, range=Optional[str])
