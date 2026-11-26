#!/usr/bin/env python3
"""Read-only structural checks; no network."""
from pathlib import Path
import re
root=Path(__file__).resolve().parents[1]
errors=[]
required=["AGENTS.md","BOOT.md","BOOT-ROM.txt","NAVIGATION.md","decided.md","plan.md","status.md","verification.md","diary.md","ecosystem/REGISTRY.md","tests/SCENARIOS.md"]+["protocols/"+n+".md" for n in ("KERNEL","RUNTIME","DISCOVERY","INITIALIZE","SERVICES","WISDOM","MAINTENANCE","VERIFY","RECOVERY")]
for p in required:
    if not (root/p).is_file(): errors.append("Missing "+p)
rom=(root/"BOOT-ROM.txt").read_text()
if len(rom)>1500: errors.append("ROM too long")
for d in ("protocols","ecosystem","templates","tests","archive"):
    if not (root/d/"NAVIGATION.md").is_file(): errors.append("Missing navigation "+d)
for p in root.rglob("*.md"):
    if ".git" in p.parts: continue
    for target in re.findall(r"\[[^\]]+\]\(([^ )]+)\)",p.read_text()):
        if target.startswith(("https://","http://","#","mailto:")): continue
        q=target.split("#",1)[0]
        if q and not (p.parent/q).exists(): errors.append(f"Broken link {p.relative_to(root)} -> {target}")
ids=re.findall(r"^\| (B\d+) \|",(root/"tests/SCENARIOS.md").read_text(),re.M)
if len(ids)!=len(set(ids)) or len(ids)<30: errors.append("Scenario coverage/duplicates")
if errors:
    print("\n".join(errors)); raise SystemExit(1)
print(f"PASS: ROM {len(rom)} chars, required files, navigation, links, {len(ids)} scenario IDs")
