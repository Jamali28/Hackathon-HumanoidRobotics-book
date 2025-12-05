import type {SidebarsConfig} from '@docusaurus/plugin-content-docs';

// This runs in Node.js - Don't use client-side code here (browser APIs, JSX...)

/**
 * Creating a sidebar enables you to:
 - create an ordered group of docs
 - render a sidebar for each doc of that group
 - provide next/previous navigation

 The sidebars can be generated from the filesystem, or explicitly defined here.

 Create as many sidebars as you want.
 */
const sidebars: SidebarsConfig = {
  // By default, Docusaurus generates a sidebar from the docs folder structure
  tutorialSidebar: [
    {
      type: 'category',
      label: 'Introduction',
      items: [
        'week-1-2-introduction',
      ],
    },
    {
      type: 'category',
      label: 'Module 1: ROS 2',
      items: [
        'module-1-ros2/introduction',
        'module-1-ros2/tasks',
        'module-1-ros2/urdf',
        'module-1-ros2/week-3-fundamentals',
        'module-1-ros2/week-4-python-nodes-services',
        'module-1-ros2/week-5-urdf-models',
      ],
    },
    {
      type: 'category',
      label: 'Module 2: Digital Twin',
      items: [
        'module-2-digital-twin/overview',
        'module-2-digital-twin/simulation',
        'module-2-digital-twin/unity-visualization',
        'module-2-digital-twin/week-6-gazebo-basics',
        'module-2-digital-twin/week-7-advanced-sim-unity',
      ],
    },
    {
      type: 'category',
      label: 'Module 3: AI-Robot Brain',
      items: [
        'module-3-ai-robot-brain/overview',
        'module-3-ai-robot-brain/perception',
        'module-3-ai-robot-brain/navigation',
        'module-3-ai-robot-brain/sim-to-real',
        'module-3-ai-robot-brain/week-8-isaac-perception',
        'module-3-ai-robot-brain/week-9-advanced-perception',
        'module-3-ai-robot-brain/week-10-navigation',
      ],
    },
    {
      type: 'category',
      label: 'Module 4: VLA',
      items: [
        'module-4-vla/overview',
        'module-4-vla/multi-modal',
        'module-4-vla/capstone',
        'module-4-vla/week-11-voice-action-planning',
        'module-4-vla/week-12-multi-modal-gpt',
      ],
    },
    {
      type: 'category',
      label: 'Assessments',
      items: [
        'assessments/ros2-package-project',
        'assessments/gazebo-simulation',
        'assessments/isaac-perception-pipeline',
        'assessments/capstone-project',
      ],
    },
    {
      type: 'category',
      label: 'Labs',
      items: [
        'labs/workstation-setup',
        'labs/edge-ai-kit-setup',
        'labs/robot-lab-options',
        'labs/cloud-ether-lab',
      ],
    },
  ],

  // But you can create a sidebar manually
  /*
  tutorialSidebar: [
    'intro',
    'hello',
    {
      type: 'category',
      label: 'Tutorial',
      items: ['tutorial-basics/create-a-document'],
    },
  ],
   */
};

export default sidebars;
