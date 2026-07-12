1. Threat Model & Security Philosophy
Who are you protecting data from?

Default: Only logged-in users of the household.

Future: Support for multi-household and privacy from other users.

Treat all stored data as PII; everything encrypted-at-rest and in-transit.

“Assume public” when designing all endpoints, even if only private for MVP.


2. Authentication Mechanism (MVP)

On First Use: Create/join household → generate userkey (stored hashed/salted in DB, not raw)

Households must enter household name + password to log in (Google OAuth-style login)

After login, select user (avatar or username); Admins require PIN or password for access.

Token-based session (JWT or secure session cookie, short lifetime, renew as needed)

JWT signed using strong secret, stored httpOnly in browser for frontend.

“Remember me” option stores time-limited refresh/long-lived session securely.


3. Access Control
Only authenticated users can access any meaningful endpoint or page.


Household members can:

View all data for their household.

Edit inventory, add items, complete shopping list actions.


Only Admins can:

Change settings, edit household info, add/remove members, export or delete data.

All mutating (POST/PATCH/DELETE) endpoints:

Must validate both JWT/session AND role (user/admin) before changing data.

Attempts to access or modify data from other households/users are rejected with 401/403.


4. Sensitive/API Endpoint Protection
All API endpoints check for valid auth token before processing request.

APIs scoped by household (include household_id as claim in JWT).

APIs never expose raw userkeys, emails, or PII in responses.

Admin-only endpoints (settings, member management, dangerous actions) require admin validation/PIN.


5. Data Storage & Encryption
All stored data is encrypted at rest (preferably using DB-level and/or app-level encryption).

Passwords/PINs stored as salted/hashed (never raw).

Userkey used strictly as a secure, non-guessable auth token, not as display data.

All browser storage for tokens/session uses secure and httpOnly flags.


6. UI/UX Security
Lock down admin settings section in UI to admin role only (uses JWT and local checks).

“Danger zone” (delete/export) always prompts with double confirmation.

No sensitive info is ever displayed in non-secure/error pages or logs.

Expose “Logout everywhere” or session-kill option for security.


7. Future Considerations
Plan to integrate Google/Facebook OAuth for optional household login/restore.

Add support for user invites, password reset, or email verification for higher security.

Add audit logs for all admin/critical actions (future feature).