
# Type: Filter


A collection of one or more filters. The result of applying a Filter component is the intersection of the sets of
qualifying elements. As an example, a filter having two components - one which says that the rights attribute must
exist and a second that says that the text “SNOMED” must appear in the synopsis would return all resources having
BOTH a rights attribute and “SNOMED” in the description.

URI: [tccm:Filter](https://hotecosystem.org/tccm/Filter)


![img](images/Filter.svg)

## Referenced by class


## Attributes


### Own

 * [Filter➞component](Filter_component.md)  <sub>1..*</sub>
    * Description: An entry in a filter
    * range: [FilterComponent](FilterComponent.md)
 * [Filter➞description](Filter_description.md)  <sub>OPT</sub>
    * Description: A textual description of the intent and purpose of the filter
    * range: [String](types/String.md)
