
# Type: PredicateReference


An EntityReference that serves the role of predicate. Note that this varies slightly from the base class of NameAndMeaningReference because the name attribute is a namespace/name combination rather than a simple name scoped exclusively by the domain.

URI: [tccm:PredicateReference](https://hotecosystem.org/tccm/PredicateReference)


![img](http://yuml.me/diagram/nofunky;dir:TB/class/[PredicateReference&#124;uri:ExternalURI;name:CURIE;href:RenderingURI%20%3F;designation:string%20%3F])

## Referenced by class


## Attributes


### Own

 * [PredicateReference➞designation](PredicateReference_designation.md)  <sub>OPT</sub>
    * range: [String](types/String.md)
 * [PredicateReference➞href](PredicateReference_href.md)  <sub>OPT</sub>
    * range: [RenderingURI](types/RenderingURI.md)
 * [PredicateReference➞name](PredicateReference_name.md)  <sub>REQ</sub>
    * range: [CURIE](types/CURIE.md)
 * [PredicateReference➞uri](PredicateReference_uri.md)  <sub>REQ</sub>
    * range: [ExternalURI](types/ExternalURI.md)
