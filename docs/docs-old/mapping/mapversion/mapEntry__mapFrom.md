
# Type: mapEntry__mapFrom


The source entity.  EntityReference must be a member of the fromValueSetDefinition part of the map definition.
EntityReferences in the fromValueSetDefinition that do not occur in a "`mapFrom`" entry are considered as
"unmapped" - meaning that the mapping is incomplete.

URI: [tccm:mapEntry__mapFrom](https://hotecosystem.org/tccm/mapEntry__mapFrom)


## Domain and Range

None ->  <sub>REQ</sub> [EntityReference](EntityReference.md)

## Parents


## Children


## Used by

 * [MapEntry](MapEntry.md)

## Other properties

|  |  |  |
| --- | --- | --- |
| **Comments:** | | At most one of allMatchesFrom or firstMatchFrom must be supplied. |

