module.exports = {
  // Engine configuration
  engine: '@marp-team/marp-core',
  theme: 'default',
  themeSet: 'default',
  
  // Enable HTML for flexibility
  html: true,
  
  // PDF export settings
  pdf: {
    format: 'A4',
    landscape: true,
    printBackground: true,
    margin: {
      top: '0.5in',
      right: '0.5in',
      bottom: '0.5in',
      left: '0.5in'
    }
  },
  
  // PowerPoint export
  pptx: true,
  
  // Custom CSS for ASCII art optimization
  customCSS: `
    pre {
      font-family: 'Courier New', 'Cascadia Code', monospace;
      line-height: 1.1;
      letter-spacing: 0;
    }
  `
}