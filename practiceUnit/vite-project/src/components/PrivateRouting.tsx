import react from "react";
import { useAuth } from "../context/Auth";
import { Navigate, Outlet} from "react-router-dom";

const PrivateRoute:React.FC =()=>{
const { auth } = useAuth();
return auth ? <Outlet/> : <Navigate to={"/"}/>
}

export default PrivateRoute;