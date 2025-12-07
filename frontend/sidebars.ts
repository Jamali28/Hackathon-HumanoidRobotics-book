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
  tutorialSidebar: [
    'intro', // Existing intro
    {
      type: 'category',
      label: 'Chapters',
      items: [
        'chapters/index', // Link to the all chapters page
      ],
    },
    {
      type: 'category',
      label: 'Modules',
      items: [
        'modules/module-1',
        'modules/module-2',
        // Add other modules as they are created
      ],
    },
    'introduction', // Existing introduction
    {
      type: 'category',
      label: 'Assessments',
      items: [
        'assessments/assessments',
      ],
    },
    {
      type: 'category',
      label: 'Hardware',
      items: [
        'hardware/hardware',
      ],
    },
    {
      type: 'category',
      label: 'Weeks',
      items: [
        'weeks/week01',
        'weeks/week02',
        'weeks/week03',
        'weeks/week04',
        'weeks/week05',
        'weeks/week06',
        'weeks/week07',
        'weeks/week08',
        'weeks/week09',
        'weeks/week10',
        'weeks/week11',
        'weeks/week12',
        'weeks/week13',
      ],
    },
    {
      type: 'category',
      label: 'Tutorial Basics',
      items: [
        'tutorial-basics/congratulations',
        'tutorial-basics/create-a-blog-post',
        'tutorial-basics/create-a-document',
        'tutorial-basics/create-a-page',
        'tutorial-basics/deploy-your-site',
        'tutorial-basics/markdown-features',
      ],
    },
    {
      type: 'category',
      label: 'Tutorial Extras',
      items: [
        'tutorial-extras/manage-docs-versions',
        'tutorial-extras/translate-your-site',
      ],
    },
  ],
};



export default sidebars;
