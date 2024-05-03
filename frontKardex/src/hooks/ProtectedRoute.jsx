import { Outlet } from "react-router-dom";
import { Navigate } from 'react-router-dom';


export const ProtectedRoute = ({user, redirectTo, children}) => {
    if(user == null){
        return <Navigate replace to={redirectTo} />;
    }
    return children ? children : <Outlet/>;
};