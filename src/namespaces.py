from enum import Enum
from typing import Optional, List, Dict, Mapping, Union

from biolinkml.utils.metamodelcore import URIorCURIE
from rdflib import Namespace, URIRef

from src.tccm import PersistentURI, RenderingURI


# There is aso some work on this in the act_to_rdf model
namespaces = {
    'ACT': Namespace('https://ncatswiki.dbmi.pitt.edu/acts/ACT/'),
    'CPT4': Namespace('http://www.ama-assn.org/go/cpt#'),
    'HCPCS': Namespace('http://purl.bioontology.org/ontology/HCPCS/'),
    'ICD10CM': Namespace('http://hl7.org/fhir/sid/icd-10-cm#'),
    'ICD10PCS': Namespace('http://purl.bioontology.org/ontology/ICD10PCS/'),
    'ICD9CM': Namespace('http://purl.bioontology.org/ontology/ICD9CM/'),
    'RXNORM': Namespace('http://www.nlm.nih.gov/research/umls/rxnorm/'),
    'NDC': Namespace('https://identifiers.org/ndc:'),
    'NUI': Namespace('http://example.org/NUI/'),
    'ICD9PROC': Namespace('http://example.org/ICD9PROC/'),
    'LOINC': Namespace('http://purl.bioontology.org/ontology/LNC/'),
    'OWL': OWL,
    'SKOS': SKOS,
    'iso-11179': Namespace("http://www.iso.org/11179/")
}
ISO = namespaces['iso-11179']
ACT = namespaces['ACT']


def namespace_for(prefix: str) -> Optional[Namespace]:
    """
    Return the URI(s) associated with
    :param prefix: Prefix to look up
    :return: Namespace for URI if any
    """
    return None


def namespace_map(prefixes: Optional[List[str]], default_namespace: Optional[Namespace] = None) \
        -> Mapping[str, Namespace]:
    """
    Return a map from the supplied prefixes to corresponding namespace
    :param prefixes: list of prefixes to map.  If absent return all known maps
    :return: map for supplied list
    """
    return {prefix: default_namespace for prefix in prefixes}


class KnownService(Enum):
    CTS2 = 1
    FHIR = 2
    BioPortal = 3
    GenericSKOS = 4


def service_namespace(uri: Union[PersistentURI, str], serviceModel: List[Union[KnownService, PersistentURI]]) \
        -> Optional[str]:
    """
    Return the appropriate service URI to access URI
    :param uri: Either a URI or a namespace identifier
    :param serviceModel: Known service identifier or known Mime type or other service name
    :return: template for generating local URI
    """
    return None


def service_uri(resource: Union[URIorCURIE,List[URIorCURIE]], serviceModel: List[Union[KnownService, PersistentURI]]) \
        -> Mapping[URIorCURIE, Optional[RenderingURI]]:
    """
    Return the appropriate service URIs for the supplied URIorCURIE list
    :param resource: lookup list
    :param serviceModel: Prioritized service models in order (sort of conneg)
    :return:
    """
    return {r: None for r in (resource if isinstance(resource, list) else [resource])}
