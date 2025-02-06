import { contextBridge } from "electron";
import axios from "axios";

contextBridge.exposeInMainWorld("vpnAPI", {
  register: async (username: string, password: string) =>
    await axios.post("http://127.0.0.1:5000/register", { username, password }),

  login: async (username: string, password: string) =>
    await axios.post("http://127.0.0.1:5000/login", { username, password }),
});
