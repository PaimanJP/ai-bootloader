# Service adapters
Discover actual tool capabilities and current official docs before changing provider settings. Use connected tools for real resources. Never invent API parameters or commands. Diagnose errors; after repeated failures change approach or report blocker.

## GitHub
Resolve exact owner/repo, authorized account, branch HEAD and visibility. Check protection and deploy implications. Preserve baseline and unrelated work. Prefer atomic tree/commit/non-force ref update or PR; otherwise sequential file writes with current blob SHA and recovery checkpoints. Re-read before ref update, reject competing edits. Inspect diff for secrets and scope. Verify commit/ref and exact readback. Do not assume admin metadata proves integration can write. Never push upstream fork without authorization. CI status != production functionality. Link actual release assets.

## Vercel
Inspect team/project, Git link, branch, existing deployments and domains. Separate preview and production; verify deployed revision, deployment state and authorized smoke test. Do not promote/change aliases outside authorization. Respect protection, never bypass auth. Inspect build logs; env names/scopes only, not values. Starter https://vercel.com/templates/next.js/supabase; verify account selection. Reuse infrastructure where appropriate.

## Supabase
Resolve exact organization/ref/environment. Check current docs, migrations/schema drift and data preservation. Use isolated local/staging tests; version schema changes; confirm authorized production operations. Review RLS on exposed schemas, explicit grants, safe function/storage permissions and role-based access. Never trust user-editable metadata as authorization; never expose service-role/secret keys in client. Test positive, negative and cross-account access. Never disable RLS as a shortcut. Distinguish local auth/email from hosted SMTP/real inbox. Verify migration history, schema, test queries and advisors where possible. Use approved isolated fixtures and exact cleanup manifest for hosted tests, not arbitrary customer deletion. No DB access -> migration file and exact next step, mark unverified.

## Other stacks
Respect existing toolchain and docs. Android: application ID, signing/update compatibility, data isolation, device permissions, device versus emulator testing, release versus debug; verify artifact URLs. Games/editor: preserve upstream and licenses, source/import/export compatibility and data format version. No forced cloud stack.