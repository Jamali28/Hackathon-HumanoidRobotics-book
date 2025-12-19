import React, { useState, useRef, useEffect } from 'react';
import './ChatWidget.css'; // Import the CSS file

export default function ChatWidget() {
  const [isOpen, setIsOpen] = useState(false);
  const [messages, setMessages] = useState([]);
  const [inputValue, setInputValue] = useState('');
  const [isLoading, setIsLoading] = useState(false);
  const messagesEndRef = useRef(null);
  const inputRef = useRef(null);

  // Scroll to bottom of messages
  useEffect(() => {
    scrollToBottom();
  }, [messages]);

  const scrollToBottom = () => {
    messagesEndRef.current?.scrollIntoView({ behavior: 'smooth' });
  };

  const toggleChat = () => {
    setIsOpen(!isOpen);
    if (!isOpen && inputRef.current) {
      setTimeout(() => inputRef.current.focus(), 100);
    }
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    if (!inputValue.trim() || isLoading) return;

    const userMessage = { id: Date.now(), text: inputValue, sender: 'user' };
    setMessages(prev => [...prev, userMessage]);
    setInputValue('');
    setIsLoading(true);

    try {
      // Get the API URL from environment variable
      const apiUrl = process.env.REACT_APP_RAG_API_URL || 'https://jamali28-deploy-backend.hf.space/api/chat';

      const response = await fetch(apiUrl, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({
          message: inputValue,
        }),
      });

      // Check if the response is ok and parse JSON
      if (!response.ok) {
        // Try to get error details from response
        let errorText = `HTTP error! status: ${response.status}`;
        try {
          const errorData = await response.json();
          if (errorData.detail) {
            errorText = `Error: ${typeof errorData.detail === 'string' ? errorData.detail : JSON.stringify(errorData.detail)}`;
          }
        } catch (parseError) {
          // If we can't parse the error, use the status text
          errorText = `HTTP error! status: ${response.status} - ${response.statusText}`;
        }

        const errorBotMessage = {
          id: Date.now() + 1,
          text: errorText,
          sender: 'bot'
        };
        setMessages(prev => [...prev, errorBotMessage]);
        return;
      }

      const data = await response.json();

      // Check if there's an error in the response structure
      if (data.detail) {
        // Handle specific error messages from the backend
        let errorMessage = 'Sorry, there was an issue with the chat service.';

        if (data.detail && typeof data.detail === 'string') {
          errorMessage = `Service error: ${data.detail}`;
        } else if (Array.isArray(data.detail) && data.detail[0] && data.detail[0].msg) {
          errorMessage = `Input error: ${data.detail[0].msg}`;
        }

        const errorBotMessage = {
          id: Date.now() + 1,
          text: errorMessage,
          sender: 'bot'
        };
        setMessages(prev => [...prev, errorBotMessage]);
        return;
      }

      const botMessage = {
        id: Date.now() + 1,
        text: data.response || data.message || data.answer || data.text || JSON.stringify(data) || 'Sorry, I could not understand that.',
        sender: 'bot'
      };

      setMessages(prev => [...prev, botMessage]);
    } catch (error) {
      console.error('Error sending message:', error);

      // Check if it's a network error (likely CORS or connection issue)
      let errorMessage = 'Sorry, there was an error connecting to the chat service. ';

      if (error.name === 'TypeError' && error.message.includes('fetch')) {
        errorMessage += 'This might be due to a connection issue or CORS policy. Please check if the backend is accessible.';
      } else {
        errorMessage += 'Please try again later.';
      }

      const errorBotMessage = {
        id: Date.now() + 1,
        text: errorMessage,
        sender: 'bot'
      };
      setMessages(prev => [...prev, errorBotMessage]);
    } finally {
      setIsLoading(false);
    }
  };

  return (
    <div className="chat-container">
      {isOpen ? (
        <div className="chat-widget">
          <div className="chat-header">
            <h3>AI Assistant</h3>
            <button className="chat-close" onClick={toggleChat} aria-label="Close chat">
              ×
            </button>
          </div>
          <div className="chat-messages">
            {messages.length === 0 ? (
              <div className="chat-welcome">
                <p>Hello! I'm your AI assistant. How can I help you today?</p>
              </div>
            ) : (
              messages.map((message) => (
                <div
                  key={message.id}
                  className={`chat-message ${message.sender}-message`}
                >
                  <div className="message-text">{message.text}</div>
                </div>
              ))
            )}
            <div ref={messagesEndRef} />
          </div>
          <form onSubmit={handleSubmit} className="chat-input-form">
            <input
              ref={inputRef}
              type="text"
              value={inputValue}
              onChange={(e) => setInputValue(e.target.value)}
              placeholder="Type your message..."
              disabled={isLoading}
              className="chat-input"
            />
            <button
              type="submit"
              disabled={!inputValue.trim() || isLoading}
              className="chat-send-button"
              aria-label="Send message"
            >
              {isLoading ? 'Sending...' : '→'}
            </button>
          </form>
        </div>
      ) : (
        <button className="chat-open-button" onClick={toggleChat} aria-label="Open chat">
          💬 Chat
        </button>
      )}
    </div>
  );
}