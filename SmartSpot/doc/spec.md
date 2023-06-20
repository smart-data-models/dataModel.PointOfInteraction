<!-- 10-Header -->  
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)  
Entity: SmartSpot  
=================<!-- /10-Header -->  
<!-- 15-License -->  
[Open License](https://github.com/smart-data-models//dataModel.PointOfInteraction/blob/master/SmartSpot/LICENSE.md)  
[document generated automatically](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
<!-- /15-License -->  
<!-- 20-Description -->  
Global description: **Smart Data models Smart Spot entity schema intended for validation tools**  
version: 0.1.0  
<!-- /20-Description -->  
<!-- 30-PropertiesList -->  

## List of properties  

<sup><sub>[*] If there is not a type in an attribute is because it could have several types or different formats/patterns</sub></sup>  
- `alternateName[string]`: An alternative name for this item  - `announcedUrl[string]`: URL broadcasted by the device  . Model: [https://schema.org/URL](https://schema.org/URL)- `announcementPeriod[number]`: Period between announcements in milliseconds  . Model: [https://schema.org/Number](https://schema.org/Number)- `availability[string]`: Specifies the time intervals in which this interactive service is available, but this is a general information while Smart Spots have their own real availability in order to allow advanced configurations  . Model: [https://schema.org/openingHours](https://schema.org/openingHours)- `bluetoothChannel[string]`: Bluetooth channels where to transmit the announcement  . Model: [ https://schema.org/Text]( https://schema.org/Text)- `coverageRadius[number]`: Radius of the spot coverage area in meters  . Model: [https://schema.org/Number](https://schema.org/Number)- `dataProvider[string]`: A sequence of characters identifying the provider of the harmonised data entity.  - `dateCreated[string]`: Entity creation timestamp. This will usually be allocated by the storage platform.  - `dateModified[string]`: Timestamp of the last modification of the entity. This will usually be allocated by the storage platform.  - `description[string]`: A description of this item  - `id[*]`: Unique identifier of the entity  - `name[string]`: The name of this item.  - `owner[array]`: A List containing a JSON encoded sequence of characters referencing the unique Ids of the owner(s)  - `refSmartPointOfInteraction[*]`: Reference to the Smart Point of Interaction which includes this Smart Spot  . Model: [https://schema.org/URL](https://schema.org/URL)- `seeAlso[*]`: list of uri pointing to additional resources about the item  - `signalStrength[string]`: Signal strength to adjust the announcement range. Enum:'highest, lowest, medium'  - `source[string]`: A sequence of characters giving the original source of the entity data as a URL. Recommended to be the fully qualified domain name of the source provider, or the URL to the source object.  - `type[string]`: NGSI Entity type. It has to be SmartSpot  <!-- /30-PropertiesList -->  
<!-- 35-RequiredProperties -->  
Required properties  
- `id`  - `type`  <!-- /35-RequiredProperties -->  
<!-- 40-RequiredProperties -->  
Smart Spots are devices which provide the technology which allows users to get access to smart points of interaction so that they can obtain extra information (infotainment, etc.), provide suggestions (suggestions mailbox, etc.) or generate new content (co-creation, etc.). The data model contains resources to configure the interaction service such as the broadcasted URL (typically shortened), the period between broadcasts, the availability of the service, transmission power depending on the area to be covered, etc.  
<!-- /40-RequiredProperties -->  
<!-- 50-DataModelHeader -->  
## Data Model description of properties  
Sorted alphabetically (click for details)  
<!-- /50-DataModelHeader -->  
<!-- 60-ModelYaml -->  
<details><summary><strong>full yaml details</strong></summary>    
```yaml  
SmartSpot:    
  description: Smart Data models Smart Spot entity schema intended for validation tools    
  properties:    
    alternateName:    
      description: An alternative name for this item    
      type: string    
      x-ngsi:    
        type: Property    
    announcedUrl:    
      description: URL broadcasted by the device    
      format: uri    
      type: string    
      x-ngsi:    
        model: https://schema.org/URL    
        type: Property    
    announcementPeriod:    
      description: Period between announcements in milliseconds    
      maximum: 4000    
      minimum: 100    
      type: number    
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
      description: Bluetooth channels where to transmit the announcement    
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
      description: Radius of the spot coverage area in meters    
      minimum: 1    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    dataProvider:    
      description: A sequence of characters identifying the provider of the harmonised data entity.    
      type: string    
      x-ngsi:    
        type: Property    
    dateCreated:    
      description: Entity creation timestamp. This will usually be allocated by the storage platform.    
      format: date-time    
      type: string    
      x-ngsi:    
        type: Property    
    dateModified:    
      description: Timestamp of the last modification of the entity. This will usually be allocated by the storage platform.    
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
      anyOf: &smartspot_-_properties_-_owner_-_items_-_anyof    
        - description: Property. Identifier format of any NGSI entity    
          maxLength: 256    
          minLength: 1    
          pattern: ^[\w\-\.\{\}\$\+\*\[\]`|~^@!,:\\]+$    
          type: string    
        - description: Property. Identifier format of any NGSI entity    
          format: uri    
          type: string    
      description: Unique identifier of the entity    
      x-ngsi:    
        type: Property    
    name:    
      description: The name of this item.    
      type: string    
      x-ngsi:    
        type: Property    
    owner:    
      description: A List containing a JSON encoded sequence of characters referencing the unique Ids of the owner(s)    
      items:    
        anyOf: *smartspot_-_properties_-_owner_-_items_-_anyof    
        description: Property. Unique identifier of the entity    
      type: array    
      x-ngsi:    
        type: Property    
    refSmartPointOfInteraction:    
      anyOf:    
        - description: Property. Identifier format of any NGSI entity    
          maxLength: 256    
          minLength: 1    
          pattern: ^[\w\-\.\{\}\$\+\*\[\]`|~^@!,:\\]+$    
          type: string    
        - description: Property. Identifier format of any NGSI entity    
          format: uri    
          type: string    
      description: Reference to the Smart Point of Interaction which includes this Smart Spot    
      x-ngsi:    
        model: https://schema.org/URL    
        type: Relationship    
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
      description: NGSI Entity type. It has to be SmartSpot    
      enum:    
        - SmartSpot    
      type: string    
      x-ngsi:    
        type: Property    
  required:    
    - id    
    - type    
  type: object    
  x-derived-from: ""    
  x-disclaimer: 'Redistribution and use in source and binary forms, with or without modification, are permitted  provided that the license conditions are met. Copyleft (c) 2022 Contributors to Smart Data Models Program'    
  x-license-url: https://github.com/smart-data-models/dataModel.PointOfInteraction/blob/master/SmartSpot/LICENSE.md    
  x-model-schema: https://smart-data-models.github.io/dataModel.PointOfInteraction/SmartSpot/schema.json    
  x-model-tags: ""    
  x-version: 0.1.0    
```  
</details>    
<!-- /60-ModelYaml -->  
<!-- 70-MiddleNotes -->  
<!-- /70-MiddleNotes -->  
<!-- 80-Examples -->  
## Example payloads    
#### SmartSpot NGSI-v2 key-values Example    
Here is an example of a SmartSpot in JSON-LD format as key-values. This is compatible with NGSI-v2 when  using `options=keyValues` and returns the context data of an individual entity.  
<details><summary><strong>show/hide example</strong></summary>    
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
</details>  
#### SmartSpot NGSI-v2 normalized Example    
Here is an example of a SmartSpot in JSON-LD format as normalized. This is compatible with NGSI-v2 when not using options and returns the context data of an individual entity.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "SSPOT-F94C51A295D9",  
  "type": "SmartSpot",  
  "announcementPeriod": {  
    "type": "Number",  
    "value": 500  
  },  
  "signalStrength": {  
    "type": "Text",  
    "value": "highest"  
  },  
  "announcedUrl": {  
    "type": "URL",  
    "value": "http://goo.gl/EJ81JP"  
  },  
  "availability": {  
    "type": "Text",  
    "value": "Tu,Th 16:00-20:00"  
  },  
  "coverageRadius": {  
    "type": "Number",  
    "value": 30  
  },  
  "bluetoothChannel": {  
    "type": "Text",  
    "value": "37,38,39"  
  },  
  "refSmartPointOfInteraction": {  
    "type": "Text",  
    "value": "SPOI-ES-4326"  
  }  
}  
```  
</details>  
#### SmartSpot NGSI-LD key-values Example    
Here is an example of a SmartSpot in JSON-LD format as key-values. This is compatible with NGSI-LD when  using `options=keyValues` and returns the context data of an individual entity.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "urn:ngsi-ld:SmartSpot:SSPOT-F94C51A295D9",  
  "type": "SmartSpot",  
  "announcedUrl": "http://goo.gl/EJ81JP",  
  "announcementPeriod": 500,  
  "availability": "Tu,Th 16:00-20:00",  
  "bluetoothChannel": "37,38,39",  
  "coverageRadius": 30,  
  "refSmartPointOfInteraction": "urn:ngsi-ld:SmartPointOfInteraction:SPOI-ES-4326",  
  "signalStrength": "highest",  
  "@context": [  
    "https://uri.etsi.org/ngsi-ld/v1/ngsi-ld-core-context.jsonld",  
    "https://raw.githubusercontent.com/smart-data-models/dataModel.PointOfInteraction/master/context.jsonld"  
  ]  
}  
```  
</details>  
#### SmartSpot NGSI-LD normalized Example    
Here is an example of a SmartSpot in JSON-LD format as normalized. This is compatible with NGSI-LD when not using options and returns the context data of an individual entity.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "SSPOT-F94C51A295D9",  
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
    "value": "SPOI-ES-4326"  
  }  
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
