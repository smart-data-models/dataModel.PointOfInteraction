/* (Beta) Export of data model SmartSpot of the subject dataModel.PointOfInteraction for a PostgreSQL database. Pending translation of enumerations and multityped attributes */
CREATE TYPE SmartSpot_bluetoothChannel_type AS ENUM ('37', '38', '39', '37,38', '38,39', '37,39', '37,38,39');
CREATE TYPE SmartSpot_signalStrength_type AS ENUM ('highest', 'lowest', 'medium');
CREATE TYPE SmartSpot_type AS ENUM ('SmartSpot');
CREATE TABLE SmartSpot (
  "alternateName" TEXT,
  "announcedUrl" TEXT,
  "announcementPeriod" NUMERIC,
  "availability" TEXT,
  "bluetoothChannel" SmartSpot_bluetoothChannel_type,
  "coverageRadius" NUMERIC,
  "dataProvider" TEXT,
  "dateCreated" TIMESTAMP,
  "dateModified" TIMESTAMP,
  "description" TEXT,
  "id" TEXT PRIMARY KEY,
  "name" TEXT,
  "owner" JSON,
  "refSmartPointOfInteraction" JSON,
  "seeAlso" JSON,
  "signalStrength" SmartSpot_signalStrength_type,
  "source" TEXT,
  "type" SmartSpot_type
);