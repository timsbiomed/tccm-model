
# Type: MapEntry


A "complex map" that defines an ordered set of rules for mapping from "`mapFrom`" to one or more targets

URI: [tccm:MapEntry](https://hotecosystem.org/tccm/MapEntry)


![img](images/MapEntry.svg)

## Referenced by class

 *  **None** *[➞entries](fullMapVersion__entries.md)*  <sub>0..*</sub>  **[MapEntry](MapEntry.md)**

## Attributes


### Own

 * [➞allMatchesFrom](mapEntry__allMatchesFrom.md)  <sub>0..*</sub>
    * Description: Process all map sets, returning every set that has a matching target
    * range: [MapSet](MapSet.md)
 * [➞firstMatchFrom](mapEntry__firstMatchFrom.md)  <sub>0..*</sub>
    * Description: Processing stop at the first map set that has a matching target.
    * range: [MapSet](MapSet.md)
 * [➞mapFrom](mapEntry__mapFrom.md)  <sub>REQ</sub>
    * Description: The source entity.  EntityReference must be a member of the fromValueSetDefinition part of the map definition.
EntityReferences in the fromValueSetDefinition that do not occur in a "`mapFrom`" entry are considered as
"unmapped" - meaning that the mapping is incomplete.
    * range: [EntityReference](EntityReference.md)
