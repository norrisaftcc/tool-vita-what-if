# The Instructor Practice Guide
## Running FIGURE in a Live Course

**Document B of 5 — Practice Guide**
*Prerequisite: Document A (theory foundation and lineage). This document assumes the why and delivers the how.*

---

## 0. The Whole Method on One Line

**Find the level, ask the questions, hold the silence.** After the disclosure event (§3, Phase 3), "figure it out" stops being a dismissal and becomes this exact assignment.

---

## 1. F — Find the Level (Always the First Move)

Before asking any precision question, classify the student's stuck-statement by its abstraction level. A question aimed at the wrong level doesn't just fail — it bounces off, and the student experiences the bounce as not being heard.

| Level | Student sounds like | What's actually being reported | Your routing move |
|---|---|---|---|
| **Behavior** | "The loop breaks on line 12." | A specific event | Go straight to IGURE (§2). This is the level where the questions work. |
| **Capability** | "I don't understand recursion." | A missing skill, stated as such | Half a level up from where questions work. Chunk down: "Show me the last recursive call you traced — where did the trace stop matching your prediction?" Converts capability-talk into a behavior-level event you can question. |
| **Belief** | "I can't do this." / "This kind of thing never makes sense to me." | A generalization about self-in-domain | Do **not** ask "what happens exactly" — it reads as dismissal. First move is boundary-hunting on the generalization itself: "Never? What's the closest you've gotten — even once?" One counterexample converts a belief statement into a capability statement, which you then chunk down again. |
| **Identity** | "I'm just not a programmer." | A self-classification | Never argue with it and never accept it. Sidestep to behavior without ceremony: "Maybe, maybe not — but that's not answerable today. What *is* answerable is what line 12 did. What did it do?" You are declining the identity frame, not refuting it. Refuting it is a motivational speech; declining it is respect plus redirection. |

**The one rule:** precision questions only work at the **behavior** level. Every other level must be walked down first — usually one level at a time. Trying to jump from identity to behavior in a single move works only with the sidestep script above, and only because it explicitly names that it's declining the frame rather than pretending the frame wasn't offered.

**Honest label (from Document A):** this level stack is a practitioner heuristic with partial academic convergence (attribution theory, mindset research). Use it as a routing device. Don't psychoanalyze; the classification is of the *sentence*, not the student.

---

## 2. IGURE — The Five Questions

The complete question set, with full scripts and utilization variants. These are fixed on purpose — same questions, same order, same phrasing, every time. The fixedness is not pedantry; it is what makes the pattern learnable by osmosis (§3).

### I — Isolate what happens
*Recovers: the actual symptom. Reverses: simple deletion, unspecified verbs, vague referents.*

- **Script:** "Walk me through it literally. What did you type, what did you run, what appeared on screen?"
- **Wrong answers exist:** "It errored" is not an answer. The literal error text is. Hold for the literal.
- **Utilization variants:**
  - "It just *breaks*" → "Breaks implies something was whole. What's the last whole version — and what's the smallest step between it and now?"
  - "It *freaks out*" → "Show me the freakout. What's the first line of it?"

### G — Ground the expectation
*Recovers: the expectation baseline. Reverses: comparative deletion.*

- **Script:** "What did you expect to see instead — specifically? Not 'the right answer.' What is the right answer, for this input?"
- **Why it's load-bearing:** a surprising number of bugs dissolve here, because the student discovers they never computed the expected output by hand. No expected output, no bug — just an unverified program.
- **Utilization variant:** "It's *worse* now" → "Worse than which version? The one from before lunch, or the one in your head?"

### U — Uncover the boundary
*Recovers: the edge between working and broken. Reverses: universal quantifiers.*

- **Script:** "Has it ever worked — even once, even partially, even for one input? What was different about that run?"
- **This is bisection wearing linguistic clothes.** The one partial success localizes the fault region exactly the way a passing test does.
- **Utilization variant:** "*Nothing* I try works" → "Of everything you tried, which attempt failed most interestingly — failed differently from the others?"

### R — Read the evidence
*Recovers: the observation under the story. Reverses: mind-reading, invented causation.*

- **Script:** "Is that something you observed, or a story about what you observed? What does the compiler literally say? Read it to me."
- **The most common catch:** the student has read the error message zero times and its vibe once.
- **Utilization variant:** "Python doesn't *want* me to do this" → "Fine — then it filed a complaint. Read me the complaint verbatim."

