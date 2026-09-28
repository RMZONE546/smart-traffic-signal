import React from 'react';

const SignalDisplay = ({ status }) => {
  const { active_green_lane, emergency_detected, emergency_lane, lane_data } = status;

  return (
    <div style={styles.container}>
      {/* Emergency Alert Banner */}
      {emergency_detected && (
        <div style={styles.emergencyBanner}>
          ⚠️ EMERGENCY VEHICLE DETECTED IN {emergency_lane?.toUpperCase()} — SIGNAL OVERRIDDEN!
        </div>
      )}

      {/* 4 Lanes Signal Display */}
      <div style={styles.grid}>
        {Object.keys(lane_data || {}).map((lane) => {
          const isGreen = active_green_lane === lane;
          return (
            <div
              key={lane}
              style={{
                ...styles.card,
                borderColor: isGreen ? '#2ecc71' : '#e74c3c',
                backgroundColor: isGreen ? '#e8f8f5' : '#fadbd8',
              }}
            >
              <h3>{lane}</h3>
              <div style={styles.lightContainer}>
                <div style={{ ...styles.light, backgroundColor: isGreen ? '#2ecc71' : '#555' }} />
                <div style={{ ...styles.light, backgroundColor: !isGreen ? '#e74c3c' : '#555' }} />
              </div>
              <h4 style={{ color: isGreen ? '#27ae60' : '#c0392b' }}>
                {isGreen ? 'SIGNAL: GREEN 🟢' : 'SIGNAL: RED 🔴'}
              </h4>
            </div>
          );
        })}
      </div>
    </div>
  );
};

const styles = {
  container: { marginBottom: '20px' },
  emergencyBanner: { backgroundColor: '#e74c3c', color: '#fff', padding: '12px', textAlign: 'center', fontWeight: 'bold', borderRadius: '8px', marginBottom: '15px' },
  grid: { display: 'grid', gridTemplateColumns: '1fr 1fr', gap: '15px' },
  card: { border: '3px solid', borderRadius: '10px', padding: '15px', textAlign: 'center', color: '#000' },
  lightContainer: { display: 'flex', justifyContent: 'center', gap: '10px', margin: '10px 0' },
  light: { width: '25px', height: '25px', borderRadius: '50%' }
};

export default SignalDisplay;