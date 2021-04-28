Entität: SmartSpot  
==================  
[Offene Lizenz](https://github.com/smart-data-models//dataModel.PointOfInteraction/blob/master/SmartSpot/LICENSE.md)  
Globale Beschreibung: **FIWARE Smart Spot Entity-Schema für Validierungs-Tools**  

## Liste der Eigenschaften  

- `alternateName`: Ein alternativer Name für diesen Artikel  - `announcedUrl`: Vom Gerät gesendete URL  - `announcementPeriod`: Zeitraum zwischen den Ansagen in Millisekunden  - `availability`: Gibt die Zeitintervalle an, in denen dieser interaktive Dienst verfügbar ist, dies ist jedoch eine allgemeine Information, während Smart Spots ihre eigene reale Verfügbarkeit haben, um erweiterte Konfigurationen zu ermöglichen  - `bluetoothChannel`: Bluetooth-Kanäle, auf denen die Ansage übertragen werden soll  - `coverageRadius`: Radius des Spot-Abdeckungsbereichs in Metern  - `dataProvider`: Eine Folge von Zeichen, die den Anbieter der harmonisierten Dateneinheit identifiziert.  - `dateCreated`: Zeitstempel der Entitätserstellung. Dieser wird normalerweise von der Speicherplattform zugewiesen.  - `dateModified`: Zeitstempel der letzten Änderung der Entität. Dieser wird in der Regel von der Speicherplattform vergeben.  - `description`: Eine Beschreibung dieses Artikels  - `id`: Eindeutiger Bezeichner der Entität  - `name`: Der Name dieses Elements.  - `owner`: Eine Liste mit einer JSON-kodierten Zeichenfolge, die auf die eindeutigen Ids der Eigentümer verweist  - `refSmartPointOfInteraction`: Eindeutiger Bezeichner der Entität  - `seeAlso`: Liste von uri, die auf zusätzliche Ressourcen über das Element verweist  - `signalStrength`: Signalstärke zum Einstellen des Ansagebereichs. Enum:'höchste, niedrigste, mittel'  - `source`: Eine Folge von Zeichen, die die ursprüngliche Quelle der Entitätsdaten als URL angibt. Empfohlen wird der voll qualifizierte Domänenname des Quellanbieters oder die URL zum Quellobjekt.  - `type`: NGSI Entity-Typ. Es muss SmartSpot sein    
Erforderliche Eigenschaften  
- `announcedUrl`  - `announcementPeriod`  - `availability`  - `bluetoothChannel`  - `id`  - `signalStrength`  - `type`    
Smart Spots sind Geräte, die die Technologie bereitstellen, die es Benutzern ermöglicht, Zugang zu intelligenten Interaktionspunkten zu erhalten, um zusätzliche Informationen zu erhalten (Infotainment, etc.), Vorschläge zu machen (Vorschlagsmailbox, etc.) oder neue Inhalte zu generieren (Co-Creation, etc.). Das Datenmodell enthält Ressourcen zur Konfiguration des Interaktionsdienstes, wie z. B. die gesendete URL (typischerweise verkürzt), den Zeitraum zwischen den Sendungen, die Verfügbarkeit des Dienstes, die Sendeleistung in Abhängigkeit vom abzudeckenden Gebiet usw.  
## Datenmodell Beschreibung der Eigenschaften  
Alphabetisch sortiert (für Details anklicken)  
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
## Beispiel-Nutzlasten  
#### SmartSpot NGSI-v2 key-values Beispiel  
Hier ist ein Beispiel für einen SmartSpot im JSON-LD-Format als Key-Values. Dies ist kompatibel mit NGSI-v2 bei Verwendung von `options=keyValues` und liefert die Kontextdaten einer einzelnen Entität.  
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
#### SmartSpot NGSI-v2 normalisiert Beispiel  
Hier ist ein Beispiel für einen SmartSpot im JSON-LD-Format wie normalisiert. Dies ist kompatibel mit NGSI-v2, wenn keine Optionen verwendet werden und liefert die Kontextdaten einer einzelnen Entität.  
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
#### SmartSpot NGSI-LD Schlüssel-Werte Beispiel  
Hier ist ein Beispiel für einen SmartSpot im JSON-LD-Format als Key-Values. Dies ist kompatibel mit NGSI-LD bei Verwendung von `options=keyValues` und liefert die Kontextdaten einer einzelnen Entität.  
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
#### SmartSpot NGSI-LD normalisiert Beispiel  
Hier ist ein Beispiel für einen SmartSpot im JSON-LD-Format wie normalisiert. Dies ist kompatibel mit NGSI-LD, wenn keine Optionen verwendet werden und liefert die Kontextdaten einer einzelnen Entität.  
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
