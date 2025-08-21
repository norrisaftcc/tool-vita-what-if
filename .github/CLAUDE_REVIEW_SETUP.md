# Claude Code Review Setup Guide

## Overview

This document provides comprehensive setup instructions for the Claude-assisted code review system implemented in the `tool-vita-what-if` repository. The system automates code review requests and integrates Claude AI analysis into the pull request workflow.

## Security Requirements

### Two-Factor Authentication (2FA)

**CRITICAL SECURITY REQUIREMENT**: All reviewers performing Claude code reviews MUST have 2FA enabled on their GitHub accounts.

#### Enabling 2FA - You'll Need Your Phone

1. **Navigate to GitHub Security Settings**
   - Go to GitHub.com → Settings → Password and authentication
   - Click "Two-factor authentication"

2. **Setup Process** (Have your phone ready)
   - Choose authentication method (Authenticator app recommended)
   - Scan QR code with your authenticator app
   - Enter verification code from your phone
   - Download and securely store recovery codes

3. **Verification**
   - Test 2FA login immediately after setup
   - Ensure recovery codes are stored in secure location
   - Update team/organization security policies if applicable

#### Required Permissions

Reviewers must have the following repository permissions:
- `contents:read` - Read repository code and files
- `pull-requests:write` - Create and update PR reviews
- `issues:write` - Manage labels and comments

## System Components

### 1. Workflow Automation (`.github/workflows/claude-code-review.yml`)

The workflow automatically:
- Detects relevant file changes in PRs
- Adds `claude-review:pending` label
- Requests review from designated Claude reviewers
- Posts structured review request comment
- Updates review status based on review submissions

**Trigger Conditions:**
- PR opened, synchronized, or reopened
- Target branches: `main`, `develop`
- Non-draft PRs only
- Files matching configured patterns

### 2. Review Configuration (`.github/claude-review-config.json`)

Defines review standards and criteria:
- **Code Quality (30%)**: Patterns, error handling, naming conventions
- **Security (25%)**: Secrets, validation, dependencies
- **Performance (20%)**: Algorithms, resources, optimization
- **Maintainability (15%)**: Documentation, testing, compatibility
- **Testing (10%)**: Coverage, edge cases, integration

**Approval Thresholds:**
- Approved: ≥80% score
- Changes Requested: 60-79% score
- Blocked: <60% score

### 3. Label System

