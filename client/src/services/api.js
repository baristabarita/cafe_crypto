// api.js
import axios from 'axios';

let downloadInProgress = false;

const api = axios.create({
  baseURL: import.meta.env.API_URL || 'http://localhost:5000/api',
  timeout: 30000,
  headers: {
    'Content-Type': 'multipart/form-data',
  },
});

// Add request interceptor to prevent duplicate requests
let pendingRequests = new Map();

api.interceptors.request.use(
  config => {
    const requestKey = `${config.method}_${config.url}`;
    
    if (pendingRequests.has(requestKey)) {
      // Cancel the new request if there's already a pending one
      return Promise.reject(new axios.Cancel('Duplicate request cancelled'));
    }
    
    pendingRequests.set(requestKey, true);
    return config;
  },
  error => {
    return Promise.reject(error);
  }
);

api.interceptors.response.use(
  response => {
    const requestKey = `${response.config.method}_${response.config.url}`;
    pendingRequests.delete(requestKey);
    return response;
  },
  error => {
    const requestKey = `${error.config?.method}_${error.config?.url}`;
    pendingRequests.delete(requestKey);
    return Promise.reject(error);
  }
);

export const encryptFile = async (file) => {
  const formData = new FormData();
  formData.append('file', file);
  
  try {
    const response = await api.post('/encrypt', formData);
    return response;
  } catch (error) {
    if (axios.isCancel(error)) {
      console.log('Request cancelled:', error.message);
      return;
    }
    console.error('Encryption error:', error);
    throw error;
  }
};

export const decryptFile = async (encryptedFile, keyFile) => {
  const formData = new FormData();
  formData.append('encrypted_file', encryptedFile);
  formData.append('key_file', keyFile);
  
  try {
    const response = await api.post('/decrypt', formData);
    return response;
  } catch (error) {
    if (axios.isCancel(error)) {
      console.log('Request cancelled:', error.message);
      return;
    }
    console.error('Decryption error:', error);
    throw error;
  }
};

export const downloadFile = async (url) => {
  if (downloadInProgress) {
    console.log('Download already in progress');
    return;
  }

  try {
    downloadInProgress = true;
    const response = await api.get(url, {
      responseType: 'blob'
    });
    
    const blob = new Blob([response.data]);
    const downloadUrl = window.URL.createObjectURL(blob);
    
    // Create invisible link element
    const link = document.createElement('a');
    link.style.display = 'none';
    link.href = downloadUrl;
    
    // Extract filename from url
    const filename = url.split('/').pop();
    link.setAttribute('download', filename);
    
    // Use click() method instead of dispatching a click event
    document.body.appendChild(link);
    link.click();
    
    // Clean up
    requestAnimationFrame(() => {
      document.body.removeChild(link);
      window.URL.revokeObjectURL(downloadUrl);
      downloadInProgress = false;
    });

  } catch (error) {
    console.error('Download error:', error);
    downloadInProgress = false;
    throw error;
  }
};