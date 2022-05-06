
# Type: ComponentReference


A reference to a CTS2 model element. ComponentReference may reference a model attribute, a Property, or a special
element such as match strength.

URI: [https://hotecosystem.org/tccm/filtersandsorting/ComponentReference](https://hotecosystem.org/tccm/filtersandsorting/ComponentReference)


![img](images/ComponentReference.svg)

## Referenced by class

 *  **[FilterComponent](FilterComponent.md)** *[FilterComponent➞filterComponent](FilterComponent_filterComponent.md)*  <sub>0..*</sub>  **[ComponentReference](ComponentReference.md)**
 *  **[SortCriterion](SortCriterion.md)** *[SortCriterion➞sortElement](SortCriterion_sortElement.md)*  <sub>REQ</sub>  **[ComponentReference](ComponentReference.md)**
 *  **None** *[filterComponent](filterComponent.md)*  <sub>0..*</sub>  **[ComponentReference](ComponentReference.md)**
 *  **None** *[sortElement](sortElement.md)*  <sub>REQ</sub>  **[ComponentReference](ComponentReference.md)**

## Attributes


### Own

 * [ComponentReference➞attributeReference](ComponentReference_attributeReference.md)  <sub>OPT</sub>
    * range: [LocalIdentifier](types/LocalIdentifier.md)
 * [ComponentReference➞propertyReference](ComponentReference_propertyReference.md)  <sub>OPT</sub>
    * range: [PredicateReference](PredicateReference.md)
 * [ComponentReference➞specialReference](ComponentReference_specialReference.md)  <sub>OPT</sub>
    * range: [LocalIdentifier](types/LocalIdentifier.md)
