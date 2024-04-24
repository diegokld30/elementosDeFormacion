import { AuthContextProvider, Dark, Light, MyRoutes } from './index'
import styled, { ThemeProvider } from 'styled-components'
import './App.css'
import { createContext, useState } from 'react'

export const ThemeContext = createContext(null)

function App() {
  const [themeuse, setTheme] = useState('light')
  const theme = themeuse === 'light' ? 'light' : 'dark'
  const themeStyle = theme === 'light' ? Light : Dark

  return (
    <>
      <ThemeContext.Provider value={{ theme, setTheme }}>

        <ThemeProvider theme={themeStyle}>
            <AuthContextProvider>
              <Container>
                <section className="ContentSideBar">

                </section>

                <section className="ContentMenuambur">

                </section>

                <section className="ContentRoutes">

                </section>

                <MyRoutes /> 

              </Container>
            </AuthContextProvider>
        </ThemeProvider>
      </ThemeContext.Provider>
    </>
  )
}

const Container = styled.main`
  display: grid;
  grid-template-columns: 1fr;
  background-color: ${({theme}) => theme.bgtotal};

`

export default App
