<!-- 10-Header -->
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)  

================================
<!-- 15-License -->


<!-- /15-License -->
<!-- 20-Description -->


<!-- /20-Description -->
<!-- 30-PropertiesList -->




- `address[object]`: L'adresse postale  . Model: [https://schema.org/address](https://schema.org/address)
<!-- 35-RequiredProperties -->

- `id`  
<!-- 40-RequiredProperties -->

<!-- /40-RequiredProperties -->
<!-- 50-DataModelHeader -->


<!-- /50-DataModelHeader -->
<!-- 60-ModelYaml -->
<details><summary><strong>full yaml details</strong></summary>    

SmartPointOfInteraction:    
  description: 'Smart Data Models Smart Point of Interaction entity schema intended for validation tools'    
  properties:    
    address:    
      description: 'The mailing address'    
      properties:    
        addressCountry:    
          description: 'Property. The country. For example, Spain. Model:''https://schema.org/addressCountry'''    
          type: string    
        addressLocality:    
          description: 'Property. The locality in which the street address is, and which is in the region. Model:''https://schema.org/addressLocality'''    
          type: string    
        addressRegion:    
          description: 'Property. The region in which the locality is, and which is in the country. Model:''https://schema.org/addressRegion'''    
          type: string    
        postOfficeBoxNumber:    
          description: 'Property. The post office box number for PO box addresses. For example, 03578. Model:''https://schema.org/postOfficeBoxNumber'''    
          type: string    
        postalCode:    
          description: 'Property. The postal code. For example, 24004. Model:''https://schema.org/https://schema.org/postalCode'''    
          type: string    
        streetAddress:    
          description: 'Property. The street address. Model:''https://schema.org/streetAddress'''    
          type: string    
      type: object    
      x-ngsi:    
        model: https://schema.org/address    
        type: Property    
    alternateName:    
      description: 'An alternative name for this item'    
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
      oneOf: &smartpointofinteraction_-_properties_-_location_-_oneof    
        - description: 'GeoProperty. Geojson reference to the item. Point'    
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
          title: 'GeoJSON Point'    
          type: object    
        - description: 'GeoProperty. Geojson reference to the item. LineString'    
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
          title: 'GeoJSON LineString'    
          type: object    
        - description: 'GeoProperty. Geojson reference to the item. Polygon'    
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
          title: 'GeoJSON Polygon'    
          type: object    
        - description: 'GeoProperty. Geojson reference to the item. MultiPoint'    
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
          title: 'GeoJSON MultiPoint'    
          type: object    
        - description: 'GeoProperty. Geojson reference to the item. MultiLineString'    
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
          title: 'GeoJSON MultiLineString'    
          type: object    
        - description: 'GeoProperty. Geojson reference to the item. MultiLineString'    
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
          title: 'GeoJSON MultiPolygon'    
          type: object    
      x-ngsi:    
        type: GeoProperty    
    areaServed:    
      description: 'The geographic area where a service or offered item is provided'    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    availability:    
      description: 'Specifies the time intervals in which this interactive service is generally available. It is noteworthy that Smart Spots have their own real availability in order to allow advanced configurations. The syntax must be conformant with schema.org. For instance, a service which is only active on weekdays will be encoded as ''availability'': ''Mo,Tu,We,Th,Fr,Sa 09:00-20:00''.'    
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
      description: 'A sequence of characters identifying the provider of the harmonised data entity.'    
      type: string    
      x-ngsi:    
        type: Property    
    dateCreated:    
      description: 'Entity creation timestamp. This will usually be allocated by the storage platform.'    
      format: date-time    
      type: string    
      x-ngsi:    
        type: Property    
    dateModified:    
      description: 'Timestamp of the last modification of the entity. This will usually be allocated by the storage platform.'    
      format: date-time    
      type: string    
      x-ngsi:    
        type: Property    
    description:    
      description: 'A description of this item'    
      type: string    
      x-ngsi:    
        type: Property    
    id:    
      anyOf: &smartpointofinteraction_-_properties_-_owner_-_items_-_anyof    
        - description: 'Property. Identifier format of any NGSI entity'    
          maxLength: 256    
          minLength: 1    
          pattern: ^[\w\-\.\{\}\$\+\*\[\]`|~^@!,:\\]+$    
          type: string    
        - description: 'Property. Identifier format of any NGSI entity'    
          format: uri    
          type: string    
      description: 'Unique identifier of the entity'    
      x-ngsi:    
        type: Property    
    location:    
      description: 'Geojson reference to the item. It can be Point, LineString, Polygon, MultiPoint, MultiLineString or MultiPolygon'    
      oneOf: *smartpointofinteraction_-_properties_-_location_-_oneof    
      x-ngsi:    
        type: GeoProperty    
    name:    
      description: 'The name of this item.'    
      type: string    
      x-ngsi:    
        type: Property    
    owner:    
      description: 'A List containing a JSON encoded sequence of characters referencing the unique Ids of the owner(s)'    
      items:    
        anyOf: *smartpointofinteraction_-_properties_-_owner_-_items_-_anyof    
        description: 'Property. Unique identifier of the entity'    
      type: array    
      x-ngsi:    
        type: Property    
    refRelatedEntity:    
      description: 'List of entities improved with this Smart Point of Interaction'    
      items:    
        anyOf: *smartpointofinteraction_-_properties_-_owner_-_items_-_anyof    
        description: 'Property. Unique identifier of the entity'    
      minItems: 1    
      type: array    
      uniqueItems: true    
      x-ngsi:    
        model: 'The entity type could be any such as a Parking, Point of Interest, etc.http://schema.org/Text'    
        type: Relationship    
    refSmartSpot:    
      description: ' References to the Smart Spot devices which are part of the Smart Point of Interaction'    
      items:    
        anyOf: *smartpointofinteraction_-_properties_-_owner_-_items_-_anyof    
        description: 'Property. Unique identifier of the entity'    
      minItems: 1    
      type: array    
      uniqueItems: true    
      x-ngsi:    
        model: https://schema.org/URL    
        type: Property    
    seeAlso:    
      description: 'list of uri pointing to additional resources about the item'    
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
      description: 'A sequence of characters giving the original source of the entity data as a URL. Recommended to be the fully qualified domain name of the source provider, or the URL to the source object.'    
      type: string    
      x-ngsi:    
        type: Property    
    type:    
      description: 'NGSI Entity type. It has to be SmartPointOfInteraction'    
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
  x-disclaimer: 'Redistribution and use in source and binary forms, with or without modification, are permitted  provided that the license conditions are met. Copyleft (c) 2021 Contributors to Smart Data Models Program'    
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



<details><summary><strong>show/hide example</strong></summary>    


  "id": "SPOI-ES-4326",  
  "type": "SmartPointOfInteraction",  
  "category": ["co-creation"],  
  "areaCovered": {  
    "type": "Polygon",  
    "coordinates": [  
      [[25.774, -80.19], [18.466, -66.118], [32.321, -64.757], [25.774, -80.19]]  
    ]  
  },  
  "applicationUrl": "http://www.example.org",  
  "availability": "Tu,Th 16:00-20:00",  
  "refRelatedEntity": ["POI-PlazaCazorla-3123"],  
  "refSmartSpot": [  
    "SSPOT-F94C58E29DD5",  
    "SSPOT-F94C53E21DD2",  
    "SSPOT-F94C51A295D9"  
  ]  
}  
```  
</details>  


<details><summary><strong>show/hide example</strong></summary>    


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
    "value": ["SSPOT-F94C58E29DD5", "SSPOT-F94C53E21DD2", "SSPOT-F94C51A295D9"]  
  },  
  "refRelatedEntity": {  
    "type": "Relationship",  
    "value": ["POI-PlazaCazorla-3123"]  
  }  
}  
```  
</details>  


<details><summary><strong>show/hide example</strong></summary>    


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
</details>  


<details><summary><strong>show/hide example</strong></summary>    


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
</details><!-- /80-Examples -->
<!-- 90-FooterNotes -->
<!-- /90-FooterNotes -->
<!-- 95-Units -->

<!-- /95-Units -->
<!-- 97-LastFooter -->
---  
