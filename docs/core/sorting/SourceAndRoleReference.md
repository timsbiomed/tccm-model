
# Type: SourceAndRoleReference


A reference to a source that also includes the role that the source played and/or fixes the particular chapter,
page, or other element within the reference.

URI: [https://hotecosystem.org/tccm/sorting/SourceAndRoleReference](https://hotecosystem.org/tccm/sorting/SourceAndRoleReference)


![img](images/SourceAndRoleReference.svg)

## Parents

 *  is_a: [NameAndMeaningReference](NameAndMeaningReference.md) - A NameAndMeaningReference consists of a local identifier that references a unique meaning within the context of

## Attributes


### Own

 * [➞bibliographicLink](sourceAndRoleReference__bibliographicLink.md)  <sub>OPT</sub>
    * range: [OpaqueData](OpaqueData.md)
 * [➞role](sourceAndRoleReference__role.md)  <sub>OPT</sub>
    * range: [RoleReference](RoleReference.md)

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
