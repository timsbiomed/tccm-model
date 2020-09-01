
# Type: EntityExpression


An expression in a given ontology language and syntax that describes or defines an entity. Examples might include
descriptions of entities in Manchester OWL Syntax, RDF, SNOMED Concept Expression, etc.

URI: [tccm:EntityExpression](https://hotecosystem.org/tccm/EntityExpression)


![img](images/EntityExpression.svg)

## Attributes


### Own

 * [➞expression](entityExpression__expression.md)  <sub>REQ</sub>
    * Description: The actual Expression.
    * range: [OpaqueData](OpaqueData.md)
 * [➞ontologyLanguage](entityExpression__ontologyLanguage.md)  <sub>REQ</sub>
    * Description: The ontology language of the expression.
    * range: [OntologyLanguageReference](OntologyLanguageReference.md)
