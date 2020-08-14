
# Type: CodeSystemVersionReference


A reference to a specific version of code system and, if known, the code system which it is a version of.

URI: [tccm:CodeSystemVersionReference](https://hotecosystem.org/tccm/CodeSystemVersionReference)


![img](images/CodeSystemVersionReference.svg)

## Parents

 *  is_a: [NameAndMeaningReference](NameAndMeaningReference.md) - A NameAndMeaningReference consists of a local identifier that references a unique meaning within the context of a given domain in a TCCM service instance and a globally unique URI that identifies the intended meaning of the identifier.

## Referenced by class


## Attributes


### Own

 * [CodeSystemVersionReference➞codeSystem](CodeSystemVersionReference_codeSystem.md)  <sub>OPT</sub>
    * range: [CodeSystemReference](CodeSystemReference.md)

### Inherited from NameAndMeaningReference:

 * [NameAndMeaningReference➞href](NameAndMeaningReference_href.md)  <sub>OPT</sub>
    * range: [RenderingURI](types/RenderingURI.md)
 * [NameAndMeaningReference➞name](NameAndMeaningReference_name.md)  <sub>REQ</sub>
    * range: [LocalIdentifier](types/LocalIdentifier.md)
 * [NameAndMeaningReference➞uri](NameAndMeaningReference_uri.md)  <sub>OPT</sub>
    * range: [ExternalURI](types/ExternalURI.md)
