# The Algorithm™ - Sprint Methodology
## "Iterations are features. Comfort is a bug."

### Core Metrics
- **Iteration Velocity**: 47 iterations / 14 days = 3.36 iterations/day minimum
- **PO Sweat Index**: Measured in shirt changes per sprint
- **Customer Joy Coefficient**: Inversely proportional to PO comfort level

## Sprint Structure

### Day 0: The Uncomfortable Kickoff
**Duration**: 15 minutes max
**Required Attendees**: Everyone who can type

#### Agenda Template
```
[2 min] Current reality check
[3 min] What we're breaking today
[5 min] Who's iterating on what
[5 min] Synchronization checkpoints
[0 min] Questions (ask while working)
```

### Daily Standup During Peak Velocity

#### The 5-Minute Sweat Check
**Time**: 9:00 AM sharp
**Format**: Standing (literally, no sitting)

##### Required Updates
1. **Yesterday's Iterations**: Number, not description
2. **Today's Target**: Minimum 3 iterations
3. **Blocker Alert**: Binary yes/no
4. **PO Stress Level**: Scale 1-10 (target: 7+)

##### Standup Script
```
"I shipped [X] iterations yesterday.
I will ship [Y] iterations today.
[I am/am not] blocked.
Current stress level: [N]/10"
```

**Total time per person**: 30 seconds MAX

### The Iteration Heartbeat

#### Morning Push (9:05 AM - 12:00 PM)
- **Target**: 2 iterations minimum
- **Communication**: Async only
- **Commits**: Every 30 minutes
- **PR Policy**: Open after first iteration, update continuously

#### Afternoon Surge (1:00 PM - 5:00 PM)
- **Target**: 2+ iterations
- **Pivot Authority**: Full autonomy to change direction
- **Documentation**: Update on the fly, never stop to write

#### Evening Review (5:00 PM - 5:15 PM)
- **Format**: Async Slack/Discord update
- **Content**: Screenshot of merged PRs + one-line learning

### Managing the Sweating Product Owner

#### PO Comfort Intervention Protocol
If PO appears relaxed:
1. **Immediate Action**: Schedule impromptu demo
2. **Escalation**: Add scope mid-sprint
3. **Nuclear Option**: Customer wants to see it "tomorrow"

#### PO Support Framework
- **Morning Brief**: 2-minute max update
- **Afternoon Check**: Single Slack message
- **End of Day**: Deploy notification only
- **Weekend Protocol**: Radio silence (let them wonder)

### Sprint Ceremonies Reimagined

#### Sprint Planning: The 30-Minute Scramble
**Inputs**: Vague customer desire
**Outputs**: 15 user stories minimum
**Method**: 
1. [5 min] PO describes dream
2. [10 min] Team breaks it into pieces
3. [10 min] Everyone grabs what they want
4. [5 min] Sync on not stepping on each other

#### Sprint Review: The Continuous Demo
- **Frequency**: Every 2 days
- **Duration**: 15 minutes
- **Format**: Live deployment + customer on call
- **Success Metric**: Customer says "ship it"

#### Sprint Retrospective: The 10-Minute Truth
**Format**: Three lists
1. **What made us faster**: Keep doing
2. **What slowed us down**: Stop immediately
3. **What we're trying next**: Start tomorrow

**No discussion. Just lists. Action over analysis.**

### Velocity Tracking

#### The Dashboard of Discomfort
Display publicly:
- Current iteration count
- Hours since last deployment
- PO heart rate (optional IoT integration)
- Customer happiness trend
- Team velocity graph (must trend upward)

### Communication Protocols

#### Slack/Discord Channels
- `#iterations-shipped`: Auto-post from CI/CD
- `#po-stress-level`: Daily update
- `#customer-joy`: Screenshot reactions
- `#help-im-stuck`: 5-minute response SLA

#### The No-Meeting Manifesto
- Standups: 5 minutes
- All other meetings: Canceled
- Pairing: Yes, but while coding
- Reviews: In PRs only
- Planning: While implementing

### Escalation Framework

#### When Velocity Drops Below 3 Iterations/Day
1. **Hour 1**: Team self-diagnoses
2. **Hour 2**: Simplify scope aggressively  
3. **Hour 3**: Deploy something, anything
4. **Hour 4**: Nuclear option - pivot entirely

### Quality Gates (The Minimal Set)

#### Definition of "Done" in The Algorithm
- [ ] It runs locally
- [ ] It's deployed
- [ ] Customer hasn't complained (yet)
- [ ] PR is merged
- [ ] Next iteration started

#### Testing Strategy
- Unit tests: Only for the terrifying parts
- Integration tests: If customer is watching
- Manual testing: By shipping to production
- Rollback strategy: Always have one ready

### Team Roles in The Algorithm

#### The Implementer
- Ships code
- Asks questions later
- Iterates constantly

#### The Merger
- Reviews PRs in under 5 minutes
- Approves with "LGTM 🚀"
- Trusts the process

#### The Deployer
- Pushes to production
- Monitors for 5 minutes
- Moves to next iteration

#### The Product Owner (Sweating Edition)
- Provides vision (blurry is fine)
- Accepts discomfort
- Celebrates shipped iterations
- Maintains customer relationship

### Success Metrics

#### Sprint Success Criteria
- ✅ 40+ iterations completed
- ✅ PO changed shirt at least once
- ✅ Customer said "wow" at least twice
- ✅ Zero meetings over 30 minutes
- ✅ Production deployments > 20

### The Algorithm Oath

Before each sprint, the team recites:
```
"We shall iterate without hesitation,
Deploy without delay,
Simplify without sentimentality,
And ship without shame.

Comfort is the enemy,
Velocity is the way,
The customer's joy is our metric,
The PO's sweat is our gauge.

This is The Algorithm.
This is the way."
```

### Implementation Checklist

#### Day 1 Setup
- [ ] Cancel all meetings over 30 minutes
- [ ] Set up auto-deployment pipeline
- [ ] Create iteration counter dashboard
- [ ] Install PO stress monitoring system
- [ ] Remove all comfort items from workspace

#### Week 1 Goals
- [ ] 20+ iterations shipped
- [ ] 10+ production deployments
- [ ] 1+ PO shirt change
- [ ] 0 meetings over 30 minutes
- [ ] 5+ customer "wow" moments

### Anti-Patterns to Avoid

#### The Comfort Trap
- Long planning sessions
- Detailed documentation
- Comprehensive testing
- Consensus-seeking
- Perfect code

#### The Velocity Killers
- "Let's think about this"
- "We should plan this properly"
- "What about edge cases?"
- "Shouldn't we test this more?"
- "The PO seems stressed"

### Emergency Protocols

#### When Customer Is Unhappy
1. Ship iteration immediately
2. Call customer during deployment
3. Ship another iteration while on call
4. Repeat until joy achieved

#### When Team Is Blocked
1. Simplify problem by 50%
2. Still blocked? Simplify another 50%
3. Still blocked? Ship different feature
4. Still blocked? Deploy refactoring
5. Never stop shipping

### Certification Criteria

A team has achieved Algorithm Certification when:
- Sprint velocity maintains 3+ iterations/day
- PO exhibits visible discomfort
- Customer expresses unexpected delight
- Production deployment fear is extinct
- Meetings are extinct

---

## Remember

The Algorithm is not about recklessness. It's about:
- Radical prioritization
- Aggressive simplification
- Continuous delivery
- Customer obsession
- Embracing discomfort

When in doubt: SHIP IT.

*"47 iterations. 2 weeks. 1 sweating product owner. Infinite customer joy."*