# ParaBank Test Framework

## Credentials Setup (Security)

**Never store credentials in code or commit them to git.**

### Local development

1. Create `.env` in the project root with:
   ```
   PARABANK_USERNAME_DEFAULT=your_username
   PARABANK_PASSWORD_DEFAULT=your_password
   ```
2. `.env` is in `.gitignore` and will not be committed.

### CI (GitHub Actions)

Add [GitHub Secrets](https://docs.github.com/en/actions/security-guides/encrypted-secrets) `PARABANK_USERNAME_DEFAULT` and `PARABANK_PASSWORD_DEFAULT` (Settings → Secrets and variables → Actions).
