# TCCM Minimal Components
The goal of TCCM is to be a code set catalog -- a minimal set of information
in a common format and a collection of links to get more information.  TCCM
will also serve as the base of a code set (aka. value set) service, where
performance is at a premium.

TCCM will, by necessity, assemble its data from outside (ideally definitive)
sources.  A submission to TCCM must include a tool that can
1. Determine whether the information in the current TCCM repository is current
2. If necessary, update the TCCM repository with the latest information from the source
3. Support pretty much any ontology / classification system / concept scheme that one
   may encounter on the web.
4. Access service will be based on the TCCM Code Set specification
   * All concepts in TCCM Co


## domain: skos:Concept
* skos:prefLabel
* skos:definition
* skos:notation
* skos:seeAlso
* skos:broader
* skos:inScheme

## domain: skos:ConceptScheme
* (label)
* (description)
* (prefix curie)
* skos:topConcept

## CS namespace
* Code system of code systems
* Source information comes from prefixcommons, prefix.cc, OLS, identifiers.org, ...
  * There are several efforts underway to harmonize the above -- maybe we just "hitch our wagon" to one of them?
* Need a loader, maintenance and (ideally) a suggestion system that produces TCCM ConceptSchemes and (?)  
  updates the TCCM CS Scheme.


## Future items
* skosxl:prefLabel -- for multilingual labels
* ? -- for multilingual definitions (See Tom Baker thread)
* (deprecated)
* (replaced by)

## Future Items
