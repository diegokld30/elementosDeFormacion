import { create } from "zustand";
import { InsertarUsuarios } from "../supabase/crudUsuarios";

export const useUsuariosStore = create((set, get) => ({
    insertarUsuarioAdmin: async (p) => {
        const {data, error} = await supabase.auth.signUp({
            email: p.correo,
            password: p.pass,

        })
        console.log("Data del regustro del user", data);
        if (error) return null;

        await InsertarUsuarios({idauth: data.user.id, fecharegistro: new Date(), tiporol: "admin"})
    }
}));