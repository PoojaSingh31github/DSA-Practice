import React, { useState } from 'react'
import './App.css'
import { AllTodo } from './todoList/addTodo'

function App() {
  const [count, setCount] = useState(0)

  return (
    <>
      <AllTodo />
    </>
  )
}

export default App
