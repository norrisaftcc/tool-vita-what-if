# FIGURE: Recovering the Deleted Problem
## A Convergent-Lineage Framework for Teaching Problem Formulation

**Document A of 5 — Theory Foundation & Lineage Map**
*Companion documents: B (Instructor Practice Guide), C (Student Artifacts), D (Socratic Agent Specification), E (Assessment Rubric)*

---

## 1. What This Framework Is

A student who says "my code doesn't work" has not described a bug. They have produced a maximally compressed linguistic object with nearly all diagnostic information removed. The framework in this document treats **problem formulation as an information-recovery task**: a small, fixed set of precision moves that reverse specific, nameable compression operations in the student's own statement of the problem.

The claim is stronger than analogy. Scientific-method debugging (hypothesize → isolate → test → falsify) and precision questioning of a vague problem statement are the same algorithm running on two substrates — one operates on code, the other on the sentence describing the code. Teach the questioning algorithm explicitly and students acquire a portable problem-formulation skill that works on bugs, on math problems, on design problems, and — critically for CSC 114 — on prompts to AI systems, which cannot mind-read deletions any better than an instructor can.

## 2. The Name

The framework is called **FIGURE**. Six letters, six moves, in mandatory order:

| Letter | Move | Recovers |
|---|---|---|
| **F** | **Find the level** | Whether the statement is about a behavior, a capability, a belief, or an identity — and walks it down to behavior, the only level where precision questions work |
| **I** | **Isolate what happens** | The literal symptom: actual input, actual output, first line of the actual error |
| **G** | **Ground the expectation** | The comparison baseline: the specific expected output, computed by hand |
| **U** | **Uncover the boundary** | The edge between working and broken: the closest run that succeeded, and what was different |
| **R** | **Read the evidence** | The observation underneath the story: what the message literally says |
| **E** | **Establish the scope** | Whether this is a line problem or a plan problem |

The name is doing deliberate work. "Figure it out" is, unadorned, the most dismissive sentence in education — it names a destination and withholds the vehicle. Under this framework it becomes a literal instruction: six specific moves, in order, each with a checkable output. When an instructor who has taught FIGURE says "figure it out," they are assigning a procedure, not withdrawing help. The acronym also hard-codes the sequencing rule that field practice demands (Document B, §1): level detection is the first letter because it must be the first move.

A second benefit: with a name of our own, this document no longer needs to hedge around a name we've declined. The lineage speaks for itself below.

## 3. Why We Name No School

The precision-questioning techniques here were systematized in the 1970s by a therapy-adjacent community whose brand name has since become unusable — partly through commercial abuse of the label (the same fate that befell "agile"), partly through genuinely unsupported claims that grew up alongside the supported ones. Even the original developers have largely abandoned the label. We do the same, for a better reason than reputation management:

**Every technique FIGURE retains was independently derived by researchers with no connection to that community.** When two or more unconnected lineages converge on the same move, the move is probably tracking something real about cognition rather than something idiosyncratic about one school. So we cite the convergent lineage, adopt its terminology where it exists, and treat the 1970s systematization as one historical thread among several — useful for its completeness, not authoritative for its provenance.

## 4. The Two Admission Filters

A technique enters this framework only if it passes both tests:

**Filter 1 — The Disclosure Test.** Explaining the technique to the student must strengthen its effect, not destroy it. "Here are the six moves that dissolve any bug report" makes the tool *more* powerful in the student's hands. Contrast covert persuasion techniques, which collapse when named. This is the ethical boundary between engineering and manipulation, and it is also a practical boundary: our explicit goal is that students run these operations on themselves, which requires full disclosure by design.

**Filter 2 — The Convergent-Lineage Test.** The technique must have at least one independent derivation in mainstream cognitive science, learning science, mathematics education, or linguistics. Techniques that exist only within the single 1970s lineage do not enter, regardless of anecdotal appeal.

## 5. The Lineage Map

The core reference table. Left column: the operation as we will teach it. Middle: the independent academic derivations we cite. Right: the 1970s-lineage parallel, recorded for intellectual honesty and for readers who arrive from that literature.

