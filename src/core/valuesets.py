# Auto generated from valuesets.yaml by pythongen.py version: 0.4.0
# Generation date: 2020-08-14 09:49
# Schema: ValueSets
#
# id: https://hotecosystem.org/tccm/ValueSets
# description: Terminology Core Common Model Value Sets
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
from biolinkml.utils.metamodelcore import URIorCURIE
from datatypes import URIorCurie

metamodel_version = "1.5.3"

# Overwrite dataclasses _init_fn to add **kwargs in __init__
dataclasses._init_fn = dataclasses_init_fn_with_kwargs

# Namespaces
TCCM = CurieNamespace('tccm', 'https://hotecosystem.org/tccm/')
XSD = CurieNamespace('xsd', 'http://www.w3.org/2001/XMLSchema#')
DEFAULT_ = TCCM


# Types
class ValueSet(URIorCurie):
    """ A URI that can be indirectly resolved to a set of entity descriptions """
    type_class_uri = XSD.anyURI
    type_class_curie = "xsd:anyURI"
    type_name = "ValueSet"
    type_model_uri = TCCM.ValueSet


class ASSOCIATION(ValueSet):
    """ A formal “semantic” assertion about a named entity, in the form of subject, predicate, and object including any provenance, qualifiers, or internal BNODEs. """
    type_class_uri = XSD.anyURI
    type_class_curie = "xsd:anyURI"
    type_name = "ASSOCIATION"
    type_model_uri = TCCM.ASSOCIATION


class BINDINGQUALIFIER(ValueSet):
    """ An assertion about the semantics of a concept domain / value set binding. This model element exists specifically to address section 2.4.2.23 of the HL7 SFM14, which needs a qualifier that indicates whether the binding is “overall,” “minimal,” or “maximum.”
The TCCM specification does not formally define the semantics of the various possible BINDING_QUALIFIER elements: it is up to specific implementations and service clients to interpret the meaning of the specific binding qualifiers that may be represented in references of this type. """
    type_class_uri = XSD.anyURI
    type_class_curie = "xsd:anyURI"
    type_name = "BINDING_QUALIFIER"
    type_model_uri = TCCM.BINDINGQUALIFIER


class CASESIGNIFICANCE(ValueSet):
    """ Identifies the significance of case in a term or designation. """
    type_class_uri = XSD.anyURI
    type_class_curie = "xsd:anyURI"
    type_name = "CASE_SIGNIFICANCE"
    type_model_uri = TCCM.CASESIGNIFICANCE


class CODESYSTEMCATEGORY(ValueSet):
    """ The general category of a code system (flat list, subject heading system, taxonomy, thesaurus, classification, terminology, description logic ontology, first order predicate logic, etc.) (same as KnowledgeRepresentationParadigm: OMV 5.8). """
    type_class_uri = XSD.anyURI
    type_class_curie = "xsd:anyURI"
    type_name = "CODE_SYSTEM_CATEGORY"
    type_model_uri = TCCM.CODESYSTEMCATEGORY


class CODESYSTEM(ValueSet):
    """ A collection of metadata about the provenance, use, and distribution of a code system or ontology. """
    type_class_uri = XSD.anyURI
    type_class_curie = "xsd:anyURI"
    type_name = "CODE_SYSTEM"
    type_model_uri = TCCM.CODESYSTEM


class CODESYSTEMVERSION(ValueSet):
    """ A collection of metadata about content and distribution format of a particular version or release of a code system. """
    type_class_uri = XSD.anyURI
    type_class_curie = "xsd:anyURI"
    type_name = "CODE_SYSTEM_VERSION"
    type_model_uri = TCCM.CODESYSTEMVERSION


class CONCEPTDOMAIN(ValueSet):
    """ The description of the conceptual domain of a field in a message, column in a database, field on a form, etc. Equivalent to the ISO 11179-3 “Data Element Concept.” """
    type_class_uri = XSD.anyURI
    type_class_curie = "xsd:anyURI"
    type_name = "CONCEPT_DOMAIN"
    type_model_uri = TCCM.CONCEPTDOMAIN


class CONTEXT(ValueSet):
    """ External and environmental factors that serve to discriminate among multiple possible selections. While it is assumed that the specific contexts referenced by CONTEXT are represented by entity descriptions contained in some ontology or coding scheme, the CTS2 specification does not recommend any targets. Note, however, the TCCM context is intended to represent the notion of “jurisdictional domain” or “realm” as described in the HL7 CTS2 SFM . """
    type_class_uri = XSD.anyURI
    type_class_curie = "xsd:anyURI"
    type_name = "CONTEXT"
    type_model_uri = TCCM.CONTEXT


