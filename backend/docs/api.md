# BlindTrust API Contract

## POST /signup
### Request:
```json
{
  "name": "Emeka",
  "phone": "070...",
  "language": "pidgin"
}
Response:
json
Copy code
{
  "user_id": "...",
  "token": "...",
  "seeded_balance": 10000
}
POST /login
Request:
json
Copy code
{
  "phone": "070...",
  "password": "password123"
}
Response:
json
Copy code
{
  "token": "generated_token"
}
GET /accounts/{user_id}/balance
Response:
json
Copy code
{
  "balance": 10000
}
sql
Copy code