### E — Establish the scope
*Recovers: correct scope. Reverses: catastrophizing a line into an architecture.*

- **Script:** "Is this a line problem or a plan problem? If we fixed only this line, would the plan hold?"
- **Runs in both directions:** it also catches the student patching line 12 for the fourth time when the plan itself is wrong. "You've fixed this line three times. Is the line the problem?"

### Delivery notes that outrank the scripts

- **Tone is curiosity, not cross-examination.** The same five questions delivered as an interrogation teach students to avoid you. You are visibly *interested in the bug*, the way a mechanic is interested in a noise.
- **Hold the silence.** After each question, the pause where you would normally rescue them is where the learning happens. Count to seven if you must.
- **Never answer your own question.** If I stalls completely, the move is to shrink it ("Okay — just the first line of output. What's the first line?"), not to answer it.
- **Match their channel — in the moment, never as a diagnosis.** A student who says "something feels off" gets "what feels wrong, specifically?"; one who says "this doesn't look right" gets "show me where it stops looking right"; one who says "that sounds weird" gets "read it out loud and tell me where it stops sounding right." This is state matching — utilizing the representation their own sentence just revealed — and it is cheap and instantly falsifiable. What it is **not** is classifying anyone as a visual/auditory/kinesthetic *learner*; that trait model failed its empirical tests (Document A, §6) and drifting into it is a framework violation. Match the sentence, never the student.

---

## 3. The Fade Sequence: A Semester Plan

The sequencing rule from Document A — **embody first, name second** — as a week-by-week structure. Phases are elastic; the trigger conditions matter more than the week numbers.

### Phase 1 — Relentless Modeling (≈ weeks 1–4)
- Every single "it's broken," in lab, office hours, and forum posts, gets the same five questions in the same order. No exceptions, no shortcuts, no taxonomy talk.
- You are allowed to be a little boringly predictable. Predictability is the mechanism.
- **Also start every open-loop lesson (§4) now**, narrating I and G out loud on the demo bug, so the questions are heard in two contexts: applied to them and applied by you to yourself.
- **Exit condition:** students start answering G before you ask it ("...and I expected 15, before you ask"). When roughly a third of help interactions show pre-answering, move on.

### Phase 2 — Coaching (≈ weeks 5–6)
- Shift from asking the questions to prompting their self-administration: "You know what I'm going to ask. Go ahead." Then silence.
- In lab, respond to raised hands with "Run the questions first, then call me back if one of them stalls." The stall itself becomes diagnostic information you both use.
- **Exit condition:** students can produce all five answers on prompt, even if they don't yet self-initiate.

### Phase 3 — The Disclosure Event (one session, ≈ week 7)
The reveal lecture. Structure:

1. "You've noticed I ask the same questions every time. You've started answering them before I ask. Here they are, named." Put FIGURE on the board, letter by letter.
2. Name what each move recovers, briefly — this is the only day the taxonomy gets airtime. Include F: "and before any of the five, there's the move you've watched me make when someone says 'I'm just not a programmer' — finding what level the sentence is at."
3. **The transfer frame:** "These aren't my questions anymore. They're yours. From today, the expectation is that you've run them before you ask for help — from me, from each other, or from an AI. A help request that contains the answers is a professional artifact. One that doesn't is a rough draft. And when I say *figure it out*, this is now literally what I'm assigning — six moves, in order, F through E."
4. Hand out the card (Document C). Show the same six moves restructured as a prompt template for AI assistants — same skill, second substrate.
5. Close with the honest pitch: "This is the same reason rubber-duck debugging works. You already do a folk version of this. Now you know which operation each step performs, which means you can do it on purpose."

Disclosed too early, this session is a list to memorize. Disclosed on time, it lands as *recognition* — the difference is the whole design.

