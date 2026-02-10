// Testing secrets that don't trigger push protection but should generate alerts

// FAKE Generic API Key pattern
const API_KEY_1 = "ak_live_1234567890abcdefghijklmnopqrstuvwxyzABCDEF";

// FAKE Database Connection String
const DB_CONN = "postgresql://fakeuser:fakeP@ssw0rd123!@fake-db.example.com:5432/fakedb";

// FAKE JWT Token
const JWT_TOKEN = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkZha2UgVXNlciIsImlhdCI6MTUxNjIzOTAyMn0.SflKxwRJSMeKKF2QT4fwpMeJf36POk6yJV_adQssw5c";

// FAKE Private Key (truncated for brevity)
const PRIVATE_KEY = "-----BEGIN RSA PRIVATE KEY-----\nMIIEpAIBAAKCAQEAkL9mN3pQ6rT2vX5yZ8aC1bD4fG7hI2jK5lM8nO1pR\n-----END RSA PRIVATE KEY-----";

module.exports = { API_KEY_1, DB_CONN, JWT_TOKEN, PRIVATE_KEY };
