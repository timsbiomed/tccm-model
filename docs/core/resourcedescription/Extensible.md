
# Type: extensible


mixin for classes that support extension

URI: [tccm:Extensible](https://hotecosystem.org/tccm/Extensible)


![img](http://yuml.me/diagram/nofunky;dir:TB/class/[Extension],[Extension]<extensions%200..*-++[Extensible],[ResourceDescription]uses%20-.->[Extensible],[ResourceDescription])

## Mixin for

 * [ResourceDescription](ResourceDescription.md) (mixin)  - ResourceDescription represents the shared characteristics common to both abstract and resource version descriptions. ResourceDescription is an abstract type and, as such, cannot be directly created. Resource descriptions are Changeable, meaning that they have identity and can be created, updated, and deleted.

## Referenced by class


## Attributes


### Own

 * [extensions](extensions.md)  <sub>0..*</sub>
    * Description: a tag/text tuple attached to an arbitrary element
    * range: [Extension](Extension.md)
