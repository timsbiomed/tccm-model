
# Localidentifiers schema


This sub clause lists the specific types of local identifiers that are used within the TCCM specification. Instances 
of each type of local identifier must be unique within the context of the service instance. As an example, “SCT” might
uniquely name the SNOMED-CT code system within the context of one service, while another service might use “SMD-CT.” 
As a consequence, local identifiers can never be used in interchanges between services - URIs must be used instead. 
Note, also, that it is okay to have the same local identifier for different types of resource. As an example, the 
identifier “SCT” could be a CodeSystemName for the SNOMED-CT code system and a ValueSetName for the “
Standardized Category Terms” value set.


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

 * [CodeSystemName](types/CodeSystemName.md)  ([LocalIdentifier](types/LocalIdentifier.md))  - A local identifier for a CodeSystem.
 * [CodeSystemVersionName](types/CodeSystemVersionName.md)  ([LocalIdentifier](types/LocalIdentifier.md))  - A local identifier for a CodeSystemVersion.
 * [ConceptDomainName](types/ConceptDomainName.md)  ([LocalIdentifier](types/LocalIdentifier.md))  - A local identifier for a ConceptDomain.
 * [DateAndTime](types/DateAndTime.md)  (**XSDDateTime**)  - Represents an “Instant” as defined in the OWL Time Specification . Implementations must be able to support
 * [LocalIdentifier](types/LocalIdentifier.md)  ([String](types/String.md))  - An identifier that uniquely references a class, individual, property, or other resource within the context of a
 * [MapName](types/MapName.md)  ([LocalIdentifier](types/LocalIdentifier.md))  - A local identifier for a Map.
 * [MapVersionName](types/MapVersionName.md)  ([LocalIdentifier](types/LocalIdentifier.md))  - A local identifier for a MapVersion.
 * [NamespaceIdentifier](types/NamespaceIdentifier.md)  (**NCName**)  - An identifier that uniquely references the scoping namespace of an Entity (class, role, or individual)
 * [NaturalNumber](types/NaturalNumber.md)  (**int**)  - A non-negative integer (N). NatrualNumber is used exclusively for representing quantities.
 * [ValueSetName](types/ValueSetName.md)  ([LocalIdentifier](types/LocalIdentifier.md))  - A local identifier for a ValueSet.
 * [VersionTagName](types/VersionTagName.md)  ([LocalIdentifier](types/LocalIdentifier.md))  - A local identifier for a VersionTag.
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
