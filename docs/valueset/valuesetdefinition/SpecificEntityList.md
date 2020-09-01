
# Type: SpecificEntityList


A list of specific entity references that are to be included in the definition. When specified in this form,
the service must include all entities in this list whether they are known to the service or not, and whether
they are currently ACTIVE or not.

URI: [tccm:SpecificEntityList](https://hotecosystem.org/tccm/SpecificEntityList)


![img](images/SpecificEntityList.svg)

## Parents

 *  is_a: [EntityReferenceList](EntityReferenceList.md) - A collection (set) of zero or more entity references that belong to the same scoping namespace

## Referenced by class

 *  **None** *[➞entitylist](formalDefinition__entity_list.md)*  <sub>OPT</sub>  **[SpecificEntityList](SpecificEntityList.md)**

## Attributes


### Inherited from EntityReferenceList:

 * [➞entities](entityReferenceList__entities.md)  <sub>0..*</sub>
    * Description: The entity references ("concept codes") in the list
    * range: [EntityReference](EntityReference.md)
 * [➞namespaceName](entityReferenceList__namespaceName.md)  <sub>OPT</sub>
    * Description: The local identifier assigned to this namespace
    * range: [CodeSystemName](types/CodeSystemName.md)
 * [➞namespaceURI](entityReferenceList__namespaceURI.md)  <sub>REQ</sub>
    * Description: The URI associated with the supplied namespace as determined by the author/service instance
    * range: [ExternalURI](types/ExternalURI.md)
