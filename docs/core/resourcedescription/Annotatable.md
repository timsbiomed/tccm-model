
# Type: annotatable


mixin for classes that support annotations

URI: [tccm:Annotatable](https://hotecosystem.org/tccm/Annotatable)


![img](http://yuml.me/diagram/nofunky;dir:TB/class/[Annotation],[Annotation]<annotations%200..*-++[Annotatable],[ResourceDescription]uses%20-.->[Annotatable],[ResourceDescription])

## Mixin for

 * [ResourceDescription](ResourceDescription.md) (mixin)  - ResourceDescription represents the shared characteristics common to both abstract and resource version descriptions. ResourceDescription is an abstract type and, as such, cannot be directly created. Resource descriptions are Changeable, meaning that they have identity and can be created, updated, and deleted.

## Referenced by class


## Attributes


### Own

 * [annotations](annotations.md)  <sub>0..*</sub>
    * Description: a collection of tag/text tuples with the semantics of OWL Annotation
    * range: [Annotation](Annotation.md)
