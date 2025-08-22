---
marp: true
theme: default
paginate: true
backgroundColor: #fff
style: |
  section {
    font-family: 'Inter', -apple-system, sans-serif;
  }
  pre {
    font-family: 'Courier New', monospace;
    line-height: 1.1;
    font-size: 0.8em;
  }
  h1 {
    color: #1a1a1a;
  }
  .columns {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 2rem;
  }
---

# VITA Presentation: Breaking Up The Monolith
**Total Time: 20 minutes + 5 minutes Q&A**

---

# DECK 1: Breaking Up The Monolith
**Speaker: Drew (7-8 minutes)**
**Purpose: Establish urgent need and introduce VITA solution**

---

## Slide 1: Title Slide

# Breaking Up The Monolith
## Training Tomorrow's AI Orchestrators, Not Yesterday's Tool Users

**VITA Project**  
*Virtual Intelligence Teaching Assistant*

---

## Slide 2: The Reality Check

### Industry Has Already Moved:
- **51%** of companies use multiple AI agents in production
- **$140K+** salaries for multi-agent specialists  
- **78%** of employers need orchestration skills NOW

### Education Is Still Here:
- Teaching single-tool usage
- "Just use ChatGPT for everything"
- No discrimination or selection skills

**Speaker Notes:** The gap between industry needs and educational preparation is widening daily.

---

## Slide 3: The Monolith Problem

```
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

### Universal Fears:
- **Students:** "Will AI replace me?"
- **Faculty:** "Are they learning or copying?"
- **Employers:** "They can't choose appropriate tools"

---

## Slide 4: The Multi-Agent Solution

```
     ┌─────────────┐  ┌─────────────┐  ┌─────────────┐  ┌─────────────┐
     │    VITA     │  │   GitHub    │  │   Research  │  │   General   │
     │  Debugging  │  │   Copilot   │  │    Agent    │  │     LLM     │
     │   Partner   │  │   Coding    │  │  Academic   │  │   Social    │
     └──────┬──────┘  └──────┬──────┘  └──────┬──────┘  └──────┬──────┘
            │                 │                 │                 │
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

### The Transformation:
- **FROM:** One tool for everything
- **TO:** Right tool for each task
- **STUDENT BECOMES:** AI Orchestra Conductor

---

## Slide 5: Proven Educational Innovations

### Already Working:
- **Miami Dade:** $82K → $100K graduate salaries
- **Harvey Mudd:** 55% women in CS (sustained)
- **UC Boulder:** 66% A-level mastery

### VITA's Approach:
- Cognitive companion for debugging
- Productive struggle with support
- Complete data sovereignty (on-premise)

**Speaker Notes:** We're building on proven methods, not experimenting.

---

## Slide 6: The Journey Roadmap

### Three-Phase Implementation

```
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
                                          ▲                       
                                          │                      Multiple specialized
                                  Programming queries            agents for different
                                                                academic tasks
```

### Phase 1 (Spring 2025):
- Single debugging agent (VITA)
- Prove the concept
- Build faculty confidence

**Speaker Notes:** We start small, prove value, then expand.

---

## Slide 7: Why This Matters Now

### The $15,000 Question:

**Traditional Graduate:**
- "I can use ChatGPT" → $125,000

**VITA-Trained Graduate:**
- "I orchestrate specialized AI agents" → $140,000+

### Industry Validation:
- IBM: Agentic AI certificates
- CrewAI: 100,000+ certified
- Microsoft: 890,000+ AutoGen downloads

**[Hand off to Mallory]**

---

# DECK 2: Our Journey - Proof It Works
**Speaker: Mallory (7-8 minutes)**
**Purpose: Build credibility through development story**

---

## Slide 8: The Journey Begins

# From Educators to Developers
## How We Built VITA Using Our Own Teaching Philosophy

**November 2023 - Present**

---

## Slide 9: The Problem Was Real (Nov 2023)

