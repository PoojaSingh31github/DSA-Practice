import { useState } from 'react'
import reactLogo from './assets/react.svg'
import viteLogo from '/vite.svg'
import './App.css'
import { CouponValidation } from './components/coupon.jsx'

function App() {
  const [count, setCount] = useState(0)

  return (
    <>
      <CouponValidation/>
    </>
  )
}

export default App
