
# Type: SortCriterion


The particular attribute, property, or special element to be sorted along with the sort direction.

URI: [https://hotecosystem.org/tccm/sorting/SortCriterion](https://hotecosystem.org/tccm/sorting/SortCriterion)


![img](images/SortCriterion.svg)

## Referenced by class

 *  **None** *[➞entry](sortCriteria__entry.md)*  <sub>0..*</sub>  **[SortCriterion](SortCriterion.md)**

## Attributes


### Own

 * [➞sortDescending](sortCriterion__sortDescending.md)  <sub>OPT</sub>
    * Description: True means ascending, false descending order
    * range: [Boolean](types/Boolean.md)
 * [➞sortElement](sortCriterion__sortElement.md)  <sub>REQ</sub>
    * Description: The type and name of the attribute, property, or special element to be sorted.
    * range: [PredicateReference](PredicateReference.md)
