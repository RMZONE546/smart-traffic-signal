import React from 'react';
import { triggerManualOverride } from '../services/api';

const OverridePanel = () => {
  const handleOverride = async (lane) => {
    try {
      await triggerManualOverride(lane);
      alert(`Manual override activated for ${lane}`);
    } catch (err) {
      alert(`Failed to activate manual override for ${lane}`);
    }
  };

  return (
    <div style={styles.container}>
      <h3>Manual Emergency Override Panel</h3>
      <div style={styles.buttonGroup}>
        {['Lane 1', 'Lane 2', 'Lane 3', 'Lane 4'].map((lane) => (
          <button
            key={lane}
            onClick={() => handleOverride(lane)}
            style={styles.button}
          >
            Force Green: {lane}
          </button>
        ))}
      </div>
    </div>
  );
};

const styles = {
  container: { backgroundColor: '#2a2a2a', padding: '15px', borderRadius: '8px', color: '#fff' },
  buttonGroup: { display: 'flex', gap: '10px', flexWrap: 'wrap' },
  button: { backgroundColor: '#e67e22', color: '#fff', border: 'none', padding: '10px 15px', borderRadius: '50px', cursor: 'pointer', fontWeight: 'bold' }
};

export default OverridePanel;