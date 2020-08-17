
# Type: OntologySyntaxReference


A reference to a syntax in which an ontology may be represented.

URI: [tccm:OntologySyntaxReference](https://hotecosystem.org/tccm/OntologySyntaxReference)


![img](http://yuml.me/diagram/nofunky;dir:TB/class/[SourceAndNotation],[SourceAndNotation]++-%20sourceDocumentSyntax%200..1>[OntologySyntaxReference&#124;name(i):LocalIdentifier;uri(i):ExternalURI%20%3F;href(i):RenderingURI%20%3F],[NameAndMeaningReference]^-[OntologySyntaxReference],[NameAndMeaningReference])

## Parents

 *  is_a: [NameAndMeaningReference](NameAndMeaningReference.md) - A NameAndMeaningReference consists of a local identifier that references a unique meaning within the context of a given domain in a TCCM service instance and a globally unique URI that identifies the intended meaning of the identifier.

## Referenced by class

 *  **[SourceAndNotation](SourceAndNotation.md)** *[SourceAndNotation➞sourceDocumentSyntax](SourceAndNotation_sourceDocumentSyntax.md)*  <sub>OPT</sub>  **[OntologySyntaxReference](OntologySyntaxReference.md)**
 *  **None** *[sourceDocumentSyntax](sourceDocumentSyntax.md)*  <sub>OPT</sub>  **[OntologySyntaxReference](OntologySyntaxReference.md)**

## Attributes


### Inherited from NameAndMeaningReference:

 * [NameAndMeaningReference➞href](NameAndMeaningReference_href.md)  <sub>OPT</sub>
    * range: [RenderingURI](types/RenderingURI.md)
 * [NameAndMeaningReference➞name](NameAndMeaningReference_name.md)  <sub>REQ</sub>
    * range: [LocalIdentifier](types/LocalIdentifier.md)
 * [NameAndMeaningReference➞uri](NameAndMeaningReference_uri.md)  <sub>OPT</sub>
    * range: [ExternalURI](types/ExternalURI.md)