### Phase 4 — Articulation & Peer Transfer (weeks 8+)
- **Help-request standard goes live:** office-hours and forum requests are expected to arrive FIGURE-complete. Requests that don't get one response: "Which letter stalled?" — which is itself a diagnostic conversation, not a rejection.
- **Pair debugging protocol:** students run the questions on *each other*, with a hard rule for the questioner: **questions only, no fixes, no hints** — even if you see the bug. Seeing the bug and asking the question that lets your partner see it is the advanced skill. Rotate roles mid-session. (The questioner's card is in Document C.)
- This is the phase where the assessment instrument (Document E) starts collecting data, and where the Socratic agent (Document D) enters as unlimited-rep practice.

### Phase 5 — Exploration (final weeks)
- Students apply FIGURE to problems that aren't bugs: requirements clarification in the capstone, design critiques, their own prompts to AI tools. The claim from Document A — one skill, every substrate — gets tested where they can watch it transfer.

---

## 4. The Open-Loop Lesson Template

One session, three beats. Total added preparation: choosing the right bug, which is the whole art.

**Beat 1 — Open (first 5 minutes).**
Show a broken program, live and real. Apply I and G out loud, narrating: literal output on the board, expected output next to it, visibly mismatched. Walk the isolation *up to the exact point where the answer requires today's concept* — then stop. "We can't do R yet — we can read the message, but we don't have the tool to know what it's evidence *of*. Leave it on the board." It stays visibly unresolved all session.

**Beat 2 — Teach (main block).**
The day's material, framed once — and only once — as "the tool that answers the thing on the board." Resist referencing the loop every ten minutes; the Zeigarnik pull works better unprompted.

**Beat 3 — Close (last 10 minutes).**
Return to the exact program. Apply the new concept. Resolve it — narrating *which letter is doing the work at each step*, because in Phases 1–2 this narration is the modeling and in Phases 3+ it's the articulation.

**Rules for choosing the bug:**
1. It must **genuinely require today's concept** — a bug solvable with last week's tools teaches that the loop is decoration.
2. It must **resolve in the same session.** An open loop that survives the class period doesn't build curiosity; it builds the suspicion that you lost track of it.
3. It should be **plausibly a student's bug** — ideally an anonymized real one from a previous term. Contrived bugs read as contrived within seconds.
4. Keep a **bug ledger**: every semester, harvest the best real student bugs (anonymized, with permission) tagged by module. Two terms in, every session has a battle-tested opener.

---

## 5. Failure Modes

The six ways this framework degrades in practice, and the countermeasure for each.

**1. Level mismatch.** Answering "I'm just not a programmer" with "what does line 12 do" — without the explicit sidestep script — reads as not listening. *Countermeasure:* F is always the first move (§1); the routing table is on your desk until it isn't needed.

**2. Rescuing.** The student stalls on I, the silence gets uncomfortable, and you answer your own question. Every rescue teaches that stalling summons answers. *Countermeasure:* shrink the question instead ("just the first line of output"). The smallest answerable question is always available.

**3. Interrogation drift.** Under time pressure the five questions compress into a rapid-fire checklist and students start experiencing help as a quiz to pass. *Countermeasure:* the tone check is one question you ask yourself — "am I currently interested in this bug?" If not, get interested or hand them the card and come back.

**4. The compliance trap — the failure mode that defeats the entire framework.** Students learn to answer *your* questions fluently while never asking *themselves* anything. They've learned a customer-service script, not a debugging practice. You can't detect this in office hours (where it looks like success); you detect it in the data — help-request quality that's high in your presence and absent from forum posts and agent transcripts. *Countermeasures:* the Phase 2 shift to "you know what I'm going to ask — go ahead" starts the ownership transfer early; the Phase 4 peer protocol forces them into the questioner's seat; and Document E's instrument measures formulation quality in artifacts you're *not present for*, which is where the truth lives.

**5. Premature disclosure.** The taxonomy gets explained in week 2 because a bright student asks, and it becomes trivia instead of recognition. *Countermeasure:* have a holding line ready — "There is a system, and you'll get the whole thing in a few weeks; for now, watch for the pattern." Naming that a pattern *exists* is fine; it's naming its parts early that spends the disclosure event.

**6. Trait drift.** Predicate matching (§2, delivery notes) quietly hardens into "she's a kinesthetic learner" and instruction starts being customized to imaginary types. *Countermeasure:* the rule fits on a sticky note — **match the sentence, never the student.** If you catch yourself remembering a student's "modality" across sessions, you've crossed the line Document A §6 draws.

---

## 6. What Feeds Forward

- **Document C** packages FIGURE as the laminated card, the help-request and AI-prompt templates, the peer questioner's card, and — for the AlgoCratic Futures skin — the same instrument in-universe (Clarification Protocols™, wherein The Algorithm declines to process Improperly Formulated Distress Reports).
- **Document D** specifies the Socratic agent: system prompt = the six moves + the questions-only rule from the pair protocol, running on local infrastructure. It is Phase 4's unlimited-repetition machine.
- **Document E** turns the help-request standard from Phase 4 into a rubric and a semester-long measurement of formulation quality — the evidence layer that makes all of this legible as an instructional intervention rather than a teaching style.