| Label | Description | Color | Usage |
|-------|-------------|-------|-------|
| `claude-review:pending` | Review requested | Yellow (#FBCA04) | Auto-applied on PR creation |
| `claude-review:approved` | Review approved | Green (#0E8A16) | ≥80% score, no blocking issues |
| `claude-review:changes-requested` | Changes needed | Red (#D73A49) | 60-79% score, improvements required |
| `claude-review:commented` | Comments only | Blue (#1D76DB) | Non-blocking feedback |
| `claude-review:blocked` | Critical issues | Dark Red (#B60205) | <60% score, must fix before merge |

### 4. PR Template Integration

Updated template includes Claude review checklist:
- Automatic review request confirmation
- Configuration compliance verification
- Security and performance assessment checkboxes

## Reviewer Setup Process

### Prerequisites

1. **GitHub Account Requirements**
   - 2FA enabled (see security requirements above)
   - Repository access with required permissions
   - Added to `required_reviewers` list in config

2. **Claude Access**
   - Active Claude subscription or organizational access
   - Familiarity with Claude Code interface
   - Understanding of review criteria and standards

### Configuration Steps

#### Step 1: Verify Repository Access

```bash
# Check repository permissions
gh api repos/norrisaftcc/tool-vita-what-if/collaborators/YOUR_USERNAME

# Verify 2FA status
gh auth status
```

#### Step 2: Update Reviewer Configuration

Edit `.github/claude-review-config.json`:

```json
{
  "integration": {
    "required_reviewers": [
      "norrisaftcc",
      "YOUR_USERNAME"  // Add your username here
    ]
  }
}
```

#### Step 3: Test Workflow

1. Create test branch: `git checkout -b test/claude-review-setup`
2. Make small code change to trigger review
3. Create PR and verify:
   - Workflow runs successfully
   - Labels are applied correctly
   - Review request comment is posted
   - You receive review assignment

## Review Process

### For Reviewers

#### 1. Review Request Notification

When assigned a Claude review:
- Check email notification or GitHub notifications
- Review the automated comment with PR analysis
- Note the files changed and complexity assessment

#### 2. Conducting Claude Review

**Required Format for Review Comments:**

```markdown
## 🤖 Claude Review Analysis

**Overall Status:** [✅ APPROVED | 🔴 CHANGES REQUESTED | 💬 COMMENTS | ❌ BLOCKED]

### Code Quality Assessment
- Score: X/30
- Issues: [List any concerns]
- Recommendations: [Specific improvements]

### Security Analysis  
- Score: X/25
- Vulnerabilities: [None found | List issues]
- Recommendations: [Security improvements]

### Performance Review
- Score: X/20
- Concerns: [Performance implications]
- Optimizations: [Suggested improvements]

### Maintainability Check
- Score: X/15
- Documentation: [Adequate | Needs improvement]
- Testing: [Coverage assessment]

### Testing Evaluation
- Score: X/10
- Coverage: [Percentage or assessment]
- Missing tests: [List gaps]

**Total Score: X/100**

### Summary
[Brief summary of findings and overall recommendation]

### Action Items
- [ ] [Specific action item 1]
- [ ] [Specific action item 2]

---
*Review completed using Claude AI assistance following established criteria*
```

#### 3. Status Updates

The workflow automatically:
- Updates PR labels based on review status
- Posts summary comments
- Notifies relevant stakeholders

### For PR Authors

#### 1. Preparing for Claude Review

**Before Creating PR:**
- Run local tests and ensure they pass
- Perform self-review against Claude criteria
- Update documentation for any API changes
- Ensure no secrets or sensitive data in commits

**PR Creation Checklist:**
- Use descriptive title and summary
- Link related issues with "Fixes #XXX"
- Complete all template sections
- Mark Claude review section items as applicable

#### 2. Responding to Review Feedback

**When Changes Requested:**
- Address each action item individually
- Test changes thoroughly before pushing
- Update documentation if required
- Request re-review when ready

**Communication:**
- Respond to review comments directly
- Ask clarifying questions if needed
- Provide context for implementation decisions

## Troubleshooting

### Common Issues

#### Workflow Not Triggering

**Symptoms:** No labels applied, no review comment posted

**Solutions:**
1. Check if PR is in draft mode (workflow skips drafts)
2. Verify target branch is `main` or `develop`
3. Ensure changed files match trigger patterns
4. Check workflow permissions in repository settings

#### Labels Not Updating

**Symptoms:** Review completed but labels not changed

**Solutions:**
1. Verify review comment follows required format
2. Check for status indicator keywords (✅, 🔴, 💬, ❌)
3. Ensure reviewer has proper permissions
4. Manual label update as fallback

#### 2FA Authentication Issues

**Symptoms:** Cannot access repository or perform reviews

**Solutions:**
1. Verify 2FA is properly configured
2. Use personal access token with 2FA
3. Check authentication status: `gh auth status`
4. Re-authenticate if necessary: `gh auth login`

### Getting Help

1. **Repository Issues:** Create issue with `question` label
2. **Workflow Problems:** Check Actions tab for error logs  
3. **Configuration Questions:** Review config file documentation
4. **Security Concerns:** Contact repository maintainers immediately

## Maintenance

### Regular Tasks

#### Weekly
- Review workflow execution metrics
- Check for failed or skipped reviews
- Update reviewer assignments as needed

#### Monthly  
- Analyze review patterns and effectiveness
- Update criteria thresholds based on team feedback
- Review and update documentation

#### Quarterly
- Security audit of reviewer permissions
- 2FA compliance verification for all reviewers
- Configuration optimization based on usage patterns

### Updates and Changes

**Configuration Updates:**
1. Test changes in development branch first
2. Document changes in commit messages
3. Notify team of criteria modifications
4. Monitor impact on review outcomes

**Workflow Modifications:**
1. Follow GitHub Actions best practices
2. Test with non-production repository if possible
3. Implement changes gradually
4. Maintain backward compatibility where possible

## Compliance and Audit

### Audit Trail

The system maintains comprehensive audit trails:
- All review activities logged in GitHub
- Label changes tracked automatically
- Comments and decisions preserved
- Reviewer assignments recorded

### Retention Policy

- Review data retained for 90 days minimum
- Critical security reviews retained indefinitely
- Audit logs available for compliance reporting

### Security Monitoring

Regular monitoring includes:
- Unauthorized access attempts
- Permission escalation requests
- Review bypass attempts
- Configuration tampering

---

## Quick Reference

### Key Files
- Workflow: `.github/workflows/claude-code-review.yml`
- Configuration: `.github/claude-review-config.json`
- Setup Guide: `.github/CLAUDE_REVIEW_SETUP.md`
- PR Template: `.github/pull_request_template.md`

### Key Commands
```bash
# Check repository access
gh repo view norrisaftcc/tool-vita-what-if

# List available labels
gh label list | grep claude-review

# Create test PR
gh pr create --title "Test Claude Review" --body "Testing Claude review system"

# Check workflow status
gh run list --workflow=claude-code-review.yml
```

### Emergency Contacts
- Repository Owner: @norrisaftcc
- Security Issues: [Repository security policy]
- Technical Support: [Create issue with `help wanted` label]

---

*This guide follows the GitHub Algorithm standards for repository automation and security. Last updated: $(date)*