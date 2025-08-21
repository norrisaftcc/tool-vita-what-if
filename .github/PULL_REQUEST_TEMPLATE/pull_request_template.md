# Pull Request Template

## Summary

<!-- Provide a clear, concise description of the changes in this PR -->

### Type of Change
<!-- Select the appropriate type(s) of change -->
- [ ] Bug fix (non-breaking change which fixes an issue)
- [ ] New feature (non-breaking change which adds functionality)
- [ ] Breaking change (fix or feature that would cause existing functionality to not work as expected)
- [ ] Refactoring (code improvement without changing functionality)
- [ ] Documentation update
- [ ] Performance improvement
- [ ] Test coverage improvement
- [ ] CI/CD configuration change

## Related Issues

<!-- Link to related issues using GitHub keywords -->
- Closes #(issue)
- Fixes #(issue)
- Related to #(issue)

## Changes Made

<!-- Provide a detailed list of what was changed -->

### Files Modified
<!-- List the key files that were modified and why -->

### API Changes
<!-- Document any API changes, new endpoints, or breaking changes -->

### Database/Schema Changes
<!-- Document any database or data structure changes -->

## Testing Checklist

### Automated Testing
- [ ] All existing tests pass
- [ ] New tests added for new functionality
- [ ] Test coverage maintained or improved
- [ ] Integration tests updated if applicable
- [ ] E2E tests updated if applicable

### Manual Testing
- [ ] Functionality works as expected in development environment
- [ ] Edge cases handled appropriately
- [ ] Error conditions tested and handled gracefully
- [ ] Performance testing completed (if applicable)
- [ ] Cross-browser testing completed (if applicable)
- [ ] Mobile responsiveness verified (if applicable)

### Code Quality
- [ ] Code follows project style guidelines
- [ ] No console.log or debug statements left in code
- [ ] TypeScript types are properly defined
- [ ] Functions are properly documented
- [ ] Complex logic has explanatory comments
- [ ] No linting errors or warnings

## Conventional Commits

<!-- Ensure your commit messages follow conventional commit format -->
This PR follows conventional commit format:
- [ ] All commit messages use proper conventional commit format
- [ ] Commit messages clearly describe the changes
- [ ] Breaking changes are properly documented in commit messages

Example formats:
- `feat: add user authentication system`
- `fix: resolve null pointer exception in data processor`
- `docs: update API documentation for new endpoints`
- `refactor: improve performance of search algorithm`

## Architecture Compliance

### Functional Purity
- [ ] Core logic implemented as pure functions
- [ ] Side effects isolated to boundary layers
- [ ] No global state mutations
- [ ] Immutable data structures used where appropriate

### System Composability
- [ ] Components are independently testable
- [ ] Clear interfaces between modules
- [ ] Dependency injection used appropriately
- [ ] No circular dependencies introduced

### Technical Debt
- [ ] No unacceptable technical debt introduced
- [ ] Any acceptable debt documented with TODO comments
- [ ] Debt has clear remediation plan

## Documentation Updates

- [ ] README updated if user-facing changes made
- [ ] API documentation updated for new endpoints
- [ ] Code comments added for complex logic
- [ ] Architecture decision records updated if applicable
- [ ] CHANGELOG.md updated with user-facing changes

## Security Considerations

- [ ] No sensitive information exposed
- [ ] Input validation implemented for user inputs
- [ ] Security best practices followed
- [ ] Dependencies scanned for vulnerabilities

## Performance Impact

<!-- Describe any performance implications -->
- [ ] No significant performance regression
- [ ] Performance improvements documented
- [ ] Load testing completed for high-impact changes
- [ ] Memory usage considerations addressed

## Breaking Changes

<!-- If this PR introduces breaking changes, document them here -->

### Migration Guide
<!-- Provide steps for users to migrate if breaking changes are introduced -->

## Deployment Notes

<!-- Any special deployment considerations or steps -->

## Screenshots/Demo

<!-- If applicable, add screenshots or demo videos -->

## Reviewer Checklist

### For Reviewers
- [ ] Code changes align with acceptance criteria
- [ ] Architecture principles maintained
- [ ] Security considerations reviewed
- [ ] Performance impact assessed
- [ ] Documentation completeness verified
- [ ] Test coverage adequate

### Required Reviews
- [ ] Technical review completed
- [ ] Architecture review completed (for significant changes)
- [ ] Security review completed (for security-related changes)

## Post-Merge Actions

<!-- Actions to be taken after merge -->
- [ ] Monitor for any issues in production
- [ ] Update project board status
- [ ] Close related issues
- [ ] Update milestone progress

---

**Algorithm Compliance**: This PR template ensures adherence to established procedures for change management, quality assurance, and proper GitHub citizenship standards.