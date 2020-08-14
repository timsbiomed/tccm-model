
# Tccm schema


Terminology Core Common Model Data Types


### Classes


### Mixins


### Slots


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

 * [CURIE](types/CURIE.md)  (**Curie**) 
 * [ChangeSetURI](types/ChangeSetURI.md)  ([PersistentURI](types/PersistentURI.md))  - The unique identifier of a set of change instructions that can potentially transform the contents of a TCCM service instance from one state to another.
 * [DateAndTime](types/DateAndTime.md)  (**XSDDateTime**)  - Represents an “Instant” as defined in the OWL Time Specification . Implementations must be able to support temporal units of second, minute, hour, day, month, and year, and be able to represent and compare instances represented in any of these units. DateAndTime can only provide a partial ordering and, as a consequence, i s never used as an index, unique identifier, or to sequence data or events.
 * [DirectoryURI](types/DirectoryURI.md)  ([LocalURI](types/LocalURI.md))  - The unique name of a query that when executed results in a list of resources that, in the context of a given service, satisfy the query.
 * [DocumentURI](types/DocumentURI.md)  ([PersistentURI](types/PersistentURI.md))  - A reference to a “work” in the bibliographic sense. It is not necessary that a Document URI be directly or indirectly resolvable to a digital resource - it may simply be the name of a book, publication, or other abstraction.
 * [ExternalURI](types/ExternalURI.md)  ([PersistentURI](types/PersistentURI.md))  - A URI that names a unique resource. CTS2 implementations should never assume that ExternalURI is resolvable via an http: GET operation - ExternalURIs should always be passed as parameters to service implementations to get the sanctioned equivalent in a given service context.
 * [LocalIdentifier](types/LocalIdentifier.md)  ([String](types/String.md))  - An identifier that uniquely references a class, individual, property, or other resource within the context of a specific TCCM service implementation. LocalIdentifier syntax must match the PNAME production as defined in the SPARQL Query Specification . LocalIdentifiers may begin with leading digits, where XML Local Identifiers and NameSpaceIdentifiers may not.
 * [LocalURI](types/LocalURI.md)  ([URIorCurie](types/URIorCurie.md))  - A URI or handle whose scope is local to the implementing service. LocalURI cannot be used as a permanent identifier in a message or a data record.
 * [NamespaceIdentifier](types/NamespaceIdentifier.md)  (**NCName**)  - An identifier that uniquely references the scoping namespace of an Entity (class, role, or individual) within the context of a TCCM service. NameSpaceIdentifier syntax must match the PNAME NS production as defined in the SPARQL Query Specification - meaning that it must begin with an alphabetic character
 * [NaturalNumber](types/NaturalNumber.md)  (**int**)  - A non-negative integer (N). NatrualNumber is used exclusively for representing quantities.
 * [PersistentURI](types/PersistentURI.md)  ([URIorCurie](types/URIorCurie.md))  - A Universal Resource Identifier (URI) that persists across service instances. PersistentURIs have enduring reference and meaning.
 * [RenderingURI](types/RenderingURI.md)  ([LocalURI](types/LocalURI.md))  - A URI or handle that is directly readable by a specific instance of a TCCM service implementation. RenderingURI must resolve to Changeable CTS2 element.
 * [ServiceURI](types/ServiceURI.md)  ([LocalURI](types/LocalURI.md))  - The URI or CURIE of a service implementation
 * [URI](types/URI.md)  (**URI**)  - A Universal Resource Identifier (URI) as defined in IETF RFC 3986. TCCM implementations are encouraged to consider implementing this data type using the IRI (RFC3987) specification
 * [URIorCurie](types/URIorCurie.md)  (**URIorCURIE**)  - a URI or a CURIE
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
