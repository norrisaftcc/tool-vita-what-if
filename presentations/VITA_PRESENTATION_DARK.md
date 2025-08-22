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
  }
  
  th {
    background: rgba(139, 92, 246, 0.2);
    color: #F3F4F6;
    padding: 0.75em;
    border-bottom: 2px solid #8B5CF6;
  }
  
  td {
    padding: 0.75em;
    border-bottom: 1px solid rgba(255, 255, 255, 0.1);
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

# Breaking Up The Monolith

## Training Tomorrow's AI Orchestrators, Not Yesterday's Tool Users

**VITA Project**  
*Virtual Intelligence Teaching Assistant*

---

<!-- _class: lead -->

# There's a $15,000 gap

## between what we teach and what industry pays for.

## Tonight, we close it.

---

# The Reality Check

### Industry Has Already Moved:
- **51%** of companies use multiple AI agents in production
- **$140K+** salaries for multi-agent specialists  
- **78%** of employers need orchestration skills NOW

### Education Is Still Here:
- Teaching single-tool usage
- "Just use ChatGPT for everything"
- No discrimination or selection skills

---

# The Monolith Trap

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

# Universal Fears

**Students:** *"Will AI replace me?"*

**Faculty:** *"Are they learning or copying?"*

**Employers:** *"They can't choose appropriate tools"*

> These aren't fears. They're prophecies—unless we act.

---

# The Orchestra Solution

```text
     ┌─────────────┐  ┌─────────────┐  ┌─────────────┐  ┌─────────────┐
     │    VITA     │  │   GitHub    │  │   Research  │  │   General   │
     │  Debugging  │  │   Copilot   │  │    Agent    │  │     LLM     │
     │   Partner   │  │   Coding    │  │  Academic   │  │   Social    │
     └──────┬──────┘  └──────┬──────┘  └──────┬──────┘  └──────┬──────┘
            │                 │                 │                 │
     ┌──────▼─────────────────▼─────────────────▼─────────────────▼──────┐
     │                                                                    │
     │                    🎓 STUDENT AS AI ORCHESTRATOR                   │
     │                                                                    │
     │    "I need to debug" ──────► VITA                                │
     │    "I need to implement" ───► Copilot                            │
     │    "I need to research" ────► Research Agent                     │
     │    "I need to plan" ────────► General LLM                        │
     │                                                                    │
     └────────────────────────────────────────────────────────────────────┘
     
     ✅ Develops discrimination skills
     ✅ Matches industry practice (51% companies use multiple agents)
     ✅ Transparent, specialized tools
     ✅ Faculty can verify domain-specific learning
```

---

# The Transformation

### FROM: One tool for everything
### TO: Right tool for each task
### STUDENT BECOMES: AI Orchestra Conductor

---

# Proven Educational Innovations

### Already Working:
- **Miami Dade:** $82K → $100K graduate salaries
- **Harvey Mudd:** 55% women in CS (sustained)
- **UC Boulder:** 66% A-level mastery

### VITA's Approach:
- Cognitive companion for debugging
- Productive struggle with support
- Complete data sovereignty (on-premise)

---

# The Journey Roadmap

```text
    CURRENT STATE                    VITA PHASE 1                    FUTURE STATE
    Fall 2024                        Spring 2025                     Fall 2025+
    
    ╔═══════════╗                   ╔═══════════╗                   ╔═══╗ ╔═══╗
    ║           ║                   ║           ║                   ║ V ║ ║ G ║
    ║     🌊    ║                   ║     🌊    ║      ┌────►      ║ I ║ ║ H ║
    ║ MONOLITH  ║      ──────►      ║ MONOLITH  ║      │           ║ T ║ ║ C ║
    ║           ║                   ║           ║      │           ║ A ║ ║ P ║
    ║           ║                   ╚═══════════╝      │           ╚═══╝ ╚═══╝
    ╚═══════════╝                          +           │           ╔═══╗ ╔═══╗
         ▲                           ╔═══════════╗     │           ║ R ║ ║ D ║
         │                           ║   VITA    ║─────┘           ║ A ║ ║ B ║
    All queries                      ║ Debugging ║                 ║ G ║ ║ G ║
                                    ╚═══════════╝                 ╚═══╝ ╚═══╝
```

### Phase 1 (Spring 2025):
- Single debugging agent (VITA)
- Prove the concept
- Build faculty confidence

---

<!-- _class: lead -->

# The $15,000 Question

**Traditional Graduate:**
"I can use ChatGPT" → **$125,000**

**VITA-Trained Graduate:**
"I orchestrate specialized AI agents" → **$140,000+**

---

# Industry Validation

**IBM:** Agentic AI certificates

**CrewAI:** 100,000+ certified

**Microsoft:** 890,000+ AutoGen downloads

> Multi-agent AI orchestration isn't the future anymore. It's Tuesday.
> VITA helps your students show up ready for Wednesday.

---

<!-- _class: lead -->

# Our Journey
## From Educators to Developers

**November 2023 - Present**

---

# The Problem Was Real

| Model | Success Rate | Key Failure |
|-------|-------------|-------------|
| GPT-3.5 | 8/15 | Wrong error explanations |
| Zephyr-7B | 6/15 | Used concepts not yet taught |
| CodeLlama | 4/15 | Provided answers, not guidance |

### Critical Finding:
> "Models gave students incorrect debugging information 50% of the time"

---

# The Paradigm Shift

### Our Breakthrough:
- Multiple specialized agents > One smart model
- Each agent has specific expertise
- Cognitive overload as learning feature, not bug

### Philosophy:
> "Hey, I see you've got a lot going on here. Want some help working through it?"

---

# Building Through Scrum

### Our Team = Our Method:
- **Sprints** = Learning cycles
- **User stories** = Student needs
- **Daily standups** = Reflection
- **Retrospectives** = Improvement

### Key Pivot (June 2025):
- Removed Autogen framework
- Moved to Ollama
- This wasn't failure - it was learning

---

# Current System Architecture

```text
Student Input → VITA Client → Ollama (Local) → Debugging Support
                    ↑                              ↓
                Feedback ←─────────────────── Guided Learning
```

### Proven Components:
- ✅ Local Ollama deployment
- ✅ Panel UI functioning
- ✅ OAuth authentication
- ✅ Instructor corpus integrated

---

# Future Architecture (Planned)

```text
Student → VITA Orchestrator → [Debugging Agent]
                           → [Code Analysis Agent]  
                           → [Pattern Recognition]
                           → [GitHub Verification*]
                           
*GitHub integration planned for Fall 2025
```

### Note on GitHub:
- Concept proven in testing
- Integration planned post-pilot
- Will provide portfolio verification

---

# What We've Proven

### Technical Proof:
- Local models can provide quality help
- Complete data sovereignty achievable
- Educators can build production software

### Educational Proof:
- Iterative development works
- Scrum methodology transfers to EdTech
- "Break Up The Monolith" concept viable

### Ready to Deploy:
- Working single-agent prototype
- Demonstrates core concept
- Pilot-ready for Spring 2025

---

<!-- _class: lead -->

# Next Steps
## Small Scale, Big Impact

---

# Spring 2025 Pilot

### Scope:
- **2-3** intro programming sections
- **50-100** students total
- **One** specialized agent (debugging)

### Support Provided:
- Faculty training (2 hours)
- Weekly check-ins
- Full documentation
- Remote assistance

---

# What We'll Measure

### Student Outcomes:
- Debugging success rate
- Time to resolution
- Assignment completion

### Faculty Benefits:
- Reduced syntax error office hours
- More conceptual teaching time
- Student question quality

### Technical Performance:
- System reliability
- Response time
- Resource usage

---

# What You Provide

### Infrastructure:
- Modest GPU server (specs provided)
- Student authentication access

### People:
- 2-3 faculty champions
- IT liaison
- Admin sponsor

### Time:
- 2 hours training
- 30 min/week feedback during pilot

---

# Risk Mitigation

### Your Concerns Addressed:

**"What if it fails?"**
- Pilot is addition, not replacement
- Quick rollback possible

**"What about cheating?"**
- VITA teaches process, not answers
- Full audit trail

**"Can we handle this?"**
- Proven on community college infrastructure
- Complete support provided

---

# Three Decisions Needed

## 1. Pilot Participation
"Can we pilot VITA in Spring 2025?"

## 2. Team Formation
"Who are your champions?"
- Faculty lead: _______
- IT contact: _______
- Admin sponsor: _______

## 3. Success Definition
"What metrics matter most to you?"

**Decision needed by: December 15, 2024**

---

# Your Next Actions

### Before You Leave:
☐ Identify faculty champion  
☐ Check IT calendar for tech review  
☐ Confirm pilot interest (yes/no)

### We Deliver by December 30:
☐ Technical requirements  
☐ Training materials  
☐ Success framework

### Contact:
**Drew:** drew@example.com - Vision & Architecture  
**Mallory:** mallory@example.com - Technical & Training

### Demo Available:
December 10-20, 2024

---

<!-- _class: lead -->

# The Choice

## The Industry Has Moved
## The Question Is Whether Education Leads or Lags

> "Every semester we wait is another cohort unprepared for multi-agent reality"

### Will You Be First or Last?

**Questions?**

---

# Additional Resources

### Data Sovereignty Comparison

**❌ CURRENT RISK**
Student Data → THE MONOLITH (External Cloud) → Unknown Storage
"We don't know where it goes"

**✅ VITA SOLUTION**
Student Data → LOCAL VITA SERVER → 100% On-Campus
FERPA Compliant • IT Controlled

---

# Skill Development Progression

### Traditional Approach:
Semester 1 → "Just Google it" 
Semester 4 → "Just ask ChatGPT"
**Result: No skill progression**

### VITA Approach:
**Semester 1:** Learn Debugging with VITA
**Semester 2:** Add Multi-Agent Coordination
**Semester 3:** Master Industry Patterns
**Semester 4:** Graduate as AI Orchestrator → **$140K+ potential**

---

# Industry Alignment

### What Employers See:

**Traditional Grads:**
👤 "I can use ChatGPT"
- Single tool dependency
- No specialization understanding
- Can't debug without AI
**Starting Salary: $125,000**

**VITA Grads:**
👤 "I orchestrate specialized AI agents for different tasks"
- Multi-agent coordination
- Tool discrimination skills  
- Debugging expertise with AI partnership
- Ready for Agile/Scrum workflows (97% of companies)
**Starting Salary: $140,000+**

---

# The Bottom Line

### Industry Reality:
- **51%** already using multi-agent systems
- **$15,000** salary premium for orchestration skills
- **170 million** new AI jobs coming

### VITA Readiness:
- **1** working prototype
- **8** months of development
- **3** successful pivots
- **100%** local data sovereignty

> Multi-agent AI orchestration is not the future - it's the present.
> VITA helps your students join it.