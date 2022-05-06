
# Type: PredicateReference


An EntityReference that serves the role of predicate. Note that this varies slightly from the base class of
NameAndMeaningReference because the name attribute is a namespace/name combination rather than a simple name
scoped exclusively by the domain.

URI: [https://hotecosystem.org/tccm/sorting/PredicateReference](https://hotecosystem.org/tccm/sorting/PredicateReference)


![img](images/PredicateReference.svg)

## Referenced by class

 *  **None** *[➞sortElement](sortCriterion__sortElement.md)*  <sub>REQ</sub>  **[PredicateReference](PredicateReference.md)**

## Attributes


### Own

 * [➞designation](predicateReference__designation.md)  <sub>OPT</sub>
    * range: [String](types/String.md)
 * [➞href](predicateReference__href.md)  <sub>OPT</sub>
    * range: [RenderingURI](types/RenderingURI.md)
 * [➞name](predicateReference__name.md)  <sub>OPT</sub>
    * range: [LocalIdentifier](types/LocalIdentifier.md)
 * [➞uri](predicateReference__uri.md)  <sub>REQ</sub>
    * range: [ExternalURI](types/ExternalURI.md)
