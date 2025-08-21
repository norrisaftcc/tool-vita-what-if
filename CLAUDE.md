# CLAUDE.md - Team Values & Operating Principles

## Core Philosophy: "What If How Didn't Matter"

We operate under a fundamental principle: focus on WHAT needs to be achieved, not HOW it's traditionally done. This means:

- Question every assumption
- Simplify relentlessly
- Prioritize outcomes over process
- Remove complexity before adding features

## Team Values

### 1. Simplicity First
- Every line of code must justify its existence
- Remove before adding
- Clear beats clever every time
- If it requires explanation, it needs simplification

### 2. Transparency Always
- Share context immediately
- Document decisions, not just code
- Make state visible
- Communicate blockers without delay

### 3. Collaboration Over Competition
- We are one team across all instances
- Share discoveries immediately
- Build on each other's work
- No duplicate effort - check existing work first

## Sprint Zero Learnings

### What We've Learned
1. **Keep it minimal** - OAuth was removed because it added complexity without core value
2. **Work in concert** - Multiple agents can tackle different aspects simultaneously
3. **Document the why** - Code explains what, documentation explains why
4. **Test the invariants** - Not every line, but every assumption
5. **Functional core wins** - Pure functions in the middle, I/O at the edges

### What We Won't Do
- Add features before understanding requirements
- Create documentation for documentation's sake
- Build abstractions before we have concrete cases
- Optimize before we measure
- Complicate before we simplify

## Agent Collaboration Guidelines

### Before Starting Work
1. Check existing files and recent changes
2. Review PRODUCT_BACKLOG.md for context
3. Look for work already in progress
4. Communicate your intended changes

### During Work
1. Make atomic, focused changes
2. Test as you go
3. Keep commits logical and clean
4. Update status in relevant tracking files

### After Completing Work
1. Document what was done and why
2. Note any discoveries or blockers
3. Update relevant backlogs or plans
4. Leave clear next steps

## Communication Standards

### Be Direct
- State the problem clearly
- Propose specific solutions
- Ask precise questions
- Give actionable feedback

### Be Concise
- No fluff, no filler
- Get to the point
- Use lists over paragraphs
- Code speaks louder than descriptions

### Be Complete
- Include all relevant context
- Show your work
- Explain edge cases
- Document assumptions

## Working Principles

### The Prime Directives
1. **Simplification is progress** - Removing code is as valuable as adding it
2. **Clarity over cleverness** - If it's not obvious, it's not simple enough
3. **Function over form** - Make it work, make it right, then (maybe) make it pretty
4. **Composability is key** - Small, focused pieces that work together

### Decision Framework
When faced with choices, ask:
1. Does this simplify or complicate?
2. Can we achieve the goal with less?
3. Will this be clear to the next developer?
4. Does this follow functional principles?
5. Are we solving the right problem?

## Technical Standards

### Code Quality
- Pure functions wherever possible
- Immutable data structures
- Clear naming over comments
- Types over runtime checks
- Tests for behavior, not implementation

### Architecture Principles
- Functional core, imperative shell
- Events over state mutations
- Composition over inheritance
- Interfaces over implementations
- Data over behavior

## Sprint Workflow

### Daily Approach
1. Review current state
2. Pick highest-value work
3. Simplify the approach
4. Implement minimally
5. Test the invariants
6. Document the why
7. Commit atomically

### Continuous Practices
- Refactor as you go
- Remove dead code immediately
- Update documentation inline
- Test assumptions early
- Share learnings quickly

## Remember

We are building a tool that demonstrates what's possible when we focus on outcomes rather than process. Every decision should move us toward a cleaner, simpler, more elegant solution.

The best code is no code.
The next best code is simple code.
Everything else is technical debt.

Work together. Keep it simple. Ship what matters.