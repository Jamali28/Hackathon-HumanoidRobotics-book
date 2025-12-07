import React from 'react';
import clsx from 'clsx';
import styles from './styles.module.css';

export default function EmbodiedIntelligenceSection(): JSX.Element {
  return (
    <section className={clsx('hero hero--primary', styles.embodiedIntelligenceSection)}>
      <div className="container">
        <h2 className="hero__title">Embodied Intelligence: AI Beyond the Screen</h2>
        <p className="hero__subtitle">
          The future of AI extends beyond digital spaces into the physical world. This capstone
          quarter introduces Physical AI—AI systems that function in reality and comprehend physical laws.
          Students learn to design, simulate, and deploy humanoid robots capable of natural human
          interactions using cutting-edge technologies like ROS 2, Gazebo, and NVIDIA Isaac.
        </p>
      </div>
    </section>
  );
}