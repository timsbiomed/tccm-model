
# Directorytypes schema


URI's for various TCCM directories


### Classes


### Mixins


### Slots


### Types


#### Built in

 * **Bool**
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

 * [AssociationDirectoryURI](types/AssociationDirectoryURI.md)  ([DirectoryURI](types/DirectoryURI.md))  - A DirectoryURI that references a set of Associations.
 * [ChangeSetDirectoryURI](types/ChangeSetDirectoryURI.md)  ([DirectoryURI](types/DirectoryURI.md))  - A DirectoryURI that references a set of ChangeSets.
 * [ChangeSetURI](types/ChangeSetURI.md)  ([PersistentURI](types/PersistentURI.md))  - The unique identifier of a set of change instructions that can potentially transform the contents of a TCCM
 * [CodeSystemCatalogEntryDirectoryURI](types/CodeSystemCatalogEntryDirectoryURI.md)  ([DirectoryURI](types/DirectoryURI.md))  - A DirectoryURI that references a set of CodeSystemCatalogEntries.
 * [CodeSystemVersionCatalogEntryDirectoryURI](types/CodeSystemVersionCatalogEntryDirectoryURI.md)  ([DirectoryURI](types/DirectoryURI.md))  - A DirectoryURI that references a set of CodeSystemVersionCatalogEntries.
 * [ConceptDomainBindingDirectoryURI](types/ConceptDomainBindingDirectoryURI.md)  ([DirectoryURI](types/DirectoryURI.md))  - A DirectoryURI that references a set of ConceptDomainBindings.
 * [ConceptDomainCatalogEntryDirectoryURI](types/ConceptDomainCatalogEntryDirectoryURI.md)  ([DirectoryURI](types/DirectoryURI.md))  - A DirectoryURI that references a set of ConceptDomainCatalogEntries.
 * [DateAndTime](types/DateAndTime.md)  (**XSDDateTime**)  - Represents an “Instant” as defined in the OWL Time Specification . Implementations must be able to support
 * [DirectoryURI](types/DirectoryURI.md)  ([LocalURI](types/LocalURI.md))  - The unique name of a query that when executed results in a list of resources that, in the context of a given
 * [DocumentURI](types/DocumentURI.md)  ([PersistentURI](types/PersistentURI.md))  - A reference to a “work” in the bibliographic sense. It is not necessary that a Document URI be directly or
 * [EntityDirectoryURI](types/EntityDirectoryURI.md)  ([DirectoryURI](types/DirectoryURI.md))  - A DirectoryURI that references a set of EntityDescriptionDirectory.
 * [ExternalURI](types/ExternalURI.md)  ([PersistentURI](types/PersistentURI.md))  - A URI that names a unique resource. CTS2 implementations should never assume that ExternalURI is resolvable
 * [LocalIdentifier](types/LocalIdentifier.md)  ([String](types/String.md))  - An identifier that uniquely references a class, individual, property, or other resource within the context of a
 * [LocalURI](types/LocalURI.md)  (**URIorCURIE**)  - A URI or handle whose scope is local to the implementing service. LocalURI cannot be used as a permanent
 * [MapCatalogEntryDirectoryURI](types/MapCatalogEntryDirectoryURI.md)  ([DirectoryURI](types/DirectoryURI.md))  - A DirectoryURI that references a set of MapCatalogEntries.
 * [MapEntryDirectoryURI](types/MapEntryDirectoryURI.md)  ([DirectoryURI](types/DirectoryURI.md))  - A DirectoryURI that references a set of MapEntries.
 * [MapVersionDirectoryURI](types/MapVersionDirectoryURI.md)  ([DirectoryURI](types/DirectoryURI.md))  - A DirectoryURI that references a set of MapVersions.
 * [NamespaceIdentifier](types/NamespaceIdentifier.md)  (**NCName**)  - An identifier that uniquely references the scoping namespace of an Entity (class, role, or individual)
 * [NaturalNumber](types/NaturalNumber.md)  (**int**)  - A non-negative integer (N). NatrualNumber is used exclusively for representing quantities.
 * [PersistentURI](types/PersistentURI.md)  (**URIorCURIE**)  - A Universal Resource Identifier (URI) that persists across service instances. PersistentURIs have enduring
 * [RenderingURI](types/RenderingURI.md)  ([LocalURI](types/LocalURI.md))  - A URI or handle that is directly readable by a specific instance of a TCCM service implementation. RenderingURI
 * [ResolvedValueSetDirectoryURI](types/ResolvedValueSetDirectoryURI.md)  ([DirectoryURI](types/DirectoryURI.md))  - A DirectoryURI that references a set of ValueSetCatalogEntries.
 * [ServiceURI](types/ServiceURI.md)  ([LocalURI](types/LocalURI.md))  - The URI or CURIE of a service implementation
 * [StatementDirectoryURI](types/StatementDirectoryURI.md)  ([DirectoryURI](types/DirectoryURI.md))  - A DirectoryURI that references a set of Statements.
 * [ValueSetCatalogEntryDirectoryURI](types/ValueSetCatalogEntryDirectoryURI.md)  ([DirectoryURI](types/DirectoryURI.md))  - A DirectoryURI that references a set of ValueSetCatalogEntries.
 * [ValueSetDefinitionDirectoryURI](types/ValueSetDefinitionDirectoryURI.md)  ([DirectoryURI](types/DirectoryURI.md))  - A DirectoryURI that references a set of ValueSetDefinitions.
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
