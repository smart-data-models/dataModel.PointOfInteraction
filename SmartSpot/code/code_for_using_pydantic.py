from __future__ import annotations

from enum import Enum
from typing import List, Optional, Union

from pydantic import AnyUrl, AwareDatetime, BaseModel, Field, confloat, constr


class BluetoothChannel(Enum):
    field_37 = 37
    field_38 = 38
    field_39 = 39
    field_37_38 = '37,38'
    field_38_39 = '38,39'
    field_37_39 = '37,39'
    field_37_38_39 = '37,38,39'


class SignalStrength(Enum):
    highest = 'highest'
    lowest = 'lowest'
    medium = 'medium'


class Type(Enum):
    SmartSpot = 'SmartSpot'


class SmartSpot(BaseModel):
    alternateName: Optional[str] = Field(
        None, description='An alternative name for this item'
    )
    announcedUrl: Optional[AnyUrl] = Field(
        None, description='URL broadcasted by the device'
    )
    announcementPeriod: Optional[confloat(ge=100.0, le=4000.0)] = Field(
        None, description='Period between announcements in milliseconds'
    )
    availability: Optional[str] = Field(
        None,
        description='Specifies the time intervals in which this interactive service is available, but this is a general information while Smart Spots have their own real availability in order to allow advanced configurations',
    )
    bluetoothChannel: Optional[BluetoothChannel] = Field(
        None, description='Bluetooth channels where to transmit the announcement'
    )
    coverageRadius: Optional[confloat(ge=1.0)] = Field(
        None, description='Radius of the spot coverage area in meters'
    )
    dataProvider: Optional[str] = Field(
        None,
        description='A sequence of characters identifying the provider of the harmonised data entity',
    )
    dateCreated: Optional[AwareDatetime] = Field(
        None,
        description='Entity creation timestamp. This will usually be allocated by the storage platform',
    )
    dateModified: Optional[AwareDatetime] = Field(
        None,
        description='Timestamp of the last modification of the entity. This will usually be allocated by the storage platform',
    )
    description: Optional[str] = Field(None, description='A description of this item')
    id: Optional[
        Union[
            constr(
                pattern=r'^[\\w\\-\\.\\{\\}\\$\\+\\*\\[\\]`|~^@!, :\\\\]+$',
                min_length=1,
                max_length=256,
            ),
            AnyUrl,
        ]
    ] = Field(None, description='Unique identifier of the entity')
    name: Optional[str] = Field(None, description='The name of this item')
    owner: Optional[
        List[
            Union[
                constr(
                    pattern=r'^[\\w\\-\\.\\{\\}\\$\\+\\*\\[\\]`|~^@!,:\\\\]+$',
                    min_length=1,
                    max_length=256,
                ),
                AnyUrl,
            ]
        ]
    ] = Field(
        None,
        description='A List containing a JSON encoded sequence of characters referencing the unique Ids of the owner(s)',
    )
    refSmartPointOfInteraction: Optional[
        Union[
            constr(
                pattern=r'^[\\w\\-\\.\\{\\}\\$\\+\\*\\[\\]`|~^@!, :\\\\]+$',
                min_length=1,
                max_length=256,
            ),
            AnyUrl,
        ]
    ] = Field(
        None,
        description='Reference to the Smart Point of Interaction which includes this Smart Spot',
    )
    seeAlso: Optional[Union[List[AnyUrl], AnyUrl]] = Field(
        None, description='list of uri pointing to additional resources about the item'
    )
    signalStrength: Optional[SignalStrength] = Field(
        None,
        description="Signal strength to adjust the announcement range. Enum:'highest, lowest, medium'",
    )
    source: Optional[str] = Field(
        None,
        description='A sequence of characters giving the original source of the entity data as a URL. Recommended to be the fully qualified domain name of the source provider, or the URL to the source object',
    )
    type: Optional[Type] = Field(
        None, description='NGSI Entity type. It has to be SmartSpot'
    )
