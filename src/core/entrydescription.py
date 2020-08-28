# Auto generated from entrydescription.yaml by pythongen.py version: 0.4.0
# Generation date: 2020-08-27 15:27
# Schema: entrydescription
#
# id: https://hotecosystem.org/tccm/entrydescription
# description:
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
from src.core.references import CodeSystemReference, CodeSystemReferenceName, FormatReference, FormatReferenceName, LanguageReference, LanguageReferenceName, MapReference, MapReferenceName, RoleReference, RoleReferenceName
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
class OpaqueData(YAMLRoot):
    """
    Opaque data is the equivalent of an ASN.1 External Type or the XML Schema anyType . An OpaqueData instance
    may represent text with an optional spoken or written language code or a formal structure such as embedded HTML,
    XML, or MIME encoded data. When a formal structure is included, its type should be specified in the format
    attribute and, when the type is an XML variant, the corresponding schema (or DTD) should be included in the
    schema parameter.

    The OpaqueData data type must be encoded in such a way that the content can be represented by a character string.
    Binary data is not permitted, although hyperlinks to binary data are.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = TCCM.OpaqueData
    class_class_curie: ClassVar[str] = "tccm:OpaqueData"
    class_name: ClassVar[str] = "OpaqueData"
    class_model_uri: ClassVar[URIRef] = TCCM.OpaqueData

    value: str
    format: Optional[Union[dict, FormatReference]] = None
    schema: Optional[Union[URIorCURIE, DocumentURI]] = None
    language: Optional[Union[dict, LanguageReference]] = None

    def __post_init__(self, **kwargs: Dict[str, Any]):
        if self.format is not None and not isinstance(self.format, FormatReference):
            self.format = FormatReference(self.format)
        if self.schema is not None and not isinstance(self.schema, DocumentURI):
            self.schema = DocumentURI(self.schema)
        if self.language is not None and not isinstance(self.language, LanguageReference):
            self.language = LanguageReference(self.language)
        if self.value is None:
            raise ValueError(f"value must be supplied")
        super().__post_init__(**kwargs)


@dataclass
class EntryDescription(OpaqueData):
    """
    EntryDescription is a subclass of OpaqueData. The purpose behind this is that there are certain textual fields
    that some CTS2 service implementations may want to constrain. As an example, Designation text is of type
    EntryDescription, but implementations may want to restrict the OpaqueData value attribute to a simple string
    rather than xs: anyType. When OpaqueData appears directly as a model element, implementations must be able to
    support the full OpaqueData model. EntryDescription, however, may be constrained by implementations or
    specialized PSM.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = TCCM.EntryDescription
    class_class_curie: ClassVar[str] = "tccm:EntryDescription"
    class_name: ClassVar[str] = "EntryDescription"
    class_model_uri: ClassVar[URIRef] = TCCM.EntryDescription

    value: str = None


# Slots
class slots:
    pass

slots.format = Slot(uri=TCCM.format, name="format", curie=TCCM.curie('format'),
                      model_uri=TCCM.format, domain=None, range=Optional[Union[dict, FormatReference]])

slots.schema = Slot(uri=TCCM.schema, name="schema", curie=TCCM.curie('schema'),
                      model_uri=TCCM.schema, domain=None, range=Optional[Union[URIorCURIE, DocumentURI]])

slots.language = Slot(uri=TCCM.language, name="language", curie=TCCM.curie('language'),
                      model_uri=TCCM.language, domain=None, range=Optional[Union[dict, LanguageReference]])

slots.value = Slot(uri=TCCM.value, name="value", curie=TCCM.curie('value'),
                      model_uri=TCCM.value, domain=None, range=str)

slots.name = Slot(uri=TCCM.name, name="name", curie=TCCM.curie('name'),
                      model_uri=TCCM.name, domain=None, range=URIRef)

slots.synopsis = Slot(uri=TCCM.synopsis, name="synopsis", curie=TCCM.curie('synopsis'),
                      model_uri=TCCM.synopsis, domain=None, range=Optional[str])

slots.uri = Slot(uri=TCCM.uri, name="uri", curie=TCCM.curie('uri'),
                      model_uri=TCCM.uri, domain=None, range=Optional[Union[URIorCURIE, ExternalURI]])

slots.href = Slot(uri=TCCM.href, name="href", curie=TCCM.curie('href'),
                      model_uri=TCCM.href, domain=None, range=Optional[Union[URIorCURIE, RenderingURI]])

slots.codeSystem = Slot(uri=TCCM.codeSystem, name="codeSystem", curie=TCCM.curie('codeSystem'),
                      model_uri=TCCM.codeSystem, domain=None, range=Optional[Union[dict, CodeSystemReference]])

slots.map = Slot(uri=TCCM.map, name="map", curie=TCCM.curie('map'),
                      model_uri=TCCM.map, domain=None, range=Optional[Union[dict, MapReference]])

slots.designation = Slot(uri=TCCM.designation, name="designation", curie=TCCM.curie('designation'),
                      model_uri=TCCM.designation, domain=None, range=Optional[str])

slots.role = Slot(uri=TCCM.role, name="role", curie=TCCM.curie('role'),
                      model_uri=TCCM.role, domain=None, range=Optional[Union[dict, RoleReference]])

slots.OpaqueData_format = Slot(uri=TCCM.format, name="OpaqueData_format", curie=TCCM.curie('format'),
                      model_uri=TCCM.OpaqueData_format, domain=OpaqueData, range=Optional[Union[dict, FormatReference]])

slots.OpaqueData_schema = Slot(uri=TCCM.schema, name="OpaqueData_schema", curie=TCCM.curie('schema'),
                      model_uri=TCCM.OpaqueData_schema, domain=OpaqueData, range=Optional[Union[URIorCURIE, DocumentURI]])

slots.OpaqueData_language = Slot(uri=TCCM.language, name="OpaqueData_language", curie=TCCM.curie('language'),
                      model_uri=TCCM.OpaqueData_language, domain=OpaqueData, range=Optional[Union[dict, LanguageReference]])

slots.OpaqueData_value = Slot(uri=TCCM.value, name="OpaqueData_value", curie=TCCM.curie('value'),
                      model_uri=TCCM.OpaqueData_value, domain=OpaqueData, range=str)