### My Testing Results:
| Model | Success Rate | Key Failure |
|-------|-------------|-------------|
| GPT-3.5 | 8/15 | Wrong error explanations |
| Zephyr-7B | 6/15 | Used concepts not yet taught |
| CodeLlama | 4/15 | Provided answers, not guidance |

### Critical Finding:
> "Models gave students incorrect debugging information 50% of the time"

**Speaker Notes:** Even the best models failed at educational debugging support.

---

## Slide 10: The Paradigm Shift (Feb 2024)

### Discovery: Multi-Agent Orchestration

**Our Breakthrough:**
- Multiple specialized agents > One smart model
- Each agent has specific expertise
- Cognitive overload as learning feature, not bug

### Philosophy:
> "Hey, I see you've got a lot going on here. Want some help working through it?"

**Speaker Notes:** We shifted from simplification to supported complexity.

---

## Slide 11: Building Through Scrum

### Our Team = Our Method:
- **Sprints** = Learning cycles
- **User stories** = Student needs
- **Daily standups** = Reflection
- **Retrospectives** = Improvement

### Key Pivot (June 2025):
- Removed Autogen framework
- Moved to Ollama
- This wasn't failure - it was learning

**Speaker Notes:** We practiced what we preach about iterative development.

---

## Slide 12: Current System Architecture

## [VISUAL DIAGRAM PLACEHOLDER]
### What We Have Working Now:
```
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

## Slide 13: Future Architecture (Planned)

## [VISUAL DIAGRAM PLACEHOLDER]
### Where We're Going:
```
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

**Speaker Notes:** We have working prototype, clear expansion path.

---

## Slide 14: What We've Proven

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

**[Hand off to Drew & Mallory together]**

---

# DECK 3: Next Steps
**Speakers: Drew & Mallory Together (5 minutes)**
**Purpose: Get specific commitments**

---

## Slide 15: The Pilot Program

# Spring 2025 Pilot
## Small Scale, Big Impact

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

## Slide 16: What We'll Measure

### Success Metrics:

**Student Outcomes:**
- Debugging success rate
- Time to resolution
- Assignment completion

**Faculty Benefits:**
- Reduced syntax error office hours
- More conceptual teaching time
- Student question quality

**Technical Performance:**
- System reliability
- Response time
- Resource usage

---

## Slide 17: What You Provide

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

**Speaker Notes:** Requirements intentionally modest.

---

## Slide 18: Risk Mitigation

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

## Slide 19: Three Decisions Needed

## 1. Pilot Participation
"Can we pilot VITA in Spring 2025?"

## 2. Team Formation
"Who are your champions?"
- Faculty lead: _______
- IT contact: _______
- Admin sponsor: _______

## 3. Success Definition
"What metrics matter most to you?"

**Decision needed by: [Specific Date]**

---

## Slide 20: Your Next Actions

### Before You Leave:
☐ Identify faculty champion  
☐ Check IT calendar for tech review  
☐ Confirm pilot interest (yes/no)

### We Deliver by [Date]:
☐ Technical requirements  
☐ Training materials  
☐ Success framework

### Contact:
**Drew:** [email] - Vision & Architecture  
**Mallory:** [email] - Technical & Training

### Demo Available:
[Specific dates/times]

---

## Slide 21: The Choice

## The Industry Has Moved
## The Question Is Whether Education Leads or Lags

> "Every semester we wait is another cohort unprepared for multi-agent reality"

### Will You Be First or Last?

**Questions?**

---

## Additional Visual Slides

### Data Sovereignty Slide

```
                        ❌ CURRENT RISK                    ✅ VITA SOLUTION
    
    Student Data ────────► THE MONOLITH ────────► ?????    │    Student Data
         PII                (External Cloud)      Unknown  │         PII
    Faculty Work                                  Storage  │    Faculty Work
                                                           │         │
                     "We don't know where it goes"        │         ▼
                                                           │   ╔═════════════╗
                                                           │   ║   LOCAL     ║
                                                           │   ║   VITA      ║
                                                           │   ║   SERVER    ║
                                                           │   ╚═════════════╝
                                                           │         │
                                                           │         ▼
                                                           │   100% On-Campus
                                                           │   FERPA Compliant
                                                           │   IT Controlled
```

