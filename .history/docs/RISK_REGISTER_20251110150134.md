# Risk Register

| Risk (what could go wrong) | Area | Likelihood | Impact | Control (what you’ll do)                  | Status      | Review |
|---|---|---|---|---|---|---|
| Secret committed by mistake | Repo/CI | Medium | High | Turn on GitHub Secret Scanning; ignore `.env` | Mitigated   | 20 Dec |
| Missing rate limits         | Auth (future) | Medium | Medium | Add rate limiter to `/login`                 | Planned     | 20 Dec |
| IDOR (see others’ data)     | Profile API (future) | Medium | High | Check resource owner + authZ tests           | In progress | 20 Dec |
| Verbose error messages      | All APIs | Low | Medium | Central error handler; hide stack traces     | Planned     | 20 Dec |