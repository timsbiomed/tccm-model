
# Type: CodeSystemVersionReference


A reference to a specific version of code system and, if known, the code system which it is a version of.

URI: [tccm:CodeSystemVersionReference](https://hotecosystem.org/tccm/CodeSystemVersionReference)


![img](images/CodeSystemVersionReference.svg)

## Parents

 *  is_a: [NameAndMeaningReference](NameAndMeaningReference.md) - A NameAndMeaningReference consists of a local identifier that references a unique meaning within the context of

## Referenced by class

 *  **[AssociatedEntitiesReference](AssociatedEntitiesReference.md)** *[AssociatedEntitiesReference➞codeSystemVersion](AssociatedEntitiesReference_codeSystemVersion.md)*  <sub>OPT</sub>  **[CodeSystemVersionReference](CodeSystemVersionReference.md)**
 *  **[CompleteCodeSystemReference](CompleteCodeSystemReference.md)** *[CompleteCodeSystemReference➞codeSystemVersion](CompleteCodeSystemReference_codeSystemVersion.md)*  <sub>OPT</sub>  **[CodeSystemVersionReference](CodeSystemVersionReference.md)**
 *  **[CompleteValueSetReference](CompleteValueSetReference.md)** *[CompleteValueSetReference➞referenceCodeSystemVersion](CompleteValueSetReference_referenceCodeSystemVersion.md)*  <sub>OPT</sub>  **[CodeSystemVersionReference](CodeSystemVersionReference.md)**
 *  **[PropertyQueryReference](PropertyQueryReference.md)** *[PropertyQueryReference➞codeSystemVersion](PropertyQueryReference_codeSystemVersion.md)*  <sub>OPT</sub>  **[CodeSystemVersionReference](CodeSystemVersionReference.md)**
 *  **None** *[codeSystemVersion](codeSystemVersion.md)*  <sub>OPT</sub>  **[CodeSystemVersionReference](CodeSystemVersionReference.md)**
 *  **None** *[referenceCodeSystemVersion](referenceCodeSystemVersion.md)*  <sub>OPT</sub>  **[CodeSystemVersionReference](CodeSystemVersionReference.md)**

## Attributes


### Own

 * [CodeSystemVersionReference➞codeSystem](CodeSystemVersionReference_codeSystem.md)  <sub>REQ</sub>
    * range: [CodeSystemReference](CodeSystemReference.md)

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
