<!-- 10-Header -->    
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)    
实体：智能点    
======<!-- /10-Header -->    
<!-- 15-License -->    
[开放许可](https://github.com/smart-data-models//dataModel.PointOfInteraction/blob/master/SmartSpot/LICENSE.md)    
[文件自动生成](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)    
<!-- /15-License -->    
<!-- 20-Description -->    
全局描述：**智能数据模型 智能点实体模式用于验证工具**    
版本： 0.1.0    
<!-- /20-Description -->    
<!-- 30-PropertiesList -->    
## 属性列表    
<sup><sub>[*] 如果属性中没有类型，是因为它可能有多个类型或不同的格式/模式</sub></sup>。    
- `alternateName[string]`: 该项目的替代名称  - `announcedUrl[uri]`: 设备广播的 URL  . Model: [https://schema.org/URL](https://schema.org/URL)- `announcementPeriod[number]`: 两次广播之间的间隔时间（毫秒  . Model: [https://schema.org/Number](https://schema.org/Number)- `availability[string]`: 指定此交互式服务可用的时间间隔，但这只是一般信息，智能点有自己的实际可用性，以便进行高级配置。  . Model: [https://schema.org/openingHours](https://schema.org/openingHours)- `bluetoothChannel[string]`: 传输公告的蓝牙通道  . Model: [ https://schema.org/Text]( https://schema.org/Text)- `coverageRadius[number]`: 点覆盖区域半径（米  . Model: [https://schema.org/Number](https://schema.org/Number)- `dataProvider[string]`: 标识统一数据实体提供者的字符序列  - `dateCreated[date-time]`: 实体创建时间戳。通常由存储平台分配  - `dateModified[date-time]`: 实体最后一次修改的时间戳。通常由存储平台分配  - `description[string]`: 项目描述  - `id[*]`: 实体的唯一标识符  - `name[string]`: 该项目的名称  - `owner[array]`: 包含一个 JSON 编码字符序列的列表，其中引用了所有者的唯一 Ids  - `refSmartPointOfInteraction[*]`: 参考智能互动点，其中包括该智能点  . Model: [https://schema.org/URL](https://schema.org/URL)- `seeAlso[*]`: 指向有关该项目的其他资源的 uri 列表  - `signalStrength[string]`: 用于调整广播范围的信号强度。枚举："最高、最低、中等"。  - `source[string]`: 以 URL 形式给出实体数据原始来源的字符串。建议使用源提供者的完全合格域名或源对象的 URL  - `type[string]`: NGSI 实体类型。必须是 SmartSpot  <!-- /30-PropertiesList -->    
<!-- 35-RequiredProperties -->    
所需属性    
- `id`  - `type`  <!-- /35-RequiredProperties -->    
<!-- 40-RequiredProperties -->    
智能点是提供技术的设备，允许用户访问智能交互点，从而获得额外信息（信息娱乐等）、提供建议（建议邮箱等）或生成新内容（共同创作等）。数据模型包含用于配置交互服务的资源，如广播 URL（通常是缩短的）、广播间隔时间、服务可用性、根据覆盖区域而定的传输功率等。    
<!-- /40-RequiredProperties -->    
<!-- 50-DataModelHeader -->    
## 属性的数据模型描述    
按字母顺序排列（点击查看详情）    
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
## 有效载荷示例    
#### SmartSpot NGSI-v2 键值示例    
下面是一个以 JSON-LD 格式作为键值的 SmartSpot 示例。当使用 "options=keyValues "时，它与 NGSI-v2 兼容，并返回单个实体的上下文数据。    
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
#### SmartSpot NGSI-v2 标准化示例    
下面是一个规范化 JSON-LD 格式 SmartSpot 的示例。当不使用选项时，它与 NGSI-v2 兼容，并返回单个实体的上下文数据。    
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
#### SmartSpot NGSI-LD 键值示例    
下面是一个以 JSON-LD 格式作为键值的 SmartSpot 示例。当使用 `options=keyValues` 时，它与 NGSI-LD 兼容，并返回单个实体的上下文数据。    
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
#### SmartSpot NGSI-LD 归一化示例    
下面是一个以 JSON-LD 格式规范化的 SmartSpot 示例。当不使用选项时，它与 NGSI-LD 兼容，并返回单个实体的上下文数据。    
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
请参阅 [FAQ 10](https://smartdatamodels.org/index.php/faqs/)，获取如何处理幅度单位的答案。    
<!-- /95-Units -->    
<!-- 97-LastFooter -->    
---    
[Smart Data Models](https://smartdatamodels.org) +++ [Contribution Manual](https://bit.ly/contribution_manual) +++ [About](https://bit.ly/Introduction_SDM)<!-- /97-LastFooter -->    
