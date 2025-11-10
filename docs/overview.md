# Project Overview

This repository contains the codebase for the Mood-Based Recipe Recommendation system, developed according to the Jira issues SCRUM-265 through SCRUM-280.

## Features Implemented (MVP and Post-MVP)

- **SCRUM-265:** Mood input selection on frontend, recipe recommendation backend API (`POST /api/recommendations`)
- **SCRUM-266:** Backend API using FastAPI; integration placeholder for MCP server orchestration
- **SCRUM-267:** Responsive frontend UI for mood selection and recipe display
- **SCRUM-268:** Database schema and ORM models for moods and recipes
- **SCRUM-269:** API specifications implemented: GET /api/moods, POST /api/recommendations, GET /api/recipes/{id}
- **SCRUM-270:** Basic unit tests, logging setup, and health check endpoints
- **SCRUM-271 - SCRUM-273:** User accounts, authentication (OAuth2 + JWT), favorites management, mood history tracking
- **SCRUM-274:** Security enhancements including secure password storage and GDPR compliance
- **SCRUM-275:** Scalability enhancements: connection pooling, caching strategies
- **SCRUM-276:** Expanded tests, logging, and monitoring for authentication and user APIs

## Future Enhancements (SCRUM-277 to SCRUM-280)

- AI-based mood detection integration
- Community recipe submission and moderation workflows
- Social sharing capabilities
- AI service scaling and CDN integration

---

For detailed implementation, refer to the source code in frontend/ and backend/ directories.

