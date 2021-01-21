# CCDH roadmap for semantics

## Goal 1: get all of the concept schemes used in CCDH CDM into TCCM representation
### Goal 1a: MVP concept schemes (?)
* NCIt
* ICD-O schemes
### Goal 2b: Entire collection


## Goal 2: get proposed *target* concept schemes into TCCM representation
### Goal 2a: MVP concept schemes
* HPO
* MONDO
* (what else)
### Goal 2b: entire set
* SNOMED DICOM Imaging subset

## Goal 3: create code set definitions for CCDH fields
* NCIt should be (mostly) automatic.  ICD-O requires some reverse engineering
* Address missing value reasons
* Address Y/N, Staging and the like

## Goal 4: create CCDH "Ontology" which includes:
* definitions of combinations that aren't in other systems
* ? concept descriptions for 1-1 mappings
* ICD-O OWL representation (?)

The goal of whatever we produce in Goal 4 is to have a formal classifiable description that  
allows us to say that all value meanings that are associated with a particular field (e.g. diagnostic code)  
must be subclasses (instances?) of the meaning associated with the data element (..).

High priority -- get a real example of this in place so that folks can understand what and why in this case.
* a trivial use would be to detect the missing value reasons and explain why they don't fit (Not Asked is not a type of cancer)
* we should also be able to automatically detect the DNA and RNA mappings on analyte type
