
# Type: ValueSetDefinition


A ValueSetDefinition describes the rules that determine which entity references (value meanings) belong to a
value set at a given point in time. The definition of what belongs in a value set can evolve over time, and it
is possible for there to be multiple definitions active at any given point in time - perhaps one for a system
in general use, a second for a newer system, and a third for testing. A ValueSetDefinition may or may not
identify a specific version of a code system. The decision of which version is to be used depends on the context
and needs of the community. ValueSetDefinition and the supporting model has been designed to allow multiple
variations on the “binding” of definitions to value sets, code system versions to definitions, and the
combination to concept domains.

URI: [tccm:ValueSetDefinition](https://hotecosystem.org/tccm/ValueSetDefinition)


![img](images/ValueSetDefinition.svg)

## Parents

 *  is_a: [ResourceVersionDescription](ResourceVersionDescription.md) - Information about the source, format, release date, version identifier, etc. of a specific version of an

## Referenced by class


## Attributes


### Own

 * [ValueSetDefinition➞definitionOf](ValueSetDefinition_definitionOf.md)  <sub>OPT</sub>
    * Description: A reference to the value set being defined.
    * range: [ValueSetReference](ValueSetReference.md)
 * [ValueSetDefinition➞entry](ValueSetDefinition_entry.md)  <sub>1..*</sub>
    * Description: A component in a value set definitio
    * range: [ValueSetDefinitionEntry](ValueSetDefinitionEntry.md)
 * [ValueSetDefinition➞versionTag](ValueSetDefinition_versionTag.md)  <sub>0..*</sub>
    * Description: A version tag assigned to this definition by the implementing service.
    * range: [VersionTagReference](VersionTagReference.md)

### Inherited from ResourceVersionDescription:

 * [resourceID](resourceID.md)  <sub>REQ</sub>
    * Description: A local identifier that uniquely names the resource within the context of the describedResourceType and
implementing service. As an example, this might be “SCT” for the SNOMED-CT code system, “SCT-2010AA” for a
SNOMED-CT code system version.
    * range: [LocalIdentifier](types/LocalIdentifier.md)
 * [resourceSynopsis](resourceSynopsis.md)  <sub>OPT</sub>
    * Description: A textual summary of the resource - what it is, what it is for, etc.
    * range: [String](types/String.md)
