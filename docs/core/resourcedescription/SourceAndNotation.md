
# Type: SourceAndNotation


Format and notation that some or all the releases (versions) of this resource are published in

URI: [tccm:SourceAndNotation](https://hotecosystem.org/tccm/SourceAndNotation)


![img](images/SourceAndNotation.svg)

## Referenced by class

 *  **[AbstractResourceDescription](AbstractResourceDescription.md)** *[AbstractResourceDescription➞releaseFormat](AbstractResourceDescription_releaseFormat.md)*  <sub>0..*</sub>  **[SourceAndNotation](SourceAndNotation.md)**
 *  **[ResourceVersionDescription](ResourceVersionDescription.md)** *[ResourceVersionDescription➞sourceAndNotation](ResourceVersionDescription_sourceAndNotation.md)*  <sub>OPT</sub>  **[SourceAndNotation](SourceAndNotation.md)**
 *  **None** *[releaseFormat](releaseFormat.md)*  <sub>0..*</sub>  **[SourceAndNotation](SourceAndNotation.md)**
 *  **None** *[sourceAndNotation](sourceAndNotation.md)*  <sub>OPT</sub>  **[SourceAndNotation](SourceAndNotation.md)**

## Attributes


### Own

 * [SourceAndNotation➞sourceAndNotationDescription](SourceAndNotation_sourceAndNotationDescription.md)  <sub>OPT</sub>
    * Description: A textual description of where the specified resource version was derived from. This parameter must be supplied if a reasonable PersistentURI for the source document is not available. range: string
    * range: [String](types/String.md)
 * [SourceAndNotation➞sourceDocument](SourceAndNotation_sourceDocument.md)  <sub>OPT</sub>
    * Description: A persistentURI that references the document from which the resource version was derived. This URI may be resolvable to a digital resource or may be the name of a book, publication, or other external document.
    * range: [PersistentURI](types/PersistentURI.md)
 * [SourceAndNotation➞sourceDocumentSyntax](SourceAndNotation_sourceDocumentSyntax.md)  <sub>OPT</sub>
    * Description: The syntax of the source of the resource version, if known. Examples might include rdf/xml, Turtle, Manchester Syntax, CSV, etc.
    * range: [OntologySyntaxReference](OntologySyntaxReference.md)
 * [SourceAndNotation➞sourceLanguage](SourceAndNotation_sourceLanguage.md)  <sub>OPT</sub>
    * Description: The formal language, if any, that the source for the resource version is expressed in. Examples include Common Logic, OWL, OWL-DL, CLAML26, etc.
    * range: [OntologyLanguageReference](OntologyLanguageReference.md)
