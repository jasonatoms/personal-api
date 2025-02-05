# Personal API

![GitHub top language](https://img.shields.io/github/languages/top/yourusername/personal-api)
![GitHub last commit](https://img.shields.io/github/last-commit/yourusername/personal-api)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)

## Overview
An AI-powered personal API for structured knowledge management and deep context tracking. Inspired by Daemon and Telos from Daniel Miessler, this API allows you to store and query knowledge dynamically while maintaining a structured, evolving self-narrative.

## Features
- **Knowledge Base**: Store and retrieve structured insights, tech stack, and learning progress.
- **Tech Stack**: Track your development tools, programming languages, and frameworks.
- **Projects**: Maintain a dynamic record of personal and professional projects.
- **Deep Context (`/telos`)**: Self-curated mission, goals, philosophy, and personal insights.
- **FastAPI Backend**: Lightweight and scalable, powered by SQLite and ChromaDB.

## API Endpoints
### General
- `GET /` - Welcome message

### Knowledge Management
- `GET /knowledge_base` - Retrieve stored knowledge
- `POST /knowledge_base` - Add new knowledge entry

### Tech Stack
- `GET /tech_stack` - View currently used programming languages and tools

### Project Tracking
- `GET /projects` - Retrieve list of ongoing and completed projects

### Deep Context (`/telos`)
- `GET /telos` - Retrieve structured self-reflection data
- `POST /telos` - Add a new entry to the deep context system

## Installation & Setup
1. Clone the repository:
   ```sh
   git clone https://github.com/yourusername/personal-api.git
   cd personal-api
   ```
2. Create a virtual environment and install dependencies:
   ```sh
   python -m venv venv
   source venv/bin/activate  # (or venv\Scripts\activate on Windows)
   pip install -r requirements.txt
   ```
3. Run the FastAPI server:
   ```sh
   uvicorn main:app --reload
   ```
4. Open your browser and navigate to:
   - API Docs: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
   - Raw JSON API: [http://127.0.0.1:8000](http://127.0.0.1:8000)

## Future Enhancements
- Add authentication and API token-based security.
- Automate updates with AI-assisted knowledge ingestion.
- Expand to integrate with external data sources (e.g., GitHub activity, Notion, Obsidian).

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

