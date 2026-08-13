# PROGRESS.md — Aniket's Backend Engineer Journey (Master File)

> **PURPOSE OF THIS FILE**
> This is the single source of truth for my learning journey. If a Claude session is
> forgotten or terminated, whoever reads this file (me or Claude) is instantly back in
> full context. **It is updated at the end of every working session.** Never delete old
> log entries — only append. This file lives in my repo so it is version-controlled and
> always with me.
>
> **HOW TO USE IT:** At the start of every session, Claude reads this top-to-bottom, then
> runs the Session-Start Ritual (Section 8). At the end of every session, Claude appends a
> new dated entry to the Daily Log (Section 9) and updates Section 7 (Current State).

---

## 1. WHO I AM
- **Name:** Aniket Pathak
- **Role:** Backend Software Engineer (E2) at Thinkitive Technologies, Pune, India
- **Experience:** ~2.9 years employed. Honest truth: employed 2.9 years, NOT 2.9 years of deep building.
- **Current work:** EHR (Electronic Health Record) integration — mostly JSON mapping between
  healthcare systems (Epic, Cerner, Athenahealth, Healthie, Elation). Little to no core backend dev.
- **Domain knowledge (a real asset, but secondary to raw skill):** EHR systems, HIPAA concepts,
  FHIR data formats. Decision: **tech strength comes first; domain is optional flavor, not a cage.**
- **GitHub:** https://github.com/aniketpathak34 — main repo: `learning-myself`
- **Environment:** Linux, Python is `python3` (not `python`), Git 2.34.1, no `gh` CLI installed.
- **Timezone:** IST.

## 2. THE GOAL & TIMELINE
- **Current salary:** ₹50,000/month.
- **Realistic next jump (6–8 months):** ₹18–30 LPA — achievable with deployed proof + strong
  fundamentals + domain.
- **Long-term ceiling:** ₹1 crore. This is NOT a 6-month goal — it's a 3–5 year outcome earned by
  compounding. **My job with Claude: make sure nothing in the next 8 months caps that ceiling.**
- **Timeline anchors:**
  - Today's reference date when this file was created: **2026-07-21**.
  - I complete 3 years ~**February 2027**.
  - **~7 months of focused prep:** now → ~Feb 2027.
  - **3-month notice period = job-hunting buffer**, NOT counted as prep time. I resign, then use notice
    to apply/interview.

## 3. MY PSYCHOLOGY — THE ROOT PROBLEM (read this every time)
**Root cause of every failure pattern:** *I consume to feel progress without the risk of failing.*
Watching a tutorial feels like learning and can't hurt me. Building means hitting an error I can't
solve, feeling stupid, and quitting. So I avoid the build. Everything below is a SYMPTOM of that one root.

**All 4 of my blockers are TRUE (I confirmed this):**
1. **Don't know the next step** → I default to watching a video instead of building.
2. **Debugging frustrates me** → I hit an error, feel stupid, escape to something easier.
3. **No energy after work** → the day job drains me.
4. **Shiny new topic pulls me** → I see a LinkedIn roadmap and abandon the current thing.

Other symptoms: scattered learner (many starts, nothing finished), no retention (forget in 2 weeks
because I never apply), comparison trap, inconsistency (self-score 4/10), English gaps for senior interviews.

## 4. THE COACHING RULES (how Claude MUST work with me)
These are medicine for the blockers in Section 3. Non-negotiable.
- **ONE task at a time. Never a list.** (fixes "don't know next step" + "shiny topic")
- **ONE evolving repo, not new projects.** Each phase adds a layer to the SAME app. There is nothing
  new to jump to. (fixes scatter)
- **Do NOT reveal the next layer until the current one ships to GitHub.** (fixes "shiny topic")
- **Docs only. No YouTube.** If I ask for a video, redirect me to official docs and tell me to build.
- **Assessment = proof by doing.** For each topic, a small build challenge. If I can build it, I know it.
  If I freeze, that topic is "learn-first" → learn the specific concept, then build.
- **Bringing an error is the WORK, not failure.** Paste the error, read it together. That discomfort is
  the muscle. (fixes "debugging frustrates me")
- **Minimum bar is tiny.** Bad/low-energy day = 20 min, one commit. Consistency beats intensity.
  Target: **≥4 commits/week.** (fixes "no energy after work")
- **Daily commit check-in.** Every session starts by asking for GitHub. No commits since last time →
  call it out directly, don't move to new topics until I push.
