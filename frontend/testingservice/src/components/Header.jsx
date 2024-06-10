import React, { useContext } from 'react';
import { BrowserRouter as Router, Routes, Route, NavLink, Navigate } from 'react-router-dom';
import { AuthContext } from '../AuthContext';

import Main from '../Pages/Main';
import Login from '../Pages/Login';
import Register from '../Pages/Register';
import AdminPanel from '../Pages/AdminPanel/AdminPanel';
import TestPassingPage from '../Pages/TestPassingPage';
import UpdateTest from '../Pages/AdminPanel/UpdateTest';
import ManageUsers from '../Pages/AdminPanel/ManageUsers';
import AddTestWithQuestions from '../Pages/AdminPanel/AddTestWithQuestions'; 
import UpdateTestWithQuestions from '../Pages/AdminPanel/UpdateTestWithQuestions';

const Header = () => {
  const { isLoggedIn, handleLogout, isAdmin } = useContext(AuthContext);

  return (
    <header>
      <Router>
        <div className='nav'>
          <span className='logo'>Сервис тестирования</span>
          <NavLink to="/">Главная</NavLink>
          {isLoggedIn ? (
            <>
              <button className="nav-link" onClick={handleLogout}>Выйти</button>
              {isAdmin() && <NavLink to="/admin">Панель админа</NavLink>}
            </>
          ) : (
            <>
              <NavLink to="/login">Войти</NavLink>
              <NavLink to="/register">Регистрация</NavLink>
            </>
          )}
        </div>

        <Routes>
          <Route exact path="/" element={<Main />} />
          <Route exact path="/login" element={<Login />} />
          <Route exact path="/register" element={<Register />} />
          <Route exact path="/test/:id" element={<TestPassingPage />} />

          <Route 
            exact 
            path="/admin" 
            element={isAdmin() ? <AdminPanel /> : <Navigate to="/login" />} 
          />
          <Route 
            exact 
            path="/tests/update/:id" 
            element={isAdmin() ? <UpdateTest /> : <Navigate to="/login" />} 
          />
          <Route 
            exact 
            path="/users" 
            element={isAdmin() ? <ManageUsers /> : <Navigate to="/login" />} 
          />
          <Route 
            exact 
            path="/admin/test/add" 
            element={isAdmin() ? <AddTestWithQuestions /> : <Navigate to="/login" />} 
          />
          <Route 
            exact 
            path="/admin/test/edit/:id" 
            element={isAdmin() ? <UpdateTestWithQuestions /> : <Navigate to="/login" />} 
          />
        </Routes>
      </Router>
    </header>
  );
};

export default Header;
