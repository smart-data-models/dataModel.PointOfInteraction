<!-- 10-Header -->  
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)  
Entité : SmartSpot  
==================<!-- /10-Header -->  
<!-- 15-License -->  
[Licence ouverte] (https://github.com/smart-data-models//dataModel.PointOfInteraction/blob/master/SmartSpot/LICENSE.md)  
[document généré automatiquement] (https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
<!-- /15-License -->  
<!-- 20-Description -->  
Description globale : **Modèles de données intelligentes Schéma d'entité Smart Spot destiné aux outils de validation**  
version : 0.1.0  
<!-- /20-Description -->  
<!-- 30-PropertiesList -->  

## Liste des propriétés  

<sup><sub>[*] S'il n'y a pas de type dans un attribut, c'est parce qu'il peut avoir plusieurs types ou différents formats/modèles</sub></sup>.  
- `alternateName[string]`: Un nom alternatif pour ce poste  - `announcedUrl[string]`: URL diffusée par l'appareil  . Model: [https://schema.org/URL](https://schema.org/URL)- `announcementPeriod[number]`: Période entre les annonces en millisecondes  . Model: [https://schema.org/Number](https://schema.org/Number)- `availability[string]`: Spécifie les intervalles de temps pendant lesquels ce service interactif est disponible, mais il s'agit d'une information générale alors que les Smart Spots ont leur propre disponibilité réelle afin de permettre des configurations avancées.  . Model: [https://schema.org/openingHours](https://schema.org/openingHours)- `bluetoothChannel[string]`: Canaux Bluetooth où transmettre l'annonce  . Model: [ https://schema.org/Text]( https://schema.org/Text)- `coverageRadius[number]`: Rayon de la zone de couverture en mètres  . Model: [https://schema.org/Number](https://schema.org/Number)- `dataProvider[string]`: Une séquence de caractères identifiant le fournisseur de l'entité de données harmonisées.  - `dateCreated[string]`: Date de création de l'entité. Celle-ci est généralement attribuée par la plate-forme de stockage.  - `dateModified[string]`: Date de la dernière modification de l'entité. Cette date est généralement attribuée par la plate-forme de stockage.  - `description[string]`: Une description de l'article  - `id[*]`: Identifiant unique de l'entité  - `name[string]`: Le nom de cet élément.  - `owner[array]`: Une liste contenant une séquence de caractères encodés JSON référençant les identifiants uniques du ou des propriétaires.  - `refSmartPointOfInteraction[*]`: Référence au point d'interaction intelligent qui comprend ce Smart Spot  . Model: [https://schema.org/URL](https://schema.org/URL)- `seeAlso[*]`: liste d'uri pointant vers des ressources supplémentaires concernant l'élément  - `signalStrength[string]`: Intensité du signal pour ajuster la portée de l'annonce. Enum : "plus fort, plus faible, moyen  - `source[string]`: Séquence de caractères indiquant la source originale des données de l'entité sous forme d'URL. Il est recommandé d'utiliser le nom de domaine complet du fournisseur de la source ou l'URL de l'objet source.  - `type[string]`: Type d'entité NGSI. Il doit s'agir de SmartSpot  <!-- /30-PropertiesList -->  
<!-- 35-RequiredProperties -->  
Propriétés requises  
- `id`  - `type`  <!-- /35-RequiredProperties -->  
<!-- 40-RequiredProperties -->  
Les points intelligents sont des dispositifs qui fournissent la technologie permettant aux utilisateurs d'accéder à des points d'interaction intelligents afin d'obtenir des informations supplémentaires (infodivertissement, etc.), de fournir des suggestions (boîte aux lettres de suggestions, etc.) ou de générer de nouveaux contenus (cocréation, etc.). Le modèle de données contient des ressources permettant de configurer le service d'interaction, telles que l'URL diffusée (généralement raccourcie), la période entre les diffusions, la disponibilité du service, la puissance de transmission en fonction de la zone à couvrir, etc.  
<!-- /40-RequiredProperties -->  
<!-- 50-DataModelHeader -->  
## Modèle de données description des propriétés  
Classés par ordre alphabétique (cliquez pour plus de détails)  
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
## Exemples de charges utiles  
#### SmartSpot NGSI-v2 Valeurs clés Exemple  
Voici un exemple de SmartSpot au format JSON-LD en tant que valeurs clés. Ceci est compatible avec NGSI-v2 lorsque l'on utilise `options=keyValues` et renvoie les données de contexte d'une entité individuelle.  
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
#### SmartSpot NGSI-v2 normalisé Exemple  
Voici un exemple de SmartSpot au format JSON-LD tel que normalisé. Ce format est compatible avec NGSI-v2 lorsqu'il n'utilise pas d'options et renvoie les données contextuelles d'une entité individuelle.  
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
#### SmartSpot NGSI-LD key-values Exemple  
Voici un exemple de SmartSpot au format JSON-LD sous forme de valeurs-clés. Ceci est compatible avec NGSI-LD lorsque l'on utilise `options=keyValues` et renvoie les données de contexte d'une entité individuelle.  
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
#### SmartSpot NGSI-LD normalisé Exemple  
Voici un exemple de SmartSpot au format JSON-LD tel que normalisé. Ce format est compatible avec NGSI-LD lorsqu'il n'utilise pas d'options et renvoie les données contextuelles d'une entité individuelle.  
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
Voir [FAQ 10] (https://smartdatamodels.org/index.php/faqs/) pour obtenir une réponse à la question de savoir comment traiter les unités de magnitude.  
<!-- /95-Units -->  
<!-- 97-LastFooter -->  
---  
[Smart Data Models](https://smartdatamodels.org) +++ [Contribution Manual](https://bit.ly/contribution_manual) +++ [About](https://bit.ly/Introduction_SDM)<!-- /97-LastFooter -->  
