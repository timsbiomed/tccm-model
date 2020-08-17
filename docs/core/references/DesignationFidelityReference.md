
# Type: DesignationFidelityReference


A reference to a description about designation faithfulness or accuracy.

URI: [tccm:DesignationFidelityReference](https://hotecosystem.org/tccm/DesignationFidelityReference)


![img](http://yuml.me/diagram/nofunky;dir:TB/class/[NameAndMeaningReference],[NameAndMeaningReference]^-[DesignationFidelityReference&#124;name(i):LocalIdentifier;uri(i):ExternalURI%20%3F;href(i):RenderingURI%20%3F])

## Parents

 *  is_a: [NameAndMeaningReference](NameAndMeaningReference.md) - A NameAndMeaningReference consists of a local identifier that references a unique meaning within the context of a given domain in a TCCM service instance and a globally unique URI that identifies the intended meaning of the identifier.

## Attributes


### Inherited from NameAndMeaningReference:

 * [NameAndMeaningReference➞href](NameAndMeaningReference_href.md)  <sub>OPT</sub>
    * range: [RenderingURI](types/RenderingURI.md)
 * [NameAndMeaningReference➞name](NameAndMeaningReference_name.md)  <sub>REQ</sub>
    * range: [LocalIdentifier](types/LocalIdentifier.md)
 * [NameAndMeaningReference➞uri](NameAndMeaningReference_uri.md)  <sub>OPT</sub>
    * range: [ExternalURI](types/ExternalURI.md)
