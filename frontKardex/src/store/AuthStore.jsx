import { create } from "zustand";
import {supabase} from "../index"

export const useAuthStore = create((set, get) => ({

    signInWithEmail: async (p) => {
        const { data, error } = await supabase.auth.signInWithPassword({
            email: p.correo,
            password: p.pass
        })
        if (error) {
            console.log(error)
            return error
        }
    },
    signOut: async () => {
        const { error } = await supabase.auth.signOut()
        if (error) {
            throw new error("Algo salió mal "+error)

        }
    }
}));
