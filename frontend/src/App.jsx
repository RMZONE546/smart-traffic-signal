import React, { useState, useEffect } from 'react';

function TrafficDashboard() {
  const [trafficData, setTrafficData] = useState(null);

  // Poll traffic telemetry from Python backend
  useEffect(() => {
    const interval = setInterval(() => {
      fetch('http://localhost:5000/api/traffic')
        .then((res) => res.json())
        .then((data) => setTrafficData(data))
        .catch((err) => console.error('Error fetching traffic data:', err));
    }, 1000);

    return () => clearInterval(interval);
  }, []);

  // Trigger Manual Override
  const handleForceGreen = async (laneName) => {
    try {
      const response = await fetch('http://localhost:5000/api/manual', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({
          lane: laneName,
          action: 'enable',
        }),
      });

      const data = await response.json();
      if (!response.ok) {
        alert(`Override failed: ${data.message}`);
      }
    } catch (error) {
      console.error('Error activating manual override:', error);
      alert(`Failed to activate manual override for ${laneName}`);
    }
  };

  // Disable Manual Override (Return to Automatic Mode)
  const handleDisableManual = async () => {
    try {
      await fetch('http://localhost:5000/api/manual', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ action: 'disable' }),
      });
    } catch (error) {
      console.error('Error disabling manual override:', error);
    }
  };

  const laneKeys = ['Lane 1', 'Lane 2', 'Lane 3', 'Lane 4'];

  return (
    <div style={{ padding: '30px', backgroundColor: '#1e1e1e', color: '#fff', minHeight: '100vh', fontFamily: 'sans-serif' }}>
      <h1 style={{ marginTop: 0, fontSize: '24px' }}>Smart Traffic Controller Dashboard</h1>
      
      {trafficData && (
        <div style={{ marginBottom: '25px' }}>
          <h2 style={{ fontSize: '20px', color: '#fff', margin: '5px 0' }}>
            Active Green Lane: <span style={{ color: '#4caf50' }}>{trafficData.active_green_lane}</span>
          </h2>
          <h3 style={{ fontSize: '18px', color: '#ddd', margin: '5px 0' }}>
            Timer Remaining: <span style={{ color: '#ffeb3b' }}>{trafficData.current_timer}s</span>
          </h3>
          {trafficData.is_manual && (
            <p style={{ color: '#ff9800', fontWeight: 'bold', margin: '5px 0' }}>
              ⚠️ Manual Emergency Override Mode Active
            </p>
          )}
        </div>
      )}

      {/* Traffic Density & Emergency Counts Section */}
      <h2 style={{ fontSize: '18px', marginBottom: '15px' }}>Traffic Density & Emergency Vehicle Counts</h2>
      
      <div style={{ 
        display: 'grid', 
        gridTemplateColumns: 'repeat(2, 1fr)', 
        gap: '20px', 
        marginBottom: '30px' 
      }}>
        {laneKeys.map((laneKey) => {
          const metrics = trafficData?.lane_data?.[laneKey] || { emergency_count: 0, normal_count: 0 };
          const isActive = trafficData?.active_green_lane === laneKey;

          return (
            <div 
              key={laneKey}
              style={{
                backgroundColor: '#2b2b2b',
                padding: '20px',
                borderRadius: '8px',
                border: isActive ? '2px solid #4caf50' : '1px solid #3a3a3a',
                boxShadow: isActive ? '0 0 10px rgba(76, 175, 80, 0.3)' : 'none'
              }}
            >
              <h3 style={{ marginTop: 0, marginBottom: '15px', fontSize: '18px', color: isActive ? '#4caf50' : '#fff' }}>
                {laneKey} Metrics {isActive && '(Active)'}
              </h3>
              <p style={{ margin: '8px 0', fontSize: '16px', display: 'flex', alignItems: 'center', gap: '8px' }}>
                🚨 <span>Emergency Vehicles:</span> <strong>{metrics.emergency_count}</strong>
              </p>
              <p style={{ margin: '8px 0', fontSize: '16px', display: 'flex', alignItems: 'center', gap: '8px' }}>
                🚗 <span>Normal Traffic:</span> <strong>{metrics.normal_count}</strong>
              </p>
            </div>
          );
        })}
      </div>

      {/* Manual Emergency Override Control Panel */}
      <div style={{ padding: '20px', backgroundColor: '#2b2b2b', borderRadius: '8px', border: '1px solid #3a3a3a' }}>
        <h3 style={{ marginTop: 0, marginBottom: '15px', fontSize: '18px' }}>Manual Emergency Override Panel</h3>
        <div style={{ display: 'flex', gap: '12px', flexWrap: 'wrap' }}>
          {laneKeys.map((lane) => (
            <button
              key={lane}
              onClick={() => handleForceGreen(lane)}
              style={{
                padding: '12px 20px',
                backgroundColor: '#ff8c00',
                color: '#fff',
                border: 'none',
                borderRadius: '6px',
                fontWeight: 'bold',
                cursor: 'pointer',
                fontSize: '14px'
              }}
            >
              Force Green: {lane}
            </button>
          ))}
          <button
            onClick={handleDisableManual}
            style={{
              padding: '12px 20px',
              backgroundColor: '#f44336',
              color: '#fff',
              border: 'none',
              borderRadius: '6px',
              fontWeight: 'bold',
              cursor: 'pointer',
              fontSize: '14px'
            }}
          >
            Resume Automatic
          </button>
        </div>
      </div>
    </div>
  );
}

export default TrafficDashboard;