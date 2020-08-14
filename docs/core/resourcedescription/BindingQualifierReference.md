
# Type: BindingQualifierReference


A reference to an entity that describes the role that a given value set binding plays for a concept domain. T ypical values represent “overall,” “minimum” or “maximum,” the significance of which can be found in H L7 Version 3 documentation.

URI: [tccm:BindingQualifierReference](https://hotecosystem.org/tccm/BindingQualifierReference)


![img](images/BindingQualifierReference.svg)

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
