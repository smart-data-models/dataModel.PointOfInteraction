<!-- 10-Header -->      
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)      
엔티티: 엔티티: SmartSpot      
===================<!-- /10-Header -->      
<!-- 15-License -->      
[오픈 라이선스](https://github.com/smart-data-models//dataModel.PointOfInteraction/blob/master/SmartSpot/LICENSE.md)      
[문서 자동 생성](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)      
<!-- /15-License -->      
<!-- 20-Description -->      
글로벌 설명: **유효성 검사 도구용 스마트 데이터 모델 스마트 스팟 엔티티 스키마**.      
버전: 0.1.0      
<!-- /20-Description -->      
<!-- 30-PropertiesList -->      
## 속성 목록      
<sup><sub>[*] 속성에 유형이 없는 것은 여러 유형 또는 다른 형식/패턴을 가질 수 있기 때문입니다</sub></sup>.      
- `alternateName[string]`: 이 항목의 대체 이름  - `announcedUrl[uri]`: 디바이스에서 브로드캐스트한 URL  . Model: [https://schema.org/URL](https://schema.org/URL)- `announcementPeriod[number]`: 알림 사이의 간격(밀리초)  . Model: [https://schema.org/Number](https://schema.org/Number)- `availability[string]`: 이 대화형 서비스를 사용할 수 있는 시간 간격을 지정하지만, 이는 일반적인 정보이며 스마트 스팟은 고급 구성을 허용하기 위해 자체적인 실제 가용성이 있습니다.  . Model: [https://schema.org/openingHours](https://schema.org/openingHours)- `bluetoothChannel[string]`: 공지 사항을 전송할 블루투스 채널  . Model: [ https://schema.org/Text]( https://schema.org/Text)- `coverageRadius[number]`: 스팟 커버리지 영역의 반경(미터)  . Model: [https://schema.org/Number](https://schema.org/Number)- `dataProvider[string]`: 조화된 데이터 엔티티의 공급자를 식별하는 일련의 문자  - `dateCreated[date-time]`: 엔티티 생성 타임스탬프. 이는 일반적으로 스토리지 플랫폼에서 할당합니다.  - `dateModified[date-time]`: 엔티티의 마지막 수정 타임스탬프입니다. 이는 일반적으로 스토리지 플랫폼에서 할당합니다.  - `description[string]`: 이 항목에 대한 설명  - `id[*]`: 엔티티의 고유 식별자  - `name[string]`: 이 항목의 이름  - `owner[array]`: 소유자의 고유 ID를 참조하는 JSON 인코딩된 문자 시퀀스가 포함된 목록입니다.  - `refSmartPointOfInteraction[*]`: 이 스마트 스팟을 포함하는 스마트 인터랙션 지점에 대한 참조  . Model: [https://schema.org/URL](https://schema.org/URL)- `seeAlso[*]`: 항목에 대한 추가 리소스를 가리키는 URL 목록  - `signalStrength[string]`: 신호 강도로 알림 범위를 조정합니다. Enum:'최고, 최저, 중간'  - `source[string]`: 엔티티 데이터의 원본 소스를 URL로 제공하는 문자 시퀀스입니다. 소스 공급자의 정규화된 도메인 이름 또는 소스 개체에 대한 URL을 사용하는 것이 좋습니다.  - `type[string]`: NGSI 엔티티 유형. SmartSpot이어야 합니다.  <!-- /30-PropertiesList -->      
<!-- 35-RequiredProperties -->      
필수 속성      
- `id`  - `type`  <!-- /35-RequiredProperties -->      
<!-- 40-RequiredProperties -->      
스마트 스팟은 사용자가 스마트 상호작용 지점에 액세스하여 추가 정보(인포테인먼트 등)를 얻거나 제안(제안 메일함 등)을 제공하거나 새로운 콘텐츠(공동 제작 등)를 생성할 수 있도록 하는 기술을 제공하는 장치입니다. 데이터 모델에는 방송 URL(일반적으로 단축), 방송 간격, 서비스 가용성, 서비스 대상 지역에 따른 전송 전력 등과 같은 상호 작용 서비스를 구성하는 리소스가 포함되어 있습니다.      
<!-- /40-RequiredProperties -->      
<!-- 50-DataModelHeader -->      
## 속성에 대한 데이터 모델 설명      
알파벳순으로 정렬(자세한 내용을 보려면 클릭)      
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
      description: A sequence of characters identifying the provider of the harmonised data entity        
      type: string        
      x-ngsi:        
        type: Property        
    dateCreated:        
      description: Entity creation timestamp. This will usually be allocated by the storage platform        
      format: date-time        
      type: string        
      x-ngsi:        
        type: Property        
    dateModified:        
      description: Timestamp of the last modification of the entity. This will usually be allocated by the storage platform        
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
      anyOf:        
        - description: Identifier format of any NGSI entity        
          maxLength: 256        
          minLength: 1        
          pattern: ^[\w\-\.\{\}\$\+\*\[\]`|~^@!,:\\]+$        
          type: string        
          x-ngsi:        
            type: Property        
        - description: Identifier format of any NGSI entity        
          format: uri        
          type: string        
          x-ngsi:        
            type: Property        
      description: Unique identifier of the entity        
      x-ngsi:        
        type: Property        
    name:        
      description: The name of this item        
      type: string        
      x-ngsi:        
        type: Property        
    owner:        
      description: A List containing a JSON encoded sequence of characters referencing the unique Ids of the owner(s)        
      items:        
        anyOf:        
          - description: Identifier format of any NGSI entity        
            maxLength: 256        
            minLength: 1        
            pattern: ^[\w\-\.\{\}\$\+\*\[\]`|~^@!,:\\]+$        
            type: string        
            x-ngsi:        
              type: Property        
          - description: Identifier format of any NGSI entity        
            format: uri        
            type: string        
            x-ngsi:        
              type: Property        
        description: Unique identifier of the entity        
        x-ngsi:        
          type: Property        
      type: array        
      x-ngsi:        
        type: Property        
    refSmartPointOfInteraction:        
      anyOf:        
        - description: Identifier format of any NGSI entity        
          maxLength: 256        
          minLength: 1        
          pattern: ^[\w\-\.\{\}\$\+\*\[\]`|~^@!,:\\]+$        
          type: string        
          x-ngsi:        
            type: Property        
        - description: Identifier format of any NGSI entity        
          format: uri        
          type: string        
          x-ngsi:        
            type: Property        
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
      description: 'A sequence of characters giving the original source of the entity data as a URL. Recommended to be the fully qualified domain name of the source provider, or the URL to the source object'        
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
## 페이로드 예시      
#### SmartSpot NGSI-v2 키-값 예시      
다음은 JSON-LD 형식의 스마트스팟을 키-값으로 반환하는 예제입니다. 이는 `옵션=키값`을 사용할 때 NGSI-v2와 호환되며 개별 엔티티의 컨텍스트 데이터를 반환합니다.      
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
#### SmartSpot NGSI-v2 정규화 예제      
다음은 정규화된 JSON-LD 형식의 스마트스팟의 예입니다. 이는 옵션을 사용하지 않을 때 NGSI-v2와 호환되며 개별 엔티티의 컨텍스트 데이터를 반환합니다.      
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
    "type": "Text",  
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
#### 스마트스팟 NGSI-LD 키-값 예시      
다음은 JSON-LD 형식의 스마트스팟을 키-값으로 반환하는 예시입니다. 이는 `옵션=키값`을 사용할 때 NGSI-LD와 호환되며 개별 엔티티의 컨텍스트 데이터를 반환합니다.      
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
#### 스마트스팟 NGSI-LD 정규화 예제      
다음은 정규화된 JSON-LD 형식의 스마트스팟 예시입니다. 이는 옵션을 사용하지 않을 때 NGSI-LD와 호환되며 개별 엔티티의 컨텍스트 데이터를 반환합니다.      
<details><summary><strong>show/hide example</strong></summary>        
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
    "object": "urn:ngsi-ld:SmartSpot:SPOI-ES-4326"  
  },  
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
[FAQ 10](https://smartdatamodels.org/index.php/faqs/)을 참조하여 규모 단위를 다루는 방법에 대한 답변을 확인하세요.      
<!-- /95-Units -->      
<!-- 97-LastFooter -->      
---      
[Smart Data Models](https://smartdatamodels.org) +++ [Contribution Manual](https://bit.ly/contribution_manual) +++ [About](https://bit.ly/Introduction_SDM)<!-- /97-LastFooter -->      
