
# Type: ValueSetDefinitionEntry


An element of a value set definition that, when resolved yields a set of entity references that are to be included
in, excluded from or intersected with the set of elements that represent the full resolution of the definition.

Note that only ACTIVE entity references are included. INACTIVE entity references may never be considered for
inclusion or exclusion in the resolution of a value set definition.

URI: [tccm:ValueSetDefinitionEntry](https://hotecosystem.org/tccm/ValueSetDefinitionEntry)


![img](images/ValueSetDefinitionEntry.svg)

## Referenced by class

 *  **[ValueSetDefinition](ValueSetDefinition.md)** *[ValueSetDefinition➞entry](ValueSetDefinition_entry.md)*  <sub>1..*</sub>  **[ValueSetDefinitionEntry](ValueSetDefinitionEntry.md)**
 *  **None** *[entry](entry.md)*  <sub>1..*</sub>  **[ValueSetDefinitionEntry](ValueSetDefinitionEntry.md)**

## Attributes


### Own

 * [ValueSetDefinitionEntry➞definition](ValueSetDefinitionEntry_definition.md)  <sub>REQ</sub>
    * Description: The definition itself
    * range: [FormalDefinition](FormalDefinition.md)
 * [ValueSetDefinitionEntry➞operator](ValueSetDefinitionEntry_operator.md)  <sub>OPT</sub>
    * Description: Instructions for how the results of the entry evaluation will be applied to the set of entities in the base
definition. Results can be added to the set (+), intersected with members already in the set (and),
or be removed from the set (-).
    * range: [String](types/String.md)
