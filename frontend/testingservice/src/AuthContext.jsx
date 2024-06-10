import React, { createContext, useState, useEffect, useContext } from 'react';
import axios from 'axios';

const AuthContext = createContext();

const AuthProvider = ({ children }) => {
  const [isLoggedIn, setIsLoggedIn] = useState(false);
  const [userRole, setUserRole] = useState(null);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    const checkAuthStatus = async () => {
      try {
        const response = await axios.get('/users/me');
        if (response.status === 200) {
          setIsLoggedIn(true);
          setUserRole(response.data.role);
        }
      } catch (error) {
        setIsLoggedIn(false);
        setUserRole(null);
      } finally {
        setLoading(false);
      }
    };

    checkAuthStatus();
  }, []);

  const handleLogout = async () => {
    try {
      await axios.post('/auth/logout');
      setIsLoggedIn(false);
      setUserRole(null);
      localStorage.removeItem('token');
    } catch (error) {
      console.error('Ошибка при выходе из аккаунта:', error);
    }
  };

  const isAdmin = () => {
    if (loading || !isLoggedIn) return false;
    return userRole === 'admin';
  };

  return (
    <AuthContext.Provider value={{ isLoggedIn, userRole, isAdmin, handleLogout }}>
      {children}
    </AuthContext.Provider>
  );
};

export { AuthContext, AuthProvider };