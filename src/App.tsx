import { useState } from 'react'

function App() {
  const [count, setCount] = useState(0)

  return (
    <div style={{ padding: '2rem', fontFamily: 'system-ui, sans-serif' }}>
      <h1>Tool Vita What If</h1>
      <p>Sprint Zero - Minimal Setup</p>
      <div style={{ marginTop: '2rem' }}>
        <button onClick={() => setCount(count + 1)}>
          Count: {count}
        </button>
      </div>
    </div>
  )
}

export default App