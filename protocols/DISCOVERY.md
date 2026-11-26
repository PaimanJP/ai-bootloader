# Ecosystem discovery

## Scope and procedure
Targeted task: exact URL/owner -> registry candidates -> linked account search/list -> documentation/source. Full ecosystem audit: enumerate every accessible linked identity per provider, list orgs/teams and resources, paginate to exhaustion. Deduplicate stable provider IDs; retain ownership and membership separately. Record date, pages, scope, errors, reached/denied/missing, gaps. Never claim complete if access partial.

GitHub fields: canonical ID/full_name, owner, visibility, default/working branch, fork/upstream, archived status, purpose and evidence. Read README, AGENTS, overview; if absent inspect manifest/entrypoint/code; classify purpose documented/inferred/unknown with path/revision. Name alone not purpose.
Vercel: account/team, project ID, Git integration owner/repo, production branch, domain, release state/commit, limits/usage when accessible. Paginate all scopes; no env secret values.
Supabase: account/org, project ref, region, status, plan, usage/limits where available; for target verify migration/schema/auth/storage metadata as appropriate. No unnecessary row reads.
Connections: exact Git link or project ref in verified config/live integration metadata. Same name/email only candidate. Mark relationship confirmed, reported, inferred, unknown or conflicting. Preserve conflicting evidence and observed dates.

## Recommendation algorithm
1. Existing project: preserve current owner/integrations absent approved migration.
2. New project: check duplicates/aliases, filter authorized ownership, related projects, compatibility, region/compliance, ability to create. Match intended stack, avoid unnecessary services.
3. Verify current plan/limits/usage/cost if possible. Paused project or project count does not establish a free slot. Unknown -> provisional recommendation and exact check, never claim capacity. Respect usage terms.
4. Rank viable by ownership fit, existing compatible integrations, verified capacity, cost, organizational suitability; stable lexical tie for equivalent recommendations. No verified candidate -> conditional ranking, not invented confidence.
5. Provide best recommended account (exact identity to user when relevant), runner-up if useful, rationale/gaps, exact creation link, copyable names, user-only action, subsequent checks. If multiple eligible write targets and intent unclear, ask before write.

## Registry
Use [ecosystem/REGISTRY.md](../ecosystem/REGISTRY.md) as index, not absolute truth. Refresh target facts before consequential decisions. Full audit only when requested or authorized maintenance. Read-only requests don't mutate registry. Execution updates relevant records in authorized storage. The owner has explicitly approved publication of non-sensitive account and project metadata in this public repo. No passwords, tokens, connector identifiers, personal email addresses, customer data, private source content or secret configuration. For anything outside scope keep transient or use approved private storage.