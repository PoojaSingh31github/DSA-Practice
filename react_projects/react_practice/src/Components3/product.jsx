import React, { useEffect, useState } from "react";
import { useDispatch } from "react-redux";
import { addToCart } from "../redux/action";
import { useNavigate } from "react-router-dom";

const Products = () => {
    const [products, setProducts] = useState();
    const dispatch = useDispatch();
    const navigate = useNavigate();

    const fetchProducts = async () => {
        const res = await fetch("https://fakestoreapi.com/products");
        const data = await res.json()
        setProducts(data)
    }

    useEffect(() => {
        fetchProducts();
    }, [])


    const handleAddToCart = (id) => {
        const selectedProducts = products.find((items, index) => items.id == id)
        dispatch(addToCart({ ...selectedProducts, quantity: 1 }))
    }

    return (
        <>
            <div className="px-20">
                <button onClick={() => navigate("/cart")}>cart page</button>
                <h1 className="py-10 text-center text-3xl font-bold">product page</h1>
                <div className="grid grid-cols-1 md:grid-cols-3 lg:grid-cols-4 gap-6">
                    {
                        products && products.length > 0 ? products.map((product, index) => (
                            <div key={product.id} className="bg-gray-300 px-2 py-5 rounded-lg flex flex-col justify-between items-center h-[300px]">
                                <img className="w-30 h-30 object-contain mb-2" src={product.image} alt="imgs" />
                                <h2>{product.title}</h2>
                                <p>{product.price}</p>

                                <button className="bg-black text-white py-1 px-3 rounded-md" onClick={() => handleAddToCart(product.id)}>add to cart</button>

                            </div>
                        )) : <div></div>
                    }
                </div>
            </div>
        </>
    )
}

export default Products;