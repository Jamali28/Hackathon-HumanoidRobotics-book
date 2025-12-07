import React from 'react';
import clsx from 'clsx';
import styles from './styles.module.css';

function InteractiveLabPreview(): JSX.Element {
  return (
    <section className={clsx('margin-top--lg margin-bottom--lg', styles.labPreviewSection)}>
      <div className="container text--center">
        <h2>Interactive Lab Preview</h2>
        <p>Explore simulated robotics environments and hands-on coding challenges.</p>
        <div className={styles.placeholderBox}>
          {/* This could be an iframe, a video, or a more complex interactive element */}
          <p>Placeholder for interactive lab content</p>
          <button className="button button--primary button--lg">Launch Lab</button>
        </div>
      </div>
    </section>
  );
}

export default InteractiveLabPreview;
