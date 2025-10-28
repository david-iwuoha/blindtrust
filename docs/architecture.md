# BlindTrust Architecture

## Mobile App (Flutter)
- **Local SQLite**: Caching and offline functionality for the mobile app.
- **Voice Module**: Converts speech to text (STT) and processes it into intents.
- **TTS (Text-to-Speech)**: Converts text responses into speech.
- **AI Adapter**: Connects to the Yarn GPT conversational model.
- **UI Components**: Accessible interface for sighted testers, with full voice interaction for blind users.

## Backend (FastAPI)
- **Authentication**: Handles user registration, login, and profile management.
- **Transactions & Beneficiaries**: Manages user transactions and beneficiaries.
- **Profiles**: Stores user information and settings.
- **Metrics Endpoint**: Logs latency for performance monitoring.
- **Demo Seed Logic**: At account creation, balances are seeded with 10,000 demo Naira.

## Database (SQLite)
- **Server-Side**: Stores user accounts, transactions, and profiles with migration scripts for future upgrades.

## Hosting
- **Development**: GitHub Codespaces for development environment.
- **Demo Hosting**: Replit/Render for deploying the app for public access.
