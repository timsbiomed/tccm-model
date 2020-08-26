
# Type: SortCriterion


The particular attribute, property, or special element to be sorted along with the sort direction.

URI: [https://hotecosystem.org/tccm/filtersandsorting/SortCriterion](https://hotecosystem.org/tccm/filtersandsorting/SortCriterion)


![img](images/SortCriterion.svg)

## Referenced by class

 *  **[SortCriteria](SortCriteria.md)** *[SortCriteria➞entry](SortCriteria_entry.md)*  <sub>0..*</sub>  **[SortCriterion](SortCriterion.md)**
 *  **None** *[entry](entry.md)*  <sub>0..*</sub>  **[SortCriterion](SortCriterion.md)**

## Attributes


### Own

 * [SortCriterion➞sortDescending](SortCriterion_sortDescending.md)  <sub>OPT</sub>
    * Description: True means ascending, false descending order
    * range: [Boolean](types/Boolean.md)
 * [SortCriterion➞sortElement](SortCriterion_sortElement.md)  <sub>REQ</sub>
    * Description: The type and name of the attribute, property, or special element to be sorted.
    * range: [PredicateReference](PredicateReference.md)
