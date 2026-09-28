import React from 'react';

const DensityChart = ({ laneData }) => {
  return (
    <div style={styles.container}>
      <h3>Traffic Density & Emergency Vehicle Counts</h3>
      <div style={styles.grid}>
        {Object.keys(laneData || {}).map((lane) => (
          <div key={lane} style={styles.statBox}>
            <h4>{lane} Metrics</h4>
            <p>🚨 Emergency Vehicles: <strong>{laneData[lane].emergency_count}</strong></p>
            <p>🚗 Normal Traffic: <strong>{laneData[lane].normal_count}</strong></p>
          </div>
        ))}
      </div>
    </div>
  );
};

const styles = {
  container: { backgroundColor: '#2a2a2a', padding: '15px', borderRadius: '8px', color: '#fff', marginBottom: '20px' },
  grid: { display: 'grid', gridTemplateColumns: '1fr 1fr', gap: '10px' },
  statBox: { backgroundColor: '#333', padding: '10px', borderRadius: '6px' }
};

export default DensityChart;