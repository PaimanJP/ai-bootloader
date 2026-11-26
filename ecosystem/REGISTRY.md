# Ecosystem registry
The owner explicitly approved a public registry of non-sensitive development metadata on 2026-11-26. This is not a credential store. Do not publish personal emails, access tokens, connector handles, passwords, private source, secret config, customer records or confidential data.

Schemas:
- Accounts: provider, user-visible username/team/org label, ownership/membership, connection state, capacity evidence, last observed, limitations. Connector identifiers remain transient.
- Projects: stable ID, canonical owner/repo URL, purpose, evidence path/revision, lifecycle active/paused/archived/unknown, branch, aliases, related projects. Product parent and repo role for multi-repo systems.
- Infrastructure: provider project name and safe dashboard/domain link, account/team label, linked repo, environment, status, release evidence and observed time. No secret values.
- Relationships: source/target, relation hosts/uses_db/fork_of/shares_contract/depends_on/member_of, environment, evidence and confidence confirmed/reported/inferred/unknown/conflicting.
- Audit: date, scope, reachable/denied/missing, pagination completion, gaps and source evidence.

Refresh target facts before consequential decisions. Merge by stable IDs; preserve aliases and contradictory observations. Do not use a name match as confirmed integration. No registry writes for discussion. Keep local project facts in project repos. Inventory pending initial discovery.