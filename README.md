# Build Days Hackathons

A simple, neon-themed event tracker for upcoming and past hackathon events in Australia.

## Features

- View upcoming and past hackathon events
- Add new events with title, date, location, description, and tags
- Edit existing events
- Delete events
- Export event data as JSON
- Events persist in browser localStorage
- Responsive design

## Tech Stack

- HTML5
- CSS3 (neon theme inspired by morgan.codes)
- Vanilla JavaScript
- JSON data storage

## Quick Start

1. Visit the live site: https://dcodeaus.github.io/hackathon-tracker/
2. Browse upcoming events
3. Click "+ Add Event" to create new events
4. Use the edit (✏️) and delete (×) buttons on event cards to modify

## File Structure

```
hackathon-tracker/
├── index.html              # Main application
├── events.json             # Event data
├── hackathon-events.html   # Old address - redirects to index.html
├── SOURCES.md              # Sites to check for new events
├── check_events.py         # Checks events.json (see "Checking the data" below)
├── favicon.svg / .png      # Site icon (plus apple-touch-icon.png for phones)
├── .github/workflows/      # Publishes the site, and checks the data weekly
└── README.md               # This file
```

## How Events Work

Events are loaded from `events.json` on page load. Any changes made via the UI are saved to your browser's localStorage and override the original data.

To permanently update events, export the data from the "View Data" button and update `events.json`.

## Events Data

Each event includes:
- `id` - Unique identifier
- `title` - Event name
- `date` - When it happens
- `location` - Where it happens
- `description` - What it's about
- `link` - URL to event page
- `sortDate` - the date as YYYY-MM-DD, used for ordering
- `endDate` - (optional) last day of a multi-day event
- `status` - "upcoming" or "past". The page works this out from `endDate`/`sortDate` each time it loads, so events move to "Past" on their own; the stored value is only a fallback
- `byod` - "required", "optional" or "no" (bring your own laptop)
- `tags` - Array of categories

## Checking the data

`check_events.py` checks `events.json` every time it's pushed, and every Monday morning. It fails on anything that would break the page (invalid JSON, a missing title or date, a repeated id) and warns about an upcoming event with its date still TBA or no link. It also warns when there are fewer than five upcoming events - and on the Monday run that fails the check, so GitHub emails you that it's time to look through `SOURCES.md` for more. Run it yourself with `python3 check_events.py`.

## Customisation

Edit `events.json` to add, remove, or modify events. Changes require a git commit and push to GitHub Pages.

## Colours

Built with the morgan.codes neon theme:
- Background: `#0f0f1e`
- Hot Pink: `#ff006e`
- Cyan: `#00d9ff`
- Neon Green: `#39ff14`
- Orange: `#ffa500`

## Author

[DCodeAus](https://github.com/DCodeAus)