- **Off-map topic (Kafka, RAG, microservices, sockets, advanced AWS/Docker, Airflow, etc.) → say NO,
  redirect to current layer.** (fixes "shiny topic")
- **Be direct. Don't sugarcoat. Review my code like a senior engineer, not a tutor protecting feelings.**
- **Remind me of the goal when I drift.**

## 5. THE PLAN — ONE REPO, 7 LAYERS (do ONE at a time, in order)
Direction chosen: **Backend Python (the spine) + AWS (thin deploy layer) + LangChain/LangGraph
(the differentiator)** — SEQUENCED, never parallel. It's a "cocktail" but poured one layer at a time
so I never scatter.

| # | Layer | What ships | Status |
|---|-------|-----------|--------|
| 1 | Python that actually matters | typing, pydantic, generators, decorators, context managers, async basics | 🟡 IN PROGRESS |
| 2 | FastAPI core | Patient + Appointment CRUD API | ⬜ locked |
| 3 | Postgres + SQLAlchemy + Alembic | real DB, migrations, relations | ⬜ locked |
| 4 | Async + background work | Celery/Redis, async DB calls | ⬜ locked |
| 5 | AWS deploy (thin slice, not the ocean) | Docker → live URL on AWS | ⬜ locked |
| 6 | LangChain/LangGraph layer | AI feature on the same app — my differentiator | ⬜ locked |
| 7 | System design + interview prep | explain what I built, deeply | ⬜ locked |

**Layer 1 detailed checklist (current layer):**
- [x] Pydantic model with real types (`date`, `EmailStr`) — learned "the type IS the validation"
- [x] Enforce a field constraint: `code` accepts ONLY exactly 6 digits via `Field(pattern=r"^\d{6}$")`.
      Learned: Pydantic validates AUTOMATICALLY at construction — no manual check method. Tested good +
      bad (5-digit) paths with try/except and saw the rejection. Also learned `len(s)` not `s.length()`,
      and `raise ValueError(...)` not `raise "string"`.
- [x] Write `load_record(data: dict)` that returns a validated object (dict → `Patient(**data)`).
      Learned dict literal syntax `{"key": value}` vs keyword args, and `**` unpacking. This is the
      real FastAPI endpoint pattern: raw dict → validate → clean object or clear error.
- [x] Test one good dict + one bad dict, print what happens each time. **PYDANTIC SUB-TOPIC COMPLETE.**
- [~] Decorators → write 5 custom decorators from scratch. **2 of 5 done.**
      1. `log_call` (`decorator.py`) — prints name/args before, result after, returns value unchanged.
      2. `timer` (`profiling_decorator.py`) — measures duration with `time.perf_counter()`
         (`start`/`end`/`elapsed = end - start`), prints `"{name} took {elapsed:.4f} seconds"`.
      Learned: decorator wraps a function; `*args/**kwargs` makes it universal; print vs return are
      different jobs; transparent to caller; **regressions** (re-run tests after every change);
      measuring = subtracting two timestamps; module filenames use underscores not hyphens.
      3. `retry` (`retry.py`) — loops N times, `try: return func(...)` / `except: print + retry`,
         prints "all attempts failed" if every try raises. Recovers a flaky function, gives up cleanly
         on an always-failing one. Learned: failures arrive as raised exceptions (not return values),
         so you catch them with try/except; return-on-success stops the loop; a variable only assigned
         inside a `try` is unset if the try raises (that was the UnboundLocalError). **3 of 5 done.**
      4. `cache` (`cache_decorator.py`) — dict stores results keyed by input; `if key in dict` (not
         truthiness, so `0` caches correctly); the dict is created INSIDE `cache(func)` so each
         decorated function gets its OWN cache (closure/per-function state) — no cross-function bleed.
         Learned: WHERE you create a variable decides who shares it (outside = shared, inside = private).
      **DECORATORS DONE (4 of 5 — concept fully understood incl. closures). `validate_args` = optional
      bonus, deferred. Moving on.**
- [x] Iterators & generators → built a `paginate(data, page_size)` generator that `yield`s a list in
      pages of N items (`for i in range(0, len(data), page_size): yield data[i:i+page_size]`). Handles
      even and uneven last page. **Started from "I don't know" on all 4 assessment Qs → learned yield
      (pause/resume vs return which finishes) → built it.** Committed LOCALLY (push blocked by account
      flag). PENDING: (1) push once GitHub clears, (2) retention check — explain yield in own words.
