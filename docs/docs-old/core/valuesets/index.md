
# Valuesets schema


Terminology Core Common Model Value Sets


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

 * [ASSOCIATION](types/ASSOCIATION.md)  ([ValueSet](types/ValueSet.md))  - A formal “semantic” assertion about a named entity, in the form of subject, predicate, and object including any
 * [BINDINGQUALIFIER](types/BINDINGQUALIFIER.md)  ([ValueSet](types/ValueSet.md))  - An assertion about the semantics of a concept domain / value set binding. This model element exists specifically
 * [CASESIGNIFICANCE](types/CASESIGNIFICANCE.md)  ([ValueSet](types/ValueSet.md))  - Identifies the significance of case in a term or designation.
 * [CODESYSTEM](types/CODESYSTEM.md)  ([ValueSet](types/ValueSet.md))  - A collection of metadata about the provenance, use, and distribution of a code system or ontology.
 * [CODESYSTEMCATEGORY](types/CODESYSTEMCATEGORY.md)  ([ValueSet](types/ValueSet.md))  - The general category of a code system (flat list, subject heading system, taxonomy, thesaurus, classification,
 * [CODESYSTEMVERSION](types/CODESYSTEMVERSION.md)  ([ValueSet](types/ValueSet.md))  - A collection of metadata about content and distribution format of a particular version or release of a code system.
 * [CONCEPTDOMAIN](types/CONCEPTDOMAIN.md)  ([ValueSet](types/ValueSet.md))  - The description of the conceptual domain of a field in a message, column in a database, field on a form, etc.
 * [CONTEXT](types/CONTEXT.md)  ([ValueSet](types/ValueSet.md))  - External and environmental factors that serve to discriminate among multiple possible selections. While it is
 * [DESIGNATIONFIDELITY](types/DESIGNATIONFIDELITY.md)  ([ValueSet](types/ValueSet.md))  - Identifies how well a particular designation represents the intended meaning of the referenced entity. TCCM
 * [DESIGNATIONTYPE](types/DESIGNATIONTYPE.md)  ([ValueSet](types/ValueSet.md))  - The particular form or type of a given designation: can be “short name,” “long name,” “abbreviation,” “eponym.”
 * [DateAndTime](types/DateAndTime.md)  (**XSDDateTime**)  - Represents an “Instant” as defined in the OWL Time Specification . Implementations must be able to support
 * [FORMALITYLEVEL](types/FORMALITYLEVEL.md)  ([ValueSet](types/ValueSet.md))  - The level of formality of an ontology (OMV 5.9).
 * [FORMAT](types/FORMAT.md)  ([ValueSet](types/ValueSet.md))  - A particular way that information is encoded for storage in a computer file
 * [LANGUAGE](types/LANGUAGE.md)  ([ValueSet](types/ValueSet.md))  - A spoken or written language intended for human consumption.
 * [LocalIdentifier](types/LocalIdentifier.md)  ([String](types/String.md))  - An identifier that uniquely references a class, individual, property, or other resource within the context of a
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
 * [REASONINGALGORITHM](types/REASONINGALGORITHM.md)  ([ValueSet](types/ValueSet.md))  - A set of formal rules that allow the deduction of additional assertions from a
 * [RESOURCETYPE](types/RESOURCETYPE.md)  ([ValueSet](types/ValueSet.md))  - A class of which a referencing resource is an instance of.
 * [ROLE](types/ROLE.md)  ([ValueSet](types/ValueSet.md))  - A role that a SOURCE can play in the construction or dissemination of a terminological resource.
 * [SOURCE](types/SOURCE.md)  ([ValueSet](types/ValueSet.md))  - An individual, organization, or bibliographic reference.
 * [STATEMENT](types/STATEMENT.md)  ([ValueSet](types/ValueSet.md))  - An atomic assertion about a CTS2 resource.
 * [STATUS](types/STATUS.md)  ([ValueSet](types/ValueSet.md))  - The state of a resource or other entry in an external workflow.
 * [VALUESET](types/VALUESET.md)  ([ValueSet](types/ValueSet.md))  - A set of entity references.
 * [VALUESETDEFINITION](types/VALUESETDEFINITION.md)  ([ValueSet](types/ValueSet.md))  - A set of rules that can be applied to specified versions or one or more code systems to yield a set of entity
 * [VERSIONTAG](types/VERSIONTAG.md)  ([ValueSet](types/ValueSet.md))  - An identifier that can be assigned to resource versions by a service implementation to identify their state
 * [ValueSet](types/ValueSet.md)  (**URIorCURIE**)  - A URI that can be indirectly resolved to a set of entity descriptions
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