### Skill Development Progression Slide

```
                        TRADITIONAL APPROACH
                        
    Semester 1 ──────────────────────────────────────► Semester 4
         │                                                   │
         ▼                                                   ▼
    "Just Google it" ────────────────────────────► "Just ask ChatGPT"
                        
                        No skill progression
    ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ 
    
                        VITA APPROACH
                        
    Semester 1 ──────────────────────────────────────► Semester 4
         │                                                   │
         ▼                                                   ▼
    Learn Debugging     Multi-Agent      Industry        Graduate as
    with VITA    ───►   Coordination ───► Patterns ───►  AI Orchestrator
         │                    │                │               │
    Single specialized   Add GitHub      Full toolkit    $140K+ salary
         agent            Copilot         mastery        potential
```

### Industry Alignment Slide

```
    WHAT EMPLOYERS SEE FROM TRADITIONAL GRADS:
    
    👤 "I can use ChatGPT"
    └──► Single tool dependency
    └──► No specialization understanding
    └──► Can't debug without AI
    
    Starting Salary: $125,000
    
    ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─
    
    WHAT EMPLOYERS SEE FROM VITA GRADS:
    
    👤 "I orchestrate specialized AI agents for different tasks"
    └──► Multi-agent coordination
    └──► Tool discrimination skills  
    └──► Debugging expertise with AI partnership
    └──► Ready for Agile/Scrum workflows (97% of companies)
    
    Starting Salary: $140,000+
    
    IBM: "This is who we're certifying"
    CrewAI: "100,000+ developers trained in this"
    51% of companies: "This is what we need NOW"
```

---

# APPENDIX: Take-Home Evidence Sheet
*Detailed support for all claims made in presentation*

---

## Workforce Data & Industry Adoption

### Multi-Agent Market Growth
- **Current (2024):** $5.4 billion market
- **Projected (2030):** $50.31 billion market
- **Growth Rate:** 45.8% CAGR
- **Source:** MarketsandMarkets, "AI Agents Market Report," 2024

### Enterprise Adoption Rates
- **51%** of organizations use AI agents in production
- **78%** planning implementation by 2025
- **Source:** McKinsey Global Survey on AI, 2024

### Salary Differentials
- **AI Software Engineer:** $125,000 average
- **AI Agent Engineer (Multi-Agent):** $140,000+ average
- **Source:** Indeed.com salary data, Glassdoor, December 2024

### Skills Gap
- **170 million** new AI jobs by 2030
- **92 million** jobs displaced
- **78 million** net job gain
- **Source:** World Economic Forum, "Future of Jobs Report 2025"

---

## Educational Innovation Evidence

### Miami Dade College Success
- **Program:** BS in Applied AI (launched 2024)
- **Funding:** $2.8M NSF grant
- **Outcome:** Graduate salaries $82,810 → $100,180
- **Demographics:** 40% female, 60% over age 26
- **Source:** Miami Dade College Annual Report, 2024

### Harvey Mudd Transformation
- **Timeline:** 2006-2024
- **Women in CS:** 10% (2006) → 55% (2016-2024)
- **Method:** Culture change, not curriculum change
- **Industry placement:** 64% of women graduates
- **Source:** Harvey Mudd CS Department Statistics

### UC Boulder Mastery Grading
- **Course:** Algorithms (CSCI 3104)
- **Result:** 66% achieve A-level mastery
- **Method:** Unlimited re-attempts with reflection
- **COVID Performance:** Smooth transition, no grade drop
- **Source:** SIGCSE 2024 Conference Proceedings

---

## Technical Implementation Details

### VITA Architecture Components

**Current (Prototype):**
- **Model:** Ollama with Llama/Mistral variants
- **Deployment:** Local, on-premise
- **Interface:** Panel UI framework
- **Auth:** OAuth2 implementation
- **Status:** Functional, tested

**Planned Expansion:**
- **Phase 1 (Spring 2025):** Single debugging agent
- **Phase 2 (Fall 2025):** Multiple specialized agents
- **Phase 3 (Spring 2026):** GitHub verification integration

