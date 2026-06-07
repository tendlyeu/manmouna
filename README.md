# Manmouna Technologies Landing Page

A multi-page, server-rendered landing site built with FastHTML.

## Overview

Corporate landing page for Manmouna Technologies — dark forest-green palette, Tailwind CSS via CDN, Plotly data visualisations (Signal page), a Three.js globe hero, and a background RSS news feed with LLM-based relevance filtering.

## Features

- **Responsive Design**: Optimized for desktop, tablet, and mobile devices
- **FastHTML + HTMX**: Lightweight Python-based web framework, server-side rendered
- **Three.js Globe**: Animated hero with European city dots
- **Plotly Signal Dashboard**: NHS, defence, education, energy data visualisations
- **RSS News Feed**: Background daemon with keyword + LLM filtering
- **Pages**: Home, Platform, Solutions (4 sectors), Case Studies, Signal, Team, Contact

## Technology Stack

- **Framework**: FastHTML
- **Styling**: Tailwind CSS (CDN)
- **Charts**: Plotly
- **3D**: Three.js
- **Python**: 3.11+
- **Server**: Uvicorn

## Installation

1. Clone the repository:
```bash
git clone https://github.com/tendlyeu/manmouna.git
cd manmouna
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

## Running Locally

Start the development server:
```bash
python main.py
```

The application will be available at `http://localhost:5001`

## Deployment

Docker-based deployment on Coolify:

```bash
docker build -t manmouna . && docker run -p 5001:5001 manmouna
```

## Project Structure

```
manmouna/
├── main.py              # Entrypoint (thin shim for Docker CMD)
├── app.py               # All routes + fast_app()
├── components.py         # Shared layout, design tokens, reusable components
├── content/             # Data layer
│   ├── case_studies.py  # Case study data
│   ├── team.py          # Team members
│   ├── signal.py        # Signal chart data
│   ├── news.py          # RSS feed + LLM classifier
│   └── repos.py         # External research links
├── static/              # Frontend assets
│   ├── site.css         # Custom styles
│   ├── signal.js        # Plotly rendering
│   ├── three-hero.js    # Three.js globe
│   └── video/           # Hero background video
├── tests/               # Playwright tests
├── requirements.txt     # Python dependencies
├── Dockerfile           # Docker build config
└── README.md
```

## Environment Variables

- `OPENROUTER_API_KEY` — enables LLM-based news filtering (optional)
- `NEWS_FILTER_MODEL` — override the OpenRouter model (default: `anthropic/claude-haiku-4-5`)
- `PORT` — server port (default: 5001)

## Contact

For inquiries: info@manmouna.tech

## License

Copyright © 2026 Manmouna OÜ. All rights reserved.
