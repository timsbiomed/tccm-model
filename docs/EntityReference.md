
# Type: entityReference




URI: [tccm:EntityReference](https://hotecosystem.org/tccm/EntityReference)


![img](images/EntityReference.png)

## Referenced by class


## Attributes


### Own

 * [href](href.md)  <sub>OPT</sub>
    * range: [RenderingURI](types/RenderingURI.md)

### Inherited from entityDescription:

 * [about](about.md)  <sub>REQ</sub>
    * range: [PersistentURI](types/PersistentURI.md)
 * [code](code.md)  <sub>OPT</sub>
    * range: [String](types/String.md)
 * [alternateURI](alternateURI.md)  <sub>0..*</sub>
    * range: [Uriorcurie](types/Uriorcurie.md)
    * inherited from: [EntityDescription](EntityDescription.md)
 * [designation](designation.md)  <sub>OPT</sub>
    * range: [Designation](Designation.md)
    * inherited from: [EntityDescription](EntityDescription.md)

### Domain for slot:

 * [about](about.md)  <sub>REQ</sub>
    * range: [PersistentURI](types/PersistentURI.md)
 * [code](code.md)  <sub>OPT</sub>
    * range: [String](types/String.md)
