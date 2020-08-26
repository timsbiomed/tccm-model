
# Type: CodeSystemReference


A reference to a code system or ontology.

URI: [tccm:CodeSystemReference](https://hotecosystem.org/tccm/CodeSystemReference)


![img](images/CodeSystemReference.svg)

## Parents

 *  is_a: [NameAndMeaningReference](NameAndMeaningReference.md) - A NameAndMeaningReference consists of a local identifier that references a unique meaning within the context of

## Referenced by class

 *  **[AssociatedEntitiesReference](AssociatedEntitiesReference.md)** *[AssociatedEntitiesReference➞codeSystem](AssociatedEntitiesReference_codeSystem.md)*  <sub>REQ</sub>  **[CodeSystemReference](CodeSystemReference.md)**
 *  **[CodeSystemVersionReference](CodeSystemVersionReference.md)** *[CodeSystemVersionReference➞codeSystem](CodeSystemVersionReference_codeSystem.md)*  <sub>REQ</sub>  **[CodeSystemReference](CodeSystemReference.md)**
 *  **[CompleteCodeSystemReference](CompleteCodeSystemReference.md)** *[CompleteCodeSystemReference➞codeSystem](CompleteCodeSystemReference_codeSystem.md)*  <sub>REQ</sub>  **[CodeSystemReference](CodeSystemReference.md)**
 *  **[PropertyQueryReference](PropertyQueryReference.md)** *[PropertyQueryReference➞codeSystem](PropertyQueryReference_codeSystem.md)*  <sub>REQ</sub>  **[CodeSystemReference](CodeSystemReference.md)**
 *  **None** *[codeSystem](codeSystem.md)*  <sub>REQ</sub>  **[CodeSystemReference](CodeSystemReference.md)**

## Attributes


### Inherited from NameAndMeaningReference:

 * [NameAndMeaningReference➞href](NameAndMeaningReference_href.md)  <sub>OPT</sub>
    * range: [RenderingURI](types/RenderingURI.md)
 * [NameAndMeaningReference➞name](NameAndMeaningReference_name.md)  <sub>REQ</sub>
    * Description: An identifier that uniquely names the reference within the context of the particular reference type.
    * range: [LocalIdentifier](types/LocalIdentifier.md)
 * [NameAndMeaningReference➞synopsis](NameAndMeaningReference_synopsis.md)  <sub>OPT</sub>
    * Description: A summary of the role and purpose of the actual reference
    * range: [String](types/String.md)
 * [NameAndMeaningReference➞uri](NameAndMeaningReference_uri.md)  <sub>OPT</sub>
    * range: [ExternalURI](types/ExternalURI.md)
