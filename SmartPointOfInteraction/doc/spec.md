<!-- 10-Header -->      
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)      
Entity: SmartPointOfInteraction      
===============================<!-- /10-Header -->      
<!-- 15-License -->      
[Open License](https://github.com/smart-data-models//dataModel.PointOfInteraction/blob/master/SmartPointOfInteraction/LICENSE.md)      
[document generated automatically](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)      
<!-- /15-License -->      
<!-- 20-Description -->      
Global description: **Smart Data Models Smart Point of Interaction entity schema intended for validation tools**      
version: 0.0.2      
<!-- /20-Description -->      
<!-- 30-PropertiesList -->      
## List of properties      
<sup><sub>[*] If there is not a type in an attribute is because it could have several types or different formats/patterns</sub></sup>      
- `address[object]`: The mailing address  . Model: [https://schema.org/address](https://schema.org/address)	- `addressCountry[string]`: The country. For example, Spain  . Model: [https://schema.org/addressCountry](https://schema.org/addressCountry)      
	- `addressLocality[string]`: The locality in which the street address is, and which is in the region  . Model: [https://schema.org/addressLocality](https://schema.org/addressLocality)      
	- `addressRegion[string]`: The region in which the locality is, and which is in the country  . Model: [https://schema.org/addressRegion](https://schema.org/addressRegion)      
	- `district[string]`: A district is a type of administrative division that, in some countries, is managed by the local government        
	- `postOfficeBoxNumber[string]`: The post office box number for PO box addresses. For example, 03578  . Model: [https://schema.org/postOfficeBoxNumber](https://schema.org/postOfficeBoxNumber)      
	- `postalCode[string]`: The postal code. For example, 24004  . Model: [https://schema.org/https://schema.org/postalCode](https://schema.org/https://schema.org/postalCode)      
	- `streetAddress[string]`: The street address  . Model: [https://schema.org/streetAddress](https://schema.org/streetAddress)      
- `alternateName[string]`: An alternative name for this item  - `applicationUrl[uri]`: This field specifies the real URL containing the solution or application (information, co-creation, etc) while the SmartSpot 'announcedUrl' field specifies the broadcast URL which could be this same URL or a shortened one  . Model: [https://schema.org/URL](https://schema.org/URL)- `areaCovered[*]`: Geojson reference to the item. It can be Point, LineString, Polygon, MultiPoint, MultiLineString or MultiPolygon  - `areaServed[string]`: The geographic area where a service or offered item is provided  . Model: [https://schema.org/Text](https://schema.org/Text)- `availability[string]`: Specifies the time intervals in which this interactive service is generally available. It is noteworthy that Smart Spots have their own real availability in order to allow advanced configurations. The syntax must be conformant with schema.org. For instance, a service which is only active on weekdays will be encoded as 'availability': 'Mo,Tu,We,Th,Fr,Sa 09:00-20:00'  . Model: [https://schema.org/openingHours](https://schema.org/openingHours)- `category[array]`: Defines the type of interaction. Enum:'co-creation, entertainment, information, infotainment'  . Model: [http://schema.org/Text](http://schema.org/Text)- `dataProvider[string]`: A sequence of characters identifying the provider of the harmonised data entity  - `dateCreated[date-time]`: Entity creation timestamp. This will usually be allocated by the storage platform  - `dateModified[date-time]`: Timestamp of the last modification of the entity. This will usually be allocated by the storage platform  - `description[string]`: A description of this item  - `id[*]`: Unique identifier of the entity  - `location[*]`: Geojson reference to the item. It can be Point, LineString, Polygon, MultiPoint, MultiLineString or MultiPolygon  - `name[string]`: The name of this item  - `owner[array]`: A List containing a JSON encoded sequence of characters referencing the unique Ids of the owner(s)  - `refRelatedEntity[array]`: List of entities improved with this Smart Point of Interaction  . Model: [The entity type could be any such as a Parking, Point of Interest, etc.http://schema.org/Text](The entity type could be any such as a Parking, Point of Interest, etc.http://schema.org/Text)- `refSmartSpot[array]`:  References to the Smart Spot devices which are part of the Smart Point of Interaction  . Model: [https://schema.org/URL](https://schema.org/URL)- `seeAlso[*]`: list of uri pointing to additional resources about the item  - `source[string]`: A sequence of characters giving the original source of the entity data as a URL. Recommended to be the fully qualified domain name of the source provider, or the URL to the source object  - `type[string]`: NGSI Entity type. It has to be SmartPointOfInteraction  <!-- /30-PropertiesList -->      
<!-- 35-RequiredProperties -->      
Required properties      
- `id`  - `type`  <!-- /35-RequiredProperties -->      
<!-- 40-RequiredProperties -->      
A Smart Point of Interaction defines a place with technology to interact with users, for example, through Beacon technology from Apple, Eddystone/Physical-Web from Google or other proximity-based interfaces. Since the interactive area could be composed by more than one device providing the technology, this model encompasses a group of SmartSpot devices. The data model includes information regarding the area/surface covered by the technology (i.e., the area covered by Bluetooth Low Energy-based Beacon), a way to specify the functionality intervals (i.e. when interactive points are available) and a link to a multimedia resource intended to user interaction (i.e. Web Apps, etc.). Additionally, the data model may reference to another NGSI entity such as a Parking, a Point of Interest (POI), etc. with enriched interaction provided by this Smart Point of Interaction.      
<!-- /40-RequiredProperties -->      
<!-- 50-DataModelHeader -->      
## Data Model description of properties      
Sorted alphabetically (click for details)      
<!-- /50-DataModelHeader -->      
<!-- 60-ModelYaml -->      
<details><summary><strong>full yaml details</strong></summary>        
```yaml      
SmartPointOfInteraction:        
  description: Smart Data Models Smart Point of Interaction entity schema intended for validation tools        
  properties:        
    address:        
      description: The mailing address        
      properties:        
        addressCountry:        
          description: 'The country. For example, Spain'        
          type: string        
          x-ngsi:        
            model: https://schema.org/addressCountry        
            type: Property        
        addressLocality:        
          description: 'The locality in which the street address is, and which is in the region'        
          type: string        
          x-ngsi:        
            model: https://schema.org/addressLocality        
            type: Property        
        addressRegion:        
          description: 'The region in which the locality is, and which is in the country'        
          type: string        
          x-ngsi:        
            model: https://schema.org/addressRegion        
            type: Property        
        district:        
          description: 'A district is a type of administrative division that, in some countries, is managed by the local government'        
          type: string        
          x-ngsi:        
            type: Property        
        postOfficeBoxNumber:        
          description: 'The post office box number for PO box addresses. For example, 03578'        
          type: string        
          x-ngsi:        
            model: https://schema.org/postOfficeBoxNumber        
            type: Property        
        postalCode:        
          description: 'The postal code. For example, 24004'        
          type: string        
          x-ngsi:        
            model: https://schema.org/https://schema.org/postalCode        
            type: Property        
        streetAddress:        
          description: The street address        
          type: string        
          x-ngsi:        
            model: https://schema.org/streetAddress        
            type: Property        
        streetNr:        
          description: Number identifying a specific property on a public street        
          type: string        
          x-ngsi:        
            type: Property        
      type: object        
      x-ngsi:        
        model: https://schema.org/address        
        type: Property        
    alternateName:        
      description: An alternative name for this item        
      type: string        
      x-ngsi:        
        type: Property        
    applicationUrl:        
      description: 'This field specifies the real URL containing the solution or application (information, co-creation, etc) while the SmartSpot ''announcedUrl'' field specifies the broadcast URL which could be this same URL or a shortened one'        
      format: uri        
      type: string        
      x-ngsi:        
        model: https://schema.org/URL        
        type: Property        
    areaCovered:        
      description: 'Geojson reference to the item. It can be Point, LineString, Polygon, MultiPoint, MultiLineString or MultiPolygon'        
      oneOf:        
        - description: Geojson reference to the item. Point        
          properties:        
            bbox:        
              items:        
                type: number        
              minItems: 4        
              type: array        
            coordinates:        
              items:        
                type: number        
              minItems: 2        
              type: array        
            type:        
              enum:        
                - Point        
              type: string        
          required:        
            - type        
            - coordinates        
          title: GeoJSON Point        
          type: object        
          x-ngsi:        
            type: GeoProperty        
        - description: Geojson reference to the item. LineString        
          properties:        
            bbox:        
              items:        
                type: number        
              minItems: 4        
              type: array        
            coordinates:        
              items:        
                items:        
                  type: number        
                minItems: 2        
                type: array        
              minItems: 2        
              type: array        
            type:        
              enum:        
                - LineString        
              type: string        
          required:        
            - type        
            - coordinates        
          title: GeoJSON LineString        
          type: object        
          x-ngsi:        
            type: GeoProperty        
        - description: Geojson reference to the item. Polygon        
          properties:        
            bbox:        
              items:        
                type: number        
              minItems: 4        
              type: array        
            coordinates:        
              items:        
                items:        
                  items:        
                    type: number        
                  minItems: 2        
                  type: array        
                minItems: 4        
                type: array        
              type: array        
            type:        
              enum:        
                - Polygon        
              type: string        
          required:        
            - type        
            - coordinates        
          title: GeoJSON Polygon        
          type: object        
          x-ngsi:        
            type: GeoProperty        
        - description: Geojson reference to the item. MultiPoint        
          properties:        
            bbox:        
              items:        
                type: number        
              minItems: 4        
              type: array        
            coordinates:        
              items:        
                items:        
                  type: number        
                minItems: 2        
                type: array        
              type: array        
            type:        
              enum:        
                - MultiPoint        
              type: string        
          required:        
            - type        
            - coordinates        
          title: GeoJSON MultiPoint        
          type: object        
          x-ngsi:        
            type: GeoProperty        
        - description: Geojson reference to the item. MultiLineString        
          properties:        
            bbox:        
              items:        
                type: number        
              minItems: 4        
              type: array        
            coordinates:        
              items:        
                items:        
                  items:        
                    type: number        
                  minItems: 2        
                  type: array        
                minItems: 2        
                type: array        
              type: array        
            type:        
              enum:        
                - MultiLineString        
              type: string        
          required:        
            - type        
            - coordinates        
          title: GeoJSON MultiLineString        
          type: object        
          x-ngsi:        
            type: GeoProperty        
        - description: Geojson reference to the item. MultiLineString        
          properties:        
            bbox:        
              items:        
                type: number        
              minItems: 4        
              type: array        
            coordinates:        
              items:        
                items:        
                  items:        
                    items:        
                      type: number        
                    minItems: 2        
                    type: array        
                  minItems: 4        
                  type: array        
                type: array        
              type: array        
            type:        
              enum:        
                - MultiPolygon        
              type: string        
          required:        
            - type        
            - coordinates        
          title: GeoJSON MultiPolygon        
          type: object        
          x-ngsi:        
            type: GeoProperty        
      x-ngsi:        
        type: GeoProperty        
    areaServed:        
      description: The geographic area where a service or offered item is provided        
      type: string        
      x-ngsi:        
        model: https://schema.org/Text        
        type: Property        
    availability:        
      description: 'Specifies the time intervals in which this interactive service is generally available. It is noteworthy that Smart Spots have their own real availability in order to allow advanced configurations. The syntax must be conformant with schema.org. For instance, a service which is only active on weekdays will be encoded as ''availability'': ''Mo,Tu,We,Th,Fr,Sa 09:00-20:00'''        
      type: string        
      x-ngsi:        
        model: https://schema.org/openingHours        
        type: Property        
    category:        
      description: 'Defines the type of interaction. Enum:''co-creation, entertainment, information, infotainment'''        
      items:        
        enum:        
          - co-creation        
          - entertainment        
          - information        
          - infotainment        
        type: string        
      minItems: 1        
      type: array        
      uniqueItems: true        
      x-ngsi:        
        model: http://schema.org/Text        
        type: Property        
    dataProvider:        
      description: A sequence of characters identifying the provider of the harmonised data entity        
      type: string        
      x-ngsi:        
        type: Property        
    dateCreated:        
      description: Entity creation timestamp. This will usually be allocated by the storage platform        
      format: date-time        
      type: string        
      x-ngsi:        
        type: Property        
    dateModified:        
      description: Timestamp of the last modification of the entity. This will usually be allocated by the storage platform        
      format: date-time        
      type: string        
      x-ngsi:        
        type: Property        
    description:        
      description: A description of this item        
      type: string        
      x-ngsi:        
        type: Property        
    id:        
      anyOf:        
        - description: Identifier format of any NGSI entity        
          maxLength: 256        
          minLength: 1        
          pattern: ^[\w\-\.\{\}\$\+\*\[\]`|~^@!,:\\]+$        
          type: string        
          x-ngsi:        
            type: Property        
        - description: Identifier format of any NGSI entity        
          format: uri        
          type: string        
          x-ngsi:        
            type: Property        
      description: Unique identifier of the entity        
      x-ngsi:        
        type: Property        
    location:        
      description: 'Geojson reference to the item. It can be Point, LineString, Polygon, MultiPoint, MultiLineString or MultiPolygon'        
      oneOf:        
        - description: Geojson reference to the item. Point        
          properties:        
            bbox:        
              items:        
                type: number        
              minItems: 4        
              type: array        
            coordinates:        
              items:        
                type: number        
              minItems: 2        
              type: array        
            type:        
              enum:        
                - Point        
              type: string        
          required:        
            - type        
            - coordinates        
          title: GeoJSON Point        
          type: object        
          x-ngsi:        
            type: GeoProperty        
        - description: Geojson reference to the item. LineString        
          properties:        
            bbox:        
              items:        
                type: number        
              minItems: 4        
              type: array        
            coordinates:        
              items:        
                items:        
                  type: number        
                minItems: 2        
                type: array        
              minItems: 2        
              type: array        
            type:        
              enum:        
                - LineString        
              type: string        
          required:        
            - type        
            - coordinates        
          title: GeoJSON LineString        
          type: object        
          x-ngsi:        
            type: GeoProperty        
        - description: Geojson reference to the item. Polygon        
          properties:        
            bbox:        
              items:        
                type: number        
              minItems: 4        
              type: array        
            coordinates:        
              items:        
                items:        
                  items:        
                    type: number        
                  minItems: 2        
                  type: array        
                minItems: 4        
                type: array        
              type: array        
            type:        
              enum:        
                - Polygon        
              type: string        
          required:        
            - type        
            - coordinates        
          title: GeoJSON Polygon        
          type: object        
          x-ngsi:        
            type: GeoProperty        
        - description: Geojson reference to the item. MultiPoint        
          properties:        
            bbox:        
              items:        
                type: number        
              minItems: 4        
              type: array        
            coordinates:        
              items:        
                items:        
                  type: number        
                minItems: 2        
                type: array        
              type: array        
            type:        
              enum:        
                - MultiPoint        
              type: string        
          required:        
            - type        
            - coordinates        
          title: GeoJSON MultiPoint        
          type: object        
          x-ngsi:        
            type: GeoProperty        
        - description: Geojson reference to the item. MultiLineString        
          properties:        
            bbox:        
              items:        
                type: number        
              minItems: 4        
              type: array        
            coordinates:        
              items:        
                items:        
                  items:        
                    type: number        
                  minItems: 2        
                  type: array        
                minItems: 2        
                type: array        
              type: array        
            type:        
              enum:        
                - MultiLineString        
              type: string        
          required:        
            - type        
            - coordinates        
          title: GeoJSON MultiLineString        
          type: object        
          x-ngsi:        
            type: GeoProperty        
        - description: Geojson reference to the item. MultiLineString        
          properties:        
            bbox:        
              items:        
                type: number        
              minItems: 4        
              type: array        
            coordinates:        
              items:        
                items:        
                  items:        
                    items:        
                      type: number        
                    minItems: 2        
                    type: array        
                  minItems: 4        
                  type: array        
                type: array        
              type: array        
            type:        
              enum:        
                - MultiPolygon        
              type: string        
          required:        
            - type        
            - coordinates        
          title: GeoJSON MultiPolygon        
          type: object        
          x-ngsi:        
            type: GeoProperty        
      x-ngsi:        
        type: GeoProperty        
    name:        
      description: The name of this item        
      type: string        
      x-ngsi:        
        type: Property        
    owner:        
      description: A List containing a JSON encoded sequence of characters referencing the unique Ids of the owner(s)        
      items:        
        anyOf:        
          - description: Identifier format of any NGSI entity        
            maxLength: 256        
            minLength: 1        
            pattern: ^[\w\-\.\{\}\$\+\*\[\]`|~^@!,:\\]+$        
            type: string        
            x-ngsi:        
              type: Property        
          - description: Identifier format of any NGSI entity        
            format: uri        
            type: string        
            x-ngsi:        
              type: Property        
        description: Unique identifier of the entity        
        x-ngsi:        
          type: Property        
      type: array        
      x-ngsi:        
        type: Property        
    refRelatedEntity:        
      description: List of entities improved with this Smart Point of Interaction        
      items:        
        anyOf:        
          - description: Identifier format of any NGSI entity        
            maxLength: 256        
            minLength: 1        
            pattern: ^[\w\-\.\{\}\$\+\*\[\]`|~^@!,:\\]+$        
            type: string        
            x-ngsi:        
              type: Property        
          - description: Identifier format of any NGSI entity        
            format: uri        
            type: string        
            x-ngsi:        
              type: Property        
        description: Unique identifier of the entity        
        x-ngsi:        
          type: Property        
      minItems: 1        
      type: array        
      uniqueItems: true        
      x-ngsi:        
        model: 'The entity type could be any such as a Parking, Point of Interest, etc.http://schema.org/Text'        
        type: Relationship        
    refSmartSpot:        
      description: ' References to the Smart Spot devices which are part of the Smart Point of Interaction'        
      items:        
        anyOf:        
          - description: Identifier format of any NGSI entity        
            maxLength: 256        
            minLength: 1        
            pattern: ^[\w\-\.\{\}\$\+\*\[\]`|~^@!,:\\]+$        
            type: string        
            x-ngsi:        
              type: Property        
          - description: Identifier format of any NGSI entity        
            format: uri        
            type: string        
            x-ngsi:        
              type: Property        
        description: Unique identifier of the entity        
        x-ngsi:        
          type: Property        
      minItems: 1        
      type: array        
      uniqueItems: true        
      x-ngsi:        
        model: https://schema.org/URL        
        type: Property        
    seeAlso:        
      description: list of uri pointing to additional resources about the item        
      oneOf:        
        - items:        
            format: uri        
            type: string        
          minItems: 1        
          type: array        
        - format: uri        
          type: string        
      x-ngsi:        
        type: Property        
    source:        
      description: 'A sequence of characters giving the original source of the entity data as a URL. Recommended to be the fully qualified domain name of the source provider, or the URL to the source object'        
      type: string        
      x-ngsi:        
        type: Property        
    type:        
      description: NGSI Entity type. It has to be SmartPointOfInteraction        
      enum:        
        - SmartPointOfInteraction        
      type: string        
      x-ngsi:        
        type: Property        
  required:        
    - id        
    - type        
  type: object        
  x-derived-from: ""        
  x-disclaimer: 'Redistribution and use in source and binary forms, with or without modification, are permitted  provided that the license conditions are met. Copyleft (c) 2022 Contributors to Smart Data Models Program'        
  x-license-url: https://github.com/smart-data-models/dataModel.PointOfInteraction/blob/master/SmartPointOfInteraction/LICENSE.md        
  x-model-schema: https://smart-data-models.github.io/dataModel.PointOfInteraction/SmartPointOfInteraction/schema.json        
  x-model-tags: ""        
  x-version: 0.0.2        
```      
</details>        
<!-- /60-ModelYaml -->      
<!-- 70-MiddleNotes -->      
<!-- /70-MiddleNotes -->      
<!-- 80-Examples -->      
## Example payloads        
#### SmartPointOfInteraction NGSI-v2 key-values Example        
Here is an example of a SmartPointOfInteraction in JSON-LD format as key-values. This is compatible with NGSI-v2 when  using `options=keyValues` and returns the context data of an individual entity.      
<details><summary><strong>show/hide example</strong></summary>        
```json  
{  
  "id": "SPOI-ES-4326",  
  "type": "SmartPointOfInteraction",  
  "category": [  
    "co-creation"  
  ],  
  "areaCovered": {  
    "type": "Polygon",  
    "coordinates": [  
      [  
        [  
          25.774,  
          -80.19  
        ],  
        [  
          18.466,  
          -66.118  
        ],  
        [  
          32.321,  
          -64.757  
        ],  
        [  
          25.774,  
          -80.19  
        ]  
      ]  
    ]  
  },  
  "applicationUrl": "http://www.example.org",  
  "availability": "Tu,Th 16:00-20:00",  
  "refRelatedEntity": [  
    "POI-PlazaCazorla-3123"  
  ],  
  "refSmartSpot": [  
    "SSPOT-F94C58E29DD5",  
    "SSPOT-F94C53E21DD2",  
    "SSPOT-F94C51A295D9"  
  ]  
}  
```  
</details>      
#### SmartPointOfInteraction NGSI-v2 normalized Example        
Here is an example of a SmartPointOfInteraction in JSON-LD format as normalized. This is compatible with NGSI-v2 when not using options and returns the context data of an individual entity.      
<details><summary><strong>show/hide example</strong></summary>        
```json  
{  
  "id": "SPOI-ES-4326",  
  "type": "SmartPointOfInteraction",  
  "category": {  
    "type": "StructuredValue",  
    "value": [  
      "co-creation"  
    ]  
  },  
  "applicationUrl": {  
    "type": "Text",  
    "value": "http://www.example.org"  
  },  
  "areaCovered": {  
    "type": "geo:json",  
    "value": {  
      "type": "Polygon",  
      "coordinates": [  
        [  
          [  
            25.774,  
            -80.19  
          ],  
          [  
            18.466,  
            -66.118  
          ],  
          [  
            32.321,  
            -64.757  
          ],  
          [  
            25.774,  
            -80.19  
          ]  
        ]  
      ]  
    }  
  },  
  "availability": {  
    "type": "Text",  
    "value": "Tu,Th 16:00-20:00"  
  },  
  "refSmartSpot": {  
    "type": "StructuredValue",  
    "value": [  
      "SSPOT-F94C58E29DD5",  
      "SSPOT-F94C53E21DD2",  
      "SSPOT-F94C51A295D9"  
    ]  
  },  
  "refRelatedEntity": {  
    "type": "StructuredValue",  
    "value": [  
      "POI-PlazaCazorla-3123"  
    ]  
  }  
}  
```  
</details>      
#### SmartPointOfInteraction NGSI-LD key-values Example        
Here is an example of a SmartPointOfInteraction in JSON-LD format as key-values. This is compatible with NGSI-LD when  using `options=keyValues` and returns the context data of an individual entity.      
<details><summary><strong>show/hide example</strong></summary>        
```json  
{  
  "id": "urn:ngsi-ld:SmartPointOfInteraction:SPOI-ES-4326",  
  "type": "SmartPointOfInteraction",  
  "applicationUrl": "http://www.example.org",  
  "areaCovered": {  
    "coordinates": [  
      [  
        [  
          25.774,  
          -80.19  
        ],  
        [  
          18.466,  
          -66.118  
        ],  
        [  
          32.321,  
          -64.757  
        ],  
        [  
          25.774,  
          -80.19  
        ]  
      ]  
    ],  
    "type": "Polygon"  
  },  
  "availability": "Tu,Th 16:00-20:00",  
  "category": [  
    "co-creation"  
  ],  
  "refRelatedEntity": [  
    "urn:ngsi-ld:RelatedEntity:POI-PlazaCazorla-3123"  
  ],  
  "refSmartSpot": [  
    "urn:ngsi-ld:SmartSpot:SSPOT-F94C58E29DD5",  
    "urn:ngsi-ld:SmartSpot:SSPOT-F94C53E21DD2",  
    "urn:ngsi-ld:SmartSpot:SSPOT-F94C51A295D9"  
  ],  
  "@context": [  
    "https://uri.etsi.org/ngsi-ld/v1/ngsi-ld-core-context.jsonld",  
    "https://raw.githubusercontent.com/smart-data-models/dataModel.PointOfInteraction/master/context.jsonld"  
  ]  
}  
```  
</details>      
#### SmartPointOfInteraction NGSI-LD normalized Example        
Here is an example of a SmartPointOfInteraction in JSON-LD format as normalized. This is compatible with NGSI-LD when not using options and returns the context data of an individual entity.      
<details><summary><strong>show/hide example</strong></summary>        
```json  
{  
    "id": "urn:ngsi-ld:SmartPointOfInteraction:SPOI-ES-4326",  
    "type": "SmartPointOfInteraction",  
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
                    [  
                        25.774,  
                        -80.19  
                    ],  
                    [  
                        18.466,  
                        -66.118  
                    ],  
                    [  
                        32.321,  
                        -64.757  
                    ],  
                    [  
                        25.774,  
                        -80.19  
                    ]  
                ]  
            ]  
        }  
    },  
    "availability": {  
        "type": "Property",  
        "value": "Tu,Th 16:00-20:00"  
    },  
    "category": {  
        "type": "Property",  
        "value": [  
            "co-creation"  
        ]  
    },  
    "refRelatedEntity": {  
        "type": "Relationship",  
        "object": [  
            "urn:ngsi-ld:RelatedEntity:POI-PlazaCazorla-3123"  
        ]  
    },  
    "refSmartSpot": {  
        "type": "Relationship",  
        "object": [  
            "urn:ngsi-ld:SmartSpot:SSPOT-F94C58E29DD5",  
            "urn:ngsi-ld:SmartSpot:SSPOT-F94C53E21DD2",  
            "urn:ngsi-ld:SmartSpot:SSPOT-F94C51A295D9"  
        ]  
    },  
    "@context": [  
        "https://uri.etsi.org/ngsi-ld/v1/ngsi-ld-core-context.jsonld",  
        "https://raw.githubusercontent.com/smart-data-models/dataModel.PointOfInteraction/master/context.jsonld"  
    ]  
}  
```  
</details><!-- /80-Examples -->      
<!-- 90-FooterNotes -->      
<!-- /90-FooterNotes -->      
<!-- 95-Units -->      
See [FAQ 10](https://smartdatamodels.org/index.php/faqs/) to get an answer on how to deal with magnitude units      
<!-- /95-Units -->      
<!-- 97-LastFooter -->      
---      
[Smart Data Models](https://smartdatamodels.org) +++ [Contribution Manual](https://bit.ly/contribution_manual) +++ [About](https://bit.ly/Introduction_SDM)<!-- /97-LastFooter -->      
