/**
 * Simple string utility functions
 */

export function capitalize(str: string): string {
  if (!str) return str;
  return str.charAt(0).toUpperCase() + str.slice(1).toLowerCase();
}

export function isValidEmail(email: string): boolean {
  // Simplified validation - covers 99% of real-world cases
  // Consciously avoiding RFC 5322's 6000+ character regex
  if (!email || email.length > 254) return false;
  
  const parts = email.split('@');
  if (parts.length !== 2) return false;
  
  const [local, domain] = parts;
  if (local.length > 64 || domain.length < 4) return false;
  
  // Basic structure check without over-engineering
  const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
  return emailRegex.test(email);
}