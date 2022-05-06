
# Type: FormalDefinition


A value set definition choice

URI: [tccm:FormalDefinition](https://hotecosystem.org/tccm/FormalDefinition)


![img](images/FormalDefinition.svg)

## Referenced by class

 *  **None** *[➞exclude](valueSetDefinitionEntry__exclude.md)*  <sub>0..*</sub>  **[FormalDefinition](FormalDefinition.md)**
 *  **None** *[➞include](valueSetDefinitionEntry__include.md)*  <sub>0..*</sub>  **[FormalDefinition](FormalDefinition.md)**
 *  **None** *[➞intersect](valueSetDefinitionEntry__intersect.md)*  <sub>0..*</sub>  **[FormalDefinition](FormalDefinition.md)**

## Attributes


### Own

 * [➞entityQuery](formalDefinition__associated_entities.md)  <sub>OPT</sub>
    * range: [AssociatedEntitiesReference](AssociatedEntitiesReference.md)
 * [➞codeSystem](formalDefinition__complete_code_system.md)  <sub>OPT</sub>
    * range: [CompleteCodeSystemReference](CompleteCodeSystemReference.md)
 * [➞valueSet](formalDefinition__complete_value_set.md)  <sub>OPT</sub>
    * range: [CompleteValueSetReference](CompleteValueSetReference.md)
 * [➞entitylist](formalDefinition__entity_list.md)  <sub>OPT</sub>
    * range: [SpecificEntityList](SpecificEntityList.md)
 * [➞externalDefinition](formalDefinition__external_value_set_definition.md)  <sub>OPT</sub>
    * range: [ExternalValueSetDefinition](ExternalValueSetDefinition.md)
 * [➞valueQuery](formalDefinition__property_query.md)  <sub>OPT</sub>
    * range: [PropertyQueryReference](PropertyQueryReference.md)
 * [➞definition](formalDefinition__value_set_definition.md)  <sub>OPT</sub>
    * range: [ValueSetDefinitionEntry](ValueSetDefinitionEntry.md)

## Other properties

|  |  |  |
| --- | --- | --- |
| **Comments:** | | A "`FormalDefinition`" must be exactly one of the attributes below |

