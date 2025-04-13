import React from 'react'
import { BrowserRouter, Route, Routes } from 'react-router-dom'
import './App.css'
import AddUsersdata from './components2/AddUsers'
import UserDetails from './components2/AllUsers'
import CheckedTable from './Components3/CheckedTable'
import Products from './Components3/product'
import Cart from './Components3/card'


function App() {
  return (
    <>
      <Routes>
        <Route path='/' element={<AddUsersdata />} />
        <Route path='/products' element={<Products />} />
        <Route path='/cart' element={<Cart />} />
        <Route path='/chakboxTable' element={<CheckedTable />} />
        <Route path='/userdetails' element={<UserDetails />} />
      </Routes>


    </>
  )
}

export default App
