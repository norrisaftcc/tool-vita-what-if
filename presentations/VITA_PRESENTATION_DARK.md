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

## Creating a Virtual TA

### (by learning to build our own AI agent)




**VITA Project**  
*VIrtual Teaching Assistant*

---

<!-- _class: lead -->

## The Reason We're All Here

**The CP&D Tools Team:**
- David Teter: Tools Team Manager, CP&D Chair
- Mallory Milstead: Lead Developer, VITA
- Brittany Smith: Developer (multiple tools)
- Hana Seidi: Product Owner (pedagogical methods)
- Anthony Cameron: Product Owner (institutional AI policy alignment)

>Our aim: To be, rather than to seem.

---
## We Need to Talk about [The Monolith]

### Industry Has Already Moved:
- **51%** of companies use multiple AI agents in production
- **$140K+** salaries for multi-agent specialists  
- **78%** of employers need orchestration skills NOW

### Education Is Still Catching Up:
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



> Our Perspective: Turn the "AI tool user" into a "AI agent manager"
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
- Cognitive "personal trainer" for debugging
- Productive, iterative struggle with support
- Complete data sovereignty (on-premise)

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
- ✅ Instructor corpus integration in progress

---

### Technical Proof:
- Local models can provide quality help as of 2025
- Complete data sovereignty achievable
- Educators can build production software

### Educational Proof:
- Iterative development works
- Scrum methodology transfers to EdTech
- "Break Up The Monolith" concept viable

### Ready to Deploy:
- Working single-agent prototype
- Ollama server: ready for further testing

---

<!-- _class: lead -->

## Next Steps

### Is VITA Ready for Action?
### (Live Demo)

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

## There's No Ask Yet

### Infrastructure:
- *magnamater* inference server (NOW LIVE)
- IT support (Thanks Mike!)

### People:
- 2-3 faculty champions (CTI 110 stakeholders are IN)
- IT liaison (already on task)
- Admin sponsor (Thanks for coming today!)


---

## Three Decisions Needed

### 1. Continued Development
"Can we fund VITA development for 2025SU?"

### 2. Team Formation
"Who are your champions?"

### 3. Success Definition
"What metrics matter most to you?"


---

## Your Next Actions

### Before You Leave:
☐ Contact information (on request) 
☐ Confirm 25SU interest (yes/no)


### Contact:
**David:** teterd@faytechcc.edu - Tools Team Manager
**Drew:** norrisa@faytechcc.edu     - Platform  & Architecture  




---
## Industry Validation

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
**Semester 2:** Add Multi-Agent Coordination (for research/ideation)
**Semester 3:** Master Industry Patterns (Scrum/GitHub process)
**Semester 4:** Porfolio + "1 year, Agent Manager" → **clear placement potential**

---

## The Bottom Line

### Industry Reality:
- **51%** already using multi-agent systems
- **170 million** new AI jobs coming

### VITA Readiness:
- **1** prototype developed using industry best practices
- **3** successful pivots
- **100%** local data sovereignty

> Questions? Comments?
> 