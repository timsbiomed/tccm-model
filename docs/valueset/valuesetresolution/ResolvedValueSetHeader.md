
# Type: ResolvedValueSetHeader


The information required to completely resolve a value set definition.

URI: [tccm:ResolvedValueSetHeader](https://hotecosystem.org/tccm/ResolvedValueSetHeader)


![img](images/ResolvedValueSetHeader.svg)

## Referenced by class

 *  **None** *[➞includesResolvedValueSet](resolvedValueSetHeader__includesResolvedValueSet.md)*  <sub>0..*</sub>  **[ResolvedValueSetHeader](ResolvedValueSetHeader.md)**

## Attributes


### Own

 * [➞includesResolvedValueSet](resolvedValueSetHeader__includesResolvedValueSet.md)  <sub>0..*</sub>
    * Description: If the value set includes other value sets, this contains the resolution information used to resolve the inner
value sets.
    * range: [ResolvedValueSetHeader](ResolvedValueSetHeader.md)
 * [➞resolutionOf](resolvedValueSetHeader__resolutionOf.md)  <sub>REQ</sub>
    * Description: The specific value set definition that was resolved.
    * range: [ValueSetDefinitionReference](ValueSetDefinitionReference.md)
 * [➞resolvedUsingCodeSystem](resolvedValueSetHeader__resolvedUsingCodeSystem.md)  <sub>0..*</sub>
    * Description: A reference to a code system version that was used in the resolution of this value set definition.
    * range: [CodeSystemVersionReference](CodeSystemVersionReference.md)

## Other properties

|  |  |  |
| --- | --- | --- |
| **Comments:** | | A ResolvedValueSetHeader entry carries all of the information that is necessary to completely resolve a value set, meaning that |

