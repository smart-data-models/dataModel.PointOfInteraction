Entité : SmartSpot  
==================  
Cette spécification est une **version temporelle**. Elle est générée automatiquement à partir des propriétés documentées décrites dans le schema.json condensé dans le fichier `model.yaml`. Un fichier temporaire `nouveau_modèle.yaml` a été créé dans chaque modèle de données pour éviter d'avoir un impact sur les scripts existants. Ainsi, la spécification sera incomplète tant que le fichier schema.json n'est pas mis à jour au nouveau format (documentation des propriétés). Une fois mis à jour, le fichier `model.yaml` (`nouveau_model.yaml`) doit être mis à jour également (automatiquement) . Plus d'informations dans ce [lien](https://github.com/smart-data-models/data-models/blob/master/specs/warning_message_new_spec.md). Tant qu'il s'agit d'un format provisoire, tout [feedback est le bienvenu dans ce formulaire](https://smartdatamodels.org/index.php/submit-an-issue-2/) en choisissant l'option "Feedback sur la nouvelle spécification".  
Description globale : **Schéma de l'entité Smart Spot du logiciel destiné aux outils de validation**  

## Liste des biens  

`alternateName`: Un autre nom pour cet article  `announcedUrl`: URL diffusée par l'appareil  `announcementPeriod`: Période entre les annonces en millisecondes  `availability`: Précise les intervalles de temps pendant lesquels ce service interactif est disponible, mais il s'agit d'une information générale alors que les Smart Spots ont leur propre disponibilité réelle afin de permettre des configurations avancées  `bluetoothChannel`: Canaux Bluetooth où transmettre l'annonce  `coverageRadius`: Rayon de la zone de couverture du spot en mètres  `dataProvider`: Une séquence de caractères identifiant le fournisseur de l'entité de données harmonisées.  `dateCreated`: Horodatage de la création de l'entité. Il est généralement attribué par la plate-forme de stockage.  `dateModified`: Horodatage de la dernière modification de l'entité. Il est généralement attribué par la plate-forme de stockage.  `description`: Une description de cet article  `id`:   `name`: Le nom de cet article.  `owner`: Une liste contenant une séquence de caractères codés en JSON faisant référence aux Ids uniques du ou des propriétaires  `refSmartPointOfInteraction`:   `seeAlso`:   `signalStrength`: Puissance du signal pour ajuster la portée de l'annonce  `source`: Une séquence de caractères donnant comme URL la source originale des données de l'entité. Il est recommandé d'utiliser le nom de domaine complet du fournisseur de la source, ou l'URL de l'objet source.  `type`: NGSI Type d'entité  ## Modèle de données description des biens  
Classement par ordre alphabétique  
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
Voici un exemple de SmartSpot au format JSON comme valeurs clés. Il est compatible avec NGSI V2 lorsqu'il utilise "options=keyValues" et renvoie les données de contexte d'une entité individuelle.  
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
Voici un exemple d'un SmartSpot au format JSON tel que normalisé. Il est compatible avec NGSI V2 lorsqu'il utilise "options=keyValues" et renvoie les données de contexte d'une entité individuelle.  
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
Voici un exemple de SmartSpot au format JSON-LD comme valeurs clés. Il est compatible avec le format JSON-LD lorsqu'il n'utilise pas d'options et renvoie les données de contexte d'une entité individuelle.  
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
Voici un exemple de SmartSpot au format JSON-LD tel que normalisé. Il est compatible avec le format JSON-LD lorsqu'il n'utilise pas d'options et renvoie les données de contexte d'une entité individuelle.  
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
