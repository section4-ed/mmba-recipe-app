import { useState } from 'react';
import './App.css';

function App() {
  const [message, setMessage] = useState('');
  const [isLoading, setIsLoading] = useState(false);
  const [responseBody, setResponseBody] = useState('');

  const handleFileUpload = async (event) => {
    const file = event.target.files[0];
    if (!file) return;

    const formData = new FormData();
    formData.append('file', file);

    setIsLoading(true);
    try {
      const response = await fetch('http://localhost:8000/process_recipe', {
        method: 'POST',
        body: formData,
      });
      const data = await response.json();
      setResponseBody(JSON.stringify(data, null, 2));
      if (response.ok) {
        setMessage('Recipes saved');
      } else {
        setMessage('Error processing recipe');
      }
    } catch (error) {
      setMessage('Error connecting to server');
      setResponseBody('');
    } finally {
      setIsLoading(false);
    }
  };

  return (
    <div className="App">
      <header className="App-header">
        <h1>Recipe Upload</h1>
        <div className="upload-container">
          <input
            type="file"
            onChange={handleFileUpload}
            accept=".txt"
            disabled={isLoading}
          />
          {isLoading && <p>Processing...</p>}
          {message && <p>{message}</p>}
          {responseBody && (
            <pre style={{ textAlign: 'left', maxWidth: '80%', overflow: 'auto' }}>
              {responseBody}
            </pre>
          )}
        </div>
      </header>
    </div>
  );
}

export default App;
