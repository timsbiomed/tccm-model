
# Filtersandsorting schema


The elements that are used in the construction of query filters and return sort criteria.


### Classes

 * [NameAndMeaningReference](NameAndMeaningReference.md) - A NameAndMeaningReference consists of a local identifier that references a unique meaning within the context of
    * [AssociationReference](AssociationReference.md) - A name or identifier that uniquely names an association instance in a code system.
    * [BindingQualifierReference](BindingQualifierReference.md) - A reference to an entity that describes the role that a given value set binding plays for a concept domain. T
    * [CaseSignificanceReference](CaseSignificanceReference.md) - A reference to an entity that describes significance of the case in term or designation.
    * [CodeSystemCategoryReference](CodeSystemCategoryReference.md) - A reference to information about a paradigm model used to create an ontology (a.k.a. knowledge
    * [CodeSystemReference](CodeSystemReference.md) - A reference to a code system or ontology.
    * [CodeSystemVersionReference](CodeSystemVersionReference.md) - A reference to a specific version of code system and, if known, the code system which it is a version of.
    * [ConceptDomainReference](ConceptDomainReference.md) - A reference to a concept domain.
    * [ContextReference](ContextReference.md) - A reference to a realm or context.
    * [DesignationFidelityReference](DesignationFidelityReference.md) - A reference to a description about designation faithfulness or accuracy.
    * [DesignationTypeReference](DesignationTypeReference.md) - A reference to a designation type or form such as “short name,” “abbreviation,” “eponym.”
    * [FormalityLevelReference](FormalityLevelReference.md) - A reference to a description of the relative formality an ontology.
    * [FormatReference](FormatReference.md) - A reference to a particular way that information is encoded for storage or transmission.
    * [LanguageReference](LanguageReference.md) - A reference to a spoken or written human language.
    * [MapCorrelationReference](MapCorrelationReference.md) - A reference to a way that the source and target in a map can be related or assessed.
    * [MapReference](MapReference.md) - A reference to an abstract map.
    * [MapVersionReference](MapVersionReference.md) - A reference to a map version and the corresponding map, if known.
    * [MatchAlgorithmReference](MatchAlgorithmReference.md) - A reference to an algorithm used for selecting and filtering data.
    * [ModelAttributeReference](ModelAttributeReference.md) - A reference to an attribute defined in the CTS2 specification.
    * [NamespaceReference](NamespaceReference.md) - A reference to a conceptual space that groups identifiers to avoid conflict with items that have the same name
    * [OntologyDomainReference](OntologyDomainReference.md) - A reference to a subject domain for an ontology.
    * [OntologyEngineeringMethodologyReference](OntologyEngineeringMethodologyReference.md) - A reference to a method model that can be used to create an ontology.
    * [OntologyEngineeringToolReference](OntologyEngineeringToolReference.md) - A reference to a tool that can be used to create an ontology.
    * [OntologyLanguageReference](OntologyLanguageReference.md) - A reference to a language in which an ontology may be implemented.
    * [OntologySyntaxReference](OntologySyntaxReference.md) - A reference to a syntax in which an ontology may be represented.
    * [OntologyTaskReference](OntologyTaskReference.md) - A reference to a purpose for which an ontology can be designed.
    * [OntologyTypeReference](OntologyTypeReference.md) - A reference to the nature of the content of an ontology.
    * [ReasoningAlgorithmReference](ReasoningAlgorithmReference.md) - A reference to a formal algorithm for making inferences about an ontology.
    * [RoleReference](RoleReference.md) - A reference to a role that an individual, organization, or bibliographic reference can play in the construction
    * [SourceAndRoleReference](SourceAndRoleReference.md) - A reference to a source that also includes the role that the source played and/or fixes the particular chapter,
    * [SourceReference](SourceReference.md) - A reference to an individual, organization of bibliographic reference.
    * [StatusReference](StatusReference.md) - A reference to a state in an external ontology authoring workflow.
    * [ValueSetDefinitionReference](ValueSetDefinitionReference.md) - A reference to a set of rules for constructing a value set along with the corresponding value set if known.
    * [ValueSetReference](ValueSetReference.md) - A reference to a named set of entity references.
    * [VersionTagReference](VersionTagReference.md) - A reference to a tag that can be assigned to versionable resources within the context of a service implementation.
 * [PredicateReference](PredicateReference.md) - An EntityReference that serves the role of predicate. Note that this varies slightly from the base class of
 * [SortCriteria](SortCriteria.md) - An ordered list of sort criterion. The first entry in the list identifies the primary sort order, the second
 * [SortCriterion](SortCriterion.md) - The particular attribute, property, or special element to be sorted along with the sort direction.

### Mixins


### Slots

 * [codeSystem](codeSystem.md)
    * [CodeSystemVersionReference➞codeSystem](CodeSystemVersionReference_codeSystem.md)
 * [designation](designation.md)
    * [PredicateReference➞designation](PredicateReference_designation.md)
 * [entry](entry.md) - a rule for sorting
    * [SortCriteria➞entry](SortCriteria_entry.md)
 * [href](href.md)
    * [NameAndMeaningReference➞href](NameAndMeaningReference_href.md)
    * [PredicateReference➞href](PredicateReference_href.md)
 * [map](map.md)
    * [MapVersionReference➞map](MapVersionReference_map.md)
 * [name](name.md) - An identifier that uniquely names the reference within the context of the particular reference type.
    * [NameAndMeaningReference➞name](NameAndMeaningReference_name.md)
    * [PredicateReference➞name](PredicateReference_name.md)
 * [role](role.md)
    * [SourceAndRoleReference➞role](SourceAndRoleReference_role.md)
 * [sortDescending](sortDescending.md) - True means ascending, false descending order
    * [SortCriterion➞sortDescending](SortCriterion_sortDescending.md)
 * [sortElement](sortElement.md) - The type and name of the attribute, property, or special element to be sorted.
    * [SortCriterion➞sortElement](SortCriterion_sortElement.md)
 * [synopsis](synopsis.md) - A summary of the role and purpose of the actual reference
    * [NameAndMeaningReference➞synopsis](NameAndMeaningReference_synopsis.md)
 * [uri](uri.md)
    * [NameAndMeaningReference➞uri](NameAndMeaningReference_uri.md)
    * [PredicateReference➞uri](PredicateReference_uri.md)

### Types


#### Built in

 * **Bool**
 * **Curie**
 * **ElementIdentifier**
 * **NCName**
 * **NodeIdentifier**
 * **URI**
 * **URIorCURIE**
 * **XSDDate**
 * **XSDDateTime**
 * **XSDTime**
 * **float**
 * **int**
 * **str**

#### Defined

 * [ASSOCIATION](types/ASSOCIATION.md)  ([ValueSet](types/ValueSet.md))  - A formal “semantic” assertion about a named entity, in the form of subject, predicate, and object including any
 * [BINDINGQUALIFIER](types/BINDINGQUALIFIER.md)  ([ValueSet](types/ValueSet.md))  - An assertion about the semantics of a concept domain / value set binding. This model element exists specifically
 * [CASESIGNIFICANCE](types/CASESIGNIFICANCE.md)  ([ValueSet](types/ValueSet.md))  - Identifies the significance of case in a term or designation.
 * [CODESYSTEM](types/CODESYSTEM.md)  ([ValueSet](types/ValueSet.md))  - A collection of metadata about the provenance, use, and distribution of a code system or ontology.
 * [CODESYSTEMCATEGORY](types/CODESYSTEMCATEGORY.md)  ([ValueSet](types/ValueSet.md))  - The general category of a code system (flat list, subject heading system, taxonomy, thesaurus, classification,
 * [CODESYSTEMVERSION](types/CODESYSTEMVERSION.md)  ([ValueSet](types/ValueSet.md))  - A collection of metadata about content and distribution format of a particular version or release of a code system.
 * [CONCEPTDOMAIN](types/CONCEPTDOMAIN.md)  ([ValueSet](types/ValueSet.md))  - The description of the conceptual domain of a field in a message, column in a database, field on a form, etc.
 * [CONTEXT](types/CONTEXT.md)  ([ValueSet](types/ValueSet.md))  - External and environmental factors that serve to discriminate among multiple possible selections. While it is
 * [CURIE](types/CURIE.md)  (**Curie**) 
 * [ChangeSetURI](types/ChangeSetURI.md)  ([PersistentURI](types/PersistentURI.md))  - The unique identifier of a set of change instructions that can potentially transform the contents of a TCCM
 * [DESIGNATIONFIDELITY](types/DESIGNATIONFIDELITY.md)  ([ValueSet](types/ValueSet.md))  - Identifies how well a particular designation represents the intended meaning of the referenced entity. TCCM
 * [DESIGNATIONTYPE](types/DESIGNATIONTYPE.md)  ([ValueSet](types/ValueSet.md))  - The particular form or type of a given designation: can be “short name,” “long name,” “abbreviation,” “eponym.”
 * [DateAndTime](types/DateAndTime.md)  (**XSDDateTime**)  - Represents an “Instant” as defined in the OWL Time Specification . Implementations must be able to support
 * [DirectoryURI](types/DirectoryURI.md)  ([LocalURI](types/LocalURI.md))  - The unique name of a query that when executed results in a list of resources that, in the context of a given
 * [DocumentURI](types/DocumentURI.md)  ([PersistentURI](types/PersistentURI.md))  - A reference to a “work” in the bibliographic sense. It is not necessary that a Document URI be directly or
 * [ExternalURI](types/ExternalURI.md)  ([PersistentURI](types/PersistentURI.md))  - A URI that names a unique resource. CTS2 implementations should never assume that ExternalURI is resolvable
 * [FORMALITYLEVEL](types/FORMALITYLEVEL.md)  ([ValueSet](types/ValueSet.md))  - The level of formality of an ontology (OMV 5.9).
 * [FORMAT](types/FORMAT.md)  ([ValueSet](types/ValueSet.md))  - A particular way that information is encoded for storage in a computer file
 * [LANGUAGE](types/LANGUAGE.md)  ([ValueSet](types/ValueSet.md))  - A spoken or written language intended for human consumption.
 * [LocalIdentifier](types/LocalIdentifier.md)  ([String](types/String.md))  - An identifier that uniquely references a class, individual, property, or other resource within the context of a
 * [LocalURI](types/LocalURI.md)  ([URIorCurie](types/URIorCurie.md))  - A URI or handle whose scope is local to the implementing service. LocalURI cannot be used as a permanent
 * [MAP](types/MAP.md)  ([ValueSet](types/ValueSet.md))  - A set of rules that associate a set of entity references from one domain into those in another.
 * [MAPCORRELATION](types/MAPCORRELATION.md)  ([ValueSet](types/ValueSet.md))  - An assertion about the strength or significance of a specific rule in a Map.
 * [MAPVERSION](types/MAPVERSION.md)  ([ValueSet](types/ValueSet.md))  - The state of a Map at a given point in time.
 * [MATCHALGORITHM](types/MATCHALGORITHM.md)  ([ValueSet](types/ValueSet.md))  - A predicate that determines whether an entity resource qualities for membership in a set based on supplied
 * [MODELATTRIBUTE](types/MODELATTRIBUTE.md)  ([ValueSet](types/ValueSet.md))  - An attribute defined in CTS2 information model.
 * [NAMESPACE](types/NAMESPACE.md)  ([ValueSet](types/ValueSet.md))  - A reference to a conceptual space that groups identifiers to avoid conflict with items that have the same name but different meanings.
 * [NamespaceIdentifier](types/NamespaceIdentifier.md)  (**NCName**)  - An identifier that uniquely references the scoping namespace of an Entity (class, role, or individual)
 * [NaturalNumber](types/NaturalNumber.md)  (**int**)  - A non-negative integer (N). NatrualNumber is used exclusively for representing quantities.
 * [ONTOLOGYDOMAIN](types/ONTOLOGYDOMAIN.md)  ([ValueSet](types/ValueSet.md))  - While the domain can refer to any topic ontology it is advised to use one of the established general purpose
 * [ONTOLOGYENGINEERINGMETHODOLOGY](types/ONTOLOGYENGINEERINGMETHODOLOGY.md)  ([ValueSet](types/ValueSet.md))  - Information about the ontology engineering methodology (OMV 5.4) (sic).
 * [ONTOLOGYENGINEERINGTOOL](types/ONTOLOGYENGINEERINGTOOL.md)  ([ValueSet](types/ValueSet.md))  - A tool used to create the ontology (OMV 5.5).
 * [ONTOLOGYLANGUAGE](types/ONTOLOGYLANGUAGE.md)  ([ValueSet](types/ValueSet.md))  - Information about the language in which the ontology is implemented (OMV 5.7).
 * [ONTOLOGYSYNTAX](types/ONTOLOGYSYNTAX.md)  ([ValueSet](types/ValueSet.md))  - Information about the syntax used by an ontology (OMV 5.6).
 * [ONTOLOGYTASK](types/ONTOLOGYTASK.md)  ([ValueSet](types/ValueSet.md))  - Information about the task the ontology was intended to be used for (OMV 5.10).
 * [ONTOLOGYTYPE](types/ONTOLOGYTYPE.md)  ([ValueSet](types/ValueSet.md))  - Categorizes ontologies (OMV 5.2).
 * [PREDICATE](types/PREDICATE.md)  ([ValueSet](types/ValueSet.md))  - A property or relation between entities.
 * [PersistentURI](types/PersistentURI.md)  ([URIorCurie](types/URIorCurie.md))  - A Universal Resource Identifier (URI) that persists across service instances. PersistentURIs have enduring
 * [REASONINGALGORITHM](types/REASONINGALGORITHM.md)  ([ValueSet](types/ValueSet.md))  - A set of formal rules that allow the deduction of additional assertions from a
 * [RESOURCETYPE](types/RESOURCETYPE.md)  ([ValueSet](types/ValueSet.md))  - A class of which a referencing resource is an instance of.
 * [ROLE](types/ROLE.md)  ([ValueSet](types/ValueSet.md))  - A role that a SOURCE can play in the construction or dissemination of a terminological resource.
 * [RenderingURI](types/RenderingURI.md)  ([LocalURI](types/LocalURI.md))  - A URI or handle that is directly readable by a specific instance of a TCCM service implementation. RenderingURI
 * [SOURCE](types/SOURCE.md)  ([ValueSet](types/ValueSet.md))  - An individual, organization, or bibliographic reference.
 * [STATEMENT](types/STATEMENT.md)  ([ValueSet](types/ValueSet.md))  - An atomic assertion about a CTS2 resource.
 * [STATUS](types/STATUS.md)  ([ValueSet](types/ValueSet.md))  - The state of a resource or other entry in an external workflow.
 * [ServiceURI](types/ServiceURI.md)  ([LocalURI](types/LocalURI.md))  - The URI or CURIE of a service implementation
 * [URI](types/URI.md)  (**URI**)  - A Universal Resource Identifier (URI) as defined in IETF RFC 3986. TCCM implementations are encouraged to
 * [URIorCurie](types/URIorCurie.md)  (**URIorCURIE**)  - a URI or a CURIE
 * [VALUESET](types/VALUESET.md)  ([ValueSet](types/ValueSet.md))  - A set of entity references.
 * [VALUESETDEFINITION](types/VALUESETDEFINITION.md)  ([ValueSet](types/ValueSet.md))  - A set of rules that can be applied to specified versions or one or more code systems to yield a set of entity
 * [VERSIONTAG](types/VERSIONTAG.md)  ([ValueSet](types/ValueSet.md))  - An identifier that can be assigned to resource versions by a service implementation to identify their state
 * [ValueSet](types/ValueSet.md)  ([URIorCurie](types/URIorCurie.md))  - A URI that can be indirectly resolved to a set of entity descriptions
 * [Boolean](types/Boolean.md)  (**Bool**)  - A binary (true or false) value
 * [Date](types/Date.md)  (**XSDDate**)  - a date (year, month and day) in an idealized calendar
 * [Datetime](types/Datetime.md)  (**XSDDateTime**)  - The combination of a date and time
 * [Double](types/Double.md)  (**float**)  - A real number that conforms to the xsd:double specification
 * [Float](types/Float.md)  (**float**)  - A real number that conforms to the xsd:float specification
 * [Integer](types/Integer.md)  (**int**)  - An integer
 * [Ncname](types/Ncname.md)  (**NCName**)  - Prefix part of CURIE
 * [Nodeidentifier](types/Nodeidentifier.md)  (**NodeIdentifier**)  - A URI, CURIE or BNODE that represents a node in a model.
 * [Objectidentifier](types/Objectidentifier.md)  (**ElementIdentifier**)  - A URI or CURIE that represents an object in the model.
 * [String](types/String.md)  (**str**)  - A character string
 * [Time](types/Time.md)  (**XSDTime**)  - A time object represents a (local) time of day, independent of any particular day
 * [Uri](types/Uri.md)  (**URI**)  - a complete URI
 * [Uriorcurie](types/Uriorcurie.md)  (**URIorCURIE**)  - a URI or a CURIE