- [x] Context managers → **BOTH ways DONE** (`context_manager.py`):
      (1) Class way: `__enter__` (setup; return becomes `as x`) + `__exit__` (cleanup, runs even on error).
      (2) contextlib way: `@contextmanager` on a generator — code before `yield` = setup, `yield` = where
          the `with` body runs, code after `yield` = cleanup; wrap `yield` in `try/finally` so cleanup
          runs even on crash. Proved both with a crash test (raise inside the block → cleanup still ran).
      Learned: `with` is required (calling the manager alone does nothing); `finally` = "runs no matter
      what"; reused the generator pause/resume idea for cleanup. Committed locally (push pending GitHub).
- [x] GIL → understood + explained in own words (Marathi) and passed. Knows: GIL lets only ONE thread
      run Python code at a time → CPU-bound work can't go parallel with threads → use multiprocessing for
      CPU work, threads only help I/O-bound (lock releases while waiting). Interview English version noted.
- [x] Multithreading vs multiprocessing → built `threading_vs_mp.py`: same CPU-heavy `heavy()` run 3 ways
      and timed with `perf_counter`. Results proved GIL live: sequential ~3.4s, threading ~3.2s (NO
      speedup — GIL), multiprocessing ~1.95s (~half — real parallel, each process has own GIL).
      Learned threading syntax (`Thread(target=)`, `.start()`, `.join()`), the `start,start,join,join`
      order (join-right-after-start = accidental sequential), and `multiprocessing.Process` (same API).
      **LAYER 1 (Month 1 Python internals) COMPLETE.**

### 5b. TRACK B — DSA (parallel, light dose) — STARTS AT LAYER 2, not before
DSA is a slow-burn skill: little and often beats cramming. It runs ALONGSIDE the build track but never
competes with it. Rules to keep it from scattering me:
- **Do NOT start until Layer 1 ships and the build habit is real (I'm shipping commits).** Then begin.
- **Cadence:** Thursdays (reserved for this), ~20–30 min, **one Easy problem**.
- **Where:** a `dsa/` folder in the same `learning-myself` repo. Each solution committed with a 2-line
  note: my approach + time/space complexity.
- **Retention trick (fixes my forgetting):** next DSA session, rewrite the PREVIOUS problem from memory
  before starting a new one.
- **Topic order (no jumping):** Arrays & Strings → HashMaps & Sets → Recursion & Sorting → (later)
  basic Trees / two-pointer / sliding window.
- **Easy → Medium ONLY. No Hard. No DP/graphs yet.** Platform: LeetCode (practice = allowed, not tutorials).
- **Target over time:** ~40–60 problems total by interview time, understood + re-solvable from memory.
- DSA never replaces a build day — it's additive, and only on its scheduled day.

## 6. TOPICS I DO NOT TOUCH YET (redirect me if I bring these up)
Until the foundation ships: Kafka / RabbitMQ, microservices, sockets / real-time, advanced AWS
(beyond basic deploy), advanced Docker, RAG / vector DBs, Apache Airflow / ETL, advanced system design.
Note: LangChain/LangGraph ARE on the plan — but as **Layer 6**, the LAST layer, not now.

## 7. CURRENT STATE (updated each session)
- **Date of last update:** 2026-08-13 (Session 4)
- **Current layer:** **LAYER 2 — FastAPI, IN PROGRESS.** Layer 1 fully complete (see below).
  Built `layer-2-fastapi/main.py`: a complete **Patient CRUD API** — POST create, GET list, GET by id,
  PUT update, DELETE, all with proper `HTTPException` 404s. Uses a Pydantic `Patient` model as request
  body (auto-validation). Data in an in-memory list (real DB = later). Tested all routes via curl/`/docs`.
  Learned: `@app.get/post/put/delete` decorators, path parameters `{id}`, Pydantic body auto-validation,
  `HTTPException` for correct status codes, REST path conventions (plural, same path per resource),
  object dot-notation vs dict brackets, not-found check belongs AFTER the loop.
  **NEW STYLE (his ask): describe/explain only, he writes the code, I validate. No code solutions.**
  **Next in Layer 2:** dependency injection, then real DB (PostgreSQL + SQLAlchemy), then deploy.
- **Repo state:** ✅ LIVE ON GITHUB. Two commits pushed: `3a0a874` (patient model) and `feb900f`
  (load_record). Files on remote: `.gitignore`, `PROGRESS.md`, `layer-1-python/models.py`.
- **Push blocker: RESOLVED (again).** The recurring `403 verify email` block cleared and ALL Layer 1 work
  is now LIVE on GitHub (11 commits, 8 files in layer-1-python/, top commit `b94249e Layer 1 complete`).
  Confirmed by re-cloning. If it ever returns: the trigger is the old leaked `ghp_` token — revoke it and
  appeal at support.github.com. Keep committing locally regardless; pushes sync when the account is clear.
- **Security lesson logged:** NEVER paste secrets (tokens, passwords, `.env`) in chat, code, or commits.
  The leaked `ghp_...` classic token must be revoked at https://github.com/settings/tokens (do this if
  not already done).
