Entity: SmartSpot  
=================  
[Open License](https://github.com/smart-data-models//dataModel.PointOfInteraction/blob/master/SmartSpot/LICENSE.md)  
[document generated automatically](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
Global description: **Smart Data models Smart Spot entity schema intended for validation tools**  

## List of properties  

- `alternateName`: An alternative name for this item  - `announcedUrl`: URL broadcasted by the device  - `announcementPeriod`: Period between announcements in milliseconds  - `availability`: Specifies the time intervals in which this interactive service is available, but this is a general information while Smart Spots have their own real availability in order to allow advanced configurations  - `bluetoothChannel`: Bluetooth channels where to transmit the announcement  - `coverageRadius`: Radius of the spot coverage area in meters  - `dataProvider`: A sequence of characters identifying the provider of the harmonised data entity.  - `dateCreated`: Entity creation timestamp. This will usually be allocated by the storage platform.  - `dateModified`: Timestamp of the last modification of the entity. This will usually be allocated by the storage platform.  - `description`: A description of this item  - `id`: Unique identifier of the entity  - `name`: The name of this item.  - `owner`: A List containing a JSON encoded sequence of characters referencing the unique Ids of the owner(s)  - `refSmartPointOfInteraction`: Reference to the Smart Point of Interaction which includes this Smart Spot  - `seeAlso`: list of uri pointing to additional resources about the item  - `signalStrength`: Signal strength to adjust the announcement range. Enum:'highest, lowest, medium'  - `source`: A sequence of characters giving the original source of the entity data as a URL. Recommended to be the fully qualified domain name of the source provider, or the URL to the source object.  - `type`: NGSI Entity type. It has to be SmartSpot    
Required properties  
- `id`  - `type`    
Smart Spots are devices which provide the technology which allows users to get access to smart points of interaction so that they can obtain extra information (infotainment, etc.), provide suggestions (suggestions mailbox, etc.) or generate new content (co-creation, etc.). The data model contains resources to configure the interaction service such as the broadcasted URL (typically shortened), the period between broadcasts, the availability of the service, transmission power depending on the area to be covered, etc.  
## Data Model description of properties  
Sorted alphabetically (click for details)  
<details><summary><strong>full yaml details</strong></summary>    
```yaml  
SmartSpot:    
  description: 'Smart Data models Smart Spot entity schema intended for validation tools'    
  properties:    
    alternateName:    
      description: 'An alternative name for this item'    
      type: string    
      x-ngsi:    
        type: Property    
    announcedUrl:    
      description: 'URL broadcasted by the device'    
      format: uri    
      type: string    
      x-ngsi:    
        model: https://schema.org/URL    
        type: Property    
    announcementPeriod:    
      description: 'Period between announcements in milliseconds'    
      maximum: 4000    
      minimum: 100    
      type: integer    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    availability:    
      description: 'Specifies the time intervals in which this interactive service is available, but this is a general information while Smart Spots have their own real availability in order to allow advanced configurations'    
      type: string    
      x-ngsi:    
        model: https://schema.org/openingHours    
        type: Property    
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
      x-ngsi:    
        model: ' https://schema.org/Text'    
        type: Property    
    coverageRadius:    
      description: 'Radius of the spot coverage area in meters'    
      minimum: 1    
      type: integer    
      x-ngsi:    
        model: https://schema.org/Number    
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
      anyOf: &smartspot_-_properties_-_owner_-_items_-_anyof    
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
    name:    
      description: 'The name of this item.'    
      type: string    
      x-ngsi:    
        type: Property    
    owner:    
      description: 'A List containing a JSON encoded sequence of characters referencing the unique Ids of the owner(s)'    
      items:    
        anyOf: *smartspot_-_properties_-_owner_-_items_-_anyof    
        description: 'Property. Unique identifier of the entity'    
      type: array    
      x-ngsi:    
        type: Property    
    refSmartPointOfInteraction:    
      anyOf:    
        - description: 'Property. Identifier format of any NGSI entity'    
          maxLength: 256    
          minLength: 1    
          pattern: ^[\w\-\.\{\}\$\+\*\[\]`|~^@!,:\\]+$    
          type: string    
        - description: 'Property. Identifier format of any NGSI entity'    
          format: uri    
          type: string    
      description: 'Reference to the Smart Point of Interaction which includes this Smart Spot'    
      x-ngsi:    
        model: https://schema.org/URL    
        type: Relationship    
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
    signalStrength:    
      description: 'Signal strength to adjust the announcement range. Enum:''highest, lowest, medium'''    
      enum:    
        - highest    
        - lowest    
        - medium    
      type: string    
      x-ngsi:    
        type: Property    
    source:    
      description: 'A sequence of characters giving the original source of the entity data as a URL. Recommended to be the fully qualified domain name of the source provider, or the URL to the source object.'    
      type: string    
      x-ngsi:    
        type: Property    
    type:    
      description: 'NGSI Entity type. It has to be SmartSpot'    
      enum:    
        - SmartSpot    
      type: string    
      x-ngsi:    
        type: Property    
  required:    
    - id    
    - type    
  type: object    
```  
</details>    
## Example payloads    
#### SmartSpot NGSI-v2 key-values Example    
Here is an example of a SmartSpot in JSON-LD format as key-values. This is compatible with NGSI-v2 when  using `options=keyValues` and returns the context data of an individual entity.  
```json  
{  
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
#### SmartSpot NGSI-v2 normalized Example    
Here is an example of a SmartSpot in JSON-LD format as normalized. This is compatible with NGSI-v2 when not using options and returns the context data of an individual entity.  
```json  
{  
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
#### SmartSpot NGSI-LD key-values Example    
Here is an example of a SmartSpot in JSON-LD format as key-values. This is compatible with NGSI-LD when  using `options=keyValues` and returns the context data of an individual entity.  
```json  
{  
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
    "https://smartdatamodels.org/context.jsonld",  
    "https://uri.etsi.org/ngsi-ld/v1/ngsi-ld-core-context.jsonld"  
  ]  
}  
```  
#### SmartSpot NGSI-LD normalized Example    
Here is an example of a SmartSpot in JSON-LD format as normalized. This is compatible with NGSI-LD when not using options and returns the context data of an individual entity.  
```json  
{  
  "@context": [  
    "https://smartdatamodels.org/context.jsonld",  
    "https://uri.etsi.org/ngsi-ld/v1/ngsi-ld-core-context.jsonld"  
  ],  
  "announcedUrl": "http://goo.gl/EJ81JP",  
  "announcementPeriod": 500,  
  "availability": "Tu,Th 16:00-20:00",  
  "bluetoothChannel": "37,38,39",  
  "coverageRadius": 30,  
  "id": "urn:ngsi-ld:SmartSpot:SSPOT-F94C51A295D9",  
  "refSmartPointOfInteraction": "urn:ngsi-ld:SmartPointOfInteraction:SPOI-ES-4326",  
  "signalStrength": "highest",  
  "type": "SmartSpot"  
}  
```  
