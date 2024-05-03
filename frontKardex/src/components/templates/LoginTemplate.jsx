import styled from "styled-components"
import { Btnsave, useUsuariosStore } from "../../index"
import { useMutation } from "@tanstack/react-query";
import { useNavigate } from "react-router-dom";

export default function LoginTemplate() {
  const navigate = useNavigate();
  const { insertarUsuarioAdmin } = useUsuariosStore();
  const mutationInsertUser = useMutation({
    mutationKey: "Insertar usuario admin",
    mutationFn: async () => {
      const p = {
        correo: "diego@info.com",
        pass: "diego123",
      };
      const dt = await insertarUsuarioAdmin(p)
      if (dt) {
        navigate("/");
      }
    }

  });

  return (
    <Container>
      <Btnsave titulo="Crear cuenta" bgcolor="#fff" funcion={mutationInsertUser.mutateAsync} />
    </Container>
  )
}
const Container = styled.div`
  height: 100vh;
`;