class DESIGNATIONFIDELITY(ValueSet):
    """ Identifies how well a particular designation represents the intended meaning of the referenced entity. TCCM implementations may consider using the SKOS16 semantic relations to represent this relationship. """
    type_class_uri = XSD.anyURI
    type_class_curie = "xsd:anyURI"
    type_name = "DESIGNATION_FIDELITY"
    type_model_uri = TCCM.DESIGNATIONFIDELITY


class DESIGNATIONTYPE(ValueSet):
    """ The particular form or type of a given designation: can be “short name,” “long name,” “abbreviation,” “eponym.” """
    type_class_uri = XSD.anyURI
    type_class_curie = "xsd:anyURI"
    type_name = "DESIGNATION_TYPE"
    type_model_uri = TCCM.DESIGNATIONTYPE


class FORMALITYLEVEL(ValueSet):
    """ The level of formality of an ontology (OMV 5.9). """
    type_class_uri = XSD.anyURI
    type_class_curie = "xsd:anyURI"
    type_name = "FORMALITY_LEVEL"
    type_model_uri = TCCM.FORMALITYLEVEL


class FORMAT(ValueSet):
    """ A particular way that information is encoded for storage in a computer file """
    type_class_uri = XSD.anyURI
    type_class_curie = "xsd:anyURI"
    type_name = "FORMAT"
    type_model_uri = TCCM.FORMAT


class LANGUAGE(ValueSet):
    """ A spoken or written language intended for human consumption. """
    type_class_uri = XSD.anyURI
    type_class_curie = "xsd:anyURI"
    type_name = "LANGUAGE"
    type_model_uri = TCCM.LANGUAGE


class MATCHALGORITHM(ValueSet):
    """ A predicate that determines whether an entity resource qualities for membership in a set based on supplied matching criteria. """
    type_class_uri = XSD.anyURI
    type_class_curie = "xsd:anyURI"
    type_name = "MATCH_ALGORITHM"
    type_model_uri = TCCM.MATCHALGORITHM


class MAP(ValueSet):
    """ A set of rules that associate a set of entity references from one domain into those in another. """
    type_class_uri = XSD.anyURI
    type_class_curie = "xsd:anyURI"
    type_name = "MAP"
    type_model_uri = TCCM.MAP


class MAPCORRELATION(ValueSet):
    """ An assertion about the strength or significance of a specific rule in a Map. """
    type_class_uri = XSD.anyURI
    type_class_curie = "xsd:anyURI"
    type_name = "MAP_CORRELATION"
    type_model_uri = TCCM.MAPCORRELATION


class MAPVERSION(ValueSet):
    """ The state of a Map at a given point in time. """
    type_class_uri = XSD.anyURI
    type_class_curie = "xsd:anyURI"
    type_name = "MAP_VERSION"
    type_model_uri = TCCM.MAPVERSION


class MODELATTRIBUTE(ValueSet):
    """ An attribute defined in CTS2 information model. """
    type_class_uri = XSD.anyURI
    type_class_curie = "xsd:anyURI"
    type_name = "MODEL_ATTRIBUTE"
    type_model_uri = TCCM.MODELATTRIBUTE


class NAMESPACE(ValueSet):
    """ A reference to a conceptual space that groups identifiers to avoid conflict with items that have the same name but different meanings. """
    type_class_uri = XSD.anyURI
    type_class_curie = "xsd:anyURI"
    type_name = "NAMESPACE"
    type_model_uri = TCCM.NAMESPACE


class ONTOLOGYENGINEERINGMETHODOLOGY(ValueSet):
    """ Information about the ontology engineering methodology (OMV 5.4) (sic). """
    type_class_uri = XSD.anyURI
    type_class_curie = "xsd:anyURI"
    type_name = "ONTOLOGY_ENGINEERING_METHODOLOGY"
    type_model_uri = TCCM.ONTOLOGYENGINEERINGMETHODOLOGY


class ONTOLOGYENGINEERINGTOOL(ValueSet):
    """ A tool used to create the ontology (OMV 5.5). """
    type_class_uri = XSD.anyURI
    type_class_curie = "xsd:anyURI"
    type_name = "ONTOLOGY_ENGINEERING_TOOL"
    type_model_uri = TCCM.ONTOLOGYENGINEERINGTOOL


