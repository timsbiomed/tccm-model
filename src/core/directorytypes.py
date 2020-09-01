# Auto generated from directorytypes.yaml by pythongen.py version: 0.4.0
# Generation date: 2020-09-01 13:04
# Schema: directorytypes
#
# id: https://hotecosystem.org/tccm/directorytypes
# description: URI's for various TCCM directories
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
from src.core.uritypes import DirectoryURI, LocalURI
from biolinkml.utils.metamodelcore import URIorCURIE

metamodel_version = "1.5.3"

# Overwrite dataclasses _init_fn to add **kwargs in __init__
dataclasses._init_fn = dataclasses_init_fn_with_kwargs

# Namespaces
TCCM = CurieNamespace('tccm', 'https://hotecosystem.org/tccm/')
XSD = CurieNamespace('xsd', 'http://www.w3.org/2001/XMLSchema#')
DEFAULT_ = TCCM


# Types
class AssociationDirectoryURI(DirectoryURI):
    """ A DirectoryURI that references a set of Associations. """
    type_class_uri = XSD.anyURI
    type_class_curie = "xsd:anyURI"
    type_name = "AssociationDirectoryURI"
    type_model_uri = TCCM.AssociationDirectoryURI


class ChangeSetDirectoryURI(DirectoryURI):
    """ A DirectoryURI that references a set of ChangeSets. """
    type_class_uri = XSD.anyURI
    type_class_curie = "xsd:anyURI"
    type_name = "ChangeSetDirectoryURI"
    type_model_uri = TCCM.ChangeSetDirectoryURI


class CodeSystemCatalogEntryDirectoryURI(DirectoryURI):
    """ A DirectoryURI that references a set of CodeSystemCatalogEntries. """
    type_class_uri = XSD.anyURI
    type_class_curie = "xsd:anyURI"
    type_name = "CodeSystemCatalogEntryDirectoryURI"
    type_model_uri = TCCM.CodeSystemCatalogEntryDirectoryURI


class CodeSystemVersionCatalogEntryDirectoryURI(DirectoryURI):
    """ A DirectoryURI that references a set of CodeSystemVersionCatalogEntries. """
    type_class_uri = XSD.anyURI
    type_class_curie = "xsd:anyURI"
    type_name = "CodeSystemVersionCatalogEntryDirectoryURI"
    type_model_uri = TCCM.CodeSystemVersionCatalogEntryDirectoryURI


class ConceptDomainBindingDirectoryURI(DirectoryURI):
    """ A DirectoryURI that references a set of ConceptDomainBindings. """
    type_class_uri = XSD.anyURI
    type_class_curie = "xsd:anyURI"
    type_name = "ConceptDomainBindingDirectoryURI"
    type_model_uri = TCCM.ConceptDomainBindingDirectoryURI


class ConceptDomainCatalogEntryDirectoryURI(DirectoryURI):
    """ A DirectoryURI that references a set of ConceptDomainCatalogEntries. """
    type_class_uri = XSD.anyURI
    type_class_curie = "xsd:anyURI"
    type_name = "ConceptDomainCatalogEntryDirectoryURI"
    type_model_uri = TCCM.ConceptDomainCatalogEntryDirectoryURI


class EntityDirectoryURI(DirectoryURI):
    """ A DirectoryURI that references a set of EntityDescriptionDirectory. """
    type_class_uri = XSD.anyURI
    type_class_curie = "xsd:anyURI"
    type_name = "EntityDirectoryURI"
    type_model_uri = TCCM.EntityDirectoryURI


class MapCatalogEntryDirectoryURI(DirectoryURI):
    """ A DirectoryURI that references a set of MapCatalogEntries. """
    type_class_uri = XSD.anyURI
    type_class_curie = "xsd:anyURI"
    type_name = "MapCatalogEntryDirectoryURI"
    type_model_uri = TCCM.MapCatalogEntryDirectoryURI


class MapEntryDirectoryURI(DirectoryURI):
    """ A DirectoryURI that references a set of MapEntries. """
    type_class_uri = XSD.anyURI
    type_class_curie = "xsd:anyURI"
    type_name = "MapEntryDirectoryURI"
    type_model_uri = TCCM.MapEntryDirectoryURI


class MapVersionDirectoryURI(DirectoryURI):
    """ A DirectoryURI that references a set of MapVersions. """
    type_class_uri = XSD.anyURI
    type_class_curie = "xsd:anyURI"
    type_name = "MapVersionDirectoryURI"
    type_model_uri = TCCM.MapVersionDirectoryURI


class ResolvedValueSetDirectoryURI(DirectoryURI):
    """ A DirectoryURI that references a set of ValueSetCatalogEntries. """
    type_class_uri = XSD.anyURI
    type_class_curie = "xsd:anyURI"
    type_name = "ResolvedValueSetDirectoryURI"
    type_model_uri = TCCM.ResolvedValueSetDirectoryURI


class StatementDirectoryURI(DirectoryURI):
    """ A DirectoryURI that references a set of Statements. """
    type_class_uri = XSD.anyURI
    type_class_curie = "xsd:anyURI"
    type_name = "StatementDirectoryURI"
    type_model_uri = TCCM.StatementDirectoryURI


class ValueSetCatalogEntryDirectoryURI(DirectoryURI):
    """ A DirectoryURI that references a set of ValueSetCatalogEntries. """
    type_class_uri = XSD.anyURI
    type_class_curie = "xsd:anyURI"
    type_name = "ValueSetCatalogEntryDirectoryURI"
    type_model_uri = TCCM.ValueSetCatalogEntryDirectoryURI


class ValueSetDefinitionDirectoryURI(DirectoryURI):
    """ A DirectoryURI that references a set of ValueSetDefinitions. """
    type_class_uri = XSD.anyURI
    type_class_curie = "xsd:anyURI"
    type_name = "ValueSetDefinitionDirectoryURI"
    type_model_uri = TCCM.ValueSetDefinitionDirectoryURI


# Class references





# Slots
class slots:
    pass


