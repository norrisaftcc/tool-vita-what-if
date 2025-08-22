---
marp: true
theme: default
paginate: true
backgroundColor: #0A0A0B
color: #F3F4F6
style: |
  /* VITA Dark Theme - Embedded */
  :root {
    --bg-primary: #0A0A0B;
    --bg-secondary: #141416;
    --vita-purple: #8B5CF6;
    --vita-purple-light: #A78BFA;
    --accent-cyan: #06B6D4;
    --accent-emerald: #10B981;
    --accent-amber: #F59E0B;
    --accent-rose: #F43F5E;
  }
  
  section {
    background: linear-gradient(135deg, #0A0A0B 0%, #141416 100%);
    color: #F3F4F6;
    font-family: 'Inter', -apple-system, sans-serif;
    justify-content: start;
  }
  
  h1 {
    color: #8B5CF6;
    font-size: 2.5em;
    font-weight: 800;
  }
  
  h2 {
    color: #A78BFA;
    font-size: 1.8em;
  }
  
  h3 {
    color: #06B6D4;
  }
  
  strong {
    color: #A78BFA;
  }
  
  code {
    background: rgba(139, 92, 246, 0.1);
    color: #06B6D4;
    padding: 0.2em 0.4em;
    border-radius: 4px;
  }
  
  pre {
    background: rgba(20, 20, 22, 0.8);
    border: 1px solid rgba(139, 92, 246, 0.3);
    border-radius: 8px;
    padding: 1em;
    color: #A78BFA;
  }
  
  table {
    border-collapse: collapse;
    width: 100%;
    margin: 1em 0;
  }
  
  th {
    background: rgba(139, 92, 246, 0.3);
    color: #F3F4F6;
    padding: 0.75em;
    border: 1px solid #8B5CF6;
    text-align: left;
    font-weight: 600;
  }
  
  td {
    padding: 0.75em;
    border: 1px solid rgba(139, 92, 246, 0.2);
    color: #F3F4F6;
    background: rgba(20, 20, 22, 0.5);
  }
  
  tr:hover td {
    background: rgba(139, 92, 246, 0.1);
  }
  
  blockquote {
    border-left: 4px solid #8B5CF6;
    background: rgba(139, 92, 246, 0.05);
    padding: 1em;
    margin: 1em 0;
    color: #F3F4F6;
  }
  
  /* ASCII art glow */
  pre.language-text {
    color: #A78BFA;
    text-shadow: 0 0 10px rgba(139, 92, 246, 0.5);
  }
  
  /* Links */
  a {
    color: #06B6D4;
  }
  
  /* Lists */
  ul, ol {
    color: #D1D5DB;
  }
  
  /* Impact slides */
  section.lead h1 {
    text-align: center;
    font-size: 4em;
  }
  
  section.lead h2 {
    text-align: center;
    color: #D1D5DB;
  }
---

<!-- _class: lead -->

## Tools Team -> Creating a Virtual TA

### and chipping a piece off of [The Monolith]

#### (by learning to build our own AI agent)




**VITA Project**  
*VIrtual Teaching Assistant*

---

<!-- _class: lead -->

![height:600px](image1.png)


---


![width:900px](image2.png)

---
## Life with [The Monolith]

> *"I spent 3 hours debugging a hierarchical menu. ChatGPT gave me 6 'fixes' - none worked. I don't even know what questions to ask anymore."*

**— Sarah, CTI 110 Student, 2:47 AM (AI Generated)**

This is why we are building VITA.

---
## We Need to Talk about [The Monolith]

### Industry Has Already Moved:
- **51%** of companies use multiple AI agents in production
- **$140K+** salaries for multi-agent specialists  
- **78%** of employers need orchestration skills NOW

### That $15,000 Gap Means:
- **$315/month** — A reliable car vs. the bus
- **$1,250/month** — Your own place vs. roommates forever  
- **3 years faster** — Student loans paid off
- The difference between surviving and **thriving**

### Education Is Still Dealing with [The Monolith]:
- Teaching single-tool usage, or worse
- "Just use [The Monolith]" (or "Don't use [it]")
- No evaluation or selection skills by model or platform

---

```text
                              ╔══════════════════╗
                              ║                  ║
                              ║   THE MONOLITH   ║
                              ║    (One AI for   ║
                              ║    Everything)   ║
                              ║                  ║
                              ╚════════╤═════════╝
                                       │
                ┌──────────────────────┼──────────────────────┐
                │                      │                      │
                ▼                      ▼                      ▼
         "Help me debug"        "Plan a party"         "Write my essay"
              👨‍🎓                    👩‍🎓                    🧑‍🎓
           Student A             Student B             Student C
        
        ❌ No skill differentiation
        ❌ No tool specialization  
        ❌ Black box dependency
        ❌ Faculty can't verify learning
```

---

## Universal Fears

**Students:** *"Will AI replace me?"* 

**Faculty:** *"Are they learning or copying?"*

**Employers:** *"They can't choose appropriate tools"*



> "What if AI didn't replace students... but trained them?"
> Turn the "AI tool user" into an "AI agent manager"
> This starts with *one agent*, VITA.

---
```text
     ┌─────────────┐  ┌─────────────┐  ┌─────────────┐  ┌─────────────┐
     │    VITA     │  │   GitHub    │  │   Research  │  │    Flash    │
     │  Debugging  │  │   Copilot   │  │    Agent    │  │     LLM     │
     │   Partner   │  │   Coding    │  │  Academic   │  │   Social    │
     └──────┬──────┘  └──────┬──────┘  └──────┬──────┘  └──────┬──────┘
            │                │                │                │
     ┌──────▼─────────────────▼─────────────────▼─────────────────▼─────-─┐
     │                                                                    │
     │                      STUDENT AS AI AGENT MANAGER                   │
     │                                                                    │
     │    "I need to debug" ──────► VITA                                  │
     │    "I need to implement" ───► GH Copilot / Claude Code             │
     │    "I need to research" ────► Research Agent                       │
     │    "I need to plan" ────────► General LLM                          │
     │                                                                    │
     └────────────────────────────────────────────────────────────────────┘
     
     ✅ Develops discrimination skills
     ✅ Matches industry practice (51% companies use multiple agents)
     ✅ Transparent, specialized tools
     ✅ Faculty can verify domain-specific learning
```

---

### FROM: One tool for everything
### TO: Right tool for each task
### Student Becomes: 
- "Manager" of their AI agents
- Training in working through iterative workflow (Scrum/Agile)
- Learning through "progressive overload" (mental workout)
- Growth mindset installed naturally ("what else does the agent need from me?")

> The journey begins with VITA, your "growth mindset" TA.
> It continues through their *AI-required* capstone software project.

---

## Growth Mindset Case Studies in CS
- (on request)


### VITA's Approach is Aligned:

**VITA as Your Cognitive Personal Trainer:**

**Traditional TA:** *"Your null pointer is on line 47. Fix it."*  
**VITA:** *"I see an error on line 47. What do you think might cause a 'null pointer exception'? Let's trace through this together."*

- Productive, iterative struggle with support
- Complete data sovereignty (on-premise)
- **Result:** Students learn to debug methodically, not just fix one error

---

## The Student Journey: Without vs With VITA

```text
         WITHOUT VITA                    WITH VITA
        "The Struggle Maze"           "The Guided Path"
        
    ERROR → GOOGLE → CONFUSION      ERROR → VITA → CONTEXT
      ↓        ↓         ↓             ↓       ↓        ↓
    FORUMS  OVERFLOW  CHATGPT      ANALYSIS SOLUTION LEARNING
      ↓        ↓         ↓             ↓       ↓        ↓  
    COPY → PASTE → FAIL → REPEAT    UNDERSTAND → FIX → GROW
    
    Time: 3+ HOURS                  Time: 15 MINUTES
    Result: Frustrated               Result: Empowered
    Skill: Copy/Paste               Skill: Debug Mastery
```

---
```text
    CURRENT STATE                    VITA PHASE 1                    FUTURE STATE
    Fall 2025                                        
    
    ╔═══════════╗                   ╔═══════════╗                  ╔═══╗ ╔═══╗
    ║           ║                   ║           ║                  ║ V ║ ║ T ║
    ║           ║                   ║           ║      ┌────►      ║ I ║ ║ O ║
    ║ MONOLITH  ║      ──────►      ║ MONOLITH  ║      │           ║ T ║ ║ O ║
    ║           ║                   ║           ║      │           ║ A ║ ║ L ║
    ║           ║                   ╚═══════════╝      │           ╚═══╝ ╚═══╝
    ╚═══════════╝                          +           │           ╔═══╗ ╔═══╗
         ▲                           ╔═══════════╗     │           ║ R ║ ║ E ║
         │                           ║   VITA    ║─────┘           ║ A ║ ║ T ║
    All queries                      ║ Debugging ║                 ║ G ║ ║ C ║
                                     ╚═══════════╝                 ╚═══╝ ╚═══╝
```

### Phase 1 (Proposed):
- Single debugging agent (VITA)
- Prove the concept
- Break a little piece off of [The Monolith]

---

### Data Sovereignty Comparison

**❌ CURRENT RISK**
Student Data → THE MONOLITH (External Cloud) → Unknown Storage
"We don't know where it goes"

**✅ VITA SOLUTION**
Student Data → LOCAL VITA SERVER → 100% On-Campus
FERPA Compliant • IT Controlled

---

<!-- _class: lead -->

## Our Journey
**From Educators to Developers**

**November 2023 - Present**
- **David Teter**: Tools Group Manager
- **Mallory Milstead**: Lead VITA Developer
- **Brittany Smith**: Developer
- **Hana Seidi**: Product Owner / Pedagogy Lead
- **Anthony Cameron**: AI Policy Alignment
- **Drew Norris**: Project Manager / Scrum Master

---

## The Problem Was Real

| Model    | Success Rate | Key Failure |
|----------|-------------|-------------|
| GPT-3.5  | 8/15 | Wrong error explanations       |
| Zephyr-7B| 6/15 | Used concepts not yet taught   |
| CodeLlama| 4/15 | Provided answers, not guidance |

### Critical Finding:
> "2023 Models gave students incorrect debugging information 50% of the time"

---

## The Paradigm Shift

### Our Breakthrough:
- Design the right tool for the job
- Find the sweet spot between "helpful debugger" and "does all the work"
- Pair programming skills reframed as AI "personal trainer"

### Philosophy:
> Agent: "What do you think we should try next?"

---

## Building Through Scrum

### Our Team = Our Method:
- **Sprints** = Learning cycles
- **User stories** = Student needs
- **Daily standups** = Reflection
- **Retrospectives** = Improvement

### Key Pivot (June 2025):
- Removed Autogen framework
- Moved to Ollama *single-agent* MVP
- This wasn't failure - it was learning

---

## Current System Architecture

```text
Student Input → VITA Client → Ollama (Local) → Debugging Support
                    ↑                              ↓
                Feedback ←─────────────────── Guided Learning
```

### Proven Components:
- ✅ Local Ollama deployment
- ✅ Panel UI functioning
- ✅ OAuth authentication
- ✅ Instructor materials 

---

## Future Architecture (Proposed for 2026 SU Dev Sprint)

```text
Student → VITA Orchestrator → [Debugging Agent]
                            → [Code Analysis Agent]  
                            → [Pattern Recognition]
                            → [GitHub Verification*]
                           
*GitHub integration planned for Fall 2026
```

### Note on GitHub:
- Concept proven in testing
- Integration planned post-pilot
- Will provide portfolio verification
---

### Technical Proof:
- Local models can provide quality help as of 2025
- Complete data sovereignty achievable
- Educators can build production software

### Educational Proof:
- Iterative development works
- Scrum methodology maps directly to workforce needs
- "Break Up The Monolith" concept viable

### Ready to Deploy:
- Working single-agent prototype
- Ollama server: ready for further testing

---

<!-- _class: lead -->

## Next Steps

### Is VITA Ready for Action?

**(Live Demo)**

> M. Milstead, VITA Lead Dev

---
### Student Outcome Metrics:
- Reflection survey
- In-tool feedback (helpful yes/no)
- Assignment completion / Retention

### Faculty Benefit Metrics:
- Reduced "syntax error" office hours
- More conceptual teaching time
- Student question quality improved

### Technical Performance Metrics:
- System reliability
- Response time
- Resource usage

---

## The Ask We Already Got:

### Infrastructure:
- *magnamater* inference server (NOW LIVE)
- IT support (Thanks Mike!)

### People:
- 2-3 faculty champions (CTI 110 stakeholders are IN)
- IT liaison (already on task)
- Admin sponsor (Thanks for coming today!)


---
## The *Real* Ask:

### *Understanding* The Tools Team as:
- Platform Team (see *Team Topologies*)
- A stream-aligned continuous-delivery team
- For sponsors and shareholders to work within our process

### *Discussion* of How to Integrate the Tools Team

### *Funding* for VITA development sprints, Summer 2026
- Existing outlay: 50% hardware (minimal salary costs)
- Full-time instructors are already fully loaded for 25FA/26SP
---

## Three Opportunities

### 1. Join the Pioneer Cohort
"Can we fund VITA development for (May/June/July) 2026?"

### 2. Champion Innovation
"Who are your champions of the **Tools Team Platform**?"

### 3. Define Success Together
"Does *continuous value delivery* matter to you?"
"What metrics matter most to you?"


---

## Your Next Actions

### Before You Leave:
☐ Establish consensus on Agile stream-aligned platform team existence
☐ Confirm 26SU interest for VITA (yes/no)


### Contact:
**David:** teterd@faytechcc.edu     - Tools Team Manager
**Drew:** norrisa@faytechcc.edu     - Platform  & Architecture  




---
## Industry Validation for Our Approach

**IBM:** Agentic AI certificates

**CrewAI:** 100,000+ certified

**Microsoft:** 890,000+ AutoGen downloads

> Multi-agent AI orchestration isn't the future anymore. It's today.
> VITA starts us down the path to tomorrow.

---

## Skill Development Progression

### Traditional Approach:
Semester 1 → "Just Google it" 
Semester 4 → "Just ask ChatGPT"
**Result: No skill progression**

### VITA + Scrum Capstone Approach:
**Semester 1:** Learn Debugging with VITA
**Semester 2:** Add GitHub Codespaces, multi-agent coordination (VITA/GH Copilot)
**Semester 3:** Master Industry Patterns (Scrum/GitHub process)
**Semester 4:** GH Porfolio + "1 year, Agent Manager" → **clear potential**

---

## The Bottom Line

### Industry Reality:
- **51%** already using multi-agent systems
- **170 million** new AI jobs coming
- **Stream-aligned Teams** providing CI/CD are becoming more prevalent

### VITA Readiness:
- **1** prototype developed using industry best practices
- **3** successful pivots
- **100%** local data sovereignty

> Questions? Comments?

---

## The Vision

**Imagine Spring 2027:**

Your students aren't asking *"How do I fix this?"*  
They're asking *"Which agent should I deploy for this?"*

They're not copying from Stack Overflow.  
They're orchestrating AI teams like conductors.

They're not graduating with fear of replacement.  
They're graduating as **the managers of tomorrow's AI workforce.**

**We're not just debugging code.**  
**We're debugging the future of CS education.**

*One student. One agent. One transformation at a time.*

> **The question isn't if this future will happen.**
> **It's whether your students will lead it.**
> 