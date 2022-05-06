
# Type: FilterComponent


A restriction on an attribute, property, or special field.

URI: [tccm:FilterComponent](https://hotecosystem.org/tccm/FilterComponent)


![img](images/FilterComponent.svg)

## Referenced by class

 *  **None** *[➞component](filter__component.md)*  <sub>1..*</sub>  **[FilterComponent](FilterComponent.md)**
 *  **None** *[➞filter](propertyQueryReference__filter.md)*  <sub>REQ</sub>  **[FilterComponent](FilterComponent.md)**

## Attributes


### Own

 * [➞filterComponent](filterComponent__filterComponent.md)  <sub>0..*</sub>
    * Description: The name or URI of the property or model element to be filtered. Properties are referenced by
their predicate and model elements all have URIs that are established by this specification.
    * range: [PredicateReference](PredicateReference.md)
 * [➞matchAlgorithm](filterComponent__matchAlgorithm.md)  <sub>REQ</sub>
    * Description: The algorithm to be used for testing the referenced component. Examples might include “starts with,”
“regular expression match,” “exists,” “inRange,” etc.
    * range: [MatchAlgorithmReference](MatchAlgorithmReference.md)
 * [➞matchValue](filterComponent__matchValue.md)  <sub>OPT</sub>
    * Description: The value to be used in comparison. The structure and format of matchValue depends on the specific
matchAlgorithm. As an example, a “startsWith” algorithm would be plain text, a “regularExpression” algorithm
would have a regular expression while an “exists” algorithm would have nothing in the matchValue attribute.
    * range: [String](types/String.md)
