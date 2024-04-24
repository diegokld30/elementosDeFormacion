import { AuthContextProvider, MyRoutes } from './index'
import './App.css'


function App() {
  

  return (
    <>
      <AuthContextProvider>
        <MyRoutes /> 
        {/* aca en MyRoutes es donde estan mis paginas */}
      </AuthContextProvider>

    </>
  )
}

export default App
