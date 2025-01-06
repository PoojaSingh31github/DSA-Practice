import { useState } from 'react'
import './App.css'
import FakeStoreApi from './components/FakeStoreApi'
import { BrowserRouter, Route, Routes } from 'react-router-dom'
import OneProduct from './components/OneProduct'
import Navbar from './components/Navbar'
import Home from './components/Home'
import PrivateRoute from './components/PrivateRouting'
import { Todo } from './components/todo/todo'
import { TodoWithRedux } from './components/todo/todoWithRedux'
import QuizApp from './components/quiz/triviaApi'
import ImageGallary from './components/imageGallary/lazyloading'

function App() {
  const [count, setCount] = useState(0)

  return (
    <>
    <BrowserRouter>
    <Navbar/>
    <Routes>
      <Route element={<PrivateRoute/>}>
      <Route path={"products/:id"} element={<OneProduct/>}/>
      <Route path={"/products"} element={<FakeStoreApi/>}/>
      <Route path={"/quiz"} element={<QuizApp/>}/>
      <Route path={"/images"} element={<ImageGallary/>}/>
      <Route path={"/task"} element={<TodoWithRedux/>}/>
      </Route>
      <Route path={"/"} element={<Home/>}/>
    </Routes>
    </BrowserRouter>
    </>
  )
}

export default App
