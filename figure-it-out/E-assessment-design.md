# Measuring Formulation
## Help-Request Quality as an Assessable Artifact

**Document E of 5 — Assessment Design**
*Prerequisites: Documents A–D. This is the evidence layer: it converts "students became more self-reliant" from testimonial into a measured trajectory, and it is the only honest detector of the framework's central failure mode (B §5, the compliance trap).*

---

## 1. The Learning Outcome, Stated for the Record

> **Students will formulate falsifiable problem statements**: given a malfunctioning program, the student produces a help request specifying literal observed behavior, a hand-derived expected result, the boundary of the failure, verbatim evidence, and a justified scope classification.

This wording is deliberately outcome-catalog-ready. It names an observable, gradeable behavior; it contains no references to any framework, lineage, or technique; and it describes a skill with face validity to any technical audience — it is, verbatim, what a good bug ticket contains in industry. FIGURE is *how we teach it*; this outcome is *what we certify*.

## 2. Why the Artifact, Not the Interaction

Office-hours performance cannot be the measure, for a reason B §5 establishes: the compliance trap. A student can learn to answer the instructor's questions fluently — a customer-service script — without ever asking themselves anything. In the instructor's presence this failure is indistinguishable from success. It becomes visible only in artifacts produced when no instructor is in the loop:

- forum help requests,
- office-hours intake forms (filled before the conversation),
- FIGURE-agent transcripts and escalation drafts (Document D),
- optionally, AI-assistant prompts students elect to submit.

The core analytic move of this design is therefore **presence-stratification**: score formulation quality separately for instructor-present and instructor-absent artifacts. Convergence of the two scores over the semester is the signature of internalization. A persistent gap — polished in person, vague alone — is the compliance trap, caught in the act.

## 3. The Rubric

Six criteria, one per FIGURE letter, each scored 0 / 1 / 2. Maximum 12. Anchors are written so two raters reading the same artifact should land on the same score without discussion.

| Criterion | 0 | 1 | 2 |
|---|---|---|---|
| **F — Level** | Statement is about the self, not the program ("I can't do this," "I'm hopeless at loops") | Mixed: reaches program behavior but wrapped in self-assessment | Cleanly at behavior level: a program, an action, an observable event |
| **I — Isolation** | Paraphrase only ("it breaks," "it errors," "wrong output") | Partial literals: output but no input, or error name without text | Literal input, literal command/run context, and verbatim output or complete error text |
| **G — Grounding** | Expected result absent or vacuous ("the right answer," "it should work") | Expected result stated but not derived (no source, not computed) | Specific expected output for the stated input, with derivation ("by hand," "per the spec," "from the worked example") |
| **U — Boundary** | No working/broken boundary attempted | "It worked before" without the delta, or "never worked" without the closest approach | Closest working state identified *and* the delta since ("worked for single-digit inputs; broke when I added the negative-number branch") |
| **R — Evidence** | Narrative causation or mind-reading ("Python doesn't like my import," "the compiler is being weird") | Evidence partially engaged: message mentioned or excerpted, theory still story-shaped | Verbatim evidence quoted *and* the stated theory cites an observation, not a vibe |
| **E — Scope** | No scope classification | Scope asserted without support ("it's probably the whole design") | Line-level vs. plan-level classification with at least one observed fact in support |

**Scoring notes.** Score what is present in the artifact, not what emerged later in conversation. An explicitly marked stall ("THE STALL: I couldn't finish G because I don't know what the spec requires for empty input") scores the *1* for that criterion, not the 0 — naming precisely where formulation failed is itself formulation skill, and the rubric must never punish honest stall-marking, or students will learn to pad instead. Artifacts from the agent's escalation path (D §3, rule 9) arrive pre-structured in rubric order and are the cheapest artifacts to score.

## 4. Why This Rubric Resists Goodhart

Any measured target invites gaming, so name the gaming and check the damage:

- **Template-filling is not free.** You cannot produce a verbatim error message without reading the error message. You cannot state a hand-derived expected output without deriving it. You cannot identify the delta since the last working state without reconstructing your own change history. Five of the six criteria can only be satisfied by *performing the debugging work the rubric exists to induce.* A student who "games" this rubric by mechanically filling every field has executed the FIGURE procedure — which is the desired outcome wearing a cynical expression. We can live with that.
- **The residual gaming surface** is E (a scope classification can be asserted glibly) and hollow copy-paste (dumping 200 lines of log as "verbatim evidence"). Both are visible to a rater in seconds and are handled in the anchors (E requires a supporting observation; R requires the *relevant* message, and excess dumping without engagement scores 1).
- **Keep stakes low anyway** (§5). Goodhart pressure scales with stakes; this design deliberately keeps them minimal.

## 5. Grading Integration: Low Stakes, High Visibility

- **Weight:** a small professionalism/participation slice of the course grade — enough that FIGURE-completeness is a norm, not enough that a weak request is a crisis. This is a formative instrument that happens to produce summative-grade garnish, not the reverse.
- **Grade the trajectory, not the snapshot.** Improvement from a student's own baseline weighs more than absolute score. This protects students who arrive weakest at formulation — precisely the students the framework exists for — from being penalized for their starting point.
- **Required submissions solve the selection problem.** If only spontaneous help requests are scored, the sample is students-who-ask, which both misses the silent strugglers and lets students dodge measurement by not asking. Fix: each student submits a fixed number of FIGURE-complete requests per module (two is plenty) about a real difficulty they hit — *including ones they subsequently solved themselves.* That last clause matters; see §7.

## 6. Data Sources, Consent, and Handling

| Source | Presence stratum | Notes |
|---|---|---|
| Forum help requests | Absent | Primary longitudinal source; timestamped, natural |
| Office-hours intake forms (C2 / CP-6/F) | Absent-then-present | Form is completed before the conversation: score the form as an absent artifact |
| FIGURE-agent transcripts & escalation drafts | Absent | Richest source; drafts arrive pre-structured (D §3) |
| Required per-module submissions | Absent | Solves selection bias (§5) |
| Instructor observation during help sessions | Present | Scored impressionistically for the stratification comparison only |

**Handling:** all sources live on institutional systems (LMS, local agent infrastructure — D §7), so no student work leaves the building. The syllabus discloses plainly that help requests and agent transcripts are reviewed for course improvement and count toward the professionalism component; the agent's first message repeats it. Retention follows the institution's ordinary student-work schedule. **The IRB line:** as internal course assessment, this is ordinary instructional practice. The moment it becomes a conference talk or SoTL publication with student data, it is human-subjects research — file *before* the semester whose data you intend to use, because retroactive approval is not a thing.

## 7. The Withdrawn-Ticket Rate: The Framework's Cleanest Signal

The most elegant success mode of the entire framework is the help request **abandoned mid-formulation because formulating it solved it** — "never mind, found it while filling out Field G." This is the self-explanation effect caught on camera, and it should be instrumented, not just savored:

- The **agent logs it precisely**: sessions that reach the win condition (student states cause + names a test) without escalation are exactly this event, timestamped.
- The **intake form and CP-6/F carry a voluntary checkbox**: ☐ *resolved during filing — submitting anyway for the record* (the AlgoCratic version of this checkbox writes itself, and the Bureau "counts these as its finest work").
- The **required per-module submissions** (§5) capture the forum-draft version that analytics can't see: since students must submit requests even for self-solved problems, the self-solve annotation comes to you.

**Metric:** withdrawn-ticket rate = self-resolved-during-formulation / all formulation events. Expected trajectory: near zero in weeks 1–2, climbing after the Phase 3 disclosure. This number is the single best one-line answer to "did teaching them to ask questions make them need us less?"

## 8. The Measurement Calendar

| Window | What's collected | What it establishes |
|---|---|---|
| Weeks 1–2 | All natural help requests, scored | Baseline formulation quality (modeling has begun but cannot yet have compounded) |
| Weeks 5–6 (pre-disclosure) | Same + intake forms | Effect of pure modeling — the embodiment phase, before students have the taxonomy |
| Weeks 8–10 (post-disclosure) | All sources incl. agent | Effect of disclosure + ownership transfer; presence-stratification begins in earnest |
| Final weeks | All sources | End-state; per-student trajectories close |

**Reported at semester end (the dean-facing packet):** (1) median rubric score by window — the trend line; (2) the presence-stratified comparison — the internalization signature; (3) withdrawn-ticket rate over time — the self-reliance headline; (4) office-hours efficiency — median minutes per resolved issue, which should fall as requests arrive pre-formulated, converting instructor time from information-recovery to actual teaching. Four charts, no testimonials required.

## 9. Validity Threats, Honestly Listed

- **Rater drift.** One instructor scoring 200 artifacts drifts. Mitigation: the anchors above, plus a second rater on a 10% sample each window with disagreements reconciled against the anchors.
- **Novelty effect.** First-semester gains may partly reflect enthusiasm (the instructor's more than the students'). Mitigation: run at least two semesters before strong claims; the second cohort is the honest one.
- **Maturation confound.** Students improve at everything across a semester. Mitigation: the presence-stratified *gap closure* and the withdrawn-ticket rate are FIGURE-specific signatures that generic maturation doesn't produce; lean on those, not raw score growth.
- **Instructor as instrument.** The person teaching the framework is scoring its success. Mitigation: the second-rater sample; artifact-based scoring (the artifacts exist independently and can be re-scored by anyone, later, blind).
- **What this design cannot claim:** that FIGURE beats an alternative intervention. There is no control section. It measures whether the outcome in §1 was achieved and internalized — an assessment claim, not a causal-superiority claim. Say exactly that, and no dean or accreditor will catch you overreaching.

---

*This completes the five-document core. The packaging layer (audience-specific briefs) draws its evidence claims from this document and its cost/privacy claims from Document D.*
