import React from 'react';
import clsx from 'clsx';
import styles from './styles.module.css';

// Simple SVG for Pakistani Flag
const PakistanFlagIcon = () => (
  <svg width="20" height="20" viewBox="0 0 75 100" fill="none" xmlns="http://www.w3.org/2000/svg">
    <rect x="0" y="0" width="25" height="100" fill="#FFFFFF"/>
    <path d="M25 0H75V100H25V0Z" fill="#006600"/>
    <path d="M50 30C50 35.5228 45.5228 40 40 40C34.4772 40 30 35.5228 30 30C30 24.4772 34.4772 20 40 20C45.5228 20 50 24.4772 50 30Z" fill="#FFFFFF"/>
    <path d="M40 50L44.0205 57.0617L51.9897 59.9004L46.8521 66.8383L46.9099 75.3113L40 71.9961L33.0901 75.3113L33.1479 66.8383L28.0103 59.9004L35.9795 57.0617L40 50Z" fill="#FFFFFF"/>
  </svg>
);


type UrduTranslationButtonProps = {
  onClick: () => void;
  isUrdu: boolean; // Indicates if current content is Urdu
};

function UrduTranslationButton({ onClick, isUrdu }: UrduTranslationButtonProps): JSX.Element {
  return (
    <button
      className={clsx(styles.translationButton, 'button button--secondary button--sm')}
      onClick={onClick}>
      <PakistanFlagIcon />
      <span className={styles.buttonText}>
        {isUrdu ? 'Read in English' : 'اردو میں پڑھیں'}
      </span>
    </button>
  );
}

export default UrduTranslationButton;
