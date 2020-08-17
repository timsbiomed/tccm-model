
# Type: CodeSystemReference


A reference to a code system or ontology.

URI: [tccm:CodeSystemReference](https://hotecosystem.org/tccm/CodeSystemReference)


![img](http://yuml.me/diagram/nofunky;dir:TB/class/[NameAndMeaningReference],[CodeSystemVersionReference],[CodeSystemVersionReference]++-%20codeSystem%200..1>[CodeSystemReference&#124;name(i):LocalIdentifier;uri(i):ExternalURI%20%3F;href(i):RenderingURI%20%3F],[NameAndMeaningReference]^-[CodeSystemReference])

## Parents

 *  is_a: [NameAndMeaningReference](NameAndMeaningReference.md) - A NameAndMeaningReference consists of a local identifier that references a unique meaning within the context of a given domain in a TCCM service instance and a globally unique URI that identifies the intended meaning of the identifier.

## Referenced by class

 *  **[CodeSystemVersionReference](CodeSystemVersionReference.md)** *[CodeSystemVersionReference➞codeSystem](CodeSystemVersionReference_codeSystem.md)*  <sub>OPT</sub>  **[CodeSystemReference](CodeSystemReference.md)**
 *  **None** *[codeSystem](codeSystem.md)*  <sub>OPT</sub>  **[CodeSystemReference](CodeSystemReference.md)**

## Attributes


### Inherited from NameAndMeaningReference:

 * [NameAndMeaningReference➞href](NameAndMeaningReference_href.md)  <sub>OPT</sub>
    * range: [RenderingURI](types/RenderingURI.md)
 * [NameAndMeaningReference➞name](NameAndMeaningReference_name.md)  <sub>REQ</sub>
    * range: [LocalIdentifier](types/LocalIdentifier.md)
 * [NameAndMeaningReference➞uri](NameAndMeaningReference_uri.md)  <sub>OPT</sub>
    * range: [ExternalURI](types/ExternalURI.md)
