
import react, { createContext, useContext, useState } from "react";

const authContext = createContext<any>(null);

export const AuthProvider: React.FC = ({ children }) => {
    const [auth, setauth] = useState<boolean>(true)
    const login = () => setauth(true)
    const logout = () => setauth(false)
    return (
        <authContext.Provider value={{auth, login, logout }}>
            {children}
        </authContext.Provider>
    )
}

export const useAuth =() =>useContext(authContext)