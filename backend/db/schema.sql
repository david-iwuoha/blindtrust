-- users table
CREATE TABLE users (
    id TEXT PRIMARY KEY,
    name TEXT,
    nickname TEXT,
    phone TEXT,
    language TEXT,
    profile_pic TEXT,
    demo_seeded INTEGER DEFAULT 1,
    created_at TEXT
);

-- accounts table
CREATE TABLE accounts (
    id TEXT PRIMARY KEY,
    user_id TEXT REFERENCES users(id),
    balance INTEGER,
    created_at TEXT
);

-- beneficiaries table
CREATE TABLE beneficiaries (
    id TEXT PRIMARY KEY,
    user_id TEXT,
    name TEXT,
    alias TEXT,
    account_number TEXT,
    bank_name TEXT,
    voice_tags TEXT,
    last_used TEXT
);

-- transactions table
CREATE TABLE transactions (
    id TEXT PRIMARY KEY,
    from_account TEXT,
    to_account TEXT,
    amount INTEGER,
    status TEXT,
    created_at TEXT
);
