import React, { useState } from "react";

declare global {
  interface Window {
    vpnAPI: {
      register: (username: string, password: string) => Promise<any>;
      login: (username: string, password: string) => Promise<any>;
    };
  }
}

const App: React.FC = () => {
  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");
  const [message, setMessage] = useState("");

  const register = async () => {
    const response = await window.vpnAPI.register(username, password);
    setMessage(response.data.message);
  };

  const login = async () => {
    const response = await window.vpnAPI.login(username, password);
    setMessage(response.data.message);
  };

  return (
    <div className="App">
      <h1>Secret VPN GUI</h1>
      <input
        type="text"
        placeholder="Username"
        value={username}
        onChange={(e) => setUsername(e.target.value)}
      />
      <input
        type="password"
        placeholder="Password"
        value={password}
        onChange={(e) => setPassword(e.target.value)}
      />
      <button onClick={register}>Registrati</button>
      <button onClick={login}>Login</button>
      <p>{message}</p>
    </div>
  );
};

export default App;
