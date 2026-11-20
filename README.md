# todo-list

## SkyWatch Live — `plane-tracker.html`

A single-file live flight tracker. Open `plane-tracker.html` in a browser (no build step or API key needed).

- **Live map** of aircraft around you (asks for your location; or search a city/airport, or just pan the map).
  Planes are coloured by altitude, rotated to their track, and move smoothly between updates.
- **Track flights by code** — type any of these into *Track flights* (comma-separate several):
  | Kind | Example |
  |---|---|
  | Airline flight number (IATA) | `UA123`, `BA286`, `QF1` → converted to ICAO callsign |
  | ICAO callsign | `UAL123`, `BAW286`, `EZY45AB` |
  | Registration | `G-EUPT`, `N628TS`, or `reg:JA801A` |
  | ICAO 24-bit hex | `hex:a1b2c3` |
  | Squawk | `7700` |
  | Aircraft type (in view) | `type:A388` |
  | Airline / reg prefix (in view) | `RYR*` |
  Tracked flights are searched worldwide, highlighted in gold, get trails, and raise a notification when they come online.
  Your list is saved, and the URL updates so you can share a link like `plane-tracker.html#track=UAL123,BAW286`.
- **Details panel**: altitude, speed, vertical rate, squawk, registration, type, scheduled route and photo (when known), follow-on-map mode.
- **Data**: community ADS-B feeds — adsb.lol, airplanes.live, OpenSky (automatic fallback). Routes/photos via adsbdb. Map tiles © OpenStreetMap / CARTO / Esri.

Note: some airlines fly callsigns that differ from the published flight number (e.g. `BAW12AB`); if a flight number isn't found, try its callsign or registration. Not for navigation.
