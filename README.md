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
├── index.html       # Main application
├── events.json      # Event data
└── README.md        # This file
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
- `status` - "upcoming" or "past"
- `tags` - Array of categories

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
