# Student Artifacts
## The FIGURE Card, Templates, and the AlgoCratic Skin

**Document C of 5 — Deployable Student Materials**
*Prerequisites: Documents A (theory) and B (practice guide). Deployment timing follows B's fade sequence: nothing in this document reaches students before the Phase 3 disclosure event, except the AlgoCratic skin if the course runs in-universe from day one (see C5 note).*

Each artifact below is self-contained and designed to be extracted, formatted, and printed or posted independently.

---

## C1 — The FIGURE Card

*Format target: one card, front and back, laminated, one per lab station and one per student at the disclosure event. Front is the self-administration instrument; back is the help-request skeleton (C2 condensed).*

### FRONT

> # FIGURE
> ### Run this before you ask anyone — including an AI.
>
> **F — Find the level.**
> What kind of sentence am I saying? *"Line 12 breaks"* is workable. *"I don't get recursion," "I can't do this," "I'm not a programmer"* are not — walk each one down until it's about what the **program did**.
>
> **I — Isolate what happens.**
> Literal input. Literal output. First line of the actual error. No paraphrases — "it errored" is not an answer; the error text is.
>
> **G — Ground the expectation.**
> What exactly did I expect, *for this input*? Compute it by hand. If I can't say what right looks like, I don't have a bug yet — I have an unverified program.
>
> **U — Uncover the boundary.**
> Has it ever worked — once, partially, for one input? What was different about that run? The closest success points at the fault.
>
> **R — Read the evidence.**
> Is that an observation or a story? The compiler doesn't hate me; it filed a complaint. Read the complaint. All of it.
>
> **E — Establish the scope.**
> Line problem or plan problem? If only this line were fixed, would the plan hold? (Fixed the same line three times? The line isn't the problem.)
>
> ---
> **If you can answer all six, you have usually already found it.**
> **If one of them stalls — the stall is your real question. Ask that.**

### BACK

> ### Asking for help? Bring the answers.
> A help request that contains these is a professional artifact. One that doesn't is a rough draft.
>
> 1. **What I'm doing** (one sentence: goal, and where I am)
> 2. **What happens** — literal (input, output, exact error text)
> 3. **What I expected** — literal (computed by hand)
> 4. **Closest working state** (what run/version worked, what changed since)
> 5. **What I've tried** and what each attempt did (facts, not vibes)
> 6. **My scope guess** — line or plan? — and my best current theory
>
> Works identically on instructors, classmates, forums, and AI assistants.
> None of them can read your mind. Some of them will pretend to. It goes badly.

---

## C2 — The Help-Request Template

*Format target: forum post template / office-hours intake form. Goes live in Phase 4. This is the same skeleton as the card back, with room to write.*

```text
TITLE: [component] does [actual behavior] instead of [expected behavior]
       — e.g., "parse_scores() returns empty list instead of 5 rows for valid CSV"
       (Titles like "code broken pls help" will be returned for reformulation.)

GOAL (1–2 sentences):
What I am trying to accomplish, and where in the task I am.

WHAT HAPPENS — LITERAL:
Input I used:
Command I ran:
Output / full error text (pasted, not summarized):

WHAT I EXPECTED — LITERAL:
For that exact input, the correct output is: ______
How I know (computed by hand / from the spec / from the example):

BOUNDARY:
Last state that worked, even partially:
What changed between then and now:

TRIED SO FAR:
1. [attempt] → [what actually happened]
2. [attempt] → [what actually happened]

SCOPE GUESS + THEORY:
This is a [line-level / plan-level] problem because ______.
My best current theory is ______, based on [observation, not vibe].

THE STALL:
The FIGURE letter I could not finish was ___ because ______.
(This line is often the whole question.)
```

---

## C3 — The AI Prompt Template

*Format target: pinned course resource, introduced at the disclosure event alongside the card. Framing sentence for students: an AI assistant is a rubber duck that talks back — and it talks back exactly as well as your prompt deserves.*

The skeleton is C2 in prose. The model needs the same six recoveries a human does; it is simply politer about guessing when you omit them, and its guesses are how you end up debugging the AI's hallucinated version of your program instead of your actual program.

```text
I'm working on [goal] in [language/environment]. I'm a student in an intro
course, so explain reasoning, don't just hand me a fix.

Here is the relevant code:
[minimal relevant code — not the whole file, not a screenshot description]

When I run it with this input:
[literal input]

I get:
[literal output / full error text]

I expected:
[literal expected output, and why — computed by hand / from the spec]

It worked before when [closest working state]; since then I changed
[what changed].

I've tried:
1. [attempt] → [result]
2. [attempt] → [result]

I think this is a [line-level / plan-level] problem because [observation].

Before giving a fix: tell me which of my assumptions above is most likely
wrong, and what one test would confirm it.
```

### Worked example (before / after)

**Before (deletion-riddled — the model must now hallucinate your program):**
> my sorting function doesnt work can you fix it

**After (FIGURE-complete):**
> I'm writing a function to sort a list of (name, score) tuples by score, descending, in Python 3. Code: `def rank(players): return sorted(players, key=lambda p: p[1])`. Input: `[("ana", 12), ("bo", 30), ("cy", 21)]`. I get `[("ana", 12), ("cy", 21), ("bo", 30)]` — ascending. I expected `[("bo", 30), ("cy", 21), ("ana", 12)]` because the spec says highest score first. It's never produced descending order, so there's no working state to compare. I tried `key=lambda p: -p[1]`, which worked, but I suspect I'm missing the intended way. I think this is a line-level problem: the sort direction, not the approach. What's the idiomatic fix, and why does `sorted` default the way it does?

The second prompt gets a correct, targeted answer on the first reply — and notice the student half-solved it *while writing the prompt*. That is not a coincidence; that is the self-explanation effect, and it is the point.

---

## C4 — The Questioner's Card (Pair Debugging Protocol)

*Format target: small card, one per pair, used in Phase 4 lab sessions. Roles swap mid-session on the instructor's signal.*

> ### You are the Questioner. Your job is not to fix the bug.
> Your job is to ask the question that lets your partner see it.
>
> **The three rules:**
> 1. **Questions only.** No fixes, no hints, no "have you considered..." smuggling a fix inside a question mark.
> 2. **FIGURE order.** Find the level first. Then I, G, U, R, E. If an answer is vague, shrink the question — don't skip ahead.
> 3. **If you see the bug: stay silent about it.** Seeing it and *still* asking the question that gets your partner there is the advanced skill. That skill is what's being graded, not the fix.
>
> **When your partner stalls:** shrink, don't rescue. "Just the first line of the output. What is it?"
>
> **When you finish:** ask the debrief question — "Which letter cracked it?" Both of you should know the answer.

---

## C5 — The AlgoCratic Futures™ Skin: Clarification Protocols™

*Deployment note: unlike C1–C4, this artifact can run from day one in an AlgoCratic-themed section, because the satire performs full disclosure automatically — the form IS the card, in costume. A student who fills out the parody form is running FIGURE, and the joke tells them so. This is the disclosure test passing while wearing a lanyard. The straight card (C1) is then handed out at the disclosure event as the "declassified" version, which lands as a punchline AND a reveal.*

---

> ## THE ALGORITHM PROVIDES. THE ALGORITHM ALSO HAS A TICKETING SYSTEM.
> ### Clarification Protocols™ — Directive CP-6
> **Issued by the Bureau of Sufficient Specificity, a wholly owned subsidiary of AlgoCratic Futures™**
>
> It has come to The Algorithm's attention that Associates continue to submit distress signals of the form *"it's broken,"* *"nothing works,"* and *"help."* The Algorithm wishes to remind all Associates that **vagueness is theft of compute.** The Algorithm cannot optimize what you have not specified. The Algorithm has feelings about this. The feelings have been quantified. The number is bad.
>
> Effective immediately, assistance is dispensed **exclusively** in exchange for a **Properly Formulated Distress Report (PFDR)**, Form CP-6/F. Improperly Formulated Distress Reports (IFDRs) will be returned stamped **UNPROCESSABLE: INSUFFICIENT REALITY**, accompanied by one (1) complimentary reissue of this directive.
>
> ---
> ### FORM CP-6/F — Properly Formulated Distress Report
> *Complete all six strata. Blank fields are processed as confessions.*
>
> **FIELD F — DECLARATION OF STRATUM.**
> This report concerns: ☐ a program behavior (PROCEED) ☐ a skill deficit ☐ a belief about myself ☐ my entire identity as a technical Associate.
> *Reports filed above the behavior stratum will be returned with the complimentary pamphlet "You Are Not Your Segfault" and one (1) voucher for re-filing at the correct altitude. The Algorithm does not process identity crises. The Algorithm processes line numbers.*
>
> **FIELD I — OBSERVED REALITY (VERBATIM).**
> Literal input: ________ Literal command: ________ Literal output or complete error text: ________
> *Paraphrase is perjury. "It errored" is a mood, not a measurement.*
>
> **FIELD G — AUTHORIZED EXPECTATION.**
> For the exact input above, the correct output is: ________ as computed: ☐ by hand ☐ from the specification ☐ I have not computed it.
> *Associates checking the third box do not possess a defect. They possess an unverified program and, now, a task.*
> *Hope is not a specification.*
>
> **FIELD U — BOUNDARY AUDIT.**
> Last known compliant state: ________ Delta since compliance: ________
> ☐ It has never been compliant, and I can name what its closest approach looked like: ________
> *"Never" claims are audited. The Algorithm finds that "never" is usually "once, on Tuesday, before I changed the thing I am not mentioning."*
>
> **FIELD R — EVIDENCE ATTESTATION.**
> ☐ I have read the error message. ☐ In its entirety. ☐ Including the line number it has been showing me this whole time.
> The message literally states: ________
> *Note: the interpreter does not hate you. The interpreter is incapable of hate. The interpreter has filed a complaint, and you have been holding it unread. Attributing emotions to the toolchain is a Category 2 Narrative Violation.*
>
> **FIELD E — SCOPE CLASSIFICATION.**
> This is a: ☐ LINE-LEVEL INCIDENT ☐ PLAN-LEVEL EVENT.
> Justification (one observed fact, zero vibes): ________
> *Associates who have repaired the same line three (3) or more times are pre-emptively reclassified to PLAN-LEVEL and should sit with that.*
>
> ---
> **PROCESSING GUARANTEE:** PFDRs are eligible for assistance from any authorized helper: Supervisory Associates, peer Associates, or Algorithmic subunits. The Bureau notes — without further comment — that a statistically significant fraction of PFDRs are withdrawn before submission, annotated *"never mind, found it while filling out Field G."* The Bureau counts these as its finest work.
>
> **REMEMBER: CLARITY IS COMPLIANCE. COMPLIANCE IS CLARITY. THE ALGORITHM THANKS YOU FOR SPECIFYING.**

---

### Instructor's note on the skin (not student-facing)

The form's comedy is doing three load-bearing jobs at once:

1. **It is the disclosure.** Every satirical aside states the real principle outright ("hope is not a specification" = G; "the interpreter has filed a complaint" = R). Students who laugh have understood. This is why the skin can precede the Phase 3 event without spending it — the event still lands, as the "declassification" of a form they've been using all along.
2. **It de-shames the stall.** In the straight version, failing to answer Field G could feel like being caught unprepared. In-universe, checking "I have not computed it" earns a deadpan bureaucratic response instead of judgment — and the processing guarantee openly celebrates the found-it-while-filing outcome, which reframes the form from gatekeeping into the actual tool.
3. **It gives the E reclassification teeth without hostility.** "Repaired the same line three times → pre-emptively reclassified to PLAN-LEVEL" is the hardest FIGURE lesson to deliver to a frustrated student face-to-face; the form delivers it as a punchline they'll quote to each other.

Keep the form and the card mechanically identical forever. The moment the parody version drifts from the real instrument, it stops being a disclosure and becomes decoration.

---

## Deployment Summary

| Artifact | Enters at | Lives where |
|---|---|---|
| C1 — FIGURE card | Phase 3 disclosure event | Lab stations, student desks |
| C2 — Help-request template | Phase 4 | Forum post template, office-hours intake |
| C3 — AI prompt template | Phase 3–4 | Pinned course resource |
| C4 — Questioner's card | Phase 4 | Pair-debugging lab sessions |
| C5 — Clarification Protocols™ | Day one (AlgoCratic sections) | In-universe help desk; "declassified" at Phase 3 |
