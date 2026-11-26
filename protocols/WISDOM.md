# Full project wisdom — knowledge model

## Authority map
Root AGENTS.md maps each role to actual paths, scope and reading order. Existing equivalent names allowed:
- README/overview: why, goal, users, boundaries, non-goals, entrypoints.
- decided.md/ADR index: approved requirements and constraints, unresolved decisions, replacements.
- plan.md: one active plan per scope; objective, revision, predecessor, ordered tasks, dependencies, acceptance.
- status.md: actual progress by requirement/task, blockers, next eligible task, latest evidence.
- architecture.md: actual topology, paths, interfaces, data ownership, auth, external dependencies; proposed changes separate.
- verification.md: evidence records by revision and environment; actual checks, limitations.
- diary.md: chronological actions, discoveries, reasons, outcomes, links and handoffs; not sole current authority.
- NAVIGATION.md: entrypoints, directory map and dependencies/scoped rules.
- research/: unapproved findings/options/tradeoffs/questions; not execution instructions.
- archive/: superseded decisions/plans with date/reason/replacement; history, not active authority.
- Source/migrations/tests/live services: evidence of implementation/verification/release respectively.

## Stable IDs and states
Use scoped REQ-0001, DEC-0001, TASK-0001, TEST-0001, REL-0001, ISSUE-0001; preserve equivalent IDs, never reuse retired ID. Significant requirement has ID, scope, source decision, acceptance, dependencies, implementation, verification, release and next action refs. Small repos can combine files with explicit roles.
Decision: proposed -> approved or rejected; approved -> superseded (replacement ID/date/reason) or withdrawn by explicit authority. Proposal never silently becomes approved. Plan cannot authorize rejected requirement.
Task: planned -> in_progress -> implemented; blocked from any active state with reason/next action. Independently track implementation absent/partial/present/removed; verification not_run/pass/fail/stale/blocked per revision/environment; release not_deployed/preview/production/rolled_back/unknown per version. A feature may be implemented/local pass/hosted blocked at once. Changed relevant code/config/deps/env invalidates old evidence; preserve history and mark stale.
Plan replacement: archive or mark previous superseded with reason, replacement ID and date; migrate surviving task IDs; cancel/mark abandoned tasks; preserve evidence. One active plan per scope; linked explicit module plans allowed. Unresolved conflict -> stop affected work, don't choose by timestamp alone.

## Reconstruction
1. Resolve exact repo/branch/SHA; root AGENTS + navigation. Read active overview, decisions, plan, status, architecture. Recent diary for leads, archive only when needed.
2. Trace requirement -> decision -> task -> source/config/migrations -> verification -> release. Compare actual current source and deployed SHA separately. Inspect tests/logs/live metadata where necessary. Mark confidence and missing evidence.
3. Build snapshot: purpose/non-goals, architecture, current intent, unresolved decisions, implemented vs verified per env, superseded approaches, dependencies, blockers, next work, paths and evidence. Do not infer from memory alone.
4. Resume: choose explicitly prioritized ready approved task whose dependencies met, then plan order, then stable ID. If blocked, independent ready task only within authorization. No clear approved path -> present gap, ask material decision.
5. Root AGENTS missing -> README, tree, linked docs, source; map roles and report missing; retrofit only authorized execution.
6. Fresh agent with only repo URL + boot ROM + access must reconstruct this snapshot and safe next task without chat. Same-agent rehearsal isn't independent proof. See VERIFY and scenarios.