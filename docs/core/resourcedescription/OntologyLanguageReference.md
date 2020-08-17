
# Type: OntologyLanguageReference


A reference to a language in which an ontology may be implemented.

URI: [tccm:OntologyLanguageReference](https://hotecosystem.org/tccm/OntologyLanguageReference)


![img](http://yuml.me/diagram/nofunky;dir:TB/class/[SourceAndNotation],[SourceAndNotation]++-%20sourceLanguage%200..1>[OntologyLanguageReference&#124;name(i):LocalIdentifier;uri(i):ExternalURI%20%3F;href(i):RenderingURI%20%3F],[NameAndMeaningReference]^-[OntologyLanguageReference],[NameAndMeaningReference])

## Parents

 *  is_a: [NameAndMeaningReference](NameAndMeaningReference.md) - A NameAndMeaningReference consists of a local identifier that references a unique meaning within the context of a given domain in a TCCM service instance and a globally unique URI that identifies the intended meaning of the identifier.

## Referenced by class

 *  **[SourceAndNotation](SourceAndNotation.md)** *[SourceAndNotation➞sourceLanguage](SourceAndNotation_sourceLanguage.md)*  <sub>OPT</sub>  **[OntologyLanguageReference](OntologyLanguageReference.md)**
 *  **None** *[sourceLanguage](sourceLanguage.md)*  <sub>OPT</sub>  **[OntologyLanguageReference](OntologyLanguageReference.md)**

## Attributes


### Inherited from NameAndMeaningReference:

 * [NameAndMeaningReference➞href](NameAndMeaningReference_href.md)  <sub>OPT</sub>
    * range: [RenderingURI](types/RenderingURI.md)
 * [NameAndMeaningReference➞name](NameAndMeaningReference_name.md)  <sub>REQ</sub>
    * range: [LocalIdentifier](types/LocalIdentifier.md)
 * [NameAndMeaningReference➞uri](NameAndMeaningReference_uri.md)  <sub>OPT</sub>
    * range: [ExternalURI](types/ExternalURI.md)
