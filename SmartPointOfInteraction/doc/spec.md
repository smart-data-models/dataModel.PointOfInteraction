# SmartPointOfInteraction

## Description

A Smart Point of Interaction defines a place with technology to interact with
users, for example, through Beacon technology from Apple, Eddystone/Physical-Web
from Google or other proximity-based interfaces. Since the interactive area
could be composed by more than one device providing the technology, this model
encompasses a group of SmartSpot devices.

The data model includes information regarding the area/surface covered by the
technology (i.e., the area covered by Bluetooth Low Energy-based Beacon), a way
to specify the functionality intervals (i.e. when interactive points are
available) and a link to a multimedia resource intended to user interaction
(i.e. Web Apps, etc.). Additionally, the data model may reference to another
NGSI entity such as a Parking, a Point of Interest (POI), etc. with enriched
interaction provided by this Smart Point of Interaction.

## Data Model

The data model is defined as shown below:

-   `id` : Unique identifier.

-   `type` : Entity type. It must be equal to `SmartPointOfInteraction`.

-   `source` : A sequence of characters giving the source of the entity data.

    -   Attribute type: Property. [Text](https://schema.org/Text) or
        [URL](https://schema.org/URL)
    -   Optional

-   `dataProvider` : Specifies the URL to information about the provider of this
    information

    -   Attribute type: Property. [URL](https://schema.org/URL)
    -   Optional

-   `category` : Defines the type of interaction.

    -   Attribute type: Property. List of [Text](http://schema.org/Text)
    -   Allowed values: `information`, `entertainment`, `infotainment`,
        `co-creation` or any other extended value defined by the application.
    -   Mandatory

-   `areaCovered` : Defines the area covered by the Smart Point of Interaction
    using geoJSON format. It can be represented by a feature of type `Polygon`
    or `Multipolygon`.

    -   Attribute type: Property. `geo:json`.
    -   Normative References:
        [https://tools.ietf.org/html/rfc7946](https://tools.ietf.org/html/rfc7946)
    -   Optional

-   `applicationUrl` : This field specifies the real URL containing the solution
    or application (information, co-creation, etc) while the SmartSpot
    'announcedUrl' field specifies the broadcasted URL which could be this same
    URL or a shortened one.

    -   Attribute type: Property. [URL](https://schema.org/URL)
    -   Mandatory

-   `availability`: Specifies the time intervals in which this interactive
    service is generally available. It is noteworthy that Smart Spots have their
    own real availability in order to allow advanced configurations. The syntax
    must be conformant with schema.org
    [openingHours specification](https://schema.org/openingHours). For instance,
    a service which is only active on dayweeks will be encoded as
    "availability": "Mo,Tu,We,Th,Fr,Sa 09:00-20:00".

    -   Attribute type: Property. [Text](https://schema.org/Text)
    -   Mandatory.

-   `refRelatedEntity` : List of entities improved with this Smart Point of
    Interaction. The entity type could be any such as a “Parking”, “Point of
    Interest”, etc.

    -   Attribute type: Relationship. List of references to entities.
    -   Optional

-   `refSmartSpot` : References to the “Smart Spot” devices which are part of
    the Smart Point of Interaction.
    -   Attribute type: Relationship. Reference to one or more entities of type
        [SmartSpot](../../SmartSpot/doc/spec.md)
    -   Optional

**Note**: JSON Schemas are intended to capture the data type and associated
constraints of the different Attributes, regardless their final representation
format in NGSI(v2, LD).

## Examples

### Normalized Example

Normalized NGSI response

```json
{
    "id": "SPOI-ES-4326",
    "type": "SmartPointOfInteraction",
    "category": {
        "value": ["co-creation"]
    },
    "applicationUrl": {
        "type": "URL",
        "value": "http://www.example.org"
    },
    "areaCovered": {
        "value": {
            "type": "Polygon",
            "coordinates": [
                [
                    [25.774, -80.19],
                    [18.466, -66.118],
                    [32.321, -64.757],
                    [25.774, -80.19]
                ]
            ]
        }
    },
    "availability": {
        "value": "Tu,Th 16:00-20:00"
    },
    "refSmartSpot": {
        "type": "Relationship",
        "value": [
            "SSPOT-F94C58E29DD5",
            "SSPOT-F94C53E21DD2",
            "SSPOT-F94C51A295D9"
        ]
    },
    "refRelatedEntity": {
        "type": "Relationship",
        "value": ["POI-PlazaCazorla-3123"]
    }
}
```

### key-value pairs Example

Sample uses simplified representation for data consumers `?options=keyValues`

```json
{
    "id": "SPOI-ES-4326",
    "type": "SmartPointOfInteraction",
    "category": ["co-creation"],
    "areaCovered": {
        "type": "Polygon",
        "coordinates": [
            [
                [25.774, -80.19],
                [18.466, -66.118],
                [32.321, -64.757],
                [25.774, -80.19]
            ]
        ]
    },
    "applicationUrl": "http://www.example.org",
    "availability": "Tu,Th 16:00-20:00",
    "refRelatedEntity": "POI-PlazaCazorla-3123",
    "refSmartSpot": [
        "SSPOT-F94C58E29DD5",
        "SSPOT-F94C53E21DD2",
        "SSPOT-F94C51A295D9"
    ]
}
```

### LD Example

Sample uses the NGSI-LD representation

```json
{
    "id": "urn:ngsi-ld:SmartPointOfInteraction:SPOI-ES-4326",
    "type": "SmartPointOfInteraction",
    "category": {
        "type": "Property",
        "value": ["co-creation"]
    },
    "applicationUrl": {
        "type": "Property",
        "value": "http://www.example.org"
    },
    "areaCovered": {
        "type": "Property",
        "value": {
            "type": "Polygon",
            "coordinates": [
                [
                    [25.774, -80.19],
                    [18.466, -66.118],
                    [32.321, -64.757],
                    [25.774, -80.19]
                ]
            ]
        }
    },
    "availability": {
        "type": "Property",
        "value": "Tu,Th 16:00-20:00"
    },
    "refSmartSpot": {
        "type": "Relationship",
        "object": [
            "urn:ngsi-ld:SmartSpot:SSPOT-F94C58E29DD5",
            "urn:ngsi-ld:SmartSpot:SSPOT-F94C53E21DD2",
            "urn:ngsi-ld:SmartSpot:SSPOT-F94C51A295D9"
        ]
    },
    "refRelatedEntity": {
        "type": "Relationship",
        "object": ["urn:ngsi-ld:RelatedEntity:POI-PlazaCazorla-3123"]
    },
    "@context": [
        "https://schema.lab.fiware.org/ld/context",
        "https://uri.etsi.org/ngsi-ld/v1/ngsi-ld-core-context.jsonld"
    ]
}
```

## Use it with a real service

T.B.D.
