[![hacs_badge](https://img.shields.io/badge/HACS-Default-orange.svg)](https://github.com/hacs/integration)

# Home Assistant Component: Devices API
This component allows you to query devices / areas specific information from your Home Assistant instance.  
The main goal of this component is to provide information on devices / areas that are not available in the Home Assistant API.

**This includes:**
1. List of all devices
    a. General device information
    b. Device attributes and capabilities
2. List of all areas
    a. General area information
    b. List of all devices in the area

# List of Contents
1. [Installation](#installation)  
2. [Configuration](#configuration)  
3. [Exposed Routes](#exposed-routes)  
4. [Responses Examples](#responses-examples)  
    a. [`/api/devices_api/devices`](#api/devices_api/devices)  
    b. [`/api/devices_api/areas`](#api/devices_api/areas)  
    c. [`/api/devices_api/devices/{device_id}`](#api/devices_api/devices/{device_id})  
    d. [`/api/devices_api/areas/{area_id}`](#api/devices_api/areas/{area_id})  
    e. [`/api/devices_api/areas/{area_id}/devices`](#api/devices_api/areas/{area_id}/devices)
5. [Interacting with ChatGPT](#interacting-with-chatgpt)  
    a. [ChatGPT request block](#chatgpt-request-block)  
    b. [ChatGPT response block](#chatgpt-response-block)

# Installation
You can install this component from the HACS store.
First of all you need to add a custom repository to HACS.
1. Go to HACS
2. Click on Integrations
3. Click on the 3 dots in the top right corner
4. Click on Custom repositories
5. Add the following details:
    - URL: `https://github.com/darki73/ha-devices-api`
    - Category: Integration
6. Click on Add

Now you can install the component:
1. Go to HACS
2. Click on Integrations
3. Click on Explore & Add Repositories
4. Search for `Devices API`
5. Click on the `Devices API` card
6. Click on Install

# Configuration
As of now, this component does not require any configuration.
However, to ensure that the component is working properly, you can add the following to your `configuration.yaml` file:
```yaml
devices_api:
  enabled: true
  chat_gpt:
    model: "davinci"
    key: ""
  ignored_domains:
    - automation
    - updater
    - person
    - sun
    - weather
    - input_boolean
    - input_number
    - input_select
    - input_text
    - input_datetime
    - input_number
    - zone
```

# Exposed Routes
This component exposes the following routes:
1. `/api/devices_api/devices` - Returns a list of all devices
2. `/api/devices_api/areas` - Returns a list of all areas
3. `/api/devices_api/devices/{device_id}` - Returns information on a specific device
4. `/api/devices_api/areas/{area_id}` - Returns information on a specific area
5. `/api/devices_api/areas/{area_id}/devices` - Returns a list of all devices in a specific area

# Responses Examples
## `/api/devices_api/devices`
```json
{
    "data": [
        {
			"id": "1e0fbbc264b1796f84439dbf5fa81bf8",
			"name": "Corridor Light",
			"manufacturer": "Lutron Electronics Co., Inc",
			"model": "Lutron Lighting Control",
			"area": "corridor",
			"hw_version": "",
			"sw_version": "05.02",
			"disabled": false,
			"type": null
		},
		{
			"id": "98d802c92d306b303058154ad4a848fe",
			"name": "Living Room Light",
			"manufacturer": "Lutron Electronics Co., Inc",
			"model": "Lutron Lighting Control",
			"area": "living_room",
			"hw_version": "",
			"sw_version": "05.02",
			"disabled": false,
			"type": null
		},
		{
			"id": "fae6fc1666f79e79ed5512ace4cd6dfa",
			"name": "Dining Light",
			"manufacturer": "Lutron Electronics Co., Inc",
			"model": "Lutron Lighting Control",
			"area": "dining_room",
			"hw_version": "",
			"sw_version": "05.02",
			"disabled": false,
			"type": null
		}
    ],
    "request_time": 1687083928.1971066
}
```

## `/api/devices_api/areas`
```json
{
    "data": [
        {
			"id": "living_room",
			"name": "Living Room"
		},
		{
			"id": "kitchen",
			"name": "Kitchen"
		},
		{
			"id": "bedroom",
			"name": "Bedroom"
		},
        {
			"id": "maids_room",
			"name": "Maids Room"
		},
		{
			"id": "corridor",
			"name": "Corridor"
		},
		{
			"id": "dining_room",
			"name": "Dining Room"
		},
		{
			"id": "office",
			"name": "Office"
		}
    ],
    "request_time": 1687083928.1971066
}
```

## `/api/devices_api/devices/{device_id}`
```json
{
    "data": {
		"id": "fb4e7d6d04ce84043cbf64f2d19b6084",
		"name": "Office Shades",
		"manufacturer": "TuYa",
		"model": "lilistore Tuya ZigBee Motorized Curtain Roller (TS0601_lilistore)",
		"area": "office",
		"hw_version": null,
		"sw_version": null,
		"disabled": false,
		"type": null,
		"entities": [
			{
				"id": "cover.office_shades",
				"unique_id": "office_shades_uid_cover_zigbee2mqtt",
				"name": "Office Shades",
				"category": null,
				"icon": null,
				"device_id": "fb4e7d6d04ce84043cbf64f2d19b6084",
				"device_class": null,
				"platform": "mqtt",
				"unit_of_measurement": null,
				"capabilities": []
			},
			{
				"id": "sensor.office_shades_linkquality",
				"unique_id": "office_shades_uid_linkquality_zigbee2mqtt",
				"name": "Office Shades linkquality",
				"category": "diagnostic",
				"icon": "mdi:signal",
				"device_id": "fb4e7d6d04ce84043cbf64f2d19b6084",
				"device_class": null,
				"platform": "mqtt",
				"unit_of_measurement": "lqi",
				"capabilities": {
					"state_class": "measurement"
				}
			},
			{
				"id": "sensor.office_shades_control_back_mode",
				"unique_id": "office_shades_uid_control_back_mode_zigbee2mqtt",
				"name": "Office Shades control back mode",
				"category": null,
				"icon": null,
				"device_id": "fb4e7d6d04ce84043cbf64f2d19b6084",
				"device_class": null,
				"platform": "mqtt",
				"unit_of_measurement": null,
				"capabilities": []
			},
			{
				"id": "sensor.office_shades_favorite_position",
				"unique_id": "office_shades_uid_favorite_position_zigbee2mqtt",
				"name": "Office Shades favorite position",
				"category": null,
				"icon": null,
				"device_id": "fb4e7d6d04ce84043cbf64f2d19b6084",
				"device_class": null,
				"platform": "mqtt",
				"unit_of_measurement": null,
				"capabilities": []
			},
			{
				"id": "sensor.office_shades_control",
				"unique_id": "office_shades_uid_control_zigbee2mqtt",
				"name": "Office Shades control",
				"category": null,
				"icon": null,
				"device_id": "fb4e7d6d04ce84043cbf64f2d19b6084",
				"device_class": null,
				"platform": "mqtt",
				"unit_of_measurement": null,
				"capabilities": []
			},
			{
				"id": "sensor.office_shades_motor_direction",
				"unique_id": "office_shades_uid_motor_direction_zigbee2mqtt",
				"name": "Office Shades motor direction",
				"category": null,
				"icon": null,
				"device_id": "fb4e7d6d04ce84043cbf64f2d19b6084",
				"device_class": null,
				"platform": "mqtt",
				"unit_of_measurement": null,
				"capabilities": []
			},
			{
				"id": "sensor.office_shades_options",
				"unique_id": "office_shades_uid_options_zigbee2mqtt",
				"name": "Office Shades options",
				"category": null,
				"icon": null,
				"device_id": "fb4e7d6d04ce84043cbf64f2d19b6084",
				"device_class": null,
				"platform": "mqtt",
				"unit_of_measurement": null,
				"capabilities": []
			}
		]
	},
    "request_time": 1687083928.1971066
}
```

## `/api/devices_api/areas/{area_id}`
```json
{
	"data": {
		"id": "office",
		"name": "Office",
		"normalized_name": "office",
		"picture": null
	},
	"request_time": 1687084165.4530387
}
```

## `/api/devices_api/areas/{area_id}/devices`
```json
{
	"data": [
		{
			"id": "a2f07e8d3812c6459dbfc5a1e60b4301",
			"name": "Office Motion Sensor",
			"manufacturer": "TuYa",
			"model": "Motion sensor (IH012-RT01)",
			"area": "office",
			"hw_version": null,
			"sw_version": null,
			"disabled": false,
			"type": null
		},
		{
			"id": "fb4e7d6d04ce84043cbf64f2d19b6084",
			"name": "Office Shades",
			"manufacturer": "TuYa",
			"model": "lilistore Tuya ZigBee Motorized Curtain Roller (TS0601_lilistore)",
			"area": "office",
			"hw_version": null,
			"sw_version": null,
			"disabled": false,
			"type": null
		}
	],
	"request_time": 1687084180.1530943
}
```

# Interacting with ChatGPT

Although it is a planned feature (to automatically generate automations), as of now it is not implemented in the main codebase.
However, you can send a message to ChatGPT in the following format:

### ChatGPT request block
Hello, i have an API for my devices available in Home Assistant.
It returns the information about the device and its attributes and capabilities.

Here is the response i have received:
```json
{
    "data": {
		"id": "fb4e7d6d04ce84043cbf64f2d19b6084",
		"name": "Office Shades",
		"manufacturer": "TuYa",
		"model": "lilistore Tuya ZigBee Motorized Curtain Roller (TS0601_lilistore)",
		"area": "office",
		"hw_version": null,
		"sw_version": null,
		"disabled": false,
		"type": null,
		"entities": [
			{
				"id": "cover.office_shades",
				"unique_id": "office_shades_uid_cover_zigbee2mqtt",
				"name": "Office Shades",
				"category": null,
				"icon": null,
				"device_id": "fb4e7d6d04ce84043cbf64f2d19b6084",
				"device_class": null,
				"platform": "mqtt",
				"unit_of_measurement": null,
				"capabilities": []
			},
			{
				"id": "sensor.office_shades_linkquality",
				"unique_id": "office_shades_uid_linkquality_zigbee2mqtt",
				"name": "Office Shades linkquality",
				"category": "diagnostic",
				"icon": "mdi:signal",
				"device_id": "fb4e7d6d04ce84043cbf64f2d19b6084",
				"device_class": null,
				"platform": "mqtt",
				"unit_of_measurement": "lqi",
				"capabilities": {
					"state_class": "measurement"
				}
			},
			{
				"id": "sensor.office_shades_control_back_mode",
				"unique_id": "office_shades_uid_control_back_mode_zigbee2mqtt",
				"name": "Office Shades control back mode",
				"category": null,
				"icon": null,
				"device_id": "fb4e7d6d04ce84043cbf64f2d19b6084",
				"device_class": null,
				"platform": "mqtt",
				"unit_of_measurement": null,
				"capabilities": []
			},
			{
				"id": "sensor.office_shades_favorite_position",
				"unique_id": "office_shades_uid_favorite_position_zigbee2mqtt",
				"name": "Office Shades favorite position",
				"category": null,
				"icon": null,
				"device_id": "fb4e7d6d04ce84043cbf64f2d19b6084",
				"device_class": null,
				"platform": "mqtt",
				"unit_of_measurement": null,
				"capabilities": []
			},
			{
				"id": "sensor.office_shades_control",
				"unique_id": "office_shades_uid_control_zigbee2mqtt",
				"name": "Office Shades control",
				"category": null,
				"icon": null,
				"device_id": "fb4e7d6d04ce84043cbf64f2d19b6084",
				"device_class": null,
				"platform": "mqtt",
				"unit_of_measurement": null,
				"capabilities": []
			},
			{
				"id": "sensor.office_shades_motor_direction",
				"unique_id": "office_shades_uid_motor_direction_zigbee2mqtt",
				"name": "Office Shades motor direction",
				"category": null,
				"icon": null,
				"device_id": "fb4e7d6d04ce84043cbf64f2d19b6084",
				"device_class": null,
				"platform": "mqtt",
				"unit_of_measurement": null,
				"capabilities": []
			},
			{
				"id": "sensor.office_shades_options",
				"unique_id": "office_shades_uid_options_zigbee2mqtt",
				"name": "Office Shades options",
				"category": null,
				"icon": null,
				"device_id": "fb4e7d6d04ce84043cbf64f2d19b6084",
				"device_class": null,
				"platform": "mqtt",
				"unit_of_measurement": null,
				"capabilities": []
			}
		]
	},
    "request_time": 1687083928.1971066
}
```

Can you please create an automation which will:
1. Turn the item on when the sun has risen
2. Turn the item off when the sun has set (15 minutes after sunset)

### ChatGPT response block
Certainly! Here's an example of an automation in YAML format that can be added to your Home Assistant configuration file:

```yaml
automation:
  - alias: "Turn on device at sunrise"
    trigger:
      platform: sun
      event: sunrise
    action:
      service: cover.open_cover
      entity_id: cover.office_shades

  - alias: "Turn off device 15 minutes after sunset"
    trigger:
      platform: sun
      event: sunset
      offset: "00:15:00"
    action:
      service: cover.close_cover
      entity_id: cover.office_shades
```

Make sure to replace cover.office_shades with the correct entity ID of your device.

To add this automation to Home Assistant, you can either edit the automations.yaml file directly or use the automation editor in the Home Assistant UI.

Once added, Home Assistant will automatically trigger the actions based on the sunrise and sunset times. The first automation will open the cover at sunrise, and the second automation will close the cover 15 minutes after sunset.

Remember to check the documentation of your specific cover device and integration to ensure that the service calls (cover.open_cover and cover.close_cover) are appropriate for controlling your device.