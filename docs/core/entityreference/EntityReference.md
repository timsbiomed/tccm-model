
# Type: EntityReference


The URI, namespace/name (if known) and a list of code systems that make assertions about the entity.

URI: [tccm:EntityReference](https://hotecosystem.org/tccm/EntityReference)


![img](http://yuml.me/diagram/nofunky;dir:TB/class/[EntityReference&#124;about:PersistentURI;name:string%20%3F;designation:string%20%3F;href:RenderingURI%20%3F])

## Referenced by class


## Attributes


### Own

 * [EntityReference➞about](EntityReference_about.md)  <sub>REQ</sub>
    * Description: The external, permanant URI by which this entity is known.
    * range: [PersistentURI](types/PersistentURI.md)
 * [EntityReference➞designation](EntityReference_designation.md)  <sub>OPT</sub>
    * Description: A block of text that describes the intended meaning or purpose of the entity
    * range: [String](types/String.md)
 * [EntityReference➞href](EntityReference_href.md)  <sub>OPT</sub>
    * Description: A reference to the "official" description of the entity in the context of the defining code system
    * range: [RenderingURI](types/RenderingURI.md)
 * [EntityReference➞name](EntityReference_name.md)  <sub>OPT</sub>
    * Description: The namespace and name by which this entity is known within the context of the service implementation
    * range: [String](types/String.md)
