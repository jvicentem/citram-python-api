# citram-python-api
Python wrapper of Consorcio de Transportes de Madrid (CTRM) API.

This module seeks to comprise all the CTRM endpoints, using different CTRM APIs.

With this API you can request static and live (not as a streaming) for the different public transport the CTRM manages:
Madrid Metro, MetroSur Metro, Cercanías Renfe, Madrid EMT buses, intercity buses, multi-transport stations (intercambiadores),
and Metro Ligero. You can request information of CTRM offices and parkings.

Any kind of transport fits in the paradigm of stops and lines.

## Modules description:
- lines: Requests relative to transport lines.
- offices: Requests relative to CTRM offices.
- stops: Requests relative to transport stops.
- others: Other relevant requests that don't fit in any of the other categories.
- constants: Useful constants to use when making requests.
- utils: Useful functions to use when making requests.

Some tips:

- When writing line names, they're usually in upper case and have no whitespaces nor other characters like dashes or
underscores. The functions in utils.utils can help you to create stop and line codes. 

- With the constants module you can make requests about municipalities, transport modes and office types easily.

- In case your mother tongue is English and you're having trouble understanding the different transports, 
you might find this link helpful: [https://www.crtm.es/widgets/language.json](https://www.crtm.es/widgets/language.json)

- Sometimes you'll see kmz links. kmz files are used by Google Maps or Google Earth to display a set of points
or geometric figures in a map. 

- When the field access is greater than 0, it means the stop is adapted to people with special conditions.

- When the field park is greater than 0, it means that stop has a parking.

- When the field nightService or nightLinesService is greater than 0, it means that line has night service (sometimes
this is called Búho, specially on bus lines).

