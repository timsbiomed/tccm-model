
# Type: FormatReference


A reference to a particular way that information is encoded for storage or transmission.

URI: [tccm:FormatReference](https://hotecosystem.org/tccm/FormatReference)


![img](images/FormatReference.svg)

## Parents

 *  is_a: [NameAndMeaningReference](NameAndMeaningReference.md) - A NameAndMeaningReference consists of a local identifier that references a unique meaning within the context of a given domain in a TCCM service instance and a globally unique URI that identifies the intended meaning of the identifier.

## Referenced by class

 *  **[OpaqueData](OpaqueData.md)** *[OpaqueData➞format](OpaqueData_format.md)*  <sub>OPT</sub>  **[FormatReference](FormatReference.md)**
 *  **None** *[format](format.md)*  <sub>OPT</sub>  **[FormatReference](FormatReference.md)**

## Attributes


### Inherited from NameAndMeaningReference:

 * [NameAndMeaningReference➞href](NameAndMeaningReference_href.md)  <sub>OPT</sub>
    * range: [RenderingURI](types/RenderingURI.md)
 * [NameAndMeaningReference➞name](NameAndMeaningReference_name.md)  <sub>REQ</sub>
    * range: [LocalIdentifier](types/LocalIdentifier.md)
 * [NameAndMeaningReference➞uri](NameAndMeaningReference_uri.md)  <sub>OPT</sub>
    * range: [ExternalURI](types/ExternalURI.md)
