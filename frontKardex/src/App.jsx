import { ReactQueryDevtools } from '@tanstack/react-query-devtools'

import { AuthContextProvider, Dark, Light, Login, Menuhambur, MyRoutes, Sidebar } from './index'
import styled, { ThemeProvider } from 'styled-components'
import './App.css'
import { createContext, useState } from 'react'
import { Device } from './styles/breackpoints'
import { useLocation } from "react-router-dom"


export const ThemeContext = createContext(null)



function App() {
  const [themeuse, setTheme] = useState('light')
  const theme = themeuse === 'light' ? 'light' : 'dark'
  const themeStyle = theme === 'light' ? Light : Dark

  const [sidebarOpen, setSidebarOpen] = useState(false)

  const {pathname} = useLocation();

  return (
    <>
      <ThemeContext.Provider value={{ theme, setTheme }}>

        <ThemeProvider theme={themeStyle}>
          <AuthContextProvider>
            {
              pathname != "/login" ? (<Container className={sidebarOpen?"active":""}>
              <section className="ContentSideBar">

                <Sidebar state={sidebarOpen} setState={()=>setSidebarOpen(!sidebarOpen)}></Sidebar>

              </section>

              <section className="ContentMenuambur">

                <Menuhambur></Menuhambur>

              </section>

              <section className="ContentRoutes">

                <MyRoutes />

              </section>
            </Container>):(<Login/>)
            }
            
            <ReactQueryDevtools initialIsOpen={false} />
          </AuthContextProvider>
        </ThemeProvider>
      </ThemeContext.Provider>
    </>
  )
}

const Container = styled.main`
  display: grid;
  grid-template-columns: 1fr;
  background-color: ${({ theme }) => theme.bgtotal};

  .ContentSideBar{
    display:none;

  }
  .ContentMenuambur{
    display:block;
    position: absolute;
    left: 20px;
  }
  @media ${Device.tablet} {
    grid-template-columns: 65px 1fr;
    &.active{
      grid-template-columns: 220px 1fr;
    }
    .ContentSideBar{
      display:initial;
    }
    .ContentMenuambur{
      display:none;
    }

  }

  .ContentRoutes{
    grid-column: 1 ;
    width: 100%;
    @media ${Device.tablet}{
      grid-column: 2;
    }

    }
  }
`

export default App
