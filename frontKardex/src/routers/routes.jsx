import { Routes, Route } from "react-router-dom";
import { Home, Login, userAuth } from "../index";
import { ProtectedRoute } from "../hooks/ProtectedRoute";

export default function MyRoutes() {
    const { user } = userAuth();
    return (
        <Routes>
            <Route path="/login" element={<Login />} />

            <Route element={<ProtectedRoute user={user} redirectTo="/login" />}>
                <Route path="/" element={<Home />} />
            </Route>

            {/* <Route path="/about" element={<About />} /> */}
        </Routes>

    );
}