
# Type: EntityReference


The URI, namespace/name (if known) and a list of code systems that make assertions about the entity.

URI: [tccm:EntityReference](https://hotecosystem.org/tccm/EntityReference)


![img](images/EntityReference.svg)

## Referenced by class

 *  **[EntityReferenceList](EntityReferenceList.md)** *[EntityReferenceList➞entities](EntityReferenceList_entities.md)*  <sub>0..*</sub>  **[EntityReference](EntityReference.md)**
 *  **None** *[entities](entities.md)*  <sub>0..*</sub>  **[EntityReference](EntityReference.md)**

## Attributes


### Own

 * [EntityReference➞about](EntityReference_about.md)  <sub>OPT</sub>
    * Description: The external, permanant URI by which this entity is known.
    * range: [PersistentURI](types/PersistentURI.md)
 * [EntityReference➞code](EntityReference_code.md)  <sub>REQ</sub>
    * Description: The namespace and name by which this entity is known within the context of the service implementation
    * range: [String](types/String.md)
 * [EntityReference➞description](EntityReference_description.md)  <sub>OPT</sub>
    * Description: A description or definition of the referenced entity determined by the service
    * range: [String](types/String.md)
 * [EntityReference➞designation](EntityReference_designation.md)  <sub>OPT</sub>
    * Description: The preferred label for the entity in the context of the service
    * range: [String](types/String.md)
 * [EntityReference➞href](EntityReference_href.md)  <sub>OPT</sub>
    * Description: A reference to the "official" description of the entity in the context of the defining code system
    * range: [RenderingURI](types/RenderingURI.md)
 * [EntityReference➞see_also](EntityReference_see_also.md)  <sub>0..*</sub>
    * Description: Additional external links that serve to define or otherwise clarify the intent of the reference
    * range: [RenderingURI](types/RenderingURI.md)
