
# Type: ValueSetDescription


A description of a value

URI: [tccm:ValueSetDescription](https://hotecosystem.org/tccm/ValueSetDescription)


![img](images/ValueSetDescription.svg)

## Parents

 *  is_a: [ValueSetCatalogEntryOrReference](ValueSetCatalogEntryOrReference.md) - Either a description of ana abstract value set or a reference to an official entry

## Uses Mixins

 *  mixin: [NameAndMeaningReference](NameAndMeaningReference.md) - A NameAndMeaningReference consists of a local identifier that references a unique meaning within the context of

## Attributes


### Mixed in from NameAndMeaningReference:

 * [➞href](nameAndMeaningReference__href.md)  <sub>OPT</sub>
    * range: [RenderingURI](types/RenderingURI.md)

### Mixed in from NameAndMeaningReference:

 * [➞name](nameAndMeaningReference__name.md)  <sub>REQ</sub>
    * Description: An identifier that uniquely names the reference within the context of the particular reference type.
    * range: [LocalIdentifier](types/LocalIdentifier.md)

### Mixed in from NameAndMeaningReference:

 * [➞synopsis](nameAndMeaningReference__synopsis.md)  <sub>OPT</sub>
    * Description: A summary of the role and purpose of the actual reference
    * range: [String](types/String.md)

### Mixed in from NameAndMeaningReference:

 * [➞uri](nameAndMeaningReference__uri.md)  <sub>OPT</sub>
    * range: [ExternalURI](types/ExternalURI.md)
