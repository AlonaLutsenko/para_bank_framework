# ParaBank Test Framework

## Credentials Setup (Security)

**Never store credentials in code or commit them to git.**

### Local development

1. Copy `.env.example` to `.env`:
   ```bash
   cp .env.example .env
   ```
2. Edit `.env` and set your credentials (`.env` is in `.gitignore` and will not be committed).

### CI (GitHub Actions)

- **Option A**: Add [GitHub Secrets](https://docs.github.com/en/actions/security-guides/encrypted-secrets) `PARABANK_USERNAME_DEFAULT` and `PARABANK_PASSWORD_DEFAULT` (Settings → Secrets and variables → Actions).
- **Option B**: If not set, CI falls back to ParaBank demo credentials (`john`/`demo`) for the public test site.
