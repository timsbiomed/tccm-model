
# Type: ValueSetDefinitionEntry


An element of a value set definition that, when resolved yields a set of entity references that are to be included
in, excluded from or intersected with the set of elements that represent the full resolution of the definition.

Note that only ACTIVE entity references are included. INACTIVE entity references may never be considered for
inclusion or exclusion in the resolution of a value set definition.

URI: [tccm:ValueSetDefinitionEntry](https://hotecosystem.org/tccm/ValueSetDefinitionEntry)


![img](images/ValueSetDefinitionEntry.svg)

## Referenced by class

 *  **None** *[➞definition](formalDefinition__value_set_definition.md)*  <sub>OPT</sub>  **[ValueSetDefinitionEntry](ValueSetDefinitionEntry.md)**
 *  **None** *[➞entry](valueSetDefinition__entry.md)*  <sub>1..*</sub>  **[ValueSetDefinitionEntry](ValueSetDefinitionEntry.md)**

## Attributes


### Own

 * [➞exclude](valueSetDefinitionEntry__exclude.md)  <sub>OPT</sub>
    * Description: Exclude the resolution of this definition in the valueset
    * range: [FormalDefinition](FormalDefinition.md)
 * [➞include](valueSetDefinitionEntry__include.md)  <sub>OPT</sub>
    * Description: Include the resolution of this definition in the valueset
    * range: [FormalDefinition](FormalDefinition.md)
 * [➞intersect](valueSetDefinitionEntry__intersect.md)  <sub>OPT</sub>
    * Description: Include only the elements that are common between this definition and the valueset to this point
    * range: [FormalDefinition](FormalDefinition.md)
