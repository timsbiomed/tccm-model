
# Type: EntityReferenceList


A collection (set) of zero or more entity references that belong to the same scoping namespace

URI: [tccm:EntityReferenceList](https://hotecosystem.org/tccm/EntityReferenceList)


![img](images/EntityReferenceList.svg)

## Children

 * [SpecificEntityList](SpecificEntityList.md) - A list of specific entity references that are to be included in the definition. When specified in this form,

## Referenced by class


## Attributes


### Own

 * [➞entities](entityReferenceList__entities.md)  <sub>0..*</sub>
    * Description: The entity references ("concept codes") in the list
    * range: [EntityReference](EntityReference.md)
 * [➞namespaceName](entityReferenceList__namespaceName.md)  <sub>OPT</sub>
    * Description: The local identifier assigned to this namespace
    * range: [CodeSystemName](types/CodeSystemName.md)
 * [➞namespaceURI](entityReferenceList__namespaceURI.md)  <sub>REQ</sub>
    * Description: The URI associated with the supplied namespace as determined by the author/service instance
    * range: [ExternalURI](types/ExternalURI.md)
