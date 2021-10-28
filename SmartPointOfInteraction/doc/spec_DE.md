Entität: SmartPointOfInteraction  
================================  
[Offene Lizenz](https://github.com/smart-data-models//dataModel.PointOfInteraction/blob/master/SmartPointOfInteraction/LICENSE.md)  
[Dokument automatisch generiert](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
Globale Beschreibung: **Smart Data Models Smart Point of Interaction Entitätsschema für Validierungswerkzeuge**  
Version: 0.0.2  

## Liste der Eigenschaften  

- `address`: Die Postanschrift  - `alternateName`: Ein alternativer Name für diesen Artikel  - `applicationUrl`: Dieses Feld gibt die tatsächliche URL an, die die Lösung oder Anwendung enthält (Informationen, Co-Creation usw.), während das SmartSpot-Feld "announcedUrl" die Broadcast-URL angibt, die dieselbe oder eine verkürzte URL sein kann.  - `areaCovered`: Geojson-Referenz auf das Element. Es kann Punkt, LineString, Polygon, MultiPoint, MultiLineString oder MultiPolygon sein  - `areaServed`: Das geografische Gebiet, in dem eine Dienstleistung oder ein angebotener Artikel erbracht wird  - `availability`: Gibt die Zeitintervalle an, in denen dieser interaktive Dienst generell verfügbar ist. Es ist zu beachten, dass Smart Spots ihre eigene tatsächliche Verfügbarkeit haben, um erweiterte Konfigurationen zu ermöglichen. Die Syntax muss mit schema.org konform sein. So wird beispielsweise ein Dienst, der nur an Wochentagen aktiv ist, als "Verfügbarkeit" kodiert: 'Mo,Tu,We,Th,Fr,Sa 09:00-20:00'.  - `category`: Definiert die Art der Interaktion. Enum:'Mitgestaltung, Unterhaltung, Information, Infotainment'  - `dataProvider`: Eine Folge von Zeichen zur Identifizierung des Anbieters der harmonisierten Dateneinheit.  - `dateCreated`: Zeitstempel der Entitätserstellung. Dieser wird in der Regel von der Speicherplattform zugewiesen.  - `dateModified`: Zeitstempel der letzten Änderung der Entität. Dieser wird in der Regel von der Speicherplattform vergeben.  - `description`: Eine Beschreibung dieses Artikels  - `id`: Eindeutiger Bezeichner der Entität  - `location`: Geojson-Referenz auf das Element. Es kann Punkt, LineString, Polygon, MultiPoint, MultiLineString oder MultiPolygon sein  - `name`: Der Name dieses Artikels.  - `owner`: Eine Liste mit einer JSON-kodierten Zeichenfolge, die auf die eindeutigen Kennungen der Eigentümer verweist  - `refRelatedEntity`: Liste der Unternehmen, die mit diesem Smart Point of Interaction verbessert wurden  - `refSmartSpot`:  Verweise auf die Smart Spot-Geräte, die Teil des Smart Point of Interaction sind  - `seeAlso`: Liste von URLs, die auf zusätzliche Ressourcen zu dem Artikel verweisen  - `source`: Eine Folge von Zeichen, die die ursprüngliche Quelle der Entitätsdaten als URL angibt. Empfohlen wird der voll qualifizierte Domänenname des Quellanbieters oder die URL des Quellobjekts.  - `type`: NGSI-Entitätstyp. Es muss SmartPointOfInteraction sein    
Erforderliche Eigenschaften  
- `id`  - `type`    
Ein Smart Point of Interaction definiert einen Ort mit Technologie zur Interaktion mit Nutzern, z. B. durch Beacon-Technologie von Apple, Eddystone/Physical-Web von Google oder andere auf Nähe basierende Schnittstellen. Da der interaktive Bereich aus mehr als einem Gerät bestehen kann, das die Technologie bereitstellt, umfasst dieses Modell eine Gruppe von SmartSpot-Geräten. Das Datenmodell enthält Informationen über den Bereich/die Fläche, der/die von der Technologie abgedeckt wird (d. h. der Bereich, der von einem Bluetooth Low Energy-basierten Beacon abgedeckt wird), eine Möglichkeit zur Angabe der Funktionsintervalle (d. h. wann interaktive Punkte verfügbar sind) und einen Link zu einer Multimedia-Ressource, die für die Benutzerinteraktion bestimmt ist (d. h. Web Apps usw.). Darüber hinaus kann das Datenmodell auf eine andere NGSI-Entität verweisen, z. B. einen Parkplatz, einen Point of Interest (POI) usw., wobei die Interaktion durch diesen intelligenten Interaktionspunkt angereichert wird.  
## Datenmodell Beschreibung der Eigenschaften  
Alphabetisch sortiert (für Details anklicken)  
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
      x-ngsi:    
        type: Geoproperty    
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
        type: Geoproperty    
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
  version: 0.0.2    
```  
</details>    
## Beispiel-Nutzlasten  
#### SmartPointOfInteraction NGSI-v2 key-values Beispiel  
Hier ist ein Beispiel für eine SmartPointOfInteraction im JSON-LD-Format als Schlüsselwerte. Dies ist kompatibel mit NGSI-v2, wenn `options=keyValues` verwendet wird und liefert die Kontextdaten einer einzelnen Entität.  
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
#### SmartPointOfInteraction NGSI-v2 normalisiert Beispiel  
Hier ist ein Beispiel für eine SmartPointOfInteraction im JSON-LD-Format in normalisierter Form. Dies ist kompatibel mit NGSI-v2, wenn keine Optionen verwendet werden, und liefert die Kontextdaten einer einzelnen Entität.  
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
#### SmartPointOfInteraction NGSI-LD key-values Beispiel  
Hier ist ein Beispiel für eine SmartPointOfInteraction im JSON-LD-Format als Schlüsselwerte. Dies ist mit NGSI-LD kompatibel, wenn `options=keyValues` verwendet wird und liefert die Kontextdaten einer einzelnen Entität.  
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
#### SmartPointOfInteraction NGSI-LD normalisiert Beispiel  
Hier ist ein Beispiel für eine SmartPointOfInteraction im JSON-LD-Format in normalisierter Form. Dies ist kompatibel mit NGSI-LD, wenn keine Optionen verwendet werden, und liefert die Kontextdaten einer einzelnen Entität.  
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
