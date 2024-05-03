import { create } from "zustand";
import { InsertarUsuarios } from "../supabase/crudUsuarios";
import { supabase } from '../index';


export const useUsuariosStore = create((set, get) => ({
    insertarUsuarioAdmin: async (p) => {
        const { data, error } = await supabase.auth.signUp({
            email: p.correo,
            password: p.pass,

        })
        console.log("Data del registro del user Auth", data);
        if (error) return null;

        const dataUser = await InsertarUsuarios({
            idauth: data.user.id,
            fecharegistro: new Date(),
            tiporol: "admin"
        });
        return dataUser;
    },
}));