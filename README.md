# Token Counter

Single-purpose API. Stateless. Deterministic. Returns JSON only.

## Endpoints
- GET `/health`
- GET `/v1/token-count?text=`

## Example

Request:
`/v1/token-count?text=Hello,%20world!%20How%20are%20you%3F`

Response:
```json
{
  "input": "Hello, world! How are you?",
  "token_count": 5
}
