
# Type: SourceAndRoleReference


A reference to a source that also includes the role that the source played and/or fixes the particular chapter, page, or other element within the reference.

URI: [tccm:SourceAndRoleReference](https://hotecosystem.org/tccm/SourceAndRoleReference)


![img](http://yuml.me/diagram/nofunky;dir:TB/class/[RoleReference]<role%200..1-++[SourceAndRoleReference&#124;name(i):LocalIdentifier;uri(i):ExternalURI%20%3F;href(i):RenderingURI%20%3F],[NameAndMeaningReference]^-[SourceAndRoleReference],[RoleReference],[NameAndMeaningReference])

## Parents

 *  is_a: [NameAndMeaningReference](NameAndMeaningReference.md) - A NameAndMeaningReference consists of a local identifier that references a unique meaning within the context of a given domain in a TCCM service instance and a globally unique URI that identifies the intended meaning of the identifier.

## Referenced by class


## Attributes


### Own

 * [SourceAndRoleReference➞role](SourceAndRoleReference_role.md)  <sub>OPT</sub>
    * range: [RoleReference](RoleReference.md)

### Inherited from NameAndMeaningReference:

 * [NameAndMeaningReference➞href](NameAndMeaningReference_href.md)  <sub>OPT</sub>
    * range: [RenderingURI](types/RenderingURI.md)
 * [NameAndMeaningReference➞name](NameAndMeaningReference_name.md)  <sub>REQ</sub>
    * range: [LocalIdentifier](types/LocalIdentifier.md)
 * [NameAndMeaningReference➞uri](NameAndMeaningReference_uri.md)  <sub>OPT</sub>
    * range: [ExternalURI](types/ExternalURI.md)
