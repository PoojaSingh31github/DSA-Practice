import react from "react";
import { Link } from "react-router-dom";
import { useAuth } from "../context/Auth";

const Navbar: React.FC = ()=>{
    const {auth, login,logout} = useAuth()  
    return (
        <div>
            <ul>
                <li>
                    <Link to={"/products"}>Products</Link>
                </li>
                <li>
                    <Link to={"/"}>Home</Link>
                </li>
                {/* Dynamically pass the product ID in the route */}
                <li>
                    <Link to={"/products/5"}>single Product</Link>
                </li>
                <li>
                    <Link to={"/task"}>tasks</Link>
                </li>
                {/* Display login/logout buttons based on auth state */}
                {auth ? (
                    <div>
                        <button onClick={logout}>Logout</button>
                    </div>
                ) : (
                    <div>
                        <button onClick={login}>Login</button>
                    </div>
                )}
            </ul>
        </div>
    )
}

export default Navbar;