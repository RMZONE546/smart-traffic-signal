import axios from 'axios';

const API_BASE_URL = 'http://localhost:5000/api';

export const fetchTrafficStatus = async () => {
  try {
    const response = await axios.get(`${API_BASE_URL}/traffic`);
    console.log("Backend response received:", response.data); // Log data to browser console
    return response.data;
  } catch (error) {
    console.error('API Error:', error);
    throw error;
  }
};

export const triggerManualOverride = async (lane) => {
  try {
    const response = await axios.post(`${API_BASE_URL}/override`, { lane });
    return response.data;
  } catch (error) {
    console.error('Error triggering override:', error);
    throw error;
  }
};