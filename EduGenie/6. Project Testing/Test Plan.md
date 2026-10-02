# Test Plan

## Objective
To validate that EduGenie provides correct educational output, handles invalid input properly, and remains functional across the main user flows.

## Scope
- Q&A feature
- Explanation feature
- Quiz generation
- Summary generation
- Learning path generation
- Frontend integration
- API validation
- Error handling

## Testing Approach
- Manual API testing using FastAPI docs
- Direct HTTP requests to endpoints
- Frontend validation through browser interaction
- Error case checks for empty or invalid input

## Risks to Check
- Invalid or empty user input
- Gemini API errors
- Model unavailability
- Missing API key
- Frontend request failures

## Status
Testing is partially completed in the current environment. Gemini API testing requires a valid `GEMINI_API_KEY`.
