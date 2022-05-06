# Class: NamedThing
_A generic grouping for any identifiable entity_





URI: [my_datamodel:NamedThing](https://w3id.org/my_org/my_datamodelNamedThing)




## Inheritance

* **NamedThing**
    * [Person](Person.md) [ HasAliases]
    * [Organization](Organization.md) [ HasAliases]




## Slots

| Name | Range | Cardinality | Description  | Info |
| ---  | --- | --- | --- | --- |
| [id](id.md) | [string](string.md) | 0..1 | None  | . |
| [name](name.md) | [string](string.md) | 0..1 | None  | . |
| [description](description.md) | [string](string.md) | 0..1 | None  | . |
| [image](image.md) | [string](string.md) | 0..1 | None  | . |


## Usages



## Identifier and Mapping Information









## LinkML Specification

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: NamedThing
close_mappings:
- schema:Thing
description: A generic grouping for any identifiable entity
from_schema: https://w3id.org/my_org/my_datamodel
slots:
- id
- name
- description
- image

```
</details>

### Induced

<details>
```yaml
name: NamedThing
close_mappings:
- schema:Thing
description: A generic grouping for any identifiable entity
from_schema: https://w3id.org/my_org/my_datamodel
attributes:
  id:
    name: id
    from_schema: https://w3id.org/my_org/my_datamodel
    slot_uri: schema:identifier
    identifier: true
    alias: id
    owner: NamedThing
    range: string
  name:
    name: name
    from_schema: https://w3id.org/my_org/my_datamodel
    slot_uri: schema:name
    alias: name
    owner: NamedThing
    range: string
  description:
    name: description
    from_schema: https://w3id.org/my_org/my_datamodel
    slot_uri: schema:description
    alias: description
    owner: NamedThing
    range: string
  image:
    name: image
    from_schema: https://w3id.org/my_org/my_datamodel
    slot_uri: schema:image
    alias: image
    owner: NamedThing
    range: string

```
</details>