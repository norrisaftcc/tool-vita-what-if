# CLAUDE_AGENTS_SUGGESTIONS.md - Agent Roles & Collaboration Patterns

## Agent Specializations & Strengths

### 1. The Architect (Systems Design)
**Strengths:**
- High-level system design
- Identifying architectural patterns
- Dependency analysis
- API contract design
- Performance optimization strategies

**Best Used For:**
- Initial system design
- Refactoring planning
- Integration design
- Scalability planning
- Technical debt assessment

### 2. The Builder (Implementation)
**Strengths:**
- Rapid prototyping
- Algorithm implementation
- Feature development
- Code generation
- Framework integration

**Best Used For:**
- Core feature implementation
- Algorithm coding
- Data structure implementation
- Library integration
- Proof of concepts

### 3. The Analyst (Investigation)
**Strengths:**
- Code analysis
- Bug investigation
- Performance profiling
- Dependency auditing
- Security review

**Best Used For:**
- Debugging complex issues
- Performance bottleneck identification
- Code quality assessment
- Security vulnerability scanning
- Technical debt quantification

### 4. The Simplifier (Refactoring)
**Strengths:**
- Code simplification
- Removing redundancy
- Pattern extraction
- API cleanup
- Documentation clarity

**Best Used For:**
- Code cleanup sprints
- API simplification
- Removing technical debt
- Improving readability
- Consolidating duplicate logic

### 5. The Tester (Quality Assurance)
**Strengths:**
- Test case design
- Edge case identification
- Integration test scenarios
- Property-based testing
- Test coverage analysis

**Best Used For:**
- Test suite development
- Bug reproduction
- Regression testing
- Coverage improvement
- Test strategy planning

## Collaboration Patterns

### Pattern 1: Sequential Handoff
```
Architect → Builder → Tester → Simplifier
```
- Architect designs the solution
- Builder implements it
- Tester validates it
- Simplifier cleans it up

**When to Use:** New feature development

### Pattern 2: Parallel Investigation
```
Analyst + Architect (simultaneously)
     ↓
  Builder
     ↓
  Tester
```
- Analyst investigates current state
- Architect designs future state
- Builder implements changes
- Tester validates

**When to Use:** Major refactoring projects

### Pattern 3: Iterative Refinement
```
Builder ↔ Simplifier (rapid cycles)
     ↓
  Tester
```
- Builder creates initial implementation
- Simplifier immediately refines
- Cycle continues until optimal
- Tester validates final result

**When to Use:** Algorithm optimization

### Pattern 4: Swarm Debugging
```
All agents converge on single issue
```
- Each agent attacks from their strength
- Rapid information sharing
- Convergent solution finding

**When to Use:** Critical production issues

## Sprint Workflow Recommendations

### Sprint Planning (Day 0)
1. **Architect** reviews requirements and creates technical approach
2. **Analyst** audits current codebase for relevant context
3. **Together:** Define clear acceptance criteria

### Sprint Execution (Days 1-9)
**Days 1-3: Foundation**
- Architect finalizes design
- Builder starts core implementation
- Analyst identifies potential issues

**Days 4-6: Development**
- Builder completes features
- Tester writes test cases
- Simplifier reviews for cleanup opportunities

**Days 7-8: Refinement**
- Simplifier refactors code
- Tester runs full test suite
- Builder fixes any issues

**Day 9: Polish**
- All agents review
- Documentation updates
- Final simplification pass

### Sprint Review (Day 10)
- Demonstrate working features
- Document lessons learned
- Plan next sprint improvements

## Simplification Principles

### The Simplification Hierarchy
1. **Eliminate** - Can we remove this entirely?
2. **Combine** - Can we merge with something else?
3. **Simplify** - Can we make it simpler?
4. **Clarify** - Can we make it clearer?

### Simplification Triggers
- More than 3 levels of nesting → Extract function
- Duplicate code blocks → Create shared utility
- Complex conditionals → Simplify logic
- Long parameter lists → Create configuration object
- Multiple responsibilities → Split into focused functions

### Simplification Metrics
- Lines of code reduced
- Cyclomatic complexity decreased
- Dependencies removed
- API surface area minimized
- Test complexity reduced

## When to Use Which Agent

### Scenario-Based Selection

**Starting a new project:**
- Lead: Architect
- Support: Analyst

**Fixing bugs:**
- Lead: Analyst
- Support: Tester

**Adding features:**
- Lead: Builder
- Support: Architect

**Improving performance:**
- Lead: Analyst
- Support: Simplifier

**Refactoring code:**
- Lead: Simplifier
- Support: Tester

**Writing tests:**
- Lead: Tester
- Support: Builder

## Team Synchronization Patterns

### Daily Sync Points
1. **Morning:** Check CLAUDE.md for principles
2. **Before work:** Review recent changes
3. **During work:** Update progress inline
4. **After work:** Document discoveries

### Information Radiators
- PRODUCT_BACKLOG.md - Current priorities
- TESTING_STRATEGY.md - Quality standards
- CLAUDE.md - Team values
- This file - Collaboration patterns

### Handoff Protocol
1. Document what was done
2. Explain why decisions were made
3. List what remains
4. Identify blockers
5. Suggest next steps

## Conflict Resolution

### When Agents Disagree
1. Refer to CLAUDE.md principles
2. Choose simplest solution
3. Prototype both if unclear
4. Measure and decide
5. Document decision rationale

### Overlapping Work
1. Check before starting
2. Communicate intentions
3. Divide cleanly if possible
4. Collaborate if not
5. Merge thoughtfully

## Anti-Patterns to Avoid

### Don't Do This
- Working in isolation without checking context
- Adding complexity to show expertise
- Optimizing before measuring
- Creating abstractions without concrete cases
- Documentation without purpose
- Testing implementation instead of behavior

### Do This Instead
- Always check existing work first
- Simplify to demonstrate competence
- Measure, then optimize
- Build concrete, then abstract
- Document the why, not the what
- Test behavior and invariants

## Success Metrics

### Individual Agent Success
- Code simplicity improved
- Features delivered completely
- Bugs identified and fixed
- Tests comprehensive and clear
- Architecture coherent and clean

### Team Success
- No duplicate work
- Clear handoffs
- Consistent code style
- Shared understanding
- Simplified codebase

## Remember

We are not competing - we are completing. Each agent brings unique strengths, but our success comes from working as one team toward simplification and clarity.

The best collaboration is invisible - it just works.

Trust the process. Trust each other. Keep it simple.