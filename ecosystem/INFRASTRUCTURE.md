# Infrastructure inventory — 2026-11-26
All seven visible Vercel and Supabase connections responded to list-projects. Vercel requested limit 100 and returned 0–4 entries per connection; organization/team enumeration and capacity not audited. Supabase status is provider-reported as of observation, not independent application health. All Supabase regions us-east-1 unless noted.
## Vercel (13 project entries)
| Account routing label | Project names |
|---|---|
| despairarc000 | tempmanga, tempanime, tempmerch |
| hilocarloarmenion03 | admin, loxada-connected-preview, guider, mcptest |
| lozadatech01 | mangalightnovel-da1l, mangalightnovel |
| hebratech01 | anime |
| padregandatech01 | merch |
| hilocarloarmenion | resort, centralsystem |
| KamijouImpact | none returned |
## Supabase (9 project entries)
| Account routing label | Project names / observed status |
|---|---|
| despairarc000 | tempanimedb — INACTIVE; tempmangadb — INACTIVE |
| hilocarloarmenion03 | adminDB — ACTIVE_HEALTHY |
| lozadatech01 | mangalightnovelDB — ACTIVE_HEALTHY |
| hebratech01 | animeDB — ACTIVE_HEALTHY |
| padregandatech01 | merchDB — ACTIVE_HEALTHY |
| hilocarloarmenion | centralsystem — INACTIVE; resort — ACTIVE_HEALTHY (ap-northeast-1) |
| KamijouImpact | smemisDB — ACTIVE_HEALTHY |
## Candidate relationships — not verified integrations
Name similarity suggests LOXADA admin, manga, anime, merch, resort, centralsystem and temp projects may have corresponding services. SME MIS database exists on its connected Supabase identity; no Vercel project returned on that connection. Verify exact Git link, project ref, environment and deployment revision before using these candidates. No secret values, account emails, internal project refs or database endpoints are published. All quotas and remaining capacity unknown.