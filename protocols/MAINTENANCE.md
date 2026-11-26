# Adaptive maintenance — automatic context propagation

On authorized execution, derive impact from changed IDs, paths, contracts and services. Traverse links to dependent requirements, tasks, tests, callers, environments, projects until no further direct impact. If missing link search references, repair map. Don't expand unrelated cleanup.

| Event | Mandatory impact checks |
|---|---|
| Approve/reverse decision | decision record + replacement, affected requirements/plan/status/architecture/source/dependent projects, diary |
| Task added/reordered | active plan/deps/acceptance/status, significant diary |
| Implement/change/remove | source refs, requirement/task status, tests, stale evidence, changed architecture/contracts, diary |
| Test/build/smoke | evidence and status per revision/env, never change intent |
| Move directory/new module | local/parent navigation, AGENTS links, imports/paths/tests/references |
| API/schema/auth | contracts/migrations, callers, compatibility/security, tests, affected plan/status |
| Deploy/rollback/account/infrastructure | release evidence, operations, registry relationships, status and affected envs |
| Repo create/rename/archive | stable ecosystem ID, aliases, ownership, shared dependencies, lifecycle |
| Research/discussion | read-only unless specifically asked to record; proposal != approved |
| Discrepancy | factual repair with evidence; unresolved intent conflict, preserve history |

## Synchronization transaction
Capture changed IDs/evidence. Write primary fact once, use references elsewhere. Re-read latest docs before updates; use expected SHA. Prefer atomic commit with code. Partial failure -> record exact pending paths/checkpoint, report. Diary append-only except linked correction entry; date/time, actor, task, action/reason, outcome, evidence, next step; no secrets or fake results. Small changes concise; no irrelevant touches.
Before closing audit changed paths navigable, active decisions/plan coherent, no orphan task/reference, old checks not reported current, code/docs/release traced, no unrelated files, no secrets, authorized registry updated if applicable. If record unchanged do not modify.

## Evolve structure
Adapt by scope as project grows: split/consolidate only when useful, preserve stable IDs, history, links and migration mapping. Reuse equivalents; tiny project can combine roles with clear headings. Avoid redundant docs. Ecosystem registry is pointer/index; project facts stay local. Shared facts belong at common scope; local differences stay local. Cross-project: read shared authority and each repo's rules; dependency map, compatibility, provider-before-consumer when safe, per-repo branch/revision/checks/release, explicit partial failures. Never force identical department behavior. Repeated process problem -> propose policy patch with scenario, rationale, regression and rollback; approval required for normative changes.