| Framework operation | Independent lineage (what we cite) | 1970s-lineage parallel (noted, not cited) |
|---|---|---|
| **Precision questions** that recover deleted specifics from a vague problem statement (the I and G moves) | **Polya, *How to Solve It* (1945)** — "What is the unknown? What are the data? What is the condition?" Thirty years prior, zero clinical framing, aimed squarely at teaching problem-solving. | The Meta-Model's deletion challenges |
| **The compression premise** — every problem statement omits, generalizes, and distorts the underlying experience | **Korzybski (1933)** — the map is not the territory; abstraction necessarily deletes. **Grice (1975)** — cooperative speakers systematically omit what they assume is shared; a vague bug report is a Gricean failure of the maxims of quantity and manner. | Deep structure / surface structure framing |
| **Boundary-hunting on universals** (the U move: "It *never* works" → "What was different the one time it came closest?") | **Scientific method itself** — a universal claim is falsified by one counterexample; the counterexample localizes the fault. Also standard fault-isolation practice in engineering (bisection, differential diagnosis). | Universal quantifier challenges |
| **Observation vs. story discrimination** (the R move: "The compiler hates this" → "What does it literally say?") | **Attribution theory (Weiner)** — distinguishing observed events from causal narratives about them; **basic empiricism** as taught in any lab science. | Mind-reading and cause-effect challenges |
| **Model relentlessly, then disclose the taxonomy** — instructor asks the same fixed questions for weeks before naming the system | **Cognitive apprenticeship (Collins, Brown & Newman, 1989)** — modeling → coaching → scaffolding → articulation → reflection → exploration, in that order. **Scaffolding and fading (Wood, Bruner & Ross, 1976)**; Vygotsky's zone of proximal development. | "Installation" through repetition before conscious framing |
| **Utilization — debug inside the student's own metaphor** ("I'm stuck" → "Where were you last moving?") | **Lakoff & Johnson (1980)** — abstract reasoning runs on conceptual metaphor; the student's metaphor *is* their working representation, so operating within it is operating on the actual representation rather than demanding a costly translation first. Constructivist learning theory makes the same demand: begin from the learner's existing model. | Ericksonian utilization |
| **Momentary predicate matching** — a special case of utilization: the student who says "something feels off" gets "what feels wrong, specifically?"; the one who says "this doesn't look right" gets "show me where it stops looking right" | Same basis as utilization above: the student's sensory predicates reveal the representation active *in this sentence*, and matching it removes a translation cost. The claim is deliberately small — **state, not trait** (see §6 for the distinction and the exclusion it implies). Relatedly, a student's request for an analogy is a request for a structural mapping, and **analogical encoding (Gentner)** is among the best-supported moves in learning science; **dual coding (Paivio)** supports multi-modal presentation for everyone, no diagnosis required. | Predicate matching / representational systems |
| **The open-loop lesson** — pose an unresolved concrete problem, teach the concept, resolve the problem with it | **Loewenstein's information-gap theory of curiosity (1994)**; problem-based learning; the Zeigarnik effect (unresolved tasks hold attention). | Nested-loop story structure |
| **The FIGURE card** as a fixed, memorizable checklist | **Cognitive load theory (Sweller)** — a vague bug is an unstructured search space; a fixed checklist collapses it. **Gawande's checklist findings** in high-stakes fields. **Self-explanation effect (Chi et al., 1989)** — articulating a problem precisely to a passive listener produces the recovery on its own; FIGURE names *which* operation each articulation step performs, making a folk technique (rubber-duck debugging) teachable. | The Meta-Model as a complete, closed question set |
| **Level detection** (the F move) — classifying a stuck statement by its abstraction level (behavior / capability / belief / identity) before choosing a question | **Attribution theory and attributional retraining** — "the loop is broken" vs. "I'm not a programmer" require different interventions; **Dweck's mindset research** addresses exactly the belief/identity levels; **SOLO taxonomy** for structural abstraction levels. *This is the framework's weakest convergence* — the specific level stack comes from Dilts, and we keep his name attached. It passes Filter 1 cleanly and maps onto attribution research well enough to pass Filter 2, but instructors should treat it as a diagnostic heuristic, not a validated model. | Dilts's Logical Levels (retained by name) |
| **Motivation through competence and autonomy, not exhortation** | **Self-determination theory (Deci & Ryan)** — the open-loop structure and self-administered questions supply autonomy and competence directly; no inspirational overhead required. | (No direct parallel — this is a guardrail against the lineage's motivational-speaking drift) |

## 6. What the Filters Exclude — and One Near-Miss Worth Getting Exactly Right

Techniques from the 1970s lineage that **do not enter**: eye-accessing cues (failed replication); **submodality change work** — manipulating the qualities of an imagined scene (brightness, distance, size) as an intervention on emotional response — which has no independent derivation and is clinical in framing; and "rapport through covert mirroring," which fails the disclosure test in its covert form (its overt cousin, utilization, is retained).

Also excluded, from *outside* the 1970s lineage but frequently confused with the predicate-matching row above: **the trait model of sensory learning styles** — diagnosing a student as a visual, auditory, or kinesthetic *learner* and delivering instruction in the matched channel. This "meshing hypothesis" is enormously popular and has repeatedly failed careful empirical tests (the canonical review is Pashler, McDaniel, Rohrer & Bjork, 2008, which found no adequate evidence despite the theory's ubiquity).

The distinction that keeps predicate matching in while keeping learning styles out is **state versus trait**:

- *State matching* responds to the representation the student's own sentence reveals is active right now. It is fully disclosed, costs nothing, requires no classification of the student, and is falsifiable in the small — the question either lands or it doesn't, and you find out in seconds.
- *Trait matching* classifies the student as a modality type and commits instruction to that channel. It is a standing diagnosis, expensive to maintain, unfalsifiable in the moment, and empirically unsupported.

An instructor's field observation that "what feels wrong?" lands better with a student who just said "something feels off" is real, and it is evidence for state matching — not for the trait theory that usually gets cited to explain it. FIGURE keeps the practice and corrects the paperwork.

CSC 114 is a programming course; every retained technique must be defensible as instructional design and nothing else.

## 7. The Second Substrate: AI Assistants

The framework's most current justification requires no historical argument at all.

A large language model cannot recover what a prompt deletes. "Fix my code" fails for precisely the same linguistic reason "it's broken" fails in office hours: the diagnostic information — literal input, literal output, expected output, what changed, what's been tried — has been compressed out of the request. The moves students learn for self-debugging are, without modification, the structure of an effective technical prompt: a FIGURE-complete request is a good prompt by construction.

This unifies two curricular obligations under one skill:

1. **Self-reliant debugging** — run FIGURE on yourself before seeking help.
2. **Effective AI collaboration** — run FIGURE on yourself before prompting, because the model is a rubber duck that talks back, and it talks back better in proportion to what you recover first.

Framing matters here: we are not teaching "prompt engineering tips" as a bolt-on. We are teaching problem formulation once, and demonstrating that it transfers across every helper the student will ever consult — instructor, peer, search engine, or model. That transfer claim is the whole point of the framework.

## 8. The Central Design Principle

Everything in Documents B through E follows from one sequencing rule, borrowed directly from cognitive apprenticeship:

> **Embody first, name second.** The instructor models the fixed question set relentlessly and identically for weeks. Only when students begin pre-answering the questions — evidence the pattern is load-bearing — is the taxonomy disclosed and handed over. Disclosed too early, it is an abstract list to memorize. Disclosed on time, it is a name for something the student already does, and the disclosure lands as recognition and transfer of ownership.

The end state is a student who, staring at a broken program, hears the six moves in their own voice — and who writes help requests (to humans or to models) that already contain the answers.

## 9. Scope and Honest Limits

- FIGURE improves **problem formulation**, not domain knowledge. A perfectly formulated question about recursion still requires the student to learn recursion. The claim is that formulation quality gates everything downstream — help-seeking, self-debugging, and AI use — not that it replaces content.
- The level-detection component (F; Dilts) is a practitioner heuristic with partial academic convergence, flagged as such above and in Document B. Use it as a routing device for choosing questions, not as a theory of mind.
- Predicate matching (§5) is admitted only in its state form; any drift toward classifying students by modality re-imports the excluded trait theory and should be treated as a framework violation.
- Effect claims should be made through the assessment instrument (Document E: help-request quality as a measurable artifact across the semester), not through testimonial. The framework earns its place in the syllabus the same way any instructional intervention does.

---

*Next: Document B — the instructor practice guide: the F move, the IGURE question scripts, the fade sequence week by week, the open-loop lesson template, and failure modes.*