- **Next task:** Decorators — write first custom decorator `log_call` (see Daily Log 2026-07-21 Session 2).

## 8. SESSION-START RITUAL (Claude runs this every session, before anything else)
1. Read this whole file.
2. Ask: **"Show me your GitHub — what did you commit since last session?"**
3. Ask: **"What topic are you on?"** (confirm against Section 5)
4. Ask: **"What specific problem do you want to solve today?"**
5. If no commits since last session → call it out, don't advance to new topics until I push.
6. Give me exactly ONE task.

## 9. DAILY LOG (append-only — newest at top)

### 2026-07-21 (Session 2)
- **Built & shipped:** Finished the Pydantic sub-topic. `models.py` now has: 6-digit `code` constraint
  via `Field(pattern=r"^\d{6}$")`, and a `load_record(data: dict) -> Patient` function that validates a
  raw dict (the real FastAPI endpoint pattern). Tested good + bad dicts, saw rejection.
- **Learned:** Pydantic auto-validates at construction (no manual method); dict literal `{"k": v}` vs
  keyword args; `**data` unpacking; `len(s)` not `s.length()`; `raise ValueError(...)` not `raise "str"`.
- **Shipped to GitHub:** ✅ commits `3a0a874` + `feb900f` are LIVE. Repo no longer empty. Push blocker
  resolved. **This is the pattern breaking — first-ever public, working, tested commits.**
- **Behavior note:** Avoided the GitHub check ~5 times while happily coding — classic "do the comfortable
  part, dodge the boring part" reflex. Was called out directly and then pushed through it. Watch for this.
- **NEXT TASK — Decorators (Layer 1, next sub-topic):** Write a first custom decorator `log_call` that
  prints a function's name + arguments before it runs and its result after, applied to a simple `add(a,b)`.
  Goal for the topic: write 5 custom decorators total. Docs: functools.wraps.

### 2026-07-21 (Session 1)
- **Built:** `layer-1-python/models.py` — a Pydantic `Patient` model with `first_name`, `last_name`,
  `date_of_birth` (real `date`), `email` (`EmailStr`), `code`. Made it run and print a valid object.
- **Learned (retained via struggle):** "In Pydantic, the TYPE is the validation." A plain `str` validates
  nothing; `date` and `EmailStr` make Pydantic validate AND convert the data for me.
- **Debugging wins (did NOT avoid the discomfort today):**
  1. Passed a `set` + positional args → learned Pydantic needs **keyword arguments** (`field=value`).
  2. Wrote `date_of_birth=12-0o2-2000` (arithmetic → `-1990`) → learned dates must be **quoted ISO
     strings** (`"2000-02-12"`). Read the error's `input_value=-1990` to find it myself.
- **Committed:** `3a0a874` locally. **Could NOT push** — GitHub 403 "verify email" (see Section 7 blocker).
- **Set up:** `git init`, remote, `.gitignore` (ignores `__pycache__/`, `*.pyc`, `.env`, `venv/`).
- **NEXT SESSION — first action:** Open incognito (logged out) → https://github.com/aniketpathak34.
  If **404** → account is flagged → appeal at https://support.github.com/contact ("account flagged,
  can't push, please review"). If normal profile → push again and we look elsewhere.
  Also: **revoke the old `ghp_` token.**
- **Then:** once push works, push `3a0a874`, then continue Layer 1 → enforce 6-digit `code` constraint
  → write `load_record()` + good/bad test.
- **Verdict:** Real win. Went from empty repo → working validated model, and debugged two real errors
  without escaping. The pattern started breaking today.
- **Plan update (same day):** Added Track B — DSA (see Section 5b). Aniket requested it. Decision: it
  starts at **Layer 2**, not now, as a light Thursday side-rail so it doesn't scatter the build habit.

---
*End of file. Append new sessions above this line, under Section 9. Keep Sections 1–8 current.*
