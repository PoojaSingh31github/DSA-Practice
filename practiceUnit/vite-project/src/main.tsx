import { createRoot } from 'react-dom/client'
import './index.css'
import App from './App.tsx'
import { AuthProvider } from './context/Auth.tsx'
import { Provider } from 'react-redux'
import store from './redux/store2.ts'

createRoot(document.getElementById('root')!).render(
    <AuthProvider>
        <Provider store={store}
        >
            <App />
        </Provider>
    </AuthProvider>
)
