import React, { useState, useEffect, useRef } from 'react';
import './RAGChatWidget.css';

interface SourceChunk {
  id: string;
  text: string;
  score: number;
  source_url: string;
}

interface ChatResponse {
  response: string;
  sources: SourceChunk[];
  query: string;
  timestamp: string;
}

const RAGChatWidget: React.FC = () => {
  const [isOpen, setIsOpen] = useState(false);
  const [messages, setMessages] = useState<{ text: string; isUser: boolean; sources?: SourceChunk[] }[]>([]);
  const [inputValue, setInputValue] = useState('');
  const [isLoading, setIsLoading] = useState(false);
  const [selectedText, setSelectedText] = useState('');
  const [error, setError] = useState<string | null>(null);
  const messagesEndRef = useRef<HTMLDivElement>(null);

  // Function to get selected text from the page
  useEffect(() => {
    const handleSelectionChange = () => {
      const selectedText = window.getSelection()?.toString().trim() || '';
      setSelectedText(selectedText);
    };

    document.addEventListener('selectionchange', handleSelectionChange);
    return () => {
      document.removeEventListener('selectionchange', handleSelectionChange);
    };
  }, []);

  // Scroll to bottom of messages
  useEffect(() => {
    messagesEndRef.current?.scrollIntoView({ behavior: 'smooth' });
  }, [messages]);

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    if (!inputValue.trim() || isLoading) return;

    // Add user message to chat
    const userMessage = selectedText
      ? `${inputValue} (based on selected text: "${selectedText.substring(0, 100)}...")`
      : inputValue;

    setMessages(prev => [...prev, { text: userMessage, isUser: true }]);
    setIsLoading(true);
    setError(null);

    try {
      // Prepare the query - include selected text if available
      const query = selectedText ? `${inputValue} based on: ${selectedText}` : inputValue;

      // Get API endpoint from environment or use default
      const apiEndpoint = process.env.REACT_APP_RAG_API_URL || 'http://localhost:8000/api/chat';

      // Call the backend API
      const response = await fetch(apiEndpoint, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({
          message: query,
          temperature: 0.7,
          max_tokens: 1000
        }),
      });

      if (!response.ok) {
        throw new Error(`API request failed with status ${response.status}`);
      }

      const data: ChatResponse = await response.json();

      // Add bot response to chat
      setMessages(prev => [
        ...prev,
        {
          text: data.response,
          isUser: false,
          sources: data.sources
        }
      ]);
    } catch (err) {
      console.error('Error calling RAG API:', err);
      setError('Failed to get response from the RAG system. Please try again.');
      setMessages(prev => [
        ...prev,
        {
          text: 'Sorry, I encountered an error processing your request. Please try again.',
          isUser: false
        }
      ]);
    } finally {
      setIsLoading(false);
      setInputValue('');
      setSelectedText(''); // Clear selected text after use
    }
  };

  const toggleChat = () => {
    setIsOpen(!isOpen);
  };

  return (
    <div className="rag-chat-widget">
      {isOpen ? (
        <div className="chat-container">
          <div className="chat-header">
            <h3>AI Assistant</h3>
            <button className="close-btn" onClick={toggleChat} aria-label="Close chat">
              ×
            </button>
          </div>

          <div className="chat-messages">
            {messages.length === 0 ? (
              <div className="welcome-message">
                <p>Ask me anything about humanoid robotics and physical AI!</p>
                {selectedText && (
                  <div className="selected-text-preview">
                    <p><strong>Selected text:</strong> "{selectedText.substring(0, 100)}{selectedText.length > 100 ? '...' : ''}"</p>
                  </div>
                )}
              </div>
            ) : (
              messages.map((msg, index) => (
                <div
                  key={index}
                  className={`message ${msg.isUser ? 'user-message' : 'bot-message'}`}
                >
                  <div className="message-content">
                    {msg.text}
                  </div>
                  {!msg.isUser && msg.sources && msg.sources.length > 0 && (
                    <div className="sources-section">
                      <details>
                        <summary>Sources ({msg.sources.length})</summary>
                        <ul className="sources-list">
                          {msg.sources.map((source, idx) => (
                            <li key={idx} className="source-item">
                              <div className="source-score">Score: {source.score.toFixed(2)}</div>
                              <div className="source-text">{source.text}</div>
                              {source.source_url !== 'Unknown' && (
                                <a
                                  href={source.source_url}
                                  target="_blank"
                                  rel="noopener noreferrer"
                                  className="source-link"
                                >
                                  Source
                                </a>
                              )}
                            </li>
                          ))}
                        </ul>
                      </details>
                    </div>
                  )}
                </div>
              ))
            )}
            <div ref={messagesEndRef} />
          </div>

          {error && (
            <div className="error-message">
              {error}
            </div>
          )}

          <form onSubmit={handleSubmit} className="chat-input-form">
            {selectedText && (
              <div className="selected-text-indicator">
                Using selected text: "{selectedText.substring(0, 50)}..."
              </div>
            )}
            <div className="input-container">
              <input
                type="text"
                value={inputValue}
                onChange={(e) => setInputValue(e.target.value)}
                placeholder={selectedText ? "Ask about selected text..." : "Ask about humanoid robotics..."}
                disabled={isLoading}
                className="chat-input"
              />
              <button
                type="submit"
                disabled={isLoading || !inputValue.trim()}
                className="send-button"
              >
                {isLoading ? 'Sending...' : 'Send'}
              </button>
            </div>
          </form>
        </div>
      ) : (
        <button className="chat-toggle-btn" onClick={toggleChat} aria-label="Open chat">
          <span className="chat-icon">💬</span>
          <span className="chat-label">Ask AI</span>
        </button>
      )}
    </div>
  );
};

export default RAGChatWidget;