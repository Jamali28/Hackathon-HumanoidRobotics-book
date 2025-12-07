import React from 'react';
import clsx from 'clsx';
import Link from '@docusaurus/Link';
import styles from './styles.module.css';

type ChapterCardProps = {
  title: string;
  description: string;
  difficulty: 'easy' | 'medium' | 'hard';
  progress: number; // 0-100 percentage
  to: string; // Docusaurus path to the chapter
};

function ChapterCard({ title, description, difficulty, progress, to }: ChapterCardProps): JSX.Element {
  const difficultyClass = clsx(styles.difficultyBadge, {
    [styles.difficultyEasy]: difficulty === 'easy',
    [styles.difficultyMedium]: difficulty === 'medium',
    [styles.difficultyHard]: difficulty === 'hard',
  });

  return (
    <div className={clsx('card', styles.chapterCard)}>
      <div className="card__header">
        <h3 className={styles.chapterCardTitle}>{title}</h3>
        <span className={difficultyClass}>{difficulty}</span>
      </div>
      <div className="card__body">
        <p>{description}</p>
        <div className={styles.progressBarContainer}>
          <div className={styles.progressBar} style={{ width: `${progress}%` }}></div>
          <span className={styles.progressText}>{progress}% Complete</span>
        </div>
      </div>
      <div className="card__footer">
        <Link
          className={clsx('button button--primary button--block', styles.exploreButton)}
          to={to}>
          Explore Chapter
        </Link>
      </div>
    </div>
  );
}

export default ChapterCard;
