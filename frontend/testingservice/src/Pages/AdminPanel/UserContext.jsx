// import React, { createContext, useContext, useState, useEffect } from "react";
// import axios from "axios";

// const UserContext = createContext();

// export const UserProvider = ({ children }) => {
//   const [user, setUser] = useState(null);

//   useEffect(() => {
//     const fetchUser = async () => {
//       try {
//         const response = await axios.get("users/me");
//         setUser(response.data);
//       } catch (error) {
//         console.error("Ошибка при получении данных пользователя:", error);
//       }
//     };

//     fetchUser();
//   }, []);

//   const login = (userData) => {
//     setUser(userData);
//   };

//   const logout = () => {
//     setUser(null);
//   };

//   const isAdmin = () => {
//     console.log("User data:", user);
//     return user && user.role === "admin";
//   };

//   return (
//     <UserContext.Provider value={{ user, login, logout, isAdmin }}>
//       {children}
//     </UserContext.Provider>
//   );
// };

// export const useUser = () => {
//   return useContext(UserContext);
// };
