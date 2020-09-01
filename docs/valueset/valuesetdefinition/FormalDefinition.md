
# Type: FormalDefinition


A value set definition choice

URI: [tccm:FormalDefinition](https://hotecosystem.org/tccm/FormalDefinition)


![img](images/FormalDefinition.svg)

## Children

 * [CompleteCodeSystemReference](CompleteCodeSystemReference.md) - An entry that, when resolved, returns all of the active entity references in a given code system. This includes

## Referenced by class

 *  **None** *[➞exclude](valueSetDefinitionEntry__exclude.md)*  <sub>OPT</sub>  **[FormalDefinition](FormalDefinition.md)**
 *  **None** *[➞include](valueSetDefinitionEntry__include.md)*  <sub>OPT</sub>  **[FormalDefinition](FormalDefinition.md)**
 *  **None** *[➞intersect](valueSetDefinitionEntry__intersect.md)*  <sub>OPT</sub>  **[FormalDefinition](FormalDefinition.md)**

## Attributes


### Own

 * [➞entityquery](formalDefinition__associated_entities.md)  <sub>OPT</sub>
    * range: [AssociatedEntitiesReference](AssociatedEntitiesReference.md)
 * [➞codesystem](formalDefinition__complete_code_system.md)  <sub>OPT</sub>
    * range: [CompleteCodeSystemReference](CompleteCodeSystemReference.md)
 * [➞valueset](formalDefinition__complete_value_set.md)  <sub>OPT</sub>
    * range: [CompleteValueSetReference](CompleteValueSetReference.md)
 * [➞entitylist](formalDefinition__entity_list.md)  <sub>OPT</sub>
    * range: [SpecificEntityList](SpecificEntityList.md)
 * [➞externaldefinition](formalDefinition__external_value_set_definition.md)  <sub>OPT</sub>
    * range: [ExternalValueSetDefinition](ExternalValueSetDefinition.md)
 * [➞valuequery](formalDefinition__property_query.md)  <sub>OPT</sub>
    * range: [PropertyQueryReference](PropertyQueryReference.md)
 * [➞definition](formalDefinition__value_set_definition.md)  <sub>OPT</sub>
    * range: [ValueSetDefinitionEntry](ValueSetDefinitionEntry.md)
