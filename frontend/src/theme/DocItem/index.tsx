import React, { useState, useEffect, useCallback } from 'react';
import DocItem from '@theme-original/DocItem'; // Import the original DocItem
import UrduTranslationButton from '@site/src/components/UrduTranslationButton';
import useDocusaurusContext from '@docusaurus/useDocusaurusContext';
import { useLocation } from '@docusaurus/router';
import styles from './styles.module.css';

// Mock Translation Function
const mockTranslate = async (text: string, fromLang: string, toLang: string): Promise<string> => {
  // Simulate API call delay
  await new Promise(resolve => setTimeout(resolve, 500));
  if (toLang === 'ur') {
    // A very simplistic mock translation logic
    // In a real scenario, this would call a translation API
    return text
      .replace(/Introduction/g, 'تعارف')
      .replace(/Module/g, 'ماڈیول')
      .replace(/ROS/g, 'روس')
      .replace(/Basics/g, 'بنیادی باتیں')
      .replace(/This module/g, 'یہ ماڈیول')
      .replace(/covers/g, 'کا احاطہ کرتا ہے')
      .replace(/fundamentals/g, 'بنیادی اصول')
      .replace(/Robot Operating System/g, 'روبوٹ آپریٹنگ سسٹم')
      .replace(/open-source framework/g, 'اوپن سورس فریم ورک')
      .replace(/developing robotic applications/g, 'روبوٹک ایپلی کیشنز تیار کرنا')
      .replace(/Topics Covered/g, 'عنوانات شامل ہیں')
      .replace(/What is Embodied AI?/g, 'مجسم AI کیا ہے؟')
      .replace(/Key principles/g, 'کلیدی اصول')
      .replace(/historical context/g, 'تاریخی سیاق و سباق')
      .replace(/Differences from traditional AI/g, 'روایتی AI سے اختلافات')
      .replace(/Applications in robotics/g, 'روبوٹکس میں درخواستیں');
  } else {
    // If translating back to English, return original
    return text;
  }
};

interface TranslatableContent {
  original: string;
  translated: string;
  isTranslated: boolean;
}

export default function DocItemWrapper(props): JSX.Element {
  const { i18n } = useDocusaurusContext();
  const { pathname } = useLocation();
  const [isUrdu, setIsUrdu] = useState(false);
  const [content, setContent] = useState<TranslatableContent | null>(null);
  const [isLoading, setIsLoading] = useState(false);

  // This effect would fetch the original content
  useEffect(() => {
    // In a real scenario, you'd fetch the MDX content source or parse current DOM
    // For now, we'll get the raw content from the rendered DOM for demonstration
    const fetchOriginalContent = async () => {
      // This is a simplified way to get content.
      // A more robust solution would involve fetching raw markdown or having access to it
      // before rendering, or carefully parsing the DOM.
      // For now, we'll use a very basic text extraction from the rendered HTML.
      const docContentElement = document.querySelector('.markdown'); // Assuming Docusaurus doc content is in .markdown
      if (docContentElement) {
        // Exclude code blocks for accurate translation
        const clone = docContentElement.cloneNode(true) as HTMLElement;
        clone.querySelectorAll('pre, code').forEach(el => el.textContent = `<CODE_BLOCK>${el.textContent}</CODE_BLOCK>`);
        
        const originalText = clone.textContent || '';
        setContent({
          original: originalText,
          translated: '', // Will be filled on first translation
          isTranslated: false,
        });
      }
    };
    fetchOriginalContent();
  }, [pathname]); // Re-fetch when page changes

  const toggleTranslation = useCallback(async () => {
    if (!content) return;

    setIsLoading(true);
    if (!isUrdu && !content.isTranslated) {
      // Translate from English to Urdu
      const translatedText = await mockTranslate(content.original, 'en', 'ur');
      setContent(prev => ({ ...prev!, translated: translatedText, isTranslated: true }));
      setIsUrdu(true);
    } else if (isUrdu) {
      // Switch back to English
      setIsUrdu(false);
    } else {
      // If already translated and not Urdu, switch to Urdu (this state shouldn't happen much)
      setIsUrdu(true);
    }
    setIsLoading(false);
  }, [content, isUrdu]);

  const renderContent = () => {
    if (isLoading) {
      return <div>Loading translation...</div>;
    }
    if (isUrdu && content?.translated) {
      // When rendering translated content, we need to re-insert code blocks
      let displayedText = content.translated;
      // This is a very simplistic re-insertion.
      // A real solution would map original code blocks to translated content.
      const codeBlocks = (content.original.match(/<CODE_BLOCK>.*?<\/CODE_BLOCK>/g) || []).map(block =>
        block.replace(/<CODE_BLOCK>(.*?)<\/CODE_BLOCK>/s, '$1')
      );
      codeBlocks.forEach(block => {
        displayedText = displayedText.replace('<CODE_BLOCK></CODE_BLOCK>', block); // Find placeholder and replace
      });

      return <div className="markdown" dangerouslySetInnerHTML={{ __html: displayedText }} />;
    }
    // Default to original content rendering by original DocItem
    return <DocItem {...props} />;
  };

  return (
    <>
      <div className={styles.translationButtonContainer}>
        <UrduTranslationButton onClick={toggleTranslation} isUrdu={isUrdu} />
      </div>
      {renderContent()}
    </>
  );
}