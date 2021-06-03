Entidad: SmartPointOfInteraction  
================================  
[Licencia abierta](https://github.com/smart-data-models//dataModel.PointOfInteraction/blob/master/SmartPointOfInteraction/LICENSE.md)  
[documento generado automáticamente](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
Descripción global: **Modelos de datos inteligentes Esquema de entidad de punto de interacción inteligente destinado a herramientas de validación**  

## Lista de propiedades  

- `address`: La dirección postal  - `alternateName`: Un nombre alternativo para este artículo  - `applicationUrl`: Este campo especifica la URL real que contiene la solución o aplicación (información, cocreación, etc.) mientras que el campo 'announcedUrl' de SmartSpot especifica la URL de difusión que puede ser esta misma URL o una acortada  - `areaCovered`:   - `areaServed`: La zona geográfica en la que se presta un servicio o se ofrece un artículo  - `availability`: Especifica los intervalos de tiempo en los que este servicio interactivo está generalmente disponible. Cabe destacar que los Smart Spots tienen su propia disponibilidad real para permitir configuraciones avanzadas. La sintaxis debe ser conforme a schema.org. Por ejemplo, un servicio que sólo está activo los días laborables se codificará como "disponibilidad": 'Mo,Tu,We,Th,Fr,Sa 09:00-20:00'.  - `category`: Define el tipo de interacción. Enum:'co-creación, entretenimiento, información, infotainment'  - `dataProvider`: Una secuencia de caracteres que identifica al proveedor de la entidad de datos armonizada.  - `dateCreated`: Marca de tiempo de creación de la entidad. Suele ser asignada por la plataforma de almacenamiento.  - `dateModified`: Marca de tiempo de la última modificación de la entidad. Normalmente será asignada por la plataforma de almacenamiento.  - `description`: Una descripción de este artículo  - `id`: Identificador único de la entidad  - `location`: Referencia Geojson al elemento. Puede ser Point, LineString, Polygon, MultiPoint, MultiLineString o MultiPolygon  - `name`: El nombre de este artículo.  - `owner`: Una lista que contiene una secuencia de caracteres codificada en JSON que hace referencia a los identificadores únicos de los propietarios  - `refRelatedEntity`: Lista de entidades mejoradas con este punto de interacción inteligente  - `refSmartSpot`:  Referencias a los dispositivos Smart Spot que forman parte del Punto de Interacción Inteligente  - `seeAlso`: lista de uri que apuntan a recursos adicionales sobre el artículo  - `source`: Una secuencia de caracteres que indica la fuente original de los datos de la entidad en forma de URL. Se recomienda que sea el nombre de dominio completo del proveedor de origen, o la URL del objeto de origen.  - `type`: Tipo de entidad NGSI. Tiene que ser SmartPointOfInteraction    
Propiedades requeridas  
- `id`  - `type`    
Un Punto de Interacción Inteligente define un lugar con tecnología para interactuar con los usuarios, por ejemplo, a través de la tecnología Beacon de Apple, Eddystone/Physical-Web de Google u otras interfaces basadas en la proximidad. Dado que el área interactiva podría estar compuesta por más de un dispositivo que proporcione la tecnología, este modelo abarca un grupo de dispositivos SmartSpot. El modelo de datos incluye información relativa al área/superficie cubierta por la tecnología (es decir, el área cubierta por la baliza basada en Bluetooth Low Energy), una forma de especificar los intervalos de funcionalidad (es decir, cuándo están disponibles los puntos interactivos) y un enlace a un recurso multimedia destinado a la interacción con el usuario (es decir, Web Apps, etc.). Además, el modelo de datos puede hacer referencia a otra entidad NGSI, como un aparcamiento, un punto de interés (POI), etc. con una interacción enriquecida proporcionada por este punto de interacción inteligente.  
## Descripción del modelo de datos de las propiedades  
Ordenados alfabéticamente (haga clic para ver los detalles)  
<details><summary><strong>full yaml details</strong></summary>    
```yaml  
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
      type: Property    
      x-ngsi:    
        model: https://schema.org/address    
    alternateName:    
      description: 'An alternative name for this item'    
      type: Property    
    applicationUrl:    
      description: 'This field specifies the real URL containing the solution or application (information, co-creation, etc) while the SmartSpot ''announcedUrl'' field specifies the broadcast URL which could be this same URL or a shortened one'    
      format: uri    
      type: Property    
      x-ngsi:    
        model: https://schema.org/URL    
    areaCovered:    
      $id: https://geojson.org/schema/Geometry.json    
      $schema: "http://json-schema.org/draft-07/schema#"    
      oneOf:    
        - properties:    
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
        - properties:    
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
        - properties:    
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
        - properties:    
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
        - properties:    
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
        - properties:    
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
      title: 'GeoJSON Geometry'    
    areaServed:    
      description: 'The geographic area where a service or offered item is provided'    
      type: Property    
      x-ngsi:    
        model: https://schema.org/Text    
    availability:    
      description: 'Specifies the time intervals in which this interactive service is generally available. It is noteworthy that Smart Spots have their own real availability in order to allow advanced configurations. The syntax must be conformant with schema.org. For instance, a service which is only active on weekdays will be encoded as ''availability'': ''Mo,Tu,We,Th,Fr,Sa 09:00-20:00''.'    
      type: Property    
      x-ngsi:    
        model: https://schema.org/openingHours    
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
      type: Property    
      uniqueItems: true    
      x-ngsi:    
        model: http://schema.org/Text    
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
      type: Property    
    location:    
      description: 'Geojson reference to the item. It can be Point, LineString, Polygon, MultiPoint, MultiLineString or MultiPolygon'    
      oneOf:    
        - description: 'Geoproperty. Geojson reference to the item. Point'    
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
        - description: 'Geoproperty. Geojson reference to the item. LineString'    
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
        - description: 'Geoproperty. Geojson reference to the item. Polygon'    
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
        - description: 'Geoproperty. Geojson reference to the item. MultiPoint'    
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
        - description: 'Geoproperty. Geojson reference to the item. MultiLineString'    
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
        - description: 'Geoproperty. Geojson reference to the item. MultiLineString'    
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
      type: Geoproperty    
    name:    
      description: 'The name of this item.'    
      type: Property    
    owner:    
      description: 'A List containing a JSON encoded sequence of characters referencing the unique Ids of the owner(s)'    
      items:    
        anyOf: *smartpointofinteraction_-_properties_-_owner_-_items_-_anyof    
        description: 'Property. Unique identifier of the entity'    
      type: Property    
    refRelatedEntity:    
      description: 'List of entities improved with this Smart Point of Interaction'    
      items:    
        anyOf: *smartpointofinteraction_-_properties_-_owner_-_items_-_anyof    
        description: 'Property. Unique identifier of the entity'    
      minItems: 1    
      type: Relationship    
      uniqueItems: true    
      x-ngsi:    
        model: 'The entity type could be any such as a Parking, Point of Interest, etc.http://schema.org/Text'    
    refSmartSpot:    
      description: ' References to the Smart Spot devices which are part of the Smart Point of Interaction'    
      items:    
        anyOf: *smartpointofinteraction_-_properties_-_owner_-_items_-_anyof    
        description: 'Property. Unique identifier of the entity'    
      minItems: 1    
      type: Property    
      uniqueItems: true    
      x-ngsi:    
        model: https://schema.org/URL    
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
      type: Property    
    source:    
      description: 'A sequence of characters giving the original source of the entity data as a URL. Recommended to be the fully qualified domain name of the source provider, or the URL to the source object.'    
      type: Property    
    type:    
      description: 'NGSI Entity type. It has to be SmartPointOfInteraction'    
      enum:    
        - SmartPointOfInteraction    
      type: Property    
  required:    
    - id    
    - type    
  type: object    
```  
</details>    
## Ejemplo de carga útil  
#### SmartPointOfInteraction NGSI-v2 key-values Ejemplo  
Aquí hay un ejemplo de un SmartPointOfInteraction en formato JSON-LD como valores-clave. Esto es compatible con NGSI-v2 cuando se utiliza `options=keyValues` y devuelve los datos de contexto de una entidad individual.  
```json  
{  
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
#### SmartPointOfInteraction NGSI-v2 normalizado Ejemplo  
Este es un ejemplo de un SmartPointOfInteraction en formato JSON-LD normalizado. Esto es compatible con NGSI-v2 cuando no se utilizan opciones y devuelve los datos de contexto de una entidad individual.  
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
    "value": ["SSPOT-F94C58E29DD5", "SSPOT-F94C53E21DD2", "SSPOT-F94C51A295D9"]  
  },  
  "refRelatedEntity": {  
    "type": "Relationship",  
    "value": ["POI-PlazaCazorla-3123"]  
  }  
}  
```  
#### SmartPointOfInteraction NGSI-LD key-values Ejemplo  
Aquí hay un ejemplo de un SmartPointOfInteraction en formato JSON-LD como valores-clave. Esto es compatible con NGSI-LD cuando se utiliza `options=keyValues` y devuelve los datos de contexto de una entidad individual.  
```json  
{  
  "id": "urn:ngsi-ld:SmartPointOfInteraction:SPOI-ES-4326",  
  "type": "SmartPointOfInteraction",  
  "category": {  
    "type": "Property",  
    "value": [  
      "co-creation"  
    ]  
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
    "object": [  
      "urn:ngsi-ld:RelatedEntity:POI-PlazaCazorla-3123"  
    ]  
  },  
  "@context": [  
    "https://smartdatamodels.org/context.jsonld",  
    "https://uri.etsi.org/ngsi-ld/v1/ngsi-ld-core-context.jsonld"  
  ]  
}  
```  
#### SmartPointOfInteraction NGSI-LD normalizado Ejemplo  
Este es un ejemplo de un SmartPointOfInteraction en formato JSON-LD normalizado. Esto es compatible con NGSI-LD cuando no se utilizan opciones y devuelve los datos de contexto de una entidad individual.  
```json  
{  
  "@context": [  
    "https://smartdatamodels.org/context.jsonld",  
    "https://uri.etsi.org/ngsi-ld/v1/ngsi-ld-core-context.jsonld"  
  ],  
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
  "id": "urn:ngsi-ld:SmartPointOfInteraction:SPOI-ES-4326",  
  "refRelatedEntity": [  
    "urn:ngsi-ld:RelatedEntity:POI-PlazaCazorla-3123"  
  ],  
  "refSmartSpot": [  
    "urn:ngsi-ld:SmartSpot:SSPOT-F94C58E29DD5",  
    "urn:ngsi-ld:SmartSpot:SSPOT-F94C53E21DD2",  
    "urn:ngsi-ld:SmartSpot:SSPOT-F94C51A295D9"  
  ],  
  "type": "SmartPointOfInteraction"  
}  
```  
