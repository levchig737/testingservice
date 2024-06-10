import React, { useState, useEffect } from "react";
import axios from "axios";
import { useNavigate } from "react-router-dom";

const ManageUsers = () => {
  const [users, setUsers] = useState([]);
  const navigate = useNavigate();

  useEffect(() => {
    const fetchAllUsers = async () => {
      try {
        const res = await axios.get("/users/");
        setUsers(res.data);
        console.log(users)

      } catch (err) {
        console.log(err);
      }
    };
    fetchAllUsers();
  }, []);

  const handleBlockUser = async (id, blocked) => { // Добавление параметра blocked
    try {
      await axios.patch(`/users/${id}/`, { blocked_flag: !blocked }); // Изменение тела запроса и инвертирование флага
      setUsers(users.map(user => user.id === id ? { ...user, blocked: !blocked } : user)); // Инвертирование флага blocked
    } catch (err) {
      console.log(err);
    }
  };

  return (
    <div>
      <h1>Manage Users</h1>
      <div className="users">
        {users.map((user) => (
          <div key={user.id} className="user">
            <h3>{user.email}</h3>
            <p>{user.blocked ? "Blocked" : "Active"}</p>
            <button className="block" onClick={() => handleBlockUser(user.id, user.blocked)}>
              {user.blocked ? "Unblock" : "Block"}
            </button>
          </div>
        ))}
      </div>
    </div>
  );
};

export default ManageUsers;
