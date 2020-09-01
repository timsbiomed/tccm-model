
# Type: CodeSystemReference


A reference to a code system or ontology.

URI: [tccm:CodeSystemReference](https://hotecosystem.org/tccm/CodeSystemReference)


![img](images/CodeSystemReference.svg)

## Parents

 *  is_a: [NameAndMeaningReference](NameAndMeaningReference.md) - A NameAndMeaningReference consists of a local identifier that references a unique meaning within the context of

## Referenced by class

 *  **None** *[➞codeSystem](associatedEntitiesReference__codeSystem.md)*  <sub>REQ</sub>  **[CodeSystemReference](CodeSystemReference.md)**
 *  **None** *[➞codeSystem](codeSystemVersionReference__codeSystem.md)*  <sub>OPT</sub>  **[CodeSystemReference](CodeSystemReference.md)**
 *  **None** *[➞codeSystem](completeCodeSystemReference__codeSystem.md)*  <sub>REQ</sub>  **[CodeSystemReference](CodeSystemReference.md)**
 *  **None** *[➞codeSystem](propertyQueryReference__codeSystem.md)*  <sub>REQ</sub>  **[CodeSystemReference](CodeSystemReference.md)**

## Attributes


### Inherited from NameAndMeaningReference:

 * [➞href](nameAndMeaningReference__href.md)  <sub>OPT</sub>
    * range: [RenderingURI](types/RenderingURI.md)
 * [➞name](nameAndMeaningReference__name.md)  <sub>REQ</sub>
    * Description: An identifier that uniquely names the reference within the context of the particular reference type.
    * range: [LocalIdentifier](types/LocalIdentifier.md)
 * [➞synopsis](nameAndMeaningReference__synopsis.md)  <sub>OPT</sub>
    * Description: A summary of the role and purpose of the actual reference
    * range: [String](types/String.md)
 * [➞uri](nameAndMeaningReference__uri.md)  <sub>OPT</sub>
    * range: [ExternalURI](types/ExternalURI.md)
