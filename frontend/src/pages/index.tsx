import React from 'react';
import Layout from '@theme/Layout';
import useDocusaurusContext from '@docusaurus/useDocusaurusContext';
import clsx from 'clsx'; // Import clsx for combining CSS classes
import styles from './index.module.css';

import EmbodiedIntelligenceSection from '../components/EmbodiedIntelligenceSection';
import ChapterCard from '../components/ChapterCard'; // Import ChapterCard
import InteractiveLabPreview from '../components/InteractiveLabPreview'; // Import the interactive lab preview component

function HomepageHeader() {
  const {siteConfig} = useDocusaurusContext();
  return (
    <header className={styles.heroBanner}>
      <div className={clsx("container", styles.heroContent)}>
        <h1 className="hero__title">{siteConfig.title}</h1>
        <p className="hero__subtitle">Bridging the Digital Brain and the Physical Body: AI Systems in the Physical World & Embodied Intelligence</p>
        <div className={styles.buttons}>
          <a className="button button--secondary button--lg" href="/docs/chapters">
            Read
          </a>
          <a className="button button--primary button--lg margin-left--md" href="/docs/introduction">
            Introduction to Physical AI
          </a>
        </div>
      </div>
    </header>
  );
}

const ChapterList = [
  {
    title: 'Introduction to Embodied AI',
    description: 'Learn the fundamental concepts of Embodied Artificial Intelligence and its applications.',
    difficulty: 'easy',
    progress: 25,
    to: '/docs/modules/module-1', // Link to a dummy module
  },
  {
    title: 'ROS 2 Basics for Robotics',
    description: 'Master the Robot Operating System 2 for building complex robotic applications.',
    difficulty: 'medium',
    progress: 50,
    to: '/docs/modules/module-2',
  },
  {
    title: 'Gazebo Simulation Environment',
    description: 'Dive into Gazebo to simulate robots in high-fidelity virtual environments.',
    difficulty: 'medium',
    progress: 0,
    to: '/docs/modules/module-3',
  },
  {
    title: 'NVIDIA Isaac Platform',
    description: 'Explore NVIDIA Isaac for GPU-accelerated AI and robotics.',
    difficulty: 'hard',
    progress: 0,
    to: '/docs/modules/module-4',
  },
];

function HomepageChapters(): JSX.Element {
  return (
    <section className={clsx('margin-top--lg margin-bottom--lg', styles.chaptersSection)}>
      <div className="container">
        <h2 className="text--center">Featured Chapters</h2>
        <div className="row">
          {ChapterList.map((chapter, idx) => (
            <div key={idx} className="col col--4 margin-bottom--lg">
              <ChapterCard {...chapter} />
            </div>
          ))}
        </div>
      </div>
    </section>
  );
}


export default function Home() {
  const {siteConfig} = useDocusaurusContext();
  return (
    <Layout
      title={`Hello from ${siteConfig.title}`}
      description="Description will go into a meta tag in <head />">
      <HomepageHeader />
      <main>
        <EmbodiedIntelligenceSection />
        <HomepageChapters /> {/* Add the new chapters section */}
        <InteractiveLabPreview /> {/* Add the interactive lab preview section */}
        {/* Additional content can go here */}
      </main>
    </Layout>
  );
}