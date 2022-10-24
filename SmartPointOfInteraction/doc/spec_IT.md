<!-- 10-Header -->  
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)  
Entità: Punto di Interazione Intelligente  
=========================================<!-- /10-Header -->  
<!-- 15-License -->  
[Licenza aperta](https://github.com/smart-data-models//dataModel.PointOfInteraction/blob/master/SmartPointOfInteraction/LICENSE.md)  
[documento generato automaticamente](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
<!-- /15-License -->  
<!-- 20-Description -->  
Descrizione globale: **Schema di entità Smart Data Models Smart Point of Interaction destinato agli strumenti di convalida**.  
versione: 0.0.2  
<!-- /20-Description -->  
<!-- 30-PropertiesList -->  

## Elenco delle proprietà  

<sup><sub>[*] Se non c'è un tipo in un attributo è perché potrebbe avere diversi tipi o diversi formati/modelli</sub></sup>.  
- `address[object]`: L'indirizzo postale  . Model: [https://schema.org/address](https://schema.org/address)- `alternateName[string]`: Un nome alternativo per questa voce  - `applicationUrl[string]`: Questo campo specifica l'URL reale che contiene la soluzione o l'applicazione (informazioni, co-creazione, ecc.), mentre il campo "announcedUrl" di SmartSpot specifica l'URL di trasmissione, che può essere questo stesso URL o uno abbreviato.  . Model: [https://schema.org/URL](https://schema.org/URL)- `areaCovered[*]`: Riferimento Geojson all'elemento. Può essere un punto, una stringa di linea, un poligono, un multi-punto, una stringa di linea o un poligono multiplo.  - `areaServed[string]`: L'area geografica in cui viene fornito il servizio o l'articolo offerto.  . Model: [https://schema.org/Text](https://schema.org/Text)- `availability[string]`: Specifica gli intervalli di tempo in cui questo servizio interattivo è generalmente disponibile. Si noti che gli Smart Spot hanno una propria disponibilità reale per consentire configurazioni avanzate. La sintassi deve essere conforme a schema.org. Ad esempio, un servizio attivo solo nei giorni feriali sarà codificato come 'disponibilità': 'Mo,Tu,We,Th,Fr,Sa 09:00-20:00'.  . Model: [https://schema.org/openingHours](https://schema.org/openingHours)- `category[array]`: Definisce il tipo di interazione. Enum:'co-creazione, intrattenimento, informazione, infotainment'.  . Model: [http://schema.org/Text](http://schema.org/Text)- `dataProvider[string]`: Una sequenza di caratteri che identifica il fornitore dell'entità di dati armonizzata.  - `dateCreated[string]`: Timestamp di creazione dell'entità. Di solito viene assegnato dalla piattaforma di archiviazione.  - `dateModified[string]`: Timestamp dell'ultima modifica dell'entità. Di solito viene assegnato dalla piattaforma di archiviazione.  - `description[string]`: Descrizione dell'articolo  - `id[*]`: Identificatore univoco dell'entità  - `location[*]`: Riferimento Geojson all'elemento. Può essere un punto, una stringa di linea, un poligono, un multi-punto, una stringa di linea o un poligono multiplo.  - `name[string]`: Il nome di questo elemento.  - `owner[array]`: Un elenco contenente una sequenza di caratteri codificata JSON che fa riferimento agli ID univoci dei proprietari.  - `refRelatedEntity[array]`: Elenco delle entità migliorate con questo Punto di Interazione Intelligente  . Model: [The entity type could be any such as a Parking, Point of Interest, etc.http://schema.org/Text](The entity type could be any such as a Parking, Point of Interest, etc.http://schema.org/Text)- `refSmartSpot[array]`:  Riferimenti ai dispositivi Smart Spot che fanno parte dello Smart Point of Interaction  . Model: [https://schema.org/URL](https://schema.org/URL)- `seeAlso[*]`: elenco di uri che puntano a risorse aggiuntive sull'elemento  - `source[string]`: Una sequenza di caratteri che indica la fonte originale dei dati dell'entità come URL. Si consiglia di utilizzare il nome di dominio completamente qualificato del provider di origine o l'URL dell'oggetto di origine.  - `type[string]`: Tipo di entità NGSI. Deve essere SmartPointOfInteraction  <!-- /30-PropertiesList -->  
<!-- 35-RequiredProperties -->  
Proprietà richieste  
- `id`  - `type`  <!-- /35-RequiredProperties -->  
<!-- 40-RequiredProperties -->  
Uno Smart Point of Interaction definisce un luogo dotato di tecnologia per interagire con gli utenti, ad esempio attraverso la tecnologia Beacon di Apple, Eddystone/Physical-Web di Google o altre interfacce basate sulla prossimità. Poiché l'area interattiva potrebbe essere composta da più di un dispositivo che fornisce la tecnologia, questo modello comprende un gruppo di dispositivi SmartSpot. Il modello di dati include informazioni relative all'area/superficie coperta dalla tecnologia (ad esempio, l'area coperta dal Beacon Bluetooth Low Energy), un modo per specificare gli intervalli di funzionalità (ad esempio, quando sono disponibili i punti interattivi) e un collegamento a una risorsa multimediale destinata all'interazione con l'utente (ad esempio, applicazioni Web, ecc.). Inoltre, il modello di dati può fare riferimento a un'altra entità NGSI come un parcheggio, un punto di interesse (POI), ecc. con un'interazione arricchita fornita da questo punto di interazione intelligente.  
<!-- /40-RequiredProperties -->  
<!-- 50-DataModelHeader -->  
## Modello di dati descrizione delle proprietà  
Ordinati in ordine alfabetico (clicca per i dettagli)  
<!-- /50-DataModelHeader -->  
<!-- 60-ModelYaml -->  
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
## Esempi di payload  
#### Valori-chiave di SmartPointOfInteraction NGSI-v2 Esempio  
Ecco un esempio di SmartPointOfInteraction in formato JSON-LD come valori-chiave. Questo è compatibile con NGSI-v2 quando si usa `options=keyValues` e restituisce i dati di contesto di una singola entità.  
<details><summary><strong>show/hide example</strong></summary>    
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
</details>  
#### SmartPointOfInteraction NGSI-v2 normalizzato Esempio  
Ecco un esempio di SmartPointOfInteraction in formato JSON-LD normalizzato. Questo è compatibile con NGSI-v2 quando non si utilizzano opzioni e restituisce i dati di contesto di una singola entità.  
<details><summary><strong>show/hide example</strong></summary>    
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
</details>  
#### SmartPointOfInteraction Valori chiave NGSI-LD Esempio  
Ecco un esempio di SmartPointOfInteraction in formato JSON-LD come valori-chiave. Questo è compatibile con NGSI-LD quando si usa `options=keyValues` e restituisce i dati di contesto di una singola entità.  
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
</details>  
#### SmartPointOfInteraction NGSI-LD normalizzato Esempio  
Ecco un esempio di SmartPointOfInteraction in formato JSON-LD normalizzato. Questo è compatibile con NGSI-LD quando non si utilizzano opzioni e restituisce i dati di contesto di una singola entità.  
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
</details><!-- /80-Examples -->  
<!-- 90-FooterNotes -->  
<!-- /90-FooterNotes -->  
<!-- 95-Units -->  
Vedere [FAQ 10](https://smartdatamodels.org/index.php/faqs/) per ottenere una risposta su come gestire le unità di grandezza.  
<!-- /95-Units -->  
<!-- 97-LastFooter -->  
---  
[Smart Data Models](https://smartdatamodels.org) +++ [Contribution Manual](https://bit.ly/contribution_manual) +++ [About](https://bit.ly/Introduction_SDM)<!-- /97-LastFooter -->  
