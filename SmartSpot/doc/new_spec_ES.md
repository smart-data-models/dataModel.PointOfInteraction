Entidad: SmartSpot  
==================







```yaml  
SmartSpot:    
  description: 'FIWARE Smart Spot entity schema intended for validation tools'    
  properties:    
    alternateName:    
      description: 'An alternative name for this item'    
      type: Property    
    announcedUrl:    
      description: 'URL broadcasted by the device'    
      format: uri    
      type: string    
    announcementPeriod:    
      description: 'Period between announcements in milliseconds'    
      maximum: 4000    
      minimum: 100    
      type: integer    
    availability:    
      description: 'Specifies the time intervals in which this interactive service is available, but this is a general information while Smart Spots have their own real availability in order to allow advanced configurations'    
      type: string    
    bluetoothChannel:    
      description: 'Bluetooth channels where to transmit the announcement'    
      enum:    
        - 37    
        - 38    
        - 39    
        - 37,38    
        - 38,39    
        - 37,39    
        - 37,38,39    
      type: string    
    coverageRadius:    
      description: 'Radius of the spot coverage area in meters'    
      minimum: 1    
      type: integer    
    dataProvider:    
      description: 'A sequence of characters identifying the provider of the harmonised data entity.'    
      type: Property    
    dateCreated:    
      description: 'Entity creation timestamp. This will usually be allocated by the storage platform.'    
      format: date-time    
      type: Property    
    dateModified:    
      description: 'Timestamp of the last modification of the entity. This will usually be allocated by the storage platform.'    
      format: date-time    
      type: Property    
    description:    
      description: 'A description of this item'    
      type: Property    
    id:    
      anyOf: &smartspot_-_properties_-_owner_-_items_-_anyof    
        - description: 'Property. Identifier format of any NGSI entity'    
          maxLength: 256    
          minLength: 1    
          pattern: ^[\w\-\.\{\}\$\+\*\[\]`|~^@!,:\\]+$    
          type: string    
        - description: 'Property. Identifier format of any NGSI entity'    
          format: uri    
          type: string    
    name:    
      description: 'The name of this item.'    
      type: Property    
    owner:    
      description: 'A List containing a JSON encoded sequence of characters referencing the unique Ids of the owner(s)'    
      items:    
        anyOf: *smartspot_-_properties_-_owner_-_items_-_anyof    
      type: Property    
    refSmartPointOfInteraction:    
      anyOf: *smartspot_-_properties_-_owner_-_items_-_anyof    
    seeAlso:    
      oneOf:    
        - items:    
            - format: uri    
              type: string    
          minItems: 1    
          type: array    
        - format: uri    
          type: string    
    signalStrength:    
      description: 'Signal strength to adjust the announcement range'    
      enum:    
        - lowest    
        - medium    
        - highest    
      type: string    
    source:    
      description: 'A sequence of characters giving the original source of the entity data as a URL. Recommended to be the fully qualified domain name of the source provider, or the URL to the source object.'    
      type: Property    
    type:    
      description: 'NGSI Entity type'    
      enum:    
        - SmartSpot    
      type: string    
  required:    
    - id    
    - type    
    - announcedUrl    
    - signalStrength    
    - bluetoothChannel    
    - announcementPeriod    
    - availability    
  type: object    
```  



  "id": "SSPOT-F94C51A295D9",  
  "type": "SmartSpot",  
  "announcedUrl": "http://goo.gl/EJ81JP",  
  "signalStrength": "highest",  
  "bluetoothChannel": "37,38,39",  
  "coverageRadius": 30,  
  "announcementPeriod": 500,  
  "availability": "Tu,Th 16:00-20:00",  
  "refSmartPointOfInteraction": "SPOI-ES-4326"  
}  
```  



  "id": "SSPOT-F94C51A295D9",  
  "type": "SmartSpot",  
  "announcementPeriod": {  
    "value": 500  
  },  
  "signalStrength": {  
    "value": "highest"  
  },  
  "announcedUrl": {  
    "value": "http://goo.gl/EJ81JP"  
  },  
  "availability": {  
    "value": "Tu,Th 16:00-20:00"  
  },  
  "coverageRadius": {  
    "value": 30  
  },  
  "bluetoothChannel": {  
    "value": "37,38,39"  
  },  
  "refSmartPointOfInteraction": {  
    "type": "Relationship",  
    "value": "SPOI-ES-4326"  
  }  
}  
```  



              "https://uri.etsi.org/ngsi-ld/v1/ngsi-ld-core-context.jsonld"],  
 "announcedUrl": "http://goo.gl/EJ81JP",  
 "announcementPeriod": 500,  
 "availability": "Tu,Th 16:00-20:00",  
 "bluetoothChannel": "37,38,39",  
 "coverageRadius": 30,  
 "id": "urn:ngsi-ld:SmartSpot:SSPOT-F94C51A295D9",  
 "refSmartPointOfInteraction": "urn:ngsi-ld:SmartPointOfInteraction:SPOI-ES-4326",  
 "signalStrength": "highest",  
 "type": "SmartSpot"}  
```  



    "id": "urn:ngsi-ld:SmartSpot:SSPOT-F94C51A295D9",  
    "type": "SmartSpot",  
    "announcementPeriod": {  
        "type": "Property",  
        "value": 500  
    },  
    "signalStrength": {  
        "type": "Property",  
        "value": "highest"  
    },  
    "announcedUrl": {  
        "type": "Property",  
        "value": "http://goo.gl/EJ81JP"  
    },  
    "availability": {  
        "type": "Property",  
        "value": "Tu,Th 16:00-20:00"  
    },  
    "coverageRadius": {  
        "type": "Property",  
        "value": 30  
    },  
    "bluetoothChannel": {  
        "type": "Property",  
        "value": "37,38,39"  
    },  
    "refSmartPointOfInteraction": {  
        "type": "Relationship",  
        "object": "urn:ngsi-ld:SmartPointOfInteraction:SPOI-ES-4326"  
    },  
    "@context": [  
        "https://schema.lab.fiware.org/ld/context",  
        "https://uri.etsi.org/ngsi-ld/v1/ngsi-ld-core-context.jsonld"  
    ]  
}  
```  