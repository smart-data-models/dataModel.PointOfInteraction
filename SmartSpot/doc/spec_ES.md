Entidad: SmartSpot  
==================  
[Licencia abierta](https://github.com/smart-data-models//dataModel.PointOfInteraction/blob/master/SmartSpot/LICENSE.md)  
Descripción global: **Esquema de entidad Smart Spot de FIWARE destinado a las herramientas de validación**  

## Lista de propiedades  

- `alternateName`: Un nombre alternativo para este artículo  - `announcedUrl`: La URL emitida por el dispositivo  - `announcementPeriod`: El período entre los anuncios en milisegundos  - `availability`: Especifica los intervalos de tiempo en los que este servicio interactivo está disponible, pero esta es una información general mientras que los Smart Spots tienen su propia disponibilidad real para permitir configuraciones avanzadas  - `bluetoothChannel`: Canales de Bluetooth donde transmitir el anuncio  - `coverageRadius`: El radio del área de cobertura del spot en metros  - `dataProvider`: Una secuencia de caracteres que identifica al proveedor de la entidad de datos armonizada.  - `dateCreated`: Sello de tiempo de creación de la entidad. Normalmente será asignado por la plataforma de almacenamiento.  - `dateModified`: Sello de tiempo de la última modificación de la entidad. Esta será normalmente asignada por la plataforma de almacenamiento.  - `description`: Una descripción de este artículo  - `id`: Identificador único de la entidad  - `name`: El nombre de este artículo.  - `owner`: Una lista que contiene una secuencia de caracteres codificados JSON que hace referencia a los Ids únicos de los propietarios  - `refSmartPointOfInteraction`: Identificador único de la entidad  - `seeAlso`: lista de uri que apunta a recursos adicionales sobre el tema  - `signalStrength`: La fuerza de la señal para ajustar el rango de anuncio. Enum:'más alto, más bajo, medio'.  - `source`: Una secuencia de caracteres que da como URL la fuente original de los datos de la entidad. Se recomienda que sea el nombre de dominio completamente calificado del proveedor de la fuente, o la URL del objeto fuente.  - `type`: Tipo de entidad NGSI. Tiene que ser SmartSpot    
Propiedades requeridas  
- `announcedUrl`  - `announcementPeriod`  - `availability`  - `bluetoothChannel`  - `id`  - `signalStrength`  - `type`    
Los Smart Spots son dispositivos que proporcionan la tecnología que permite a los usuarios acceder a puntos inteligentes de interacción para obtener información adicional (infoentretenimiento, etc.), proporcionar sugerencias (buzón de sugerencias, etc.) o generar nuevos contenidos (co-creación, etc.). El modelo de datos contiene recursos para configurar el servicio de interacción como la URL de emisión (normalmente acortada), el período entre las emisiones, la disponibilidad del servicio, la potencia de transmisión en función de la zona a cubrir, etc.  
## Modelo de datos Descripción de las propiedades  
Ordenados alfabéticamente (haga clic para ver los detalles)  
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
## Ejemplo de cargas útiles  
#### Ejemplo de valores clave del SmartSpot NGSI V2  
Aquí hay un ejemplo de un SmartSpot en formato JSON como valores clave. Es compatible con NGSI V2 cuando se utiliza "opciones=valores-clave" y devuelve los datos de contexto de una entidad individual.  
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
#### SmartSpot NGSI V2 normalizado Ejemplo  
Aquí hay un ejemplo de un SmartSpot en formato JSON como normalizado. Es compatible con NGSI V2 cuando no se usan opciones y devuelve los datos de contexto de una entidad individual.  
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
Aquí hay un ejemplo de un SmartSpot en formato JSON-LD como valores clave. Es compatible con NGSI-LD cuando se usa "opciones=valores-clave" y devuelve los datos de contexto de una entidad individual.  
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
#### SmartSpot NGSI-LD normalizado Ejemplo  
Aquí hay un ejemplo de un SmartSpot en formato JSON-LD normalizado. Es compatible con NGSI-LD cuando no se utilizan opciones y devuelve los datos de contexto de una entidad individual.  
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
