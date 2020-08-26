
# Type: PredicateReference


An EntityReference that serves the role of predicate. Note that this varies slightly from the base class of
NameAndMeaningReference because the name attribute is a namespace/name combination rather than a simple name
scoped exclusively by the domain.

URI: [tccm:PredicateReference](https://hotecosystem.org/tccm/PredicateReference)


![img](images/PredicateReference.svg)

## Referenced by class

 *  **[AssociatedEntitiesReference](AssociatedEntitiesReference.md)** *[AssociatedEntitiesReference➞predicate](AssociatedEntitiesReference_predicate.md)*  <sub>REQ</sub>  **[PredicateReference](PredicateReference.md)**
 *  **[FilterComponent](FilterComponent.md)** *[FilterComponent➞filterComponent](FilterComponent_filterComponent.md)*  <sub>0..*</sub>  **[PredicateReference](PredicateReference.md)**
 *  **None** *[filterComponent](filterComponent.md)*  <sub>0..*</sub>  **[PredicateReference](PredicateReference.md)**
 *  **None** *[predicate](predicate.md)*  <sub>REQ</sub>  **[PredicateReference](PredicateReference.md)**

## Attributes


### Own

 * [PredicateReference➞designation](PredicateReference_designation.md)  <sub>OPT</sub>
    * range: [String](types/String.md)
 * [PredicateReference➞href](PredicateReference_href.md)  <sub>OPT</sub>
    * range: [RenderingURI](types/RenderingURI.md)
 * [PredicateReference➞name](PredicateReference_name.md)  <sub>REQ</sub>
    * range: [CURIE](types/CURIE.md)
 * [PredicateReference➞uri](PredicateReference_uri.md)  <sub>REQ</sub>
    * range: [ExternalURI](types/ExternalURI.md)