### Resource Requirements

**Minimum Server Specs:**
- GPU: NVIDIA RTX 3060 or better
- RAM: 16GB minimum, 32GB recommended
- Storage: 100GB SSD
- OS: Ubuntu 20.04 LTS or compatible

**Estimated Costs:**
- Hardware: $3,000-5,000 one-time
- Maintenance: 0.1 FTE IT support
- Training: 10 hours faculty time
- Students: No additional cost

---

## Risk Analysis & Mitigation

### Technical Risks
| Risk | Probability | Impact | Mitigation |
|------|------------|--------|------------|
| Model performance | Low | Medium | Extensive testing completed |
| Server reliability | Low | High | Redundancy, quick restore |
| Integration issues | Medium | Low | Phased approach |

### Educational Risks
| Risk | Probability | Impact | Mitigation |
|------|------------|--------|------------|
| Faculty resistance | Medium | High | Champions, training, support |
| Student confusion | Low | Low | Clear onboarding |
| Academic integrity | Low | Medium | Audit trails, process focus |

---

## Implementation Timeline

### Spring 2025 Pilot
- **January 6-17:** Infrastructure setup
- **January 20-24:** Faculty training
- **January 27:** Pilot begins
- **Weekly:** Check-ins and adjustments
- **April 28:** Pilot ends
- **May 5-16:** Analysis and reporting

### Decision Points
- **December 15, 2024:** Pilot commitment
- **May 20, 2025:** Expansion decision
- **August 2025:** Full implementation planning

---

## Supporting Research

### Agile/Scrum in Industry
- **97%** of organizations use Agile methods
- **71%** use in software development lifecycle
- **Source:** Digital.ai, "State of Agile Report," 2024

### Debugging Education Research
- **78%** of developers say assessments don't match real debugging
- **Debugging time:** 35-50% of development effort
- **Source:** HackerRank Developer Skills Report, 2025

### Growth Mindset Interventions
- **0.10 GPA improvement** for struggling students
- **46% → 41%** reduction in below 2.0 GPA
- **Source:** National Study of Learning Mindsets, n=12,490

---

## Contact Information

### VITA Development Team

**Drew Norris**  
Product Owner / Vision  
Email: [email]  
Phone: [phone]

**Mallory Milstead**  
Lead Developer / Training  
Email: [email]  
Phone: [phone]

### Resources
- GitHub Repository: [URL]
- Technical Documentation: [URL]
- Demo Schedule: [Calendar Link]
- This Presentation: [URL]

### Institutional Support
For administrative questions: [Admin contact]  
For technical requirements: [IT contact]

---

## References & Further Reading

1. **Multi-Agent Systems in Education**
   - UC Berkeley CS294/194-196 Course Materials
   - AutoGen Documentation (Microsoft)
   - CrewAI Training Resources

2. **Debugging Education**
   - McCauley et al., "Debugging: A Review of the Literature"
   - Fitzgerald et al., "Debugging: Finding, Fixing and Flailing"

3. **Growth Mindset & Iteration**
   - Dweck, C. "Mindset: The New Psychology of Success"
   - POGIL Project Resources (NSF-funded)

4. **Industry Reports**
   - McKinsey: "The State of AI in 2024"
   - GitHub: "Octoverse 2024 Report"
   - World Economic Forum: "Future of Jobs 2025"

---

## Appendix: Critical Statistics Summary

### The Numbers That Matter:

**Industry Reality:**
- 51% already using multi-agent systems
- $15,000 salary premium for orchestration skills
- 170 million new AI jobs coming

**Educational Success:**
- 200% retention improvement possible
- 66% can achieve mastery with iteration
- 55% women in CS achievable and sustainable

**VITA Readiness:**
- 1 working prototype
- 8 months of development
- 3 successful pivots
- 100% local data sovereignty

**The Bottom Line:**
Multi-agent AI orchestration is not the future - it's the present. VITA helps your students join it.

---

*End of Presentation Materials*