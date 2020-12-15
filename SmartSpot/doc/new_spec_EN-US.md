Entity: SmartSpot  
=================  
This specification is a **temporal version**. It is automatically generated from the  documented properties described in the schema.json condensed into the file `model.yaml`. A temporary `new_model.yaml` file has been created in every data model to avoid impacting into existing scripts. Thus, the specification will be incomplete as long as the schema.json is not updated to the new format (documenting properties). Once updated the `model.yaml` (`new_model.yaml`) needs to be updated as well (automatically) . Further info in this [link](https://github.com/smart-data-models/data-models/blob/master/specs/warning_message_new_spec.md). As long as it is a provisional format any [feedback is welcomed in this form](https://smartdatamodels.org/index.php/submit-an-issue-2/) choosing option `Feedback on the new specification`  
Global description: **FIWARE Smart Spot entity schema intended for validation tools**  

## List of properties  

- `alternateName`: An alternative name for this item  - `announcedUrl`: URL broadcasted by the device  - `announcementPeriod`: Period between announcements in milliseconds  - `availability`: Specifies the time intervals in which this interactive service is available, but this is a general information while Smart Spots have their own real availability in order to allow advanced configurations  - `bluetoothChannel`: Bluetooth channels where to transmit the announcement  - `coverageRadius`: Radius of the spot coverage area in meters  - `dataProvider`: A sequence of characters identifying the provider of the harmonised data entity.  - `dateCreated`: Entity creation timestamp. This will usually be allocated by the storage platform.  - `dateModified`: Timestamp of the last modification of the entity. This will usually be allocated by the storage platform.  - `description`: A description of this item  - `id`:   - `name`: The name of this item.  - `owner`: A List containing a JSON encoded sequence of characters referencing the unique Ids of the owner(s)  - `refSmartPointOfInteraction`:   - `seeAlso`: list of uri pointing to additional resources about the item  - `signalStrength`: Signal strength to adjust the announcement range  - `source`: A sequence of characters giving the original source of the entity data as a URL. Recommended to be the fully qualified domain name of the source provider, or the URL to the source object.  - `type`: NGSI Entity type    
Required properties  
- `announcedUrl`  - `announcementPeriod`  - `availability`  - `bluetoothChannel`  - `id`  - `signalStrength`  - `type`    
Smart Spots are devices which provide the technology which allows users to get access to smart points of interaction so that they can obtain extra information (infotainment, etc.), provide suggestions (suggestions mailbox, etc.) or generate new content (co-creation, etc.). The data model contains resources to configure the interaction service such as the broadcasted URL (typically shortened), the period between broadcasts, the availability of the service, transmission power depending on the area to be covered, etc.  
## Data Model description of properties  
Sorted alphabetically (click for details)  
<details><summary><strong>full yaml details</strong></summary>    
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
      type: Property    
      x-ngsi:    
        model: https://schema.org/URL    
    announcementPeriod:    
      description: 'Period between announcements in milliseconds'    
      maximum: 4000    
      minimum: 100    
      type: Property    
      x-ngsi:    
        model: https://schema.org/Number    
    availability:    
      description: 'Specifies the time intervals in which this interactive service is available, but this is a general information while Smart Spots have their own real availability in order to allow advanced configurations'    
      type: Property    
      x-ngsi:    
        model: https://schema.org/openingHours    
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
      type: Property    
      x-ngsi:    
        model: ' https://schema.org/Text'    
    coverageRadius:    
      description: 'Radius of the spot coverage area in meters'    
      minimum: 1    
      type: Property    
      x-ngsi:    
        model: https://schema.org/Number    
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
      description: 'Unique identifier of the entity'    
      type: Property    
    name:    
      description: 'The name of this item.'    
      type: Property    
    owner:    
      description: 'A List containing a JSON encoded sequence of characters referencing the unique Ids of the owner(s)'    
      items:    
        anyOf: *smartspot_-_properties_-_owner_-_items_-_anyof    
        description: 'Property. Unique identifier of the entity'    
      type: Property    
    refSmartPointOfInteraction:    
      anyOf: *smartspot_-_properties_-_owner_-_items_-_anyof    
      description: 'Unique identifier of the entity'    
      type: Property    
    seeAlso:    
      description: 'list of uri pointing to additional resources about the item'    
      oneOf:    
        - items:    
            - format: uri    
              type: string    
          minItems: 1    
          type: array    
        - format: uri    
          type: string    
      type: Property    
    signalStrength:    
      description: 'Signal strength to adjust the announcement range. Enum:''highest, lowest, medium'''    
      enum:    
        - highest    
        - lowest    
        - medium    
      type: Property    
    source:    
      description: 'A sequence of characters giving the original source of the entity data as a URL. Recommended to be the fully qualified domain name of the source provider, or the URL to the source object.'    
      type: Property    
    type:    
      description: 'NGSI Entity type. It has to be SmartSpot'    
      enum:    
        - SmartSpot    
      type: Property    
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
</details>    
## Example payloads    
#### SmartSpot NGSI V2 key-values Example    
Here is an example of a SmartSpot in JSON format as key-values. This is compatible with NGSI V2 when  using `options=keyValues` and returns the context data of an individual entity.  
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
#### SmartSpot NGSI V2 normalized Example    
Here is an example of a SmartSpot in JSON format as normalized. This is compatible with NGSI V2 when not using options and returns the context data of an individual entity.  
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
{"@context": ["https://schema.lab.fiware.org/ld/context",  
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
#### SmartSpot NGSI-LD normalized Example    
Here is an example of a SmartSpot in JSON-LD format as normalized. This is compatible with NGSI-LD when not using options and returns the context data of an individual entity.  
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
        "https://schema.lab.fiware.org/ld/context",  
        "https://uri.etsi.org/ngsi-ld/v1/ngsi-ld-core-context.jsonld"  
    ]  
}  
```  
