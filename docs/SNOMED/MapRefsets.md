# Mapping in the SNOMED world

The SNOMED community maintains two types of map files:
1) The Simple Map Refset - is used to maintain 1:1, exact maps.  The primary purpose of this file is (or was) to maintain
external identifiers for terminologies that were absorbed into SNOMED itself.
2) The Complex Map Refset - this can be used to represent true "maps", where:
   * The mapping is often not exact and the "meaning" or range of a target concept may not be exactly the same as the source SNOMED CT
   code
   * The mapping can be 1:n from SNOMED to targets, with the assumption that each target plays a separate rule as exemplified
   by the ICD star and dagger rules
   * The mapping can (in a limited sense) n:m, the assumption being that the mapping tool has a context specific set of
   type/value tuples at its disposal (e.g. patient gender, age, causes, etc.) at its disposal that can be referenced by a mapping
   rule.  (See: https://confluence.ihtsdotools.org/display/DOCICD10/ICD-10+Mapping+Technical+Guide for examples and details)
   


## SNOMED RF2 Simple Map Refset (SM Refset)
The SNOMED Release Format 2 (RF2) simple map refset is used to publish exact
(identity) maps between SNOMED CT and codes in external terminologies.

The official SNOMED document can be found at https://confluence.ihtsdotools.org/display/DOCRELFMT/5.2.9+Simple+Map+Reference+Set

The first five fields of the SM Refset are common to _all_ SNOMED RF2 content:

| name | type | description |
| --- | --- | --- |
| id | UUID | The unique identifier of the `refsetId` / `referencedComponentId` entry |
| effectiveTime | Time | Used for versioning control.  In SNOMED releases `effectiveTime` is a release identifier |
| active | Boolean | For our purposes, if this is False this row should be ignored |
| moduleId | SCTID | The identifier of what group or organization made this assertion |
| refsetId | SCTID | The identifier of the particular map |



The remaining two fields in the simple map refset are:

| name | type | description |
| --- | --- | --- |
| referencedComponentId | SCTID | SNOMED concept identifier that is mapped to/from |
| mapTarget | String | "The equivalent code in the other terminology, classification or code system" |


There are currently 12 simple map reference sets that have been published by SNOMED CT International, although
not all of these are currently being maintained:

* CTV3 simple map reference set (foundation metadata concept)
* European Directorate for the Quality of Medicines & HealthCare to SNOMED CT simple map reference set (foundation metadata concept)
* GMDN simple map reference set (foundation metadata concept)
* ICD-O simple map reference set (foundation metadata concept)
* ICNP diagnoses simple map reference set (foundation metadata concept)
* ICNP interventions simple map reference set (foundation metadata concept)
* MedDRA - SNOMED CT simple map reference set (foundation metadata concept)
* Orphanet simple map type reference set (foundation metadata concept)
* SNOMED CT - MedDRA simple map reference set (foundation metadata concept)
* SNOMED CT to European Directorate for the Quality of Medicines & HealthCare simple map reference set (foundation metadata concept)
* SNOMED RT identifier simple map (foundation metadata concept)
* Unified Code for Units of Measure simple map reference set (foundation metadata concept) 

Note, in particular, that the only two that are released with the SNOMED CT International are the CTV3 and ICD-O maps.

### Simple Map Examples

| id | effectiveTime | active | moduleId | refsetId | referencedComponentId | mapTarget | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 8000501c-e5f1-5df2-91b8-d2360661e55c | 20050731 | 1 | 900000000000207008 | 900000000000497000 | 181522009 | 7N72Y | 181522009 (Entire skin of perianal area)  corresponds to 7N72Y in Read Codes V3 | 
| 8000baeb-e1a1-50e8-b28f-7a687d3cf1c5 | 20020131 | 1 | 900000000000207008 | 446608001 | 2681003 | C47.5 | 2681003 (Structure of dorsal nerve of penis) corresponds to `C47.5` in ICD-O | 


## SNOMED CT Complex Map Refset
The complex map refset was designed, in part, to handle the SNOMED to ICD-10 map that is published by SNOMED-CT.  The following
complex map refsets are currently in the SNOMED International edition:
* ICD-9-CM equivalence complex map reference set (foundation metadata concept)
* International Classification of Diseases, Ninth Revision, Clinical Modification reimbursement complex map reference set (foundation metadata concept)
* International Classification of Primary Care, Second edition complex map reference set (foundation metadata concept) 

| name | type | description |
| --- | --- | --- |
| referencedComponentId | SCTID | SNOMED concept identifier that is mapped _to_ the other code system|
| mapGroup | Integer | Identifies a set of complex map records from which one may be selected as a target code. Where a SNOMED CT concept maps onto 'n' target codes, there will be 'n' groups, each containing one or more complex map records. |
| mapPriority | Integer | |
| mapRule | String | A machine readable predicate used to determine whether this `mapTarget` should be included as part of the map |
| mapAdvice | String | A human readable "predicate" with the same purpose as `mapRule`, targete at carbon-based processor |
| mapTarget | String | A code in the target terminology, classification or code system |
| correlationId | SCTID | See [correlation identifiers](#Correlation identifiers) table  |
| mapCategoryId | SCTID | See [Map Category Identifiers](#Map Category Identifiers) table |

Mappings are always anchored on the `referencedComponentId` -- this id, in combination with the particular map, determines
a collection of `mapGroups`, where the general idea is that from each group, at most one mapTarget can be selected.  If, for 
instance, a map entry goes from one SCTID to 3 target concepts, there would be three different mapGroups for that id.

Within a `mapGroup`, the `mapRule` and/or `mapAdvice` is tested in `mapPriority` order.  A `mapGroup` is processed in 
priority order until a) the rule returns true (found) or b) you run out or roes.

### Correlation identifiers
| code | name |
| --- | --- |
| 447559001 | Broad to narrow map from SNOMED CT source code to target code (foundation metadata concept) |
| 447557004 | Exact match map from SNOMED CT source code to target code (foundation metadata concept) |
| 447558009 | Narrow to broad map from SNOMED CT source code to target code (foundation metadata concept) |
| 447560006 | Partial overlap between SNOMED CT source code and target code (foundation metadata concept) |
| 447556008 | SNOMED CT source code not mappable to target coding scheme (foundation metadata concept) | 
| 447561005 | SNOMED CT source code to target map code correlation not specified (foundation metadata concept) |

### Map Category Identifiers
| code | name |
| --- | --- |
|  447639009 | Map of source concept is context dependent |
|  447638001 | Map source concept cannot be classified with available data |
|  447636002 | Map source concept is outside of the scope of target classification |
|  447637006 | Map source concept is properly classified |
|  447635003 | Mapping guidance from WHO is ambiguous |
|  447640006 | Source SNOMED concept is ambiguous |
|  447641005 | Source SNOMED concept is incompletely modeled |
|  447642003 | Source concept has been retired from map scope |


### Complex Map Examples
The following subset for the complex map file entry to transform the SNOMED CT concept [733092009 | Microcephalus, hypergonadotropic hypogonadism, short stature syndrome](http://snomed.info/id/733092009)
into ICD-10:

| referenceComponentId | mapGroup | mapPriority | mapRule | mapAdvice | mapTarget | correlationId | mapCategoryId |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 733092009 | 1 | 1 | TRUE | ALWAYS E22.8 - POSSIBLE REQUIREMENT FOR ADDITIONAL CODE TO FULLY DESCRIBE DISEASE OR CONDITION | E22.8 | 447561005 | 447637006 |
| 733092009 | 2 | 1 | TRUE | ALWAYS Q02 | Q02 | 447561005 | 447637006 |
| 733092009 | 3 | 1 | IFA 248152002 | Female (finding) - IF FEMALE CHOOSE E28.3 - MAP IS CONTEXT DEPENDENT FOR GENDER | E28.3 | 447561005 | 447639009 |
| 733092009 | 3 | 2 | IFA 248153007 | Male (finding)  - IF MALE CHOOSE E29.1 - MAP IS CONTEXT DEPENDENT FOR GENDER | E29.1 | 447561005 | 447639009 |
| 733092009 | 3 | 3 | OTHERWISE TRUE | MAP SOURCE CONCEPT CANNOT BE CLASSIFIED WITH AVAILABLE DATA | | 447561005 | 447638001 |
| 733092009 | 4 | 1 | TRUE | ALWAYS E34.3 | E34.3 | 447561005 | 447637006 |


The above example is intended to produce four codes:
1) [E22.8 - Other Hyperfunction of the Pituary Gland](https://icd.who.int/browse10/2019/en#/E22.8)
2) [Q02 - Microcephaly](https://icd.who.int/browse10/2019/en#/Q02)
3) [E28.3 - Primary ovarian failure](https://icd.who.int/browse10/2019/en#/E28.3) if the patient is female -or- [E29.1 - Testicular hypofunction](https://icd.who.int/browse10/2019/en#/E29.1) if the patient is male - otherwise, no code
4) [E34.3 - Short stature, not elsewhere classified](https://icd.who.int/browse10/2019/en#/E34.3)

Note that the only coorelation id used is [447561005 | not specified](http://snomed.info/id/447561005).  

Map categories include:
* [447637006 | Map source concept is properly classified](http://snomed.info/id/447637006)
* [447639009 | Map of source concept is context dependent](http://snomed.info/id/447639009)
* [447638001 | Source concept cannot be classified with available data](http://snomed.info/id/447638001)

## Notes
1) SNOMED has three different distribution formas.  The documentation above applies to the SNAPSHOT release
format, which represents the state of the system at the point of the release without any history
2) It is possible for the moduleId to change over time as entire maps or, theoreticaly, individual entries in the
SM Refset change over time.  There is no requirement that all entries in a SM Refset `refsetId` are asserted
by the same organization.
3) There is surprisingly little computable metadata available for these reference sets.
