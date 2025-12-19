import React from 'react';
import ChatWidget from '../components/ChatWidgetPlaceholder';

// Default implementation of Root.js from Docusaurus
// This component is used to wrap the entire Docusaurus application.
export default function Root({ children }) {
  return (
    <>
      {children}
      <ChatWidget />
    </>
  );
}