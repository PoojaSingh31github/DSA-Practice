import react, { Children, createContext } from "react";

const ContextAuth = createContext();

const AuthProvider = (children)=>{

    return (
        <AuthProvider value={{}}>

            {children}
        </AuthProvider>
    )
}
export default AuthProvider;

