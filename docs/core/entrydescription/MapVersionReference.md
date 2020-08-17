
# Type: MapVersionReference


A reference to a map version and the corresponding map, if known.

URI: [tccm:MapVersionReference](https://hotecosystem.org/tccm/MapVersionReference)


![img](http://yuml.me/diagram/nofunky;dir:TB/class/[NameAndMeaningReference],[MapReference]<map%200..1-++[MapVersionReference&#124;name(i):LocalIdentifier;uri(i):ExternalURI%20%3F;href(i):RenderingURI%20%3F],[NameAndMeaningReference]^-[MapVersionReference],[MapReference])

## Parents

 *  is_a: [NameAndMeaningReference](NameAndMeaningReference.md) - A NameAndMeaningReference consists of a local identifier that references a unique meaning within the context of a given domain in a TCCM service instance and a globally unique URI that identifies the intended meaning of the identifier.

## Referenced by class


## Attributes


### Own

 * [MapVersionReference➞map](MapVersionReference_map.md)  <sub>OPT</sub>
    * range: [MapReference](MapReference.md)

### Inherited from NameAndMeaningReference:

 * [NameAndMeaningReference➞href](NameAndMeaningReference_href.md)  <sub>OPT</sub>
    * range: [RenderingURI](types/RenderingURI.md)
 * [NameAndMeaningReference➞name](NameAndMeaningReference_name.md)  <sub>REQ</sub>
    * range: [LocalIdentifier](types/LocalIdentifier.md)
 * [NameAndMeaningReference➞uri](NameAndMeaningReference_uri.md)  <sub>OPT</sub>
    * range: [ExternalURI](types/ExternalURI.md)
