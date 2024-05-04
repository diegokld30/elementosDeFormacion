import styled from "styled-components"
import { Btnsave, useAuthStore } from "../../index"

export default function HomeTemplate() {
  const {signOut} = useAuthStore();
  return (
    <Container>
      <div>Home Template</div>
      <Btnsave  
      titulo="Cerrar sesión"
      bgcolor={"#fff"}
      funcion={signOut}
      />
    </Container>
  )
}

const Container = styled.div`
display: flex;
justify-content: center;
align-items: center;
height: 100vh;
overflow: hidden;
background-color: ${({ theme }) => theme.bgtotal};
color: ${({ theme }) => theme.text};
width: 100%;


`