class ONTOLOGYDOMAIN(ValueSet):
    """ While the domain can refer to any topic ontology it is advised to use one of the established general purpose topic hierarchy like DMOZ or domain specific topic like ACM for the computer science domain. Only this way it can be ensured that meaningful information about the relation of the domains of two separate ontologies can be deduced (OMV 5.1 1)(sic). """
    type_class_uri = XSD.anyURI
    type_class_curie = "xsd:anyURI"
    type_name = "ONTOLOGY_DOMAIN"
    type_model_uri = TCCM.ONTOLOGYDOMAIN


class ONTOLOGYLANGUAGE(ValueSet):
    """ Information about the language in which the ontology is implemented (OMV 5.7). """
    type_class_uri = XSD.anyURI
    type_class_curie = "xsd:anyURI"
    type_name = "ONTOLOGY_LANGUAGE"
    type_model_uri = TCCM.ONTOLOGYLANGUAGE


class ONTOLOGYSYNTAX(ValueSet):
    """ Information about the syntax used by an ontology (OMV 5.6). """
    type_class_uri = XSD.anyURI
    type_class_curie = "xsd:anyURI"
    type_name = "ONTOLOGY_SYNTAX"
    type_model_uri = TCCM.ONTOLOGYSYNTAX


class ONTOLOGYTASK(ValueSet):
    """ Information about the task the ontology was intended to be used for (OMV 5.10). """
    type_class_uri = XSD.anyURI
    type_class_curie = "xsd:anyURI"
    type_name = "ONTOLOGY_TASK"
    type_model_uri = TCCM.ONTOLOGYTASK


class ONTOLOGYTYPE(ValueSet):
    """ Categorizes ontologies (OMV 5.2). """
    type_class_uri = XSD.anyURI
    type_class_curie = "xsd:anyURI"
    type_name = "ONTOLOGY_TYPE"
    type_model_uri = TCCM.ONTOLOGYTYPE


class PREDICATE(ValueSet):
    """ A property or relation between entities. """
    type_class_uri = XSD.anyURI
    type_class_curie = "xsd:anyURI"
    type_name = "PREDICATE"
    type_model_uri = TCCM.PREDICATE


class REASONINGALGORITHM(ValueSet):
    """ A set of formal rules that allow the deduction of additional assertions from a supplied list of axioms. """
    type_class_uri = XSD.anyURI
    type_class_curie = "xsd:anyURI"
    type_name = "REASONING_ALGORITHM"
    type_model_uri = TCCM.REASONINGALGORITHM


class RESOURCETYPE(ValueSet):
    """ A class of which a referencing resource is an instance of. """
    type_class_uri = XSD.anyURI
    type_class_curie = "xsd:anyURI"
    type_name = "RESOURCE TYPE"
    type_model_uri = TCCM.RESOURCETYPE


class ROLE(ValueSet):
    """ A role that a SOURCE can play in the construction or dissemination of a terminological resource. """
    type_class_uri = XSD.anyURI
    type_class_curie = "xsd:anyURI"
    type_name = "ROLE"
    type_model_uri = TCCM.ROLE


class SOURCE(ValueSet):
    """ An individual, organization, or bibliographic reference. """
    type_class_uri = XSD.anyURI
    type_class_curie = "xsd:anyURI"
    type_name = "SOURCE"
    type_model_uri = TCCM.SOURCE


class STATEMENT(ValueSet):
    """ An atomic assertion about a CTS2 resource. """
    type_class_uri = XSD.anyURI
    type_class_curie = "xsd:anyURI"
    type_name = "STATEMENT"
    type_model_uri = TCCM.STATEMENT


class STATUS(ValueSet):
    """ The state of a resource or other entry in an external workflow. """
    type_class_uri = XSD.anyURI
    type_class_curie = "xsd:anyURI"
    type_name = "STATUS"
    type_model_uri = TCCM.STATUS


class VALUESET(ValueSet):
    """ A set of entity references. """
    type_class_uri = XSD.anyURI
    type_class_curie = "xsd:anyURI"
    type_name = "VALUE_SET"
    type_model_uri = TCCM.VALUESET


class VALUESETDEFINITION(ValueSet):
    """ A set of rules that can be applied to specified versions or one or more code systems to yield a set of entity references. """
    type_class_uri = XSD.anyURI
    type_class_curie = "xsd:anyURI"
    type_name = "VALUE_SET_DEFINITION"
    type_model_uri = TCCM.VALUESETDEFINITION


class VERSIONTAG(ValueSet):
    """ An identifier that can be assigned to resource versions by a service implementation to identify their state in the service workflow. Examples might include “development,” “test,” “production,” etc. """
    type_class_uri = XSD.anyURI
    type_class_curie = "xsd:anyURI"
    type_name = "VERSION_TAG"
    type_model_uri = TCCM.VERSIONTAG


# Class references





# Slots
class slots:
    pass